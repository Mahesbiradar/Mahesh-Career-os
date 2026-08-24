
---

# SECTION 5 — Output Prediction

Now let's test whether you can mentally execute Python code.

**Do not run these.**

For each question, give me the **exact output** or tell me the exact exception.

---

## 🧪 Output Q1

```python
try:
    x = int("10")
except ValueError:
    print("A")
else:
    print("B")
finally:
    print("C")
```

What is the output?

---
# Ans:
B
C
# Bcz the try block runs succesfully therefor the else block prints the b and finnaly block code cleaning runs irrespective of exceptions.

## 🧪 Output Q2

```python
try:
    x = int("hello")
except ValueError:
    print("A")
else:
    print("B")
finally:
    print("C")
```

What is the output?

---
# Ans:
A
C
Here the try block raise the value error bcz "hello" cant be converted into int. and the except block print the error message A. and finally block prints C

## 🧪 Output Q3

```python
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except ValueError:
    print("Value")
except IndexError:
    print("Index")
finally:
    print("Done")
```

What is the output?

---
# Ans:

Index
Done

Here the try block raises the index error bcz the list has only 4 elemenets and aceesing the 5th index raises index error.and finnaly blockprints the Done.


## 🧪 Output Q4

```python
class MyError(Exception):
    pass


try:
    raise MyError("Something went wrong")
except Exception:
    print("Exception")
except MyError:
    print("MyError")
```

What is the output?

**Be careful. This tests exactly the hierarchy issue we just discussed.**

---
# Ans:
Exception

Here the exception is the main branch and the cuxtome exetion is a part of the Eception so cutome exception will not run bcz python cathes the Exception and never reaches the My error bcz of hierarchy Exception has a first priority as it catches lla the exceptions

## 🧪 Output Q5

```python
try:
    print("A")

    with open("missing.txt", "r") as file:
        print("B")

except FileNotFoundError:
    print("C")

else:
    print("D")

finally:
    print("E")

print("F")
```

Assume `missing.txt` does not exist.

Give the exact output order.

---

# Ans:

A
C
E
F

Here the program start at try block and prints A then it raises the file not found error bcz file doesnt exist and then python cathes the FileNotFoundError and Prints the C else block not runs and finnaly block prints the E and the next print statment excutes and prints the F


### Your turn

Answer **Output Q1 → Q5**.

After I evaluate those, we'll do **Section 6 — 5 interview questions**, and then I'll give you your **final /100 score, weak areas, revision plan, and whether you're ready for the next topic.**
