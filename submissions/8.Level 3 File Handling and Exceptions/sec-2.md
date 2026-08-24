
---

# SECTION 4 — Debugging Round 🐛

Now **don't modify your mini-project**.

We'll test your ability to diagnose other people's code.

For each question, answer:

**1. What's wrong?
2. Why?
3. What happens?
4. How would you fix it?**

## 🐛 Debug Q1

```python
with open("data.txt", "r") as file:
    data = file.read()

print(data)

file.close()
```

What's wrong here?

---
# Here we dont need to close the file while using context managers.
# The with statement automatically closes the file once block of code executes and releases the resources.
# still the code runs and closing the closed file in python works but if we want to run a operations after the block of code on that file using the manuall file.close() raises the valueerror.
# Ill remove the file.close() line bcz it not usefull and redundant. 

## 🐛 Debug Q2

```python
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except Exception:
        print("Something went wrong")

    except FileNotFoundError:
        print("File not found")
```

There is an exception-handling problem here.

Identify it and explain **why** it is a problem.

---
# The problems lies in the line except Exception
# The except Exception catches all the exceptions and siply print the message given in next print statement and it causes dibugging difuclt bcz no specific error messages and even the next except block will alos not run.
# 
# Here to fix this ill remove the except Exception block and try to raise application specific exception and handle the same.
## 🐛 Debug Q3

```python
def get_marks(filename):
    try:
        with open(filename) as file:
            marks = []

            for line in file:
                marks.append(int(line))

            return marks

    except ValueError:
        print("Invalid mark")

    except FileNotFoundError:
        print("File missing")
```

The file contains:

```text
85
72
hello
91
```

Is the exception handling correct?

What happens to `marks`?

---

# No here we shoud raise exceptions whoile appending the marks to the list so we can eliminate non intergers and continue with next lines with above given exception it will not run even if single line contains the non int data.
# In the loop at the third line throws the valueerro.

# We can fix this by raising the exception or continue for non int lines data.

## 🐛 Debug Q4

```python
class InvalidAgeError(Exception):
    pass


def validate_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("Valid age")


try:
    validate_age(15)

except ValueError:
    print("Invalid age")
```

The programmer expects:

```text
Invalid age
```

to be printed.

What is wrong?

---

# Here the exception is raised with cutome exeption and the program prints the message written in the cutome exception. and not prints the line written aftre the valueerror statement.

# Even i need more deeper explain for this secnarioues pls explain

## 🐛 Debug Q5

```python
def load_config(filename):
    try:
        with open(filename) as file:
            for line in file:
                key, value = line.strip().split("=")
                print(key, value)

    except ValueError:
        print("Invalid configuration")
```

The file contains:

```text
host=localhost
port=5432
debug=True=extra
```

What happens when the third line is processed?

Which exception occurs and why?

---
# Here in whne the third line processed in file for this line we have 3 data but we are unpacking with two variables only.
# Not sure about which exception occuures.





