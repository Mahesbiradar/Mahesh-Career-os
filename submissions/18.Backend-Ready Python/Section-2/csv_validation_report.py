import csv

import logging

import math

import re

from collections import Counter


logging.basicConfig(filename="csv_validation_report.log", level=logging.DEBUG, format= "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)


def csv_validation_report(filename):

    try:

        with open(filename,"r", newline="") as file:

            csv_reader = csv.DictReader(file)

            required_fields = ["order_id", "customer", "amount", "status"]

            valid_status = ["pending","processing","completed"]

            valid_data = []

            invalid_data = []

            list_of_statuses = []

            for row_num,row in enumerate(csv_reader,start=1):

                is_valid = True

                # Structural validation

                for field in required_fields:

                    if field not in row:

                        logger.error(f"Skiping the row number: {row_num} Due to missing data at row num : {row_num}")

                        is_valid = False

                        break

                if not is_valid:

                    clean_invalid_row = {field: row.get(field, "MISSING") for field in required_fields}

                    invalid_data.append(clean_invalid_row)

                    continue

                # Amount Field Validation

                try:

                    amount = float(row["amount"])

                except ValueError as e:

                    invalid_data.append(row)

                    logger.error(f"The amount is not numeric Data at row num : {row_num}")

                    continue

                if not math.isfinite(amount):

                    invalid_data.append(row)

                    logger.error(f"The amount is not finite at row num : {row_num}")

                    continue

                if amount < 0:

                    invalid_data.append(row)

                    logger.error(f"The amount is negative at row num : {row_num}")

                    continue

                # order id feild validation.

                pattern = r"ORD-\d{4}"

                order_id = row["order_id"]

                if not re.fullmatch(pattern=pattern,string=order_id):

                    invalid_data.append(row)

                    logger.error(f"The order id is invalid with ID: {row['order_id']} at row_num : {row_num}")

                    continue


                # Accept only the statuses `pending`, `processing`, and `completed`.

                status_clean = row["status"].strip().lower()

                if status_clean not in valid_status:
                    invalid_data.append(row)
                    logger.error(f"The status is not valid status with status: {row['status']} at row_num: {row_num}")
                    continue

                # Customer name validation

                cust_name = row["customer"].strip()

                if not cust_name:

                    invalid_data.append(row)

                    logger.error(f"The cutomer name is empty on row num: {row_num}")

                    continue

                
                # Processiong valid rows

                row["status"] = status_clean

                list_of_statuses.append(status_clean)

                valid_data.append(row)

            counter = Counter(list_of_statuses)

            print(counter)


            #Writing valid data to csv file

            with open("valid_data.csv", "w", newline="") as file:

                csv_writer = csv.DictWriter(file,fieldnames=required_fields)

                csv_writer.writeheader()

                csv_writer.writerows(valid_data)

            # Writing invalide data to csv file

            with open("invalid.csv", "w",newline="") as file:

                csv_writer = csv.DictWriter(file,fieldnames=required_fields)

                csv_writer.writeheader()

                csv_writer.writerows(invalid_data)
            
            return valid_data, invalid_data

            
    except FileNotFoundError as e:

        logger.error("File Not found")

        return None

if __name__ == "__main__":
    logger.info("The application has started")
    # Make sure your testing file matches this string name or create a placeholder "export.csv"
    csv_validation_report("export.csv")


