
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

### Your turn

Answer **Debug Q1 → Q5**.

Don't give me code immediately. **First explain the bug in your own words.** That will tell me whether you actually understand the exception flow or are just pattern-matching syntax.
