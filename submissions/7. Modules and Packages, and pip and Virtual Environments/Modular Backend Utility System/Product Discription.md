
---

# Section 3 — Mini Project ⭐⭐⭐

Now let's combine **modules + packages + pip + virtual environments + `__name__`**.

## Mini Project — Modular Backend Utility System

Imagine you're building the foundation of a small backend application.

Create:

```text
backend_app/
│
├── .venv/
│
├── requirements.txt
│
├── main.py
│
└── app/
    ├── __init__.py
    │
    ├── users/
    │   ├── __init__.py
    │   └── service.py
    │
    └── products/
        ├── __init__.py
        └── service.py
```

### Part A — User Module

`app/users/service.py`

Create:

```python
def create_user(name, email):
    return {
        "name": name,
        "email": email
    }
```

---

### Part B — Product Module

`app/products/service.py`

Create:

```python
def create_product(name, price):
    return {
        "name": name,
        "price": price
    }
```

---

### Part C — Main Application

`main.py`

Import both services and produce:

```text
User: {'name': 'Mahesh', 'email': 'mahesh@example.com'}
Product: {'name': 'Laptop', 'price': 55000}
```

---

### Part D — Main Guard

Inside `main.py`, use:

```python
if __name__ == "__main__":
```

to execute the application.

Explain why this is useful.

---

### Part E — External Dependency

Since you've already practiced `requests`, use it in the project.

Your project should be able to:

```python
import requests
```

without an import error.

Then make sure:

```text
requirements.txt
```

contains the dependency.

---

### Part F — Environment

Perform:

```text
Create .venv
      ↓
Activate
      ↓
Install dependencies
      ↓
Run application
      ↓
Deactivate
```

Then explain:

**What remains after deactivation?**

---

### Part G — Architecture Explanation

Finally explain:

```text
app
├── users
│   └── service.py
│
└── products
    └── service.py
```

What is:

* `app`?
* `users`?
* `products`?
* `service.py`?
* `__init__.py`?

---

## Section 4 — Debugging 🐛

### Q1 — Import Bug

```python
# calculator.py

def add(a, b):
    return a + b
```

```python
# main.py

import calculator

result = add(10, 20)

print(result)
```

Answer:

1. What error occurs?
2. Why?
3. Give **two different ways** to fix it.

---

### Q2 — `__name__` Bug

```python
# users.py

def greet():
    print("Hello")


if __name__ == "main":
    greet()
```

The developer expects:

```text
Hello
```

when running:

```bash
python users.py
```

but nothing happens.

Find the bug and fix it.

---

### Q3 — Virtual Environment Bug

A developer runs:

```bash
python -m venv .venv
```

Then:

```bash
pip install requests
```

Then:

```python
import requests
```

But another developer activates the project's `.venv` and gets:

```text
ModuleNotFoundError: No module named 'requests'
```

What could have happened?

Give the likely explanation and the correct workflow to fix it.

---

### Submit Sections 3 + 4 together.

After that I'll give you **Sections 5 + 6**, and we'll finish with your final `/100`, weak areas, revision plan, and whether you're ready for the next topic.
