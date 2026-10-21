
"""
[ ] 4. CSV report generator

Medium
10 marks

Create `csv_report.py`. Given a list of order dictionaries, write a CSV with the columns order_id, customer, status, and amount. 

Include a header, use DictWriter, and reopen the generated file to verify the rows.

"""

import csv


orders_data = [
    {
        "order_id": "ORD-2026-001",
        "customer": "Alex Mercer",
        "status": "processing",
        "amount": 128.50
    },
    {
        "order_id": "ORD-2026-002",
        "customer": "Elena Rostova",
        "status": "completed",
        "amount": 250.00
    },
    {
        "order_id": "ORD-2026-003",
        "customer": "Marcus Vance",
        "status": "pending",
        "amount": 540.75
    },
    {
        "order_id": "ORD-2026-004",
        "customer": "Diana Prince",
        "status": "shipped",
        "amount": 19.99
    },
    {
        "order_id": "ORD-2026-005",
        "customer": "Bruce Wayne",
        "status": "completed",
        "amount": 12500.00
    }
]


def csv_report(data):


    fieldnames = ["order_id", "customer", "status", "amount"]


    with open("orders_export.csv", "w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(data)

    print("\n--- Reopening CSV File for Verification ---")

    with open("orders_export.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            print(f"Verified Row: {row}")
    

csv_report(orders_data)

