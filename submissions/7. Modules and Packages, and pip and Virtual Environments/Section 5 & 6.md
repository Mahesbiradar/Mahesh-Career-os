
# Section 5 — Output Prediction 🔍

No running the code. Predict the output **exactly**.

## Q1 — Import + `__name__`

### `calculator.py`

```python
def add(a, b):
    return a + b


print("Calculator loaded")

if __name__ == "__main__":
    print("Calculator executed directly")
```

### `main.py`

```python
import calculator

print(calculator.add(10, 20))
```

What is the exact output when we run:

```bash
python main.py
```

Explain why both or only one of the messages appears.

## Ans: The O/p will be 
Calculator loaded
30

Here in calculator.py file contains two print statements the print("Calculator executed directly") is executed when the calculator.py file is executed but while we run the main file  the print("Calculator loaded") statement will be didplayed.
bcz its zero indented statement and it will run even if its imported from other module.

---

## Q2 — Package Import

Suppose:

```text
project/
│
├── main.py
└── shop/
    ├── __init__.py
    └── products.py
```

`products.py`:

```python
def get_price():
    return 500
```

`main.py`:

```python
from shop import products

price = products.get_price()

print(price)
```

What is the output?

Also explain the chain:

```text
shop → products → get_price()
```

---
## Ans: The O/p will be 500 

The main file import the module called products from the package shop. then the product module calls teh function get_price and the function return the value 500. same value is printed on disply.

## Q3 — Virtual Environment

Suppose:

```text
myproject/
├── .venv/
├── app.py
└── requirements.txt
```

You run:

```bash
.venv\Scripts\activate
pip install requests
deactivate
```

Then run:

```bash
python app.py
```

without activating `.venv`.

`app.py` contains:

```python
import requests

print("Success")
```

What can happen?


Don't just say "it works" or "doesn't work." Explain **why the result depends on which Python environment the final `python` command is using**.

---

# Ans: Here the venv deactivated and once we run app file python throughs the Nameerror : The requests module is not defined.bcz the module is installed in the venv but not the venv is deactivated and running app.py python trys to import requests in scipt but not found the installed files bcz of even deactivation.

# Section 6 — Interview Questions 🎯

Answer as if you're sitting in a Python backend interview. Keep each answer around **2–5 sentences**.

## Q1 — Modules vs Packages

> What is the difference between a Python module and a package?

Explain using a backend example.

---
# Ans: a single python file with extention .py is called module which contains reusable code blocks. and the package is directory of related modules and it caontains the package repo marking __init__.py file and related modules.

Ex:
backend/
    .venv/
    main.py
    app/
        __init__.py
        users.py

here in above structure the app is package contais the related modules and the package marking file __init__.py.
the users.py is the module contains the reusable code.


## Q2 — `__name__ == "__main__"`

An interviewer asks:

> "Why do we use `if __name__ == '__main__':` instead of simply writing the code directly at the bottom of the file?"

Give a practical explanation.

---
## Ans: we use `if __name__ == '__main__':` instead of simply writing the code directly at the bottom of the file bcz we write the code that need to be executes when the file is excuted and its useful for the file level execution and debugging.

Ex: suppose we have module which contians some functions we want to check these functions so we can write the function calls inside the __name__ == '__main__' bcz we dont want the the other files dircetly excutes the function calls without calling in the imported file.

## Q3 — pip vs Virtual Environment

> "What's the relationship between `pip`, a virtual environment, and `requirements.txt`?"

Explain how all three work together when onboarding a new developer to a backend project.

---
 ## Ans: pip is standard external python package installer and virtual environment isolates the project in the sandbox requirements.txt file contains the external packages installed in the project.

## So installing the vertual environment then activating the venv and the installing the packages and importing it into the files and then using pip freeze > requirements.txt where requirements.txt contains all the external dependecies Helps the project keep isolated in sandbox. 


## Q4 — Dependency Isolation ⭐

Suppose you have:

```text
Project A → requests 2.x
Project B → requests 3.x
```

Why is a separate `.venv` useful even though both projects use the same Python language?

---

## Ans: a seperate .venv is usful bcz each .venv isolates the prokject in sadndbox and avoids the conflicts b/w the packages. since both the modules are differnt version so keepng both are isolated using .venv is useful rather than isntalling in gloabal environment where python uses single module at a time this causes the conflict b/w same modules of differnt versions.

## Q5 — Backend Scenario ⭐⭐⭐

You join a backend team and receive this repository:

```text
backend/
├── app/
├── tests/
├── requirements.txt
└── README.md
```

You clone it onto your laptop.

Explain the **complete setup process from cloning the repository to running the application**, including:

* virtual environment
* activation
* dependency installation
* `requirements.txt`
* running the application

Don't just give commands—explain **why each step is needed**.

---

## Ans:

# First all will clone backend folder and then.
1.insatll venv (python -m venv .venv)
2.the activate the vertual environment (.venv\Scripts\Activate)
3.install all dependencies by running (pip install -r requirements.txt)
4.Then ill run the main app.

# First and second step isolates the project in python sandbox then installing the dependencies these dependencies will be installed in the same virtual environment so it will not cause the confilct of the modules. then we can run the application.



