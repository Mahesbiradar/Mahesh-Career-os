
# Section 4 — Debugging & Output Prediction

**20 marks**

This section is deliberately different. **Don't modify the code first.** Tell me what happens and why.

## Q17 — Closure Debugging

**5 marks**

What happens when this code runs?

```python
def counter():
    count = 0

    def increment():
        count += 1
        return count

    return increment


c = counter()

print(c())
```

Answer:

1. Does it execute successfully?
2. If not, what exception occurs?
3. Why does Python produce that exception?
4. How would `nonlocal` fix it?

---

# Ans:
1. It will not execute and 
2. Python will raises UnboundLocalError exeption.
3. In python, any variable that is assigned value inside the function is automatically treated as local variable by Python at compile time, Beacuse python thinks count is local to increment it tries to read its corrent value before it has been assigned anything locally, which triggers the UnboundLocalError.
4. nonlocal explicitly tells python not to create a new local variable, but instead to modify the existing count variable located in enclosed function. 

## Q18 — Decorator Debugging

**5 marks**

Consider:

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function")
        func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

### Questions:

1. What will be printed?
2. Why isn't `result` equal to `30`?
3. What single change is required to fix the problem?

---

# Ans: 
1.
Calling function
None

2.In wrapper function we are executing the the originla target function but we are not returning the value returned value by target function after execution. 
3. in wrapper we shoud return the value returned by target function. Then the caller gets the value to print.

# fix this:
func(*args, **kwargs)

# To this:
return func(*args, **kwargs)


## Q19 — Predict the Output

**5 marks**

Don't run this code. Trace it manually.

```python
def decorator_a(func):

    def wrapper():
        print("A before")
        result = func()
        print("A after")
        return result

    return wrapper


def decorator_b(func):

    def wrapper():
        print("B before")
        result = func()
        print("B after")
        return result

    return wrapper


@decorator_a
@decorator_b
def test():
    print("Original")


test()
```

Write the **exact output order**.

---
# Ans:

A before
B before
Original
B after
A after

but here i was wrong intialy i thought it diffremtly.

## Q20 — Decorator + Closure Debugging

**5 marks**

Find the bug in this implementation:

```python
def limit_calls(limit):

    count = 0

    def decorator(func):

        def wrapper():

            if count < limit:
                count += 1
                return func()

            return "Limit exceeded"

        return wrapper

    return decorator
```

Then explain:

1. Why does this fail?
2. Which scope does Python consider `count` to belong to inside `wrapper()`?
3. What keyword is required?
4. Where should it be placed?

---

1.Due to UnboundLocalError exeption this fails.

2.Python considers count as local to wrapper 

3. To explicily access the count from the enclosed function nonlocal keyword is required.

4. It must be placed at the very beginning inside the wrapper() function


