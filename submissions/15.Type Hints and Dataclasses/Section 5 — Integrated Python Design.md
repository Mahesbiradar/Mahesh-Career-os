
# 🧠 Section 5 — Integrated Python Design
### **20 marks**

## Q18. Design a Typed User Model — 5 marks

Create a dataclass:

```python
@dataclass
class User:
    ...
```

Requirements:

- `id` → `int`
- `name` → `str`
- `email` → `str`
- `roles` → `list[str]`
- `is_active` → `bool`, default `True`

`roles` must use `default_factory` so every `User` gets an independent list.

Then write:

```python
def activate_user(user):
    ...
```

Requirements:

- Accept a `User`.
- Return `None`.
- Set the user's `is_active` to `True`.

Add complete type annotations.

---

# Ans:

```python
from dataclasses import dataclass,field

@dataclass
class User:

    id : int
    name : str
    email : str
    roles : list[str] = field(default_factory=list)
    is_active : bool = True


def activate_user(user: User) -> None:

    user.is_active = True

```




## Q19. Typed Transformation — 5 marks

Given:

```python
users = [
    User(1, "Mahesh", "mahesh@example.com", ["admin"], True),
    User(2, "Rahul", "rahul@example.com", ["user"], False),
    User(3, "Anita", "anita@example.com", ["user"], True),
]
```

Write:

```python
def get_active_emails(users):
    ...
```

Requirements:

- Input: list of `User`
- Output: list of strings
- Return the email addresses of only active users.
- Properly annotate the function.

Expected:

```python
[
    "mahesh@example.com",
    "anita@example.com"
]
```

You may use either a loop or comprehension.

---

# Ans:

``` Python 
users = [
    User(1, "Mahesh", "mahesh@example.com", ["admin"], True),
    User(2, "Rahul", "rahul@example.com", ["user"], False),
    User(3, "Anita", "anita@example.com", ["user"], True),
]

def get_active_emails(users : list[User])-> list[str]:

    result = [user.email for user in users if user.is_active]

    # for user in users:

    #     if user.is_active:
    #         result.append(user.email)

    return result


print(get_active_emails(users))

```


## Q20. Dataclass + Validation + Optional — 5 marks

Design:

```python
@dataclass
class Employee:
    ...
```

Fields:

```text
id
name
email
salary
manager
```

Requirements:

- `id` → `int`
- `name` → `str`
- `email` → `str`
- `salary` → `float`
- `manager` → another `Employee` **or `None`**
- `manager` should default to `None`

Add `__post_init__()`:

- salary cannot be negative
- name cannot be empty/whitespace

Then explain how you would represent an employee who has **no manager**.

> **Important:** You are being tested on your type design here. Think carefully about how you annotate `manager`.

---

``` Python
from __future__ import annotations  # Allows using 'Employee' inside its own definition
from dataclasses import dataclass

@dataclass
class Employee:

    id: int
    name : str
    email : str
    salary : float
    manager : Employee | None = None


    def __post_init__(self):

        if self.salary < 0:
            raise ValueError("Salary cannot be Negative")

        name = self.name

        if not name.strip():

            raise ValueError("name cannot be empty/whitespace")

```
# Explanation: to annotate an employee without manager , we simply ommit the manager argument during the instantiation,Because manager defaults to None


## Q21. Explain the Design — 5 marks

Consider this backend model:

```python
@dataclass
class Order:
    id: int
    customer_id: int
    items: list[str] = field(default_factory=list)
    total: float = 0.0
    status: str = "pending"
```

Answer:

### a)
Why is `items` using `default_factory=list` instead of:

```python
items: list[str] = []
```

### b)
Why can `customer_id: int` be more useful than simply storing:

```python
"customer_id": 101
```

inside an untyped dictionary?

### c)
Why might `status: str = "pending"` **not** require `default_factory`?

### d)
Would `frozen=True` necessarily be appropriate for an `Order` object? Explain your reasoning.

---
# Ans:

# A : Using default_factory list we are creating unique list for each object created from class Order whenare as using = [] is shared list amongst all the objects so it will be common list for all object not unique. Here we want the unique list for each object therefor we are used default_factory

# B: Type annotations explicitly tells the users what type of data it expects so user can pass the data without type annotation diffrent dev may assume the data type diffrent instead what actully it expects. as well as tye hints provide other benifts like IDE auto-completion, static type checking and preventing runtime errors.

# C: strings are immutable in python. since a string cannot be modified in place, sharing the defulkat value "pending" across multiple objects is completly safe and wont leak state. A default_factory is only required for mutable types.

# D: No, frozen=True would not be appropriate. An order is a dynamic business entity whose attributes must change over time Freezing the object would throw an error upon any state update.











