import logging

import sys

import os

import json

import csv

import re

import math

import random

from collections import Counter


from datetime import datetime , timezone


logging.basicConfig(filename="audit_logs.log",level=logging.DEBUG,format= "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


logger = logging.getLogger(__name__)


def order_audit_service(file_path):


    ### 1. Configuration and startup

    logger.info("The application started")

    required_config_keys = ["input_path","output_path"]

    # Reading Json Config file
    try:
        with open(file_path, "r",encoding='utf-8') as file:

            config_file_data = json.load(file)

    except json.JSONDecodeError as e:

        logger.error(f"The config file invalid with error: {e}")

        sys.exit(1)

    for key in required_config_keys:

        if key not in config_file_data:

            logger.error(f"The required field {key} is missing in the file")

            sys.exit(1)

    if not isinstance(config_file_data["input_path"],str):

        logger.error(f"The input_path path is invalid data type")

        sys.exit(1)

    if not isinstance(config_file_data["output_path"],str):

        logger.error(f"The output path is invalid data type")

        sys.exit(1)

    if not os.path.exists(config_file_data["input_path"]):

        logger.error("The input order file not exist")

        sys.exit(1)

    input_file_path = config_file_data["input_path"]

    output_path = config_file_data["output_path"]

    # Validate and create the output path tree safely

    try:
        # If the directory exists, it does nothing. If it's missing, it builds it!
        os.makedirs(output_path, exist_ok=True)
        logger.info(f"Output directory validated/created at: {output_path}")

    except Exception as e:
        # If the path is illegal (e.g., character issues or permissions), it catches it here!
        logger.error(f"Failed to validate or create output directory due to error: {e}")
        sys.exit(1)

    
    ### 2. Data ingestion and validation

    required_csv_keys = ["order_id","timestamp","amount","status"]

    accepted_statuses = ["COMPLETED","PENDING","SHIPPED"]

    accepted_records = []

    rejected_records = []

    try:

        with open(input_file_path,"r",newline="",encoding='utf-8') as csv_file:

            reader = csv.DictReader(csv_file)

            headers = reader.fieldnames
            
            for key in required_csv_keys:

                if key not in headers:

                    logger.error(f"The required key {key} not found in the csv headers")

                    sys.exit(1)

            for row_num,row in enumerate(reader,start=1):

                is_valid = True

                # Validating missing feild

                for key in required_csv_keys:

                    if key not in row:

                        logger.error(f"The required {key} field is missing at row num {row_num}")

                        row["rejection_remark"] = f"Required {key} field is missing"

                        is_valid = False 

                        break

                    data = row[key].strip()

                    if not data:

                        logger.error(f"The required {key} field data is missing at row num {row_num}")
                        
                        row["rejection_remark"] = f"Required {key} field data is missing"
                        
                        is_valid = False 
                        
                        break


                if not is_valid:

                    rejected_records.append(row)

                    continue

                # Validating statuses feild

                if row["status"].strip().upper() not in accepted_statuses:

                    logger.error(f"The order id{row['order_id']} has invalid status {row['status']} on row_num :{row_num}")

                    row["rejection_remark"] = "Invalid status"

                    rejected_records.append(row)

                    continue    

                # Validate order IDs using `re`.

                pattern = r"ORD-\d{5}"
                
                if not re.fullmatch(pattern=pattern,string=row["order_id"]):

                    logger.error(f"The order id {row['order_id']} is invalid on row_num: {row_num}")

                    row["rejection_remark"] = "Invalid order id"

                    rejected_records.append(row)

                    continue


                # - Validate amounts as finite, non-negative numbers.
                
                try:

                    amount = float(row["amount"].strip())

                except ValueError as e:

                    logger.error(f"The row num :{row_num} contains {row['amount']} invalid amount")

                    row["rejection_remark"] = f"Invalid Amount {row['amount']}"

                    rejected_records.append(row)

                    continue


                if not math.isfinite(amount):

                    logger.error(f"The amount {row['amount']} is Not finite at row num {row_num}")

                    row["rejection_remark"] = f"The amount {row['amount']} is not finite"

                    rejected_records.append(row)

                    continue

                if amount < 0:

                    logger.error(f"The amount {row['amount']} is negative at row num {row_num}")

                    row["rejection_remark"] = f"Invalid {row['amount']} amount"

                    rejected_records.append(row)

                    continue

                # Parsing and validating timestamp

                
                try:

                    parsed_time = datetime.fromisoformat(row["timestamp"].strip())

                except ValueError as e:

                    logger.error(f"The timestamp {row['timestamp']} is invalid with error: {e}")

                    row["rejection_remark"] = "Invalid time stamp"

                    rejected_records.append(row)

                    continue


                if parsed_time.tzinfo is None or parsed_time.tzinfo.utcoffset(parsed_time) is None:

                    logger.error(f"The time stamp not contains the Time zone info at row num {row_num}")

                    row["rejection_remark"] = "Time stamp not contains the time zone info"

                    rejected_records.append(row)

                    continue


                parsed_time = parsed_time.astimezone(timezone.utc)


                row["timestamp"] = parsed_time

                row["amount"] = amount

                row["timestamp"] = parsed_time.isoformat()

                accepted_records.append(row)

            
    except FileNotFoundError as e:

        logger.error(f"The CSV File not exist with error: {e}")

        sys.exit(1)

    ### 3. Processing and analytics

    accepted_statuses = [row["status"] for row in accepted_records]

    counter1 = Counter(accepted_statuses)

    rejected_reasons = [row["rejection_remark"] for row in rejected_records]

    counter2 = Counter(rejected_reasons)

    if len(accepted_records) > 0:

        total_amount = sum(item["amount"] for item in accepted_records)

        average_amount = total_amount / float(len(accepted_records))

    else:

        total_amount = 0.0

        average_amount = 0.0


    sample = []

    random.seed(42)

    if accepted_records:

        sample_count = max(1,len(accepted_records)//2)

        sample = random.sample(accepted_records,k=sample_count)

    ### 4. Reports and audit trail

    accepted_orders = os.path.join(output_path,"accepted_orders.csv")

    rejected_orders = os.path.join(output_path,"rejected_orders.csv")

    # Exporting accepted_orders.csv
    try:

        with open(accepted_orders, "w", newline="") as file:

            writer = csv.DictWriter(file, fieldnames= required_csv_keys)

            writer.writeheader()

            writer.writerows(accepted_records)

    except Exception  as e:

        logger.error(f"Failed to export the accepted_orders.csv file with error {e}")

        sys.exit(1)

    # Exporting rejected_orders.csv file 

    fieldnames= required_csv_keys + ["rejection_remark"]


    try:

        with open (rejected_orders,"w",newline="") as file:

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rejected_records)

    except Exception as e:

        logger.error(f"Failed to export the rejected_orders.csv file with error {e}")

        sys.exit(1)

    timestamp_string = datetime.now(timezone.utc).isoformat()

    report_payload = {
        "generated_at_utc": timestamp_string,
        "total_accepted_amount" : total_amount,
        "average_amount" : average_amount,
        "total_accepted_statuses" : dict(counter1),
        "total_rejected_reasons" : dict(counter2)   
    }

    json_file_path = os.path.join(output_path,"summary.json")

    try:

        with open(json_file_path, "w") as file:

            json.dump(report_payload,file,indent=4)

    except Exception as e:

        logger.error(f"Failed to export the summary.json file with error {e}")

        sys.exit(1)

    return report_payload



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python order_audit_service.py <path_to_config.json>", file=sys.stderr)
        logger.error("Fatal: Missing configuration file argument.")
        sys.exit(1)

    target_config_path = sys.argv[1]

    if not os.path.exists(target_config_path):

        print(f"Error: The configuration file '{target_config_path}' does not exist.", file=sys.stderr)
        logger.error(f"Fatal: Configuration file not found at '{target_config_path}'.")
        sys.exit(1)

    order_audit_service(target_config_path)






    
