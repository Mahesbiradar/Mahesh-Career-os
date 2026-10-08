
---

# Section 1 — Type Hints & `typing` Fundamentals

### **15 marks**

### Q1. Identify the types — 3 marks

For each function, write the correct parameter and return annotations.

**a)** Takes two strings and returns a string.

```python
def combine(first, second):
    return first + second
```

**b)** Takes a list of integers and returns a dictionary mapping each integer to its frequency.

```python
def frequency(numbers):
    ...
```

**c)** Takes an integer ID and returns either a string or `None`.

```python
def find_user(user_id):
    ...
```

---

# Ans:

```python
def combine(first: str, second: str) -> str:
    return first + second
```

```python
def frequency(numbers: list[int]) ->dict[int:int]:
    ...
```

```python
def find_user(user_id: int) -> str | None:
    ...
```

### Q2. `Optional` / `None` — 3 marks

Consider:

```python
def get_email(user_id: int) -> str | None:
    if user_id == 101:
        return "mahesh@example.com"
    return None
```

Answer:

**a)** What does `str | None` mean?

**b)** Why is the return type not simply `str`?

**c)** What should the caller consider before doing:

```python
email.upper()
```

---

# Ans: 

a : Here the function either resturns string or None

b: Because the function may return None also based on the condition defined inside the function therfor None is Mentioned and this info will helps the devoloper while working on the retuned result and proccessing this info further so suppose the function retunrned None so dev can handle this without Annotation he may things the function will return the string and process this data and if the function returns none then the next proceesing may crash.

c: The called shoud conside the edge case whne the function returns None.


### Q3. `Any` vs specific types — 3 marks

You have:

```python
from typing import Any

def process(data: Any) -> None:
    ...
```

Answer:

**a)** What does `Any` mean?

**b)** Why can excessive use of `Any` reduce the benefit of type hints?

**c)** In this API response:

```python
data = {
    "id": 101,
    "name": "Mahesh",
    "active": True
}
```

Would you prefer `Any` for the whole `data` value or a more specific annotation? Explain your reasoning.

---

# Ans:

A: Any referce to all data no specific type.
**b)** Why can excessive use of `Any` reduce the benefit of type hints?
B:Because annotation helps with information of what kind of spefic data the function excepts or returns excessive use of `Any` will not help to analyze the same any simply referce to anykind of data so No use of type hints here. 
C: for data i would use specific annotation insted of any because the data represents type so ill use the specific type and this helps devs to understand the type of data the function paramerts may expects or return type.

### Q4. `Callable` — 3 marks

You already learned Higher-Order Functions.

Consider:

```python
def apply_operation(a, b, operation):
    return operation(a, b)
```

Write the complete type annotations for this function using `Callable`.

The function should accept:

```text
a → int
b → int
operation → function accepting two ints and returning an int
```

and return an `int`.

---
# Ans:

```python

from collections.abc import Callable

def apply_operation(a: int, b:int, operation : Callable[[int,int],int]) -> int:
    return operation(a, b)
```


### Q5. Type hints vs runtime validation — 3 marks

Consider:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Someone calls:

```python
add("10", "20")
```

Answer:

**a)** Will Python automatically reject this because of the type hints?

**b)** What is the difference between a **type hint** and **runtime validation**?

**c)** What tool can be used to statically check code against type annotations?


# Ans:

A: No python will not reject this becuase of the type hints the type hints are just additional info of the data type. Pythone process the above function call add("10","20") and returns '1020' 

B: Type Hints (Static): Documentation for developers and IDEs about expected data types. They are evaluated before the code runs and do not stop execution if violated.Runtime Validation (Dynamic): Actual code instructions (like if statements or libraries like Pydantic) that check data values while the program is running and actively block bad data by raising errors.

C: A Static Type Checker tool can be used. The industry-standard example tool is mypy (other options include Pyright or Pyre).


