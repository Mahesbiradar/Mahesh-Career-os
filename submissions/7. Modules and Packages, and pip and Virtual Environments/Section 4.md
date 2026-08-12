## Section 4 — Debugging 🐛

### Q1 — Import Bug

```python
# calculator.py

def add(a, b):
    return a + b
```

```python
# main.py

import calculator

result = add(10, 20)

print(result)
```

Answer:

1. What error occurs?
ans: NameError: name 'add' is not defined

2. Why?
ans: bcz the add is not explicity imported from the module called calculator or its not used as calculator.add

3. Give **two different ways** to fix it.
ans:
1.one way is calling both model and function as calculator.add() 
2.we can explicity import the function from module.  from calculator import add

---

### Q2 — `__name__` Bug

```python
# users.py

def greet():
    print("Hello")


if __name__ == "main":
    greet()
```

The developer expects:

```text
Hello
```

when running:

```bash
python users.py
```

but nothing happens.

Find the bug and fix it.

---

ans: the module levelm varible value shoud be '__main__' not "main" by using '__main__' we can fix the same.

### Q3 — Virtual Environment Bug

A developer runs:

```bash
python -m venv .venv
```

Then:

```bash
pip install requests
```

Then:

```python
import requests
```

But another developer activates the project's `.venv` and gets:

```text
ModuleNotFoundError: No module named 'requests'
```

What could have happened?

ans: Here as per the above commands the virtual envornment is installed but not activated and the and then the reqestes package is installed and this pacakge is installed in global env then the another user activated the virtual env therefor the error occured bcz python venv dont have any package called requests in venv.

Give the likely explanation and the correct workflow to fix it.

To fix this 1.Either the first devolope must activate the venv before importing the package 2.Either the dev2 shoud install package once again after activating venv then he can import packages in scripts.

---

### Submit Sections 3 + 4 together.

After that I'll give you **Sections 5 + 6**, and we'll finish with your final `/100`, weak areas, revision plan, and whether you're ready for the next topic.
