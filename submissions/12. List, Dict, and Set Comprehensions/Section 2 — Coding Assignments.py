"""

# Section 2 — Coding Assignments

**3 problems | 30 marks**

Here I want actual Python code, not pseudocode.


"""

"""

## Q11 — Easy — List Comprehension

**8 marks**

Given:

```python
numbers = range(1, 21)
```

Create **one list comprehension** that produces:

```text
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

Then explain in one or two sentences:

* what you're filtering
* what you're transforming

**Constraint:** Use a list comprehension. Do not use a normal `for` loop.

---

"""
numbers = range(1, 21)

even_squares = [x**2 for x in numbers if x % 2 == 0]

print(even_squares)

# We are filtering out the odd numbers to keep only the even values from the range. 
# We are then transforming each remaining even number by squaring it.


"""
## Q12 — Medium — Dictionary + Set

**10 marks**

Given:

```python
employees = [
    {"id": 101, "name": "Mahesh", "department": "Backend", "salary": 60000},
    {"id": 102, "name": "Rahul", "department": "HR", "salary": 45000},
    {"id": 103, "name": "Amit", "department": "Backend", "salary": 80000},
    {"id": 104, "name": "Priya", "department": "Finance", "salary": 55000},
    {"id": 105, "name": "Kiran", "department": "Backend", "salary": 70000},
]
```

Using comprehensions, create:

### A

A list containing the names of Backend employees earning **₹60,000 or more**.

Expected structure:

```python
["Mahesh", ...]
```

### B

A dictionary:

```text
employee_id → salary
```

for only Backend employees.

### C

A set containing all **unique department names**.

### D

A dictionary:

```text
employee_id → "eligible"/"not eligible"
```

where an employee is `"eligible"` if salary >= 60000, otherwise `"not eligible"`.

**Constraint:** Use comprehensions where appropriate. Don't write unnecessary loops.

---

"""

employees = [
    {"id": 101, "name": "Mahesh", "department": "Backend", "salary": 60000},
    {"id": 102, "name": "Rahul", "department": "HR", "salary": 45000},
    {"id": 103, "name": "Amit", "department": "Backend", "salary": 80000},
    {"id": 104, "name": "Priya", "department": "Finance", "salary": 55000},
    {"id": 105, "name": "Kiran", "department": "Backend", "salary": 70000},
]


# A.A list containing the names of Backend employees earning ₹60,000 or more.

result = [employee["name"] for employee in employees if employee["department"] == "Backend" and employee["salary"] >=60000 ]

print(result)


# B. A dictionary:

backend_employees = {employee["id"]:employee["salary"] for employee in employees if employee["department"] == "Backend"}

print(backend_employees)

# C.A set containing all unique department names.

departments = {employee["department"] for employee in employees}

print(departments)

# D.A dictionary:

eligibility_dict = {employee["id"]:"eligible" if employee["salary"] >= 60000 else "not eligible" for employee in employees}

print(eligibility_dict)

"""
## Q13 — Hard — Nested + Conditional Comprehension

**12 marks**

Given:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Create **three different results**.

### A — Flatten only even numbers

Expected:

```python
[2, 4, 6, 8]
```

### B — Preserve matrix structure, but transform values

Every even number should become its square.

Every odd number should become `0`.

Expected:

```python
[
    [0, 4, 0],
    [16, 0, 36],
    [0, 64, 0]
]
```

### C — Backend-style transformation

Imagine every row represents:

```text
[id, salary]
```

For example:

```python
employees = [
    [101, 60000],
    [102, 45000],
    [103, 80000],
    [104, 55000]
]
```

Create a dictionary:

```text
employee_id → salary
```

**only for employees earning >= 55000.**

Expected:

```python
{
    101: 60000,
    103: 80000,
    104: 55000
}
```

---

"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# A — Flatten only even numbers

even_numbers = [
    value
    for row in matrix
    for value in row if value % 2 == 0
    ]

print(even_numbers)

# B — Preserve matrix structure, but transform values

even_and_zeros = [

    [value**2 if value % 2 == 0 else 0 for value in row] 
    for row in matrix 
]

print(even_and_zeros)

# C — Backend-style transformation

employees = [
    [101, 60000],
    [102, 45000],
    [103, 80000],
    [104, 55000]
]


result = {row[0]:row[1] for row in employees if row[1] >= 55000}


print(result)

