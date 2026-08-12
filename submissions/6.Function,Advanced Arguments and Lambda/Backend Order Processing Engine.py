"""
# Section 3 — Mini Project ⭐⭐⭐

## Mini Project: Backend Order Processing Engine

This combines:

* Functions
* Parameters / arguments
* Default arguments
* `*args`
* `**kwargs`
* Dictionaries
* Lists
* Sets
* Conditions
* `return`
* `map()` / `filter()` / `lambda`
* Mutation
* Unpacking

The project is intentionally compact so you can finish it without eating into your DSA time.

---

## Initial Data

```python
orders = [
    {
        "id": 101,
        "customer": "Mahesh",
        "items": [500, 1200, 300],
        "city": "Bangalore"
    },
    {
        "id": 102,
        "customer": "Rahul",
        "items": [800, 400],
        "city": "Pune"
    },
    {
        "id": 103,
        "customer": "Anjali",
        "items": [1500, 700, 200],
        "city": "Bangalore"
    }
]
```

---

# Part A — Calculate Order Total

Create:

```python
def calculate_total(items):
    ...
```

Calculate the total using a loop.

Example:

```python
calculate_total([500, 1200, 300])
```

Expected:

```text
2000
```

### Rule

❌ Don't use `sum()`.

---

# Part B — Apply Discount

Create:

```python
def apply_discount(total, discount=0):
    ...
```

Rules:

```text
discount = 10 → 10% discount
discount = 20 → 20% discount
discount omitted → no discount
```

Example:

```python
apply_discount(2000, 10)
```

Expected:

```text
1800
```

Use `return`.

---

# Part C — Process Order

Create:

```python
def process_order(order, discount=0):
    ...
```

It should:

1. Calculate the order total.
2. Apply the discount.
3. Return a new dictionary:

```python
{
    "id": 101,
    "customer": "Mahesh",
    "city": "Bangalore",
    "total": 2000,
    "final_amount": 1800
}
```

For this example, assume a 10% discount.

---

# Part D — `*args`

Create:

```python
def calculate_extra_charges(*charges):
    ...
```

The function should accept any number of charges and return their total.

Example:

```python
calculate_extra_charges(50, 100, 25)
```

Expected:

```text
175
```

Use a loop.

---

# Part E — `**kwargs`

Create:

```python
def create_order_summary(order, **metadata):
    ...
```

Example:

```python
create_order_summary(
    orders[0],
    payment="UPI",
    status="Paid",
    delivery="Express"
)
```

Return:

```python
{
    "id": 101,
    "customer": "Mahesh",
    "payment": "UPI",
    "status": "Paid",
    "delivery": "Express"
}
```

You don't need to include the entire original order—only the fields shown above.

---

# Part F — `filter()` + `lambda`

Create:

```python
def get_large_orders(orders):
    ...
```

An order is considered **large** if its total is greater than `1500`.

Return the orders satisfying the condition.

You may use:

```python
filter()
```

and:

```python
lambda
```

But because the total isn't directly stored in the original order, think carefully about how you want to handle that.

---

# Part G — Unique Cities

Create:

```python
def get_unique_cities(orders):
    ...
```

Return a set containing the unique cities.

Expected:

```python
{"Bangalore", "Pune"}
```

---

# Part H — Unpacking

Use the following function:

```python
def display_order(order_id, customer, city):
    print(f"{order_id} | {customer} | {city}")
```

Given:

```python
order_data = {
    "order_id": 101,
    "customer": "Mahesh",
    "city": "Bangalore"
}
```

Call the function using:

```python
**
```

dictionary unpacking.

Expected:

```text
101 | Mahesh | Bangalore
```

---

# Part I — Final Pipeline ⭐⭐⭐

Now create:

```python
def generate_report(orders):
    ...
```

For every order:

1. Process the order.
2. Calculate the total.
3. Apply a 10% discount.
4. Store the processed result in a list.
5. Calculate the class/order statistics:

   * Number of orders
   * Total revenue **before discount**
   * Total revenue **after discount**
   * Unique cities

Return one dictionary:

```python
{
    "total_orders": 3,
    "revenue_before_discount": ...,
    "revenue_after_discount": ...,
    "unique_cities": {...},
    "orders": [...]
}
```

### Restrictions

❌ No `sum()`
❌ No `Counter`
❌ No external libraries

✅ Functions
✅ Loops
✅ Dictionaries
✅ Lists
✅ Sets
✅ `return`
✅ Default arguments
✅ `*args` / `**kwargs` where appropriate

---

## ⭐ Final Interview Challenge

After completing the project, answer this in **3–5 sentences**:

> In this project, why did we use functions instead of putting all the logic inside one large loop? Explain how this design would help if the backend application later added features such as tax calculation, multiple discount types, or different payment methods.

---

### Submission

You can submit **all Parts A–I together**. Don't worry about making it extremely Pythonic—I want to see **your reasoning and function design first**.


"""


orders = [
    {
        "id": 101,
        "customer": "Mahesh",
        "items": [500, 1200, 300],
        "city": "Bangalore"
    },
    {
        "id": 102,
        "customer": "Rahul",
        "items": [800, 400],
        "city": "Pune"
    },
    {
        "id": 103,
        "customer": "Anjali",
        "items": [1500, 700, 200],
        "city": "Bangalore"
    }
]

# Part A — Calculate Order Total

def calculate_total(items):

    total_amount = 0
    for amount in items:
        total_amount += amount

    return total_amount


# Part B — Apply Discount

def apply_discount(total, discount=0):

    return int(total*discount/100)

# Part C — Process Order


def process_order(order, discount=0):

    total = calculate_total(order["items"])

    discount = apply_discount(total,discount)

    order["total"]= total
    order["final_amount"]= total - discount

    # del order["items"]

    return order

# Part D — *args

def calculate_extra_charges(*charges):


    total_charges = 0

    for charge in charges:
        total_charges += charge

    return total_charges


# Part E — **kwargs

def create_order_summary(order, **metadata):

    for key, value in metadata:
        order[key] = value

    return order


# Part F — filter() + lambda

def get_large_orders(orders):

    large_orders = list(filter(lambda order : sum(order["items"])>1500,orders))

    return large_orders


# Part G — Unique Cities

def get_unique_cities(orders):

    unique_cities = set()

    for order in orders:

        unique_cities.add(order["city"])

    return unique_cities


# Part H — Unpacking

def display_order(order_id, customer, city):
    print(f"{order_id} | {customer} | {city}")


order_data = {
    "order_id": 101,
    "customer": "Mahesh",
    "city": "Bangalore"
}

# display_order(**order_data)


# Part I — Final Pipeline ⭐⭐⭐

def generate_report(orders):

    """
    1.Process the order.
    2.Calculate the total.
    3.Apply a 10% discount.
    4.Store the processed result in a list.
    
    """

    processed_orders = []

    for order in orders:

        processed_orders.append(process_order(order,10))

    # 5.Calculate the class/order statistics:

    final_report = {}

    total_orders = 0

    revenue_before_discount = 0

    revenue_after_discount = 0

    for order in processed_orders:

        total_orders += 1

        revenue_before_discount += order["total"]

        revenue_after_discount += order["final_amount"]

    cities = get_unique_cities(orders)

    final_report = {"total_orders":total_orders,"revenue_before_discount":revenue_before_discount,"revenue_after_discount":revenue_after_discount,"unique_cities":cities, "orders": processed_orders}


    return final_report


print(generate_report(orders))
























    

















   






