"""
---

# Section 1 — Concept Questions 🧠

**10 questions — Easy → Medium → Hard**

Don't look for answers. Explain in your own words.

## Q1 — Module

What is a **Python module**?

Explain:

* What makes a file a module?
* Why do we create modules?
* Give one example.

---
# Python module is single file python code that can be reused in other python scripts.
Any standart file with extention as .py is python module. the filename becomes the module name when we import it.
we use python mudules which helps us in code reusibility write function once and use across multiple project or files without copy pasting it. and maintaininbilty large codebases are broken into small,organized files which helps in faster debugging.

Ex;

1.Define module(calculator.py)

def add(a,b):
    return a + b

2.Use module(main.py)

import calculator

result = add(10,20)

print(result)


## Q2 — Import

Explain the difference between:

```python
import math
```

and:

```python
from math import sqrt
```

What changes when you use each approach?

---
Ans: In first one we are importing the the package math and in second we are importing a specific module called sqrt from the math package.

when we import math we can use multiple modules from math like math.sqrt(num) . while using a specific thing is useful for specific purpose ex: sqrt(num)  no need to use math.sqrt(num)



## Q3 — Aliasing

What does this mean?

```python
import numpy as np
```

Why would developers use aliases?

Give one example of an alias you have seen in Python development.

---
## Ans: Here we are importing the library numpy in our script and we are using this library in our script as np we just renamed the library name in our project.
The aliaing shortens the longer librry names. speeding up typing during devolopment.improves the code readibility.

A very common alias used in data science, analytics, and backend reporting is for the Pandas library:

import pandas as pd

# Creating a DataFrame using the short 'pd' alias instead of typing 'pandas'
result = pd.Dataframe({"user":["mahesh"],"status":["active"]})


## Q4 — `__name__`

What is:

```python
__name__
```

What value does it generally have when:

```bash
python calculator.py
```

is executed directly?

What value does it have when `calculator.py` is imported by another module?

---

## Ans: The __name__ is a built in variable.
the __name__ contains the value when python calculator.py  is __name__='__main__'

when the above python calculator.py is executed the code after he __name__='__main__' is executed.

the built in varible have the value = module name when the module is imported by another module.

## Q5 — `__main__`

Explain:

```python
if __name__ == "__main__":
    print("Running directly")
```

Why do we use this pattern?

What happens when the file is imported instead of executed directly?

---

__main__ is value assigned to the inbuild varibale __name__.

We use the above given pattern to to test the modules or for debugging.
when we import model insted of executed deirectly then the code after the pattern doenot executes.

## Q6 — Module vs Package

Explain the difference between a **module** and a **package**.

Given:

```text
shop/
    __init__.py
    users.py
    products.py
```

Identify:

* Package
* Modules
* Purpose of `__init__.py`

---
#Ans: Module is a single file with extention .py and package is repository of related modules.

shop is the package contains the realted modules.
users.py and products.py are the modules.
__init__.py is used in old versions of python and the when python detected the __init__.py file it reads it as the this repo is the package.

## Q7 — `pip`

What is `pip`?

Explain the difference between:

```bash
pip install requests
```

and:

```python
import requests
```

---
## Ans:
# In python pip is standard external python package intaller.

# pip install requests installes the library called requests in the Environment. where as the the import requests imports the packages in the python scipts.


## Q8 — `requirements.txt`

Why do Python projects use:

```text
requirements.txt
```

What is the difference between:

```bash
pip freeze
```

and:

```bash
pip install -r requirements.txt
```

---

#Ans: the requirements.txt contains all the external dependencies installed installed or required in the project. and it helps other devolper to install depencies without finding themselves one by one.

# pip freeze is used to output the list if currently installed packages.while pip install -r requirements.txt is used to install all the external dependecies mentioned in the requirements.txt file



## Q9 — Virtual Environment ⭐

Why do we create virtual environments?

Suppose:

```text
Project A → Django 4.x
Project B → Django 5.x
```

Why could installing both globally cause problems?

How does `.venv` solve this?

---

## Ans: we create the virtual environment to isolate the project environment from the global pythin environment.
# installing both cause a dependency conflicts bcz python can only map s single version of a package to its global site-packages directory at one time.

A virtual environment creates an isolated sandbox for each individual project.

Global Python Installation (Clean / Base)
   ├── Project A Folder
   │     └── .venv/ ──> Isolated copies of Python & Django 4.x
   │
   └── Project B Folder
         └── .venv/ ──> Isolated copies of Python & Django 5.x

         


## Q10 — Complete Workflow ⭐⭐⭐

You're starting a new Python backend project.

Explain the purpose/order of these:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install requests
```

```bash
pip freeze > requirements.txt
```

```bash
deactivate
```

Also explain what happens to the project when you run `deactivate`.

---

# Ans. 1 installing the virtual environment to isolate project into sandbox. 2.Activating the virtual environment.3. installing the external libraruies or packages.4.lISTING THE THE External dependecies in the requirements.txt 5.Deactivating the vertual environment.

deactivating the vertual environment just deactivates the vertual environment it wont remove any files or folders. Just diactivates the venv.

"""

