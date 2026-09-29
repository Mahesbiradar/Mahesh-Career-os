
# Section 3 — Mini Project

# **15 marks**

### 🛒 Mini Project: Lazy Active Order Processor

"""

You are building a backend system that receives a large number of orders.

Each order looks like:

```python
orders = [
    {"id": 101, "user_id": 1, "status": "completed", "amount": 500},
    {"id": 102, "user_id": 2, "status": "pending", "amount": 300},
    {"id": 103, "user_id": 1, "status": "completed", "amount": 700},
    {"id": 104, "user_id": 3, "status": "cancelled", "amount": 200},
    {"id": 105, "user_id": 2, "status": "completed", "amount": 900},
]
```

Your task is to build a **lazy processing pipeline**.

### Requirements

Create a generator function:

```python
completed_orders(orders)
```

It should yield only orders whose:

```python
status == "completed"
```

Then create another generator:

```python
order_amounts(orders)
```

which uses the first generator and yields only the `amount` of each completed order.

Finally, use the generator to calculate the **total amount of completed orders**.

Expected total:

```text
2100
```

### Constraints

1. Use `yield`.
2. Do **not** create a list of completed orders.
3. Do **not** use `sum()` for the final total.
4. The processing should remain lazy.
5. Use a `for` loop to calculate the final total.

### What I want from you

Submit:

```python
# your complete solution
```

Then briefly explain:

**Why is this design more memory-efficient than first creating a list of all completed orders?**

---

"""


orders = [
    {"id": 101, "user_id": 1, "status": "completed", "amount": 500},
    {"id": 102, "user_id": 2, "status": "pending", "amount": 300},
    {"id": 103, "user_id": 1, "status": "completed", "amount": 700},
    {"id": 104, "user_id": 3, "status": "cancelled", "amount": 200},
    {"id": 105, "user_id": 2, "status": "completed", "amount": 900},
]

def completed_orders(orders):

    for order in orders:

        if order["status"] == "completed":
            yield order

processed_orders = completed_orders(orders)

def order_amounts(orders):

    for order in orders:
        yield order["amount"]

amount_orders = order_amounts(processed_orders)

total_amount = 0

for amount in amount_orders:

    total_amount += amount

print(total_amount)


# Then briefly explain:

"""
In this above design is we store the list of all completed orders this cost an O(k) memory bcz all the compled oredes stored in the memory.
whereas in the above implemented lazy processing pipeline. which processes one odred at time and no need to store the data in list we just compute the sum amount of all completed orders and stire teh sum in total amount which cost O(1). Therefor this desing is more more efficient than storing the completed orders in a list.

"""


