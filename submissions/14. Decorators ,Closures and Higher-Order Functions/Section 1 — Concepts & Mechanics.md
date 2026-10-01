
---

## Section 1 — Concepts & Mechanics

**20 marks | 10 questions × 2 marks**

Answer in your own words. Keep each answer concise but technically precise.

### Q1

What is a **higher-order function** in Python?

Give **one example** of how a function can behave as a higher-order function.

---

# Ans: Heigher order functions are the functions which either:

1.acceptes another function are agruments,or
2.returns a function
3.or does both.

def execute(func):

    func()


def create_greeting():

    def greet():

        print(Hello!)
    
    return greet

Here create_greeting is heigher order function which returns another function.

### Q2

What is the difference between:

```python
def outer():
    def inner():
        pass

    return inner
```

and a **closure**?

---
# Ans: In this program the the outer function return the innner function unexecuted. this is example of heigher order function.

where as the clousers rememebers the enclosed variables and maintains the state even when the enclosing function stoped its execution.


### Q3

Consider:

```python
def multiplier(n):
    def multiply(x):
        return n * x
    return multiply
```

After:

```python
double = multiplier(2)
```

Where does `multiply()` get the value `n` from when `double(5)` is called?

Explain using the term **free variable**.

---
# Ans: The multiply() function gets a value n when double(5) is called from a free variable. a free variable is variable used inside a function but the varibale is not declared inside the function and its nonlocal so this varibles is from enclosed scope.

in the above code the double is varible which refers to non executed function multiply returned from the multiplier function and multiply get the value of n through the clouser which remebers the enclosing the variables and its state.

### Q4

What is a **closure**?

Your answer should mention the relationship between:

* nested function
* enclosing scope
* captured variable
* returned function

---
# Ans:

clouser is functions which remembers the enclosing varibles and enclosing state even the enclosing function stops execution.

The nested funtions access the variables and state from the enclosed functions even whne outer enclosed functions stops its execution this is done by enclouser. The varibles refered inside the nested functons from the nonlocal scope are the captured variables.


### Q5

Why is `nonlocal` required here?

```python
def counter():
    count = 0

    def increment():
        count += 1
        return count

    return increment
```

What would happen without `nonlocal count`?

---

# Ans: Here the python treates the count variable as local variable and we are trying the increment the variable value by one and python will produce the type error bcz here variable is not declaired yet if we want to access the enclosed variable from the enclode function counter we shoud use nonlocal so the function treates the count variable as nolocal and access it from enclosed function.



### Q6

What does `functools.partial()` allow us to do?

Explain this:

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
```

What exactly has `partial()` created for `square`?

---

# Ans:The partial is buit in tool which allows us to prefill the arguments values. 

in above code the partial() prefilled the exponent argumet value as 2 so now while calling the square() we need to pass only the base value.

and square is refering to the power function.

### Q7

Explain what this syntax means internally:

```python
@logger
def process():
    pass
```

Write the equivalent assignment **without using `@`**.

---
# Ans: The above code simply referred as

result = logger(process())

here when we call the function process it passes throw the decorater which adds additional functionality and then executes.

the equivalent assignment **without using `@` for the above code is as follow:

def logger(func):

    def wrapper():
        func()
    
    return wrapper

then 

def process():
    pass

result = logger(process)


### Q8

Why do we use:

```python
@functools.wraps(func)
```

inside a decorator?

Mention at least **two things** that can be preserved.

---
# Ans: the @functools.wraps(func) preserves the metadata related to the orginal function passed in the wraps(func)

the metadate such as __name__,__doc__ withoud the @functools.wraps(func) the these methods will reffer to the wrapper which we added funntionality in wrapper.


### Q9

Consider:

```python
@A
@B
def test():
    pass
```

In what order are the decorators **applied**?

Write the equivalent transformation.

---

# Ans:

result = A(B(test)) in this order decorates are applied.

The decorates are applied on basis of bottom to top. 

In application order the @B is appllied first wrapping the original test function.

then @A is applied second, wrapping the warapper retuned by B.

1.In execution order. on calling test() This triggers A's wrapper first

2.A's wrapper calls its internal function which triggres b's warapper.

3.B's wrapper calls its internal function, which finally executes the originla funtion test()




### Q10

Why does a decorator with arguments require an additional function layer?

For example:

```python
@repeat(3)
def greet():
    pass
```

Explain the roles of:

```text
repeat(3)
    ↓
decorator
    ↓
wrapper
```

---

# Ans: The decorater with arguments required and extra layer beacuse python evaluates the decorator expression before it ever looks at the target function.

whne we wruter @repeat(3), Python executes repeat(3) first, that execution must return a standard decorator function. which can then receive the great function. 


repeat(3) is confuguration layer its job is to accept the confugutaion argumenst. it created the clouser that remeberes the configuration arguments (3).

decorator the standard decorator layer. this is the actula decorator its only job is to recive the target function. it takes greet store it in clouser and 3 from the firts layer. creates the final layer and returns it.

wrappet- The execution layer. this runs the target function greet() when user calls greet()