
---

# Section 6 — Final Interview & Real-World Assessment

**10 marks**

This is the final section. No coding required unless you want to illustrate something.

### Q23 — Backend Application

**2 marks**

You're building a Django REST API.

You need to ensure that only authenticated users with the required role can execute certain operations.

Why would a **decorator** be useful for this?

Give **two advantages** over writing the same authorization logic separately inside every view/function.

---
# Ans: To ensure that only authenticate users with the required role can execute certain operations. we need mechanism which checks the authenticated users must perform that operation so we can achive this by two ways one is to write the authenticaion logic inside all the operation this results in redundant code and another way is where we can extend the functionality of the originla function without changing the original function here decorates does the same.

so insted of writing the same code inside the all operations we can write a single code and in decorator function and then. The function is passed thoeugh the decorator makes same thing here we simply @decorator on required operations and this ensures same thing what we required for authentication. inseatd of reting code at multiple location we can achive same thing woith decorators.

advantages of writing authorization logic using decorator over the separately inside every view/function.

1.Code Reusability
2.Centralised Maintenance and Scaling.

### Q24 — Closure vs Class

**2 marks**

You need to maintain a counter that stores state between function calls.

You can implement it using either:

```python
closure
```

or:

```python
class + object
```

Give **one situation where a closure is a good choice**, and **one situation where a class would be a better choice**.

---

# Ans: 

• When a Closure is a good choice: For simple, lightweight tasks with a single action, such as writing function decorators or a basic tracking counter. It has less memory overhead and keeps the code minimal.
• When a Class is a better choice: For complex states requiring multiple distinct actions (e.g., needing methods to increment, decrement, and reset a value). Classes allow you to cleanly organize multiple behaviors around the same data.


### Q25 — `partial()` vs Closure

**2 marks**

You have:

```python
def connect(host, port, timeout):
    ...
```

You frequently use:

```text
host = "localhost"
port = 5432
```

Would you prefer `partial()` or a closure for creating a reusable function with those values pre-filled?

Explain **why**.

---

# Ans: I would prefer partial() for creating a reusable function with those values pre-filled . beacuse partials are used to prefill the arguments. Whereas clousers are useful for the maintaing the state. if we use clouser here the we have to changes explicitly but using partiall we can pass prefilled arguments if we need to chnage then with function call we can pass the required value.

### Q26 — Decorator Design

**2 marks**

You create this decorator:

```python
def log_call(func):

    def wrapper(*args, **kwargs):
        print("Calling...")
        return func(*args, **kwargs)

    return wrapper
```

What important improvement should you make before using this in production code?

Explain why.

---

# Ans: I would add @wraps(func) decorater above the wrapper function defination because it preserver the metadata of the originla function. such as __name__,__doc__. which is critical in production for accurate logging, stack traces, and debugging tools.

### Q27 — Mental Model

**2 marks**

Complete this chain in your own words:

```text
Function
   ↓
Higher-Order Function
   ↓
Nested Function
   ↓
Free Variable
   ↓
Closure
   ↓
Decorator
```

Explain **how these concepts connect to each other**.

This is the most important question of the final section.

---

# Ans: 

Ill start from the bottom to top

Decorators are the functions whoich adds additionla functinlaity to the original function without modifying the original function.
decorators uses clousers to maintin the state. clousers maintain the state. Free variable are the variables used inside the function but thes variable are from the enclosed functions so clousers access these free variables. Nested fucntions are the functios which are written inside another function. and Heigher order functions are the functions which accepts other function as argument or returns the other function or does both. and Fucntions are the reusable code for performing specific task and this mental modal describels decoraters design.