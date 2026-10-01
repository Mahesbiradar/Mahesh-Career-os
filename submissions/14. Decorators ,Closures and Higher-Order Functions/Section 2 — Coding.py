"""

# Section 2 — Coding

**20 marks**

Write actual Python code for each problem.

## Q11 — Higher-Order Function

**5 marks**

Create:

```python
apply_operation(operation, a, b)
```

It should accept a function and two numbers and return the result of applying that function.

Example:

```python
def add(a, b):
    return a + b
```

Expected:

```python
apply_operation(add, 10, 5)
# 15
```

Also make it work with:

```python
multiply
subtract
```

---
# Ans:
"""

def apply_operation(operation, a, b):

    return operation(a,b)


def add(a, b):

    return a + b

def multiply(a, b):

    return a * b

def subtract(a, b):

    return a - b


print(apply_operation(add,10,15))
print(apply_operation(multiply,10,15))
print(apply_operation(subtract,10,15))


"""
## Q12 — Stateful Closure

**5 marks**

Create:

```python
create_counter(start)
```

It should return a function that increments the counter by `1` every time it is called.

Example:

```python
counter = create_counter(10)

print(counter())  # 11
print(counter())  # 12
print(counter())  # 13
```

You **must use a closure** and `nonlocal`.

---
"""
def create_counter(start):

    count = start

    def counter():

        nonlocal count

        count += 1

        return count

    return counter


counter = create_counter(10)

print(counter())
print(counter())
print(counter())


"""
## Q13 — Decorator with `wraps`

**5 marks**

Create a decorator called:

```python
log_call
```

When applied:

```python
@log_call
def add(a, b):
    return a + b
```

Calling:

```python
add(3, 4)
```

should:

1. Print that the function is being called.
2. Execute the original function.
3. Return the original result.
4. Preserve the original function's metadata using `functools.wraps`.

---
"""
from functools import wraps

def log_call(func):

    @wraps(func)

    def wrapper(*args, **kwargs):
        print(f"The function {func.__name__} is being called with arguments args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        return result

    return wrapper


@log_call
def add(a, b):
    return a + b

print(add(100,15))

"""
## Q14 — Decorator with Arguments

**5 marks**

Create:

```python
@repeat(3)
def greet(name):
    return f"Hello {name}"
```

The decorator should execute the function **3 times**.

Expected conceptual behavior:

```text
Hello Mahesh
Hello Mahesh
Hello Mahesh
```

Your implementation must correctly handle the three layers:

```text
repeat(times)
    ↓
decorator(func)
    ↓
wrapper(*args, **kwargs)
```

---

"""

def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            result = None

            for _ in range(times):

                result = func(*args, **kwargs)

                print(result)

            return result

        return wrapper

    return decorator

    
@repeat(3)
def greet(name):

    return f"Hello {name}"

greet("Mahesh")