"""

# Section 2 — Practical Coding Assignments 💻

## Assignment 1 — Easy ⭐

### Create Your Own Module

Create:

```text
project/
│
├── main.py
└── calculator.py
```

### `calculator.py`

Create these functions:

```python
def add(a, b):
    ...

def subtract(a, b):
    ...

def multiply(a, b):
    ...
```

### `main.py`

Import your module and produce:

```text
Addition: 30
Subtraction: 10
Multiplication: 200
```

for:

```python
10, 20
```

### Extra requirement

Put a test statement inside:

```python
if __name__ == "__main__":
```

in `calculator.py`.

Demonstrate that the test statement runs when `calculator.py` is executed directly but **doesn't run when imported by `main.py`**.

---

Done in the project repo(package)

"""
#project/main.py

import calculator


addition = calculator.add(10,20)
subtraction = calculator.substract(10,20)
multiplication = calculator.multiply(10,20)


print(addition)
print(subtraction)
print(multiplication)

#__________

#project/calculator.py


def add(a, b):

    return a + b


def substract(a, b):

    return a - b

def multiply(a, b):

    return a * b


if __name__== "__main__":

    print("This line is printed inside the calculator.py")

    print(add(10,20))
    print(substract(10,20))
    print(multiply(10,20))


"""
# Assignment 2 — Medium ⭐⭐

## Create a Python Package

Create:

```text
backend/
│
├── main.py
│
└── shop/
    ├── __init__.py
    ├── users.py
    └── products.py
```

### `users.py`

Create:

```python
def create_user(name):
    return f"User created: {name}"
```

### `products.py`

Create:

```python
def get_product(product_id):
    return f"Product ID: {product_id}"
```

### `main.py`

Import both modules using:

```python
from shop import users
from shop import products
```

Then produce:

```text
User created: Mahesh
Product ID: 101
```

### Requirements

Also demonstrate:

1. Why `__init__.py` exists.
2. That `users.py` and `products.py` are modules.
3. That `shop` is the package.
4. Use `if __name__ == "__main__":` in at least one module.

---
# The requirements are done as per given isntructions.
1. the __init__.py exist bcz it indicates the package exist in this repo.
2.That `users.py` and `products.py` are modules  bcz these are the single python files consist of reuabale code.
3. shop is package bcz it contains the repo of related modules.
4. yes its created in both modules.

# Assignment 3 — Hard ⭐⭐⭐

## Environment + Dependency Workflow

Inside a new project:

```text
backend_project/
```

perform the following workflow.

### Step 1

Create:

```text
.venv/
```

using:

```bash
python -m venv .venv
```

### Step 2

Activate the environment.

### Step 3

Install:

```bash
requests
```

### Step 4

Verify that the package is available from the active environment.

For example, write a small Python file that successfully does:

```python
import requests
```

### Step 5

Create:

```text
requirements.txt
```

containing the installed dependency.

### Step 6

Deactivate the environment.

### Step 7 — Explain

Answer:

> After `deactivate`, does `.venv` disappear?

> What happens to the installed `requests` package inside `.venv`?

> If you activate `.venv` again, will the package still be available?

---

# Ans: All 6 steps are Done 
> No
> its exist in the .venv
> Yes
"""