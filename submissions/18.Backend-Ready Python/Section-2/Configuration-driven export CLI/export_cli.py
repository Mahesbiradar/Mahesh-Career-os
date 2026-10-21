

import os

import sys

import logging

import json

import math

from collections import Counter

import csv

import random

import re

from datetime import datetime,timezone


logging.basicConfig(filename="config.log", level=logging.DEBUG, format= "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)


    
def run_export_pipeline(config_path):

    print(f"Core logic received configuration file path: {config_path}")

    required_keys = ["input_path", "output_path", "max_records"]

    try:
        with open(config_path,"r",newline="") as file:

            file_data = json.load(file)

    except json.JSONDecodeError as e:

        logger.error(f"The file is invalid with error{e}")

        sys.exit(1)

    for key in required_keys:

        if key not in file_data:

            logger.error(f"The required feild {key} is missing in the file")

            sys.exit(1)



    if not os.path.exists(file_data["input_path"]):

        logger.error(f"The input path not exist")

        sys.exit(1)
    
    input_data = file_data["input_path"]

    if not isinstance(file_data["max_records"],int) or file_data["max_records"] <= 0 :

        logger.error(f"The Max Record data is empty")
        
        sys.exit(1)

    max_records = file_data["max_records"]

    
    output_path = file_data["output_path"]

    # Validate and create the output path tree safely
    try:
        # If the directory exists, it does nothing. If it's missing, it builds it!
        os.makedirs(output_path, exist_ok=True)
        logger.info(f"Output directory validated/created at: {output_path}")
    except Exception as e:
        # If the path is illegal (e.g., character issues or permissions), it catches it here!
        logger.error(f"Failed to validate or create output directory due to error: {e}")
        sys.exit(1)


    # Processing csv file:

    try:

        random.seed(42)

        with open(input_data,"r", newline="") as file:

            csv_reader = csv.DictReader(file)

            required_fields = ["order_id", "customer", "amount", "status"]

            valid_status = ["pending","processing","completed"]

            valid_data = []

            invalid_data = []

            list_of_statuses = []

            for row_num,row in enumerate(csv_reader,start=1):

                if len(valid_data) >= max_records:
                    break  # Stops processing early as soon as the cap is reached!

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

                row["amount"] = amount

                row["sample_tracking_id"] = f"SMP-{random.randint(10000, 99999)}"

                list_of_statuses.append(row["status"])
                
                valid_data.append(row)

            
            if len(valid_data) > 0:

                total_amount = 0

                for data in valid_data:
                
                    total_amount += data["amount"]

                average_amount = total_amount /float(len(valid_data))

            else:

                total_amount = 0.0

                average_amount = 0.0


            counter = Counter(list_of_statuses)

            timestamp_string = datetime.now(timezone.utc).isoformat()


            report_payload = {
                "metadata": {
                    "generated_at_utc": timestamp_string,
                    "total_accepted_records": len(valid_data),
                    "total_rejected_records": len(invalid_data)
                },
                "statistics": {
                    "total_amount": total_amount,
                    "average_amount": average_amount,
                    "status_counts": dict(counter)
                },
                "records": valid_data
            }

            report_file_path = os.path.join(output_path,"report.json")

            try:

                with open(report_file_path, "w", newline="") as file:

                    json.dump(report_payload,file,indent=2)

                    logger.info(f"Successfully generated final JSON report output at: {report_file_path}")

            except Exception as e:
                logger.error(f"Failed to write final JSON report: {e}")
                sys.exit(1)



            return report_payload



    except FileNotFoundError as e:

        logger.error("File Not found")

        return None




if __name__ == "__main__":

    logger.info("The configuration-driven export CLI has started.")

    if len(sys.argv) < 2:
        print("Usage: python export_cli.py <path_to_config.json>", file=sys.stderr)
        logger.error("Fatal: Missing configuration file argument.")
        sys.exit(1)
    
    target_config_path = sys.argv[1]

    if not os.path.exists(target_config_path):

        print(f"Error: The configuration file '{target_config_path}' does not exist.", file=sys.stderr)
        logger.error(f"Fatal: Configuration file not found at '{target_config_path}'.")
        sys.exit(1)

    run_export_pipeline(target_config_path)


