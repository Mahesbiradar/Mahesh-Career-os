
---

# Section 5 — Output Tracing & Deep Understanding

**10 marks**

This is the last technical section.

## Q21 — Closure State

**5 marks**

Predict the **exact output** without running the code:

```python
def make_counter():

    count = 0

    def increment(step=1):
        nonlocal count
        count += step
        return count

    return increment


counter1 = make_counter()
counter2 = make_counter()

print(counter1())
print(counter1(5))
print(counter2())
print(counter1())
```

Give the exact four outputs **and explain why `counter1` and `counter2` don't share the same `count`.**

---

# Ans: 

1
6
1
7

Every time the make_counter called Python executes the function body from scratch. This creates a completely brand new, independent local scope and a fresh count variable in memory

when counter1 and counter2 returned they form two distict clousers. each clouser captures the unique variable from its own perspective modifying the state of counter1 dont affect the state of counter2

## Q22 — Decorator Order + Return Value

**5 marks**

Predict the **exact output**:

```python
def uppercase(func):

    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def exclaim(func):

    def wrapper():
        result = func()
        return result + "!"

    return wrapper


@uppercase
@exclaim
def greet():
    return "hello"


print(greet())
```

Then answer:

1. What is the decorator transformation?
2. Which wrapper executes first?
3. What value does `exclaim` receive from `greet()`?
4. What does `uppercase` finally return?

---


# Ans: 


1. greet = uppercase(exclaim(greet))

2. when we call greet it reffreing to wrapper of uppercase and starts execution the result inside uppercase refers to wrapper of exclaim the result inside the exclaim refers to original greet function and the greet function executes and returns the hello then the wrapper of exclaim adds ! with hello returned from greet function the returns hello! to result of uppercase_wrapper then uppercase wrapper returns the hello! by making uppercase Hello! to the caller greet().

3.exclaim recived hello from greet.

4.upper case finnalky return Hello!.
