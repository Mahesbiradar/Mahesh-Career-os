"""
Exercise C1 — Order Status Analytics
Build order_analytics.py.

Requirements:
- Create or load at least 20 order records.
- Use Counter to count orders by status.
- Display the two most common statuses.
- Count how many records have each rejection reason.
- Include a status that does not appear in the input and safely retrieve its count.
Focus on getting correct counts without manually maintaining separate counters for every status.

"""
from collections import Counter


orders = [
    {"order_id": "ORD-001", "status": "completed", "rejection_reason": None},
    {"order_id": "ORD-002", "status": "failed", "rejection_reason": "Insufficient Funds"},
    {"order_id": "ORD-003", "status": "processing", "rejection_reason": None},
    {"order_id": "ORD-004", "status": "completed", "rejection_reason": None},
    {"order_id": "ORD-005", "status": "failed", "rejection_reason": "Timeout"},
    {"order_id": "ORD-006", "status": "pending", "rejection_reason": None},
    {"order_id": "ORD-007", "status": "completed", "rejection_reason": None},
    {"order_id": "ORD-008", "status": "failed", "rejection_reason": "Insufficient Funds"},
    {"order_id": "ORD-009", "status": "processing", "rejection_reason": None},
    {"order_id": "ORD-010", "status": "completed", "rejection_reason": None},
    {"order_id": "ORD-011", "status": "pending", "rejection_reason": None},
    {"order_id": "ORD-012", "status": "failed", "rejection_reason": "Invalid Address"},
    {"order_id": "ORD-013", "status": "completed", "rejection_reason": None},
    {"order_id": "ORD-014", "status": "processing", "rejection_reason": None},
    {"order_id": "ORD-015", "status": "failed", "rejection_reason": "Insufficient Funds"},
    {"order_id": "ORD-016", "status": "completed", "rejection_reason": None},
    {"order_id": "ORD-017", "status": "pending", "rejection_reason": None},
    {"order_id": "ORD-018", "status": "processing", "rejection_reason": None},
    {"order_id": "ORD-019", "status": "completed", "rejection_reason": None},
    {"order_id": "ORD-020", "status": "failed", "rejection_reason": "Timeout"}
]

print("--- 1. Order Counts by Status ---")

status_counts = Counter(order["status"] for order in orders)
print(status_counts)


print("\n--- 2. Two Most Common Statuses ---")
print(status_counts.most_common(2))


print("\n--- 3. Rejection Reason Frequencies ---")
rejections  = [order["rejection_reason"] for order in orders if order["rejection_reason"] is not None]
rejection_counts = Counter(rejections)
print(rejection_counts)

print("\n--- 4. Safe Retrieval of Non-Existent Status ---")
print(f"Count for missing status 'cancelled': {status_counts['cancelled']}")