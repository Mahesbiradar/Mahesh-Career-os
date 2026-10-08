# 🧠 Section 6 — Backend Engineering Challenge
### **20 marks**

This is the most important section.

## Q22. Build a Small Typed Service Layer — 10 marks

You are building a small backend service.

Create:

```python
@dataclass
class Product:
    ...
```

with:

```text
id
name
price
stock
```

Use appropriate types.

Then create:

```python
def find_product(products, product_id):
    ...
```

Requirements:

- `products` → list of `Product`
- `product_id` → int
- return → `Product` **or `None`**
- return the matching product if found
- otherwise return `None`

Then create:

```python
def calculate_inventory_value(products):
    ...
```

Requirements:

For every product:

```text
price × stock
```

Calculate the total inventory value.

Properly annotate the function.

---

# Ans:

```Python 

from dataclasses import dataclass
@dataclass
class Product:

    id : int
    name : str
    price : float
    stock : int

def find_product(products: list[Product], product_id: int) -> Product | None:


    for product in products:

        if product.id == product_id:

            return product

    return None

def calculate_inventory_value(products: list[Product]) -> float:

    inventory_value = 0

    for product in products:

        inventory_value += product.price * product.stock

    return inventory_value

```


## Q23. API Response Model — 5 marks

Create:

```python
@dataclass
class APIResponse:
    ...
```

Requirements:

```text
status_code → int
message → str
data → optional dictionary
```

`data` should default to `None`.

Then create:

```python
def build_product_response(product):
    ...
```

Requirements:

- Accept `Product | None`.
- If product exists, return an `APIResponse` representing success.
- If product is `None`, return an `APIResponse` representing "Product not found".

Use appropriate status codes.

**Do not use `Any` unless you genuinely think it is necessary.**

---

# Ans:

```python

from dataclasses import dataclass , asdict


from dataclasses import dataclass
@dataclass
class Product:

    id : int
    name : str
    price : float
    stock : int

@dataclass
class APIResponse:

    status_code : int
    message : str
    data : dict | None = None


def build_product_response(product: Product | None) -> APIResponse:

    if product is None:

        return APIResponse(
            status_code = 404,
            message= "Product not found" 
        )

    product_dict = asdict


    return APIResponse(
        status_code=200,
        message= "Success",
        data = product_dict 
        )

```


## Q24. Code Review — 5 marks

A junior developer wrote:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    roles: list[str] = []

def create_user(name: str, roles: list[str] | None):
    if roles is None:
        roles = []

    return User(name, roles)
```

Identify **all important problems** you can find.

For each problem:

1. Explain why it is a problem.
2. Explain how you would fix it.

Don't just rewrite the code. I want your reasoning.

---

# Ans: 


1. The Mutable Default Argument Bug (Critical)

writing list[str] = [] in dataclass causes Python to throw a immediate ValueError at runtime.Python explicitly forbids using mutable defaults in dataclasses fields because that single list would be shared across all instances of User.If one user gets a new role, every user gets that role.

How to fix it: Use default_factory=field(default_factory=list) from the dataclasses module. This ensures a brand new, empty list is generated every single time a new User is instantiated.


2. Missing Return Type Hint in create_user (Minor/Best Practice)

The create_user function returns a User object, but it completely lacks a return type hint. For a code review question, omitting this hurts code readability and defeats the purpose of modern Python type hints.

How to fix it: Add -> User to the function signature.



3. Redundant Function Logic / Code Smell (Design)

The create_user function manually checks if roles is None: to assign an empty list. Because of this, the function is essentially doing the exact same job the dataclass's default values are designed to handle. It adds unnecessary boilerplate code.

Once default_factory is correctly set up in the dataclass, you can leverage it directly. If you want the factory function to accept None, you can default roles=None in the function arguments and handle it cleanly.


``` python
from dataclasses import dataclass, field
@dataclass
class User:
    name: str
    roles: list[str] = field(default_factory=list)

def create_user(name: str, roles: list[str] | None = None) -> User :
    # if roles is None:
    #     roles = []
    return User(name, roles)

```
