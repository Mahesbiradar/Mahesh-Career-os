"""
Exercise C2 — Customer Order Grouping
Build customer_order_groups.py.

Requirements:
- Group orders by customer using defaultdict(list).
- Store order IDs under each customer.
- Count orders per customer.
- Print a customer summary.
- Handle an empty input list.
Make sure a customer with three orders has three order IDs in the result, not just the latest one.

"""

from collections import defaultdict


orders = [
    {"customer_id": "CUST-101", "order_id": "ORD-001"},
    {"customer_id": "CUST-102", "order_id": "ORD-002"},
    {"customer_id": "CUST-101", "order_id": "ORD-003"},
    {"customer_id": "CUST-103", "order_id": "ORD-004"},
    {"customer_id": "CUST-102", "order_id": "ORD-005"},
    {"customer_id": "CUST-101", "order_id": "ORD-006"},
    {"customer_id": "CUST-104", "order_id": "ORD-007"},
    {"customer_id": "CUST-102", "order_id": "ORD-008"},
    {"customer_id": "CUST-105", "order_id": "ORD-009"},
    {"customer_id": "CUST-101", "order_id": "ORD-010"},
    {"customer_id": "CUST-103", "order_id": "ORD-011"},
    {"order_id": "ORD-012"},
    {"customer_id": "CUST-104", "order_id": "ORD-013"},
    {"customer_id": "CUST-102", "order_id": "ORD-014"},
    {"customer_id": "CUST-105", "order_id": "ORD-015"},
    {"customer_id": "CUST-107", "order_id": "ORD-016"},
    {"customer_id": "CUST-101", "order_id": "ORD-017"},
    {"customer_id": "CUST-103", "order_id": "ORD-018"},
    {"customer_id": "CUST-102", "order_id": "ORD-019"},
    {"customer_id": "CUST-108", "order_id": "ORD-020"}
]


{"customer_id": "CUST-106",}

def group_orders(order_list):

    group_by_cutomer = defaultdict(list)

    keys = ["customer_id","order_id"]

    for order in order_list:

        is_valid = True

        for key in keys:

            if key not in order:

                is_valid = False
                
                break

        if not is_valid:

            print("Skipping the Current Record Due to incomplete Data")

            continue

        group_by_cutomer[order["customer_id"]].append(order["order_id"])
        

    return group_by_cutomer

# --- Test Scenario 1: Populate Mock Data ---
print("--- 1. Processing Full Orders List ---")

result = group_orders(orders)

for customer,items in result.items():

    print(f"Customer {customer}: Orders Count = {len(items)} | IDs = {items}")


# --- Test Scenario 2: Handle Empty Input List Edge Case ---


print("\n--- 2. Testing Empty Input Edge Case ---")

empty_orders = []

empty_result  = group_orders(empty_orders)

print(f"Resulting dictionary size: {len(empty_result)}")
print(f"Dictionary output: {dict(empty_result)}")








