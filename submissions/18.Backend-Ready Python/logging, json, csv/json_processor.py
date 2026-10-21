"""
2. JSON API payload processor

Medium
10 marks

Create `json_processor.py`. Given a JSON string containing order_id, customer, amount, and status, parse it and validate required fields and types. 
Reject malformed JSON, missing fields, and invalid amounts. Convert a Python dictionary back to readable JSON using dumps().

"""


import json


raw_json_input = """
[
    {"order_id": "ORD-2026-001", "customer": "Alex Mercer", "amount": 128.50, "status": "processing"},
    {"order_id": "ORD-2026-002", "customer": "Elena Rostova", "amount": -45.00, "status": "processing"},
    {"order_id": "ORD-2026-003", "customer": "", "amount": 75.25, "status": "processing"},
    {"order_id": "ORD-2026-004", "customer": "Marcus Vance", "amount": 540.00, "status": "pending"},
    {"order_id": "ORD-2026-005", "customer": "Diana Prince", "amount": "twelve", "status": "processing"}
]
"""


processed_orders = []

order_keys = ["order_id","customer","amount","status"]

try:

    orders = json.loads(raw_json_input)

    for order in orders:

        is_valid = True

        for key in order_keys:

            if key not in order:

                print(f"Rejected: Missing required field '{key}' in order data.")

                is_valid = False

                break

        if not is_valid:

            continue

        if not isinstance(order["order_id"], str) or not order["order_id"].strip():

            print(f"Rejected Order {order.get('order_id')}: 'order_id' must be a non-empty string.")

            continue

        if not isinstance(order["customer"], str) or not order["customer"].strip():
        
            print(f"Rejected Order {order.get('customer')}: 'customer' must be a non-empty string.")
        
            continue

        if not isinstance(order["status"], str) or not order["status"].strip():

            print(f"Rejected Order {order['order_id']}: 'status' must be a non-empty string.")

            continue

        amount = order["amount"]

        if not isinstance(amount, (int, float)):

            print(f"Rejected Order {order['order_id']}: Invalid amount type (Must be a number). Got: '{amount}'")

            continue

        if amount < 0:

            print(f"Rejected Order {order['order_id']}: Invalid amount value  (Must be a greater than 0). Got: '{amount}'")


        processed_orders.append(order)


    readable_json_output = json.dumps(processed_orders, indent=2)


    print("\n--- Processed & Validated Read-Ready Output ---")

    print(readable_json_output)


except json.JSONDecodeError as e:

    print(f"Execution Halted: Malformed JSON payload. System Error: {e}")



        




        
    


    



    


