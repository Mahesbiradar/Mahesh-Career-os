
# 🧠 Section 4 — Backend Design & Type Reasoning
### **15 marks**

This section is deliberately more realistic.

### Q14. API Response Design — 5 marks

You need to represent these API responses:

### Success

```json
{
    "status": 200,
    "message": "User fetched",
    "data": {
        "id": 101,
        "name": "Mahesh"
    }
}
```

### Failure

```json
{
    "status": 404,
    "message": "User not found",
    "data": null
}
```

Design a dataclass:

```python
@dataclass
class APIResponse:
    ...
```

Requirements:

- Proper type annotations.
- `data` must be able to represent both the dictionary and `None`.
- `data` should default to `None`.

Then write:

```python
def is_success(response):
    ...
```

with proper type annotations.

It should return `True` when the status code is in the successful HTTP range `200–299`, otherwise `False`.

---

# Ans: 


```python
from dataclasses import dataclass
@dataclass
class APIResponse:

    status : int
    message : str 
    data : dict | None = None


def is_success(response: APIResponse) -> bool:

    return 200 <= response.status <= 299


suceess_responce = APIResponse(
    status=200,
    message="User fetched",
    data={
        "id": 101,
        "name": "Mahesh"
    })

failure_responce = APIResponse(
    status = 404,
    message ="User not found",
    data = null
)

print(is_success(suceess_responce))
print(is_success(failure_responce))

    ...


### Q15. Dataclass vs Dictionary — 3 marks

Suppose you have:

```python
user = {
    "id": 101,
    "name": "Mahesh",
    "email": "mahesh@example.com"
}
```

and:

```python
@dataclass
class User:
    id: int
    name: str
    email: str
```

Answer:

**a)** Give **two advantages** of using the dataclass instead of the dictionary for a structured backend model.

**b)** Give **one situation** where a dictionary might still be more appropriate.

Don't just say "dataclass is better." Explain the reasoning.

---

# Ans:

A: Two advantages of using the dataclass instead of the dictionary for a structured backend model.

1. Type safety and IDE support: Dataclasses enforces explicit data type for each feild. This allows our IDE to provide autucomlete suggestions and flag type mismatches before we run the code.
2.We can access the data cleanly using user.name intead of user["name"]. This prevents typos that cause KeyError crashes at runtime.

B:Dictionaries are better when the data structure changes frequenty, has unpredictable keys,or is arbitatry data,where we don't want to define a rigid schema upfront.


### Q16. Find the Type Problem — 4 marks

Consider:

```python
def calculate_total(
    prices: list[float],
    discount: float | None
) -> float:

    total = sum(prices)

    if discount is not None:
        total = total - discount

    return total
```

A developer changes it to:

```python
def calculate_total(
    prices: list[float],
    discount: float | None
) -> float:

    total = sum(prices)

    total = total - discount

    return total
```

Answer:

**a)** What type-related problem exists?

**b)** Why does `discount: float | None` require special handling?

**c)** What kind of error could occur at runtime if `discount` is actually `None`?

---

# Ans:

A: The code attempts to perform an arithmetic subtraction (total - discount) without verifying if discount is None. Because discount is annotated as float | None, it can be a non-numeric type, which violates type safety rules.

B:The type hint float | None is a Union type. This means the value can be a valid float or a NoneType. Because the discount may contain the Value None and we cant perform any operation None with float or int values and this will crash we not handel the discount.

C: If the discount is actully None then the Type error occur at runtime.



### Q17. Mini Design Challenge — 3 marks

Design a dataclass for a backend **`Order`**.

It must contain:

```text
id
customer_name
items
total_amount
status
```

Requirements:

- `id` → integer
- `customer_name` → string
- `items` → list of strings
- `total_amount` → float
- `status` → string with default `"pending"`
- Each order must get its **own independent items list**

Write only the dataclass.

Then briefly explain why `default_factory` is needed for `items`.

---

# Ans:




```python
from dataclasses import dataclass,field

@dataclass

class Order:

    id: int
    customer_name: str
    total_amount: float
    items: list[str] = field(default_factory=list)
    status: str = "pending"
    
```

# default_factory is needed for items because each object created using Order class needs a unique - independent items list without the default_factory this list is hared amongsts the objects created using the Order class.