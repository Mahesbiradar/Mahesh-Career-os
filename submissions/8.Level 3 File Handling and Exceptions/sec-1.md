
---

# SECTION 1 — 10 Interview Questions

### 🟢 Easy — Q1

What is the difference between:

```python
open("data.txt", "r")
```

and

```python
open("data.txt", "w")
```

Also tell me what happens if `data.txt` already exists.

---

## Ans: Here in above code we have two modes of file handling. r (read) is used to read the entire file. if the file exist we can read the file through the read mode. Where as using th w(write) mode is used to write / overwrite the file. if file alredy exist the w mode overwrites the file.

### 🟢 Easy — Q2

What is the difference between these three?

```python
file.read()
file.readline()
file.readlines()
```

Give a simple example of when you would use each one.

---

## Ans: The read method is used to read the entire file ex: if i want the entire file content to print on my terminal ill use read() method. the readline() method is used to read the single line in the file. In case if i want to print the specific line in file ill use the readline() method. Whereas the readlines() method is used to read the lines as list. 

### 🟢 Easy — Q3

Consider:

```python
with open("users.txt", "r") as file:
    data = file.read()

print(data)
```

What is the purpose of the `with` statement here?

Why is this generally preferred over manually doing:

```python
file = open(...)
...
file.close()
```

---
## Ans: Here with is a context manager used to manage ths resources effectively.
In above code block the the context manager releases the resources once the code block is executed. 

suppose the user does open the file manually and then forgot to close the file untill the file is closed the resources are occupied by files are not realeased untill the file is closed therefor usingbthe with statement is preferred over the manually doing opening and closing here with statemnet automatically closed the file and relaeses the resources.


### 🟢 Easy → Medium — Q4

You have:

```text
users.txt
```

containing:

```text
Mahesh
Rahul
Amit
```

Write Python code that:

1. Reads the file.
2. Converts the contents into a list of names.
3. Removes the newline characters.
4. Prints the list.

Expected idea:

```text
["Mahesh", "Rahul", "Amit"]
```

---
## Ans:

with open("users.txt","r") as file:

    list_of_lines = file.read().splitlines()

    print(list_of_lines)


Here the read method read all the lines in file as single string. the splitlines method remove all \n newline text from the each line string and add each lines in file as string element in the list.


### 🟡 Medium — Q5

What is the difference between these?

```python
try:
    x = int(input())
except ValueError:
    print("Invalid input")
```

and

```python
try:
    x = int(input())
except Exception:
    print("Something went wrong")
```

**As an interviewer, I want to know:** which one would you generally prefer and why?

---

## Ans:

Here In both the code blocks the main diff is ine first block catches the Value error and prints the message invalid input. but the second block also catches the error but not specifies the error it generalize the error.It catches all the errors and its difficult to identify the bug.

I would prefer the first block of code as it catches the specic error and it woud help to debug as well as to display a relevant message. The second one will be genralized statement.


### 🟡 Medium — Q6

Explain the difference between:

```python
try
except
else
finally
```

Then answer this:

> Which block executes regardless of whether an exception occurs?

---
## Ans:

try: Houses the risky code that might throw an exception.except: Houses the error-handling code. It only runs if an exception occurs inside the try block.
else: Houses code that should run only if the try block succeeds without any errors. It prevents you from accidentally catching errors that you didn't mean to.finally: Houses cleanup code. It is guaranteed to run regardless of whether an exception was raised, caught, or completely unhandled.


### 🟡 Medium — Q7

What happens here?

```python
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except ValueError:
    print("Value error")
```

Will `"Value error"` be printed?

If not:

1. What exception occurs?
2. What happens to the program?

---

## ans:

Here the try block contains the buggy code block where the print statemnet is written to print the element at index 5 in list called number but index 5 not exist in list. Therefor the program raises index error.

The "Value error" is  not printed. bcz ite exception is index error not value error.    

1.index error.
2.Program will crash and raises the index error in the terminal.


### 🟠 Medium — Q8

Look at this function:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")

    return a / b
```

Why might we use `raise` here instead of simply returning:

```python
return None
```

Explain the difference conceptually.

---

## Ans:

In above code the raise keyword is used to handle the divisible by zero error. since diision by zero raises the division by zero error in python. therefor raise is useful intead of simply returning.

returning None my be simply return none all the time even if there is correct operation and returning none is not useful for next operations as well as debugging.

raise will be useful to detect the error early and usful for debugging but returning none may cause debugging deficult.


### 🔴 Hard — Q9

You are writing a small user-registration system.

You want to reject usernames shorter than 5 characters.

Would you do:

```python
def register(username):
    if len(username) < 5:
        raise ValueError("Username too short")
```

or create:

```python
class InvalidUsernameError(Exception):
    pass
```

and raise that?

**When would a custom exception make more sense?**

I'm looking for your reasoning, not just "custom exceptions are better."

---

## ans: Ill use custom exception bcz we can make cutome exception for the specific requirement and which are helpful in user friesdly exception for specific purpose.

### 🔴 Hard — Q10

Consider this:

```python
def read_numbers(filename):
    try:
        with open(filename, "r") as file:
            numbers = file.read().split()

        return [int(x) for x in numbers]

    except FileNotFoundError:
        print("File doesn't exist")

    except ValueError:
        print("File contains invalid data")

    finally:
        print("Finished processing")

result = read_numbers("numbers.txt")
```

Assume `numbers.txt` contains:

```text
10
20
hello
40
```

Answer **all four**:

1. What happens when the function runs?
2. Which exception occurs?
3. Does `finally` execute?
4. What is the value of `result`?

---

## Ans:
1.The function runs and opens the file and reads all the lines in files and added all lines as elements in list and which the lits comprehension block runs then when it reaches the hello element when python tries to convert this to int then python raises the exception and seaches the exeption block then the value erro block prints the message. and then cleanup code runs. and function terminates.
2.valueerror exception occures bcz hello is string cant be converted to int.
3.Yes finally excecutes bcz this executes all the time not dependent on exceptions.
4.None.
.
# SECTION 2 — 3 Coding Assignments

These are deliberately more practical than the questions.

**Don't look for solutions online.** Write the code yourself and send it to me. I'll review it like an interview.

---

## 🟢 Assignment 1 — Easy

### Simple File Reader

Create a function:

```python
def count_words(filename):
    ...
```

It should:

1. Open a text file safely using `with`.
2. Read the contents.
3. Count the total number of words.
4. Return the count.
5. Handle `FileNotFoundError`.

Example file:

```text
Python is easy to learn
Python is powerful
```

Expected result:

```text
7
```

**Bonus:** Handle an empty file.

---

## 🟡 Assignment 2 — Medium

### Student Marks Processor

Create:

```python
def process_marks(filename):
    ...
```

Suppose `marks.txt` contains:

```text
Mahesh,85
Rahul,72
Amit,91
Priya,66
```

Your function should:

1. Read the file using `with`.
2. Parse each line.
3. Store the data in a dictionary.
4. Calculate the average marks.
5. Return the dictionary and average.

For example, conceptually:

```python
{
    "Mahesh": 85,
    "Rahul": 72,
    "Amit": 91,
    "Priya": 66
}
```

Also handle:

* `FileNotFoundError`
* Invalid mark values using `ValueError`

**Don't use pandas.** This is a Python fundamentals assessment.

---

## 🔴 Assignment 3 — Hard

### Safe Configuration Loader

Create:

```python
def load_config(filename):
    ...
```

The file contains:

```text
host=localhost
port=5432
debug=True
```

Your function should:

1. Open the file safely.
2. Read each line.
3. Split each line into key/value.
4. Store the result in a dictionary.
5. Convert:

   * `port` → `int`
   * `debug` → `bool`
6. Handle a missing file.
7. Handle malformed lines.
8. Handle invalid integer values.
9. Use appropriate exceptions.
10. Create **at least one custom exception** for a configuration-specific error.

For example, a malformed line such as:

```text
invalid_line
```

should not silently pass.

---

## 🎯 How I want you to answer

Don't answer everything in one giant message if that's uncomfortable.

Start with:

**Q1 → Q10**

Then send:

**Assignment 1**

and your code.

I'll evaluate your answers **one by one**, point out exactly where your reasoning is correct/wrong, and **I will not reveal answers before your attempt**.

After we finish Sections 1 & 2, we'll move to **Section 3 + Section 4: Mini Project + Debugging**.
