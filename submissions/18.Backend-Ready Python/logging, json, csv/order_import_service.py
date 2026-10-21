"""
[ ] 5. Mini-project — Order import service

Challenge
15 marks

Create `order_import_service.py`. Read a JSON configuration that specifies the input CSV path and accepted statuses. 
Import orders from CSV, validate each row, calculate the total amount of accepted orders, and log the start, success, rejected rows, and unexpected errors. 
Write accepted orders to a new CSV report and summarize the valid and rejected counts. Handle missing files and malformed JSON without crashing.

"""


import logging , csv , json


logging.basicConfig(filename="logging.log", level=logging.DEBUG, format= "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)

# [Start Execution]

logger.info("The application is started")


# Load config.json

def read_json(json_file):

    try:

        with open(json_file, "r", newline="") as file:

            data = json.load(file)

            input_csv_path = data["input_csv_path"]

            accepted_statuses = data["accepted_statuses"]


        return input_csv_path, accepted_statuses


    except FileNotFoundError as e:


        logger.exception(f"The json file is not found with error:{e}")

        return None,None

    except json.JSONDecodeError as e:

        logger.exception(f"The JSON file is not valid: {e}")

        return None,None



# Open Input CSV 

def read_csv(csv_path,accepted_statuses):

    if not csv_path:

        logger.error("The CSV Path is Invalid")

    elif not accepted_statuses:

        logger.error("The status fileds are empty")

    else:

        try: 

            with open(csv_path, "r",newline="") as file:

                reader = csv.DictReader(file)

                if not reader.fieldnames or "status" not in reader.fieldnames or "amount" not in reader.fieldnames:
                    logger.error("CSV file structure is missing required columns.")
                    return None

                valid_status = set(accepted_statuses)

                total_amount = 0

                rejected_count = 0

                valid_count  = 0

                logger.info("The Validation of csv data is started")

                valid_orders = []



                for row_num, row in enumerate(reader,start=2):


                    if row["status"].strip() not in valid_status:

                        rejected_count += 1

                        logger.info(f"The order is not in valid statuses in row number:{row_num}")

                        continue

                    try:

                        amount = float(row["amount"])

                    except ValueError as e:

                        rejected_count += 1

                        logger.info(f"The given amount is invalid formate at row num:{row_num}")

                        continue

                    if amount < 0:

                        logger.info(f"The amount shoud not be negative and got:{amount}")

                        rejected_count += 1

                        continue

                    total_amount += amount

                    valid_count  += 1

                    logger.info(f"sucessfully validated the row num:{row_num}")

                    valid_orders.append(row)


                print("The file is read successfully")

                logger.info(f"The file is read successfully with succes rows:{valid_count} and failed rows:{rejected_count}")

                print(f"The total amount of accepted status of orders is : {total_amount}")
                print(f"The Total failed row in the CSV File is  : {rejected_count}")

                return valid_orders
            
        except FileNotFoundError as e:

            logger.error(f"The csv file is not found with error:{e}")

        except Exception as e:

            logger.error(f"An unexpected critical error occurred while exporting report: {e}")



def export_csv(orders):

    field_names = ["order_id", "customer", "status", "amount"]

    try:
        with open("export.csv", "w", newline="") as file:

            writer = csv.DictWriter(file, fieldnames=field_names)

            writer.writeheader()

            writer.writerows(orders)

        print("\n--- Reopening CSV File for Verification ---")
        
        with open("export.csv", "r", newline="") as file:
        
            reader = csv.DictReader(file)
        
            for row in reader:
        
                print(f"Verified Row: {row}")

    except Exception as e:
        logger.error(f"An unexpected critical error occurred while exporting report: {e}")
    

    

if __name__ == "__main__":

    # 1. Load the initial JSON config file
    input_csv_path, accepted_statuses = read_json("config.json")

    # 2. If the config loaded without crashing, run the CSV importer engine
    if input_csv_path is not None:
        accepted_orders = read_csv(input_csv_path, accepted_statuses)

        # 3. If valid orders were parsed out, write the final clean report file
        if accepted_orders:
            export_csv(accepted_orders)



