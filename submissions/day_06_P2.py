
# Section 2 — Coding Assignments

"""

## Assignment 1 — Easy ⭐

### Reusable Calculator

Create a function:

```python
def calculate(a, b, operation):
    ...
```

It should support:

```text
add
subtract
multiply
divide
```

Example:

```python
calculate(10, 5, "add")       # 15
calculate(10, 5, "subtract")  # 5
calculate(10, 5, "multiply")  # 50
calculate(10, 5, "divide")    # 2.0
```

### Requirements

* Use `return`, not `print`, inside the function.
* Handle division by zero.
* Return a sensible result/message for an unsupported operation.
* Use `if/elif/else`.

### Think about

Why is returning the result better than printing it?

"""
def calculate(a, b, operation):

    if b == 0:
        return f"Pls Enter Valid number Divisible by zero is unsupported"

    if operation.lower() == "add":
        return a + b
    elif operation.lower() == "subtract":
        return a - b
    elif operation.lower() == "multiply":
        return a * b
    elif operation.lower() == "divide":
        return a / b
    else:
        return f"Pls Enter Valid operation such as add, substract, multiply, divide"

# explanation: Here in this functions we take 3 argumenets two as numvbers and one as operation.
# Here we handle divisible by zero as well as invalid operations also. and returns the sensible message or result.
# returning the result is more useful bcz we can use the same result in further program. if i just print the result then we cannot use result unless we return the same.


"""
# Assignment 2 — Medium ⭐⭐

## Flexible Student Record

Create a function:

```python
def create_student(name, age=18, *subjects, **details):
    ...
```

Example call:

```python
student = create_student(
    "Mahesh",
    22,
    "Python",
    "Django",
    "SQL",
    city="Bangalore",
    cgpa=8.64
)
```

The function should return:

```python
{
    "name": "Mahesh",
    "age": 22,
    "subjects": ("Python", "Django", "SQL"),
    "details": {
        "city": "Bangalore",
        "cgpa": 8.64
    }
}
```

### Requirements

1. `name` must be a required parameter.
2. `age` must have a default value of `18`.
3. `*subjects` must store all positional subjects.
4. `**details` must store additional information.
5. Return the complete dictionary.
6. Do not print from inside the function.

### Bonus

Call the function without providing `age`:

```python
create_student(
    "Rahul",
    "Python",
    "SQL",
    city="Pune"
)
```

Think carefully about how Python interprets positional arguments here.

"""
def create_student(name, age=18, *subjects, **details):
    student_details = {}

    student_details["name"] = name
    student_details["age"] = age
    student_details["subjects"] = subjects
    student_details["details"] = details

    return student_details

# student = create_student(
#     "Mahesh",
#     22,
#     "Python",
#     "Django",
#     "SQL",
#     city="Bangalore",
#     cgpa=8.64
# )

# print(student)

student = create_student(
    "Rahul",
    "Python",
    "SQL",
    city="Pune"
)

print(student)

#In the second test case the python interpreting the second argumnet python as age because of position sequnce. There for keyword arguments are useful for these types of use cases.



"""
# Assignment 3 — Hard ⭐⭐⭐

## Function Pipeline + Mutation

You are given:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Build the following functions:

### Part A — Transform

Create:

```python
def square_numbers(numbers):
    ...
```

Return a new list containing the square of every number.

Expected:

```python
[1, 4, 9, 16, 25, 36]
```

Use `map()` and `lambda`.

---

### Part B — Filter

Create:

```python
def get_even_numbers(numbers):
    ...
```

Return only even numbers.

Expected:

```python
[2, 4, 6]
```

Use `filter()` and `lambda`.

---

### Part C — Mutation Test

Create:

```python
def add_number(data, value):
    ...
```

The function should add `value` to the original list.

Example:

```python
numbers = [1, 2, 3]

add_number(numbers, 4)

print(numbers)
```

Expected:

```python
[1, 2, 3, 4]
```

**Do not use `global`.**

---

### Part D — Unpacking

Create:

```python
def calculate_total(a, b, c):
    return a + b + c
```

Then:

```python
values = [10, 20, 30]
```

Call the function using **list unpacking**.

Expected:

```text
60
```

---

### Part E — Dictionary Unpacking

Create:

```python
def display_student(name, age, city):
    print(f"{name} | {age} | {city}")
```

Given:

```python
student = {
    "name": "Mahesh",
    "age": 22,
    "city": "Bangalore"
}
```

Call `display_student()` using **dictionary unpacking**.

Expected:

```text
Mahesh | 22 | Bangalore
```

---

## Final Challenge

After completing all parts, create this pipeline:

```text
Original List
      ↓
square_numbers()
      ↓
get_even_numbers()
      ↓
Final Result
```

For:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Expected final result:

```python
[4, 16, 36]
```

"""



"""

# What I'm Evaluating

| Skill                           | Weight |
| ------------------------------- | -----: |
| Function design                 |    20% |
| `return` vs `print`             |    10% |
| Default arguments               |    10% |
| `*args` / `**kwargs`            |    15% |
| `map()` / `filter()` / `lambda` |    15% |
| Mutation vs reassignment        |    15% |
| `*` / `**` unpacking            |    15% |

### Important

For Assignment 3, **don't just make the code work**. After writing it, explain in your own words:

> Why does `add_number(numbers, 4)` modify the original list, while assigning `numbers = [...]` inside a function would not reassign the caller's variable?

That explanation is specifically testing the Q10 weakness from Section 1.

Submit all **three assignments together**, and I'll review them before we move to the mini project.

"""


### Part A — Transform

numbers = [1, 2, 3, 4, 5, 6]

def square_numbers(numbers):
     
    return list(map(lambda x:x*x,numbers))


print(square_numbers(numbers))


### Part B — Filter

def get_even_numbers(numbers):

    return list(filter(lambda x : x % 2== 0,numbers))

print(get_even_numbers(numbers))


### Part C — Mutation Test

numbers = [1, 2, 3]

def add_number(data, value):
    data.append(value)
    return data

print(add_number(numbers, 4))

print(numbers)


### Part D — Unpacking


def calculate_total(a, b, c):
    return a + b + c


values = [10, 20, 30]

print(calculate_total(*values))



### Part E — Dictionary Unpacking

def display_student(name, age, city):
    print(f"{name} | {age} | {city}")


student = {
    "name": "Mahesh",
    "age": 22,
    "city": "Bangalore"
}
display_student(**student)


## Final Challenge


numbers = [1, 2, 3, 4, 5, 6]


sqr_numbers=square_numbers(numbers)


print(get_even_numbers(sqr_numbers))



