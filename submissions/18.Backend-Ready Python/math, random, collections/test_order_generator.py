"""
Exercise R1 — Test Data Generator
Build test_order_generator.py.

Requirements:
- Generate 20 mock orders.
- Give each order a unique order ID.
- Randomize the status from a list of at least four statuses.
- Generate a non-negative amount within a range you define.
- Use random.seed() or a dedicated random.Random instance so the output can be reproduced.
- Print the records and verify that all IDs are unique.
"""

import random


random.Random(42)

statuses = ["pending", "processing", "completed", "failed"]


def generate_test_order(order_id):

    return{

        "order_id": order_id,
        "amount": round(random.uniform(100,5000),2),
        "status": random.choice(statuses)
    }

orders = []

seen = set()

for order_id in range(1,21):


    order = generate_test_order(f"ORD:{order_id:03d}")

    seen.add(order["order_id"])

    orders.append(order)


print("--- GENERATED ORDERS ---")
for o in orders:
    print(f"ID: {o['order_id']} | Amount: ${o['amount']:7.2f} | Status: {o['status']}")

print("\n--- UNIQUENESS VERIFICATION ---")
if len(orders) == len(seen):
    print(f"✅ Success: All {len(orders)} order IDs are completely unique.")
else:
    print("❌ Warning: Duplicate order IDs were detected!")


