"""
3. CSV import and validation

Medium
10 marks

Create `csv_importer.py`. Read an orders CSV using DictReader. 
Validate that each row has an order ID, a customer, and a valid non-negative amount. Count valid and rejected rows, and report why each rejected row failed. 
Don't let one invalid row terminate the entire import.

"""

import csv

def csv_importer(orders):
    required_keys = ["order_id", "customer", "amount"]

    try:
        with open(orders, "r", newline="") as file:
            reader = csv.DictReader(file)
            validrows = 0
            invaliderows = 0

            for row_num, raw in enumerate(reader, start=2):
                is_valid = True
                missing_key = None

                # 1. Structural Validation (Missing columns)
                for key in required_keys:
                    if key not in raw or raw[key] is None:
                        is_valid = False
                        missing_key = key
                        break

                if not is_valid:
                    print(f"Row {row_num} Rejected: Missing required column structural field '{missing_key}'.")
                    invaliderows += 1
                    continue

                # 2. Field Validation: Empty Order ID
                if not raw["order_id"].strip():
                    print(f"Row {row_num} Rejected: 'order_id' value cannot be empty or blank.")
                    invaliderows += 1
                    continue

                # 3. Field Validation: Empty Customer Name
                if not raw["customer"].strip():
                    print(f"Row {row_num} Rejected: Order '{raw['order_id']}' has an empty or blank 'customer' field.")
                    invaliderows += 1
                    continue

                # 4. Type Validation: Numeric Parsing Check
                try:
                    amount = float(raw["amount"])
                except ValueError:
                    print(f"Row {row_num} Rejected: Order '{raw['order_id']}' has an invalid amount type (Must be a numeric value). Got: '{raw['amount']}'")
                    invaliderows += 1
                    continue

                # 5. Value Constraint Validation: Non-negative Check
                if amount < 0:
                    print(f"Row {row_num} Rejected: Order '{raw['order_id']}' has a negative amount. Got: {amount}")
                    invaliderows += 1
                    continue

                # If all evaluations clear successfully
                validrows += 1

            return validrows, invaliderows

    except FileNotFoundError:
        print(f"File Error: The system could not find the specified target file path: '{orders}'")
        return 0, 0
    except csv.Error as e:
        print(f"CSV Parsing Error: The file structure is malformed or corrupted. Details: {e}")
        return 0, 0
    except Exception as e:
        print(f"An unexpected structural error occurred: {e}")
        return 0, 0


# Execution block running against your sample test data
valid_rows, invalid_rows = csv_importer("ord.csv")
print(f"\nValid rows processed: {valid_rows}")
print(f"Invalid rows rejected: {invalid_rows}")



