# List Comprehentions 

# numbers = [2, 4, 6, 8, 10]

# cubes = [num**3 for num in numbers]

# print(cubes)

# half = [num//2 for num in numbers]

# print(half)

# strings = [str(num) for num in numbers]

# print(strings)


# Conditional experesion vs conditional filtering

numbers = [1, 2, 3, 4, 5, 6]

# conditional filtering


even = [num for num in numbers if num % 2 == 0]

print (even)

# Conditional experesion

odd = [num if num % 2 == 0 else 0 for num in numbers]

print(odd)


square = [num**2 for num in numbers if num % 2 == 0]

print (square)


# 7. Dictionary Comprehension

employees = {
    "Mahesh": 60000,
    "Rahul": 45000,
    "Amit": 80000,
    "Priya": 55000
}

a = {name:salary for name,salary in employees.items() if salary >= 55000}

print(a)

b = {name:salary+int(salary*0.10) for name,salary in employees.items()}

print(b)

c = {name:salary*2 for name,salary in employees.items()}

print(c)


# 11. Set Comprehension



# Exercise 1 — List
"""
Given:

numbers = range(1, 21)

Create:

1. squares
2. even numbers
3. squares of even numbers
4. numbers divisible by 3
5. "even"/"odd" labels

"""

numbers = range(1, 21)

squares = [x**2 for x in numbers]

even = [x for x in numbers if x % 2 == 0]

even_squares = [x**2 for x in numbers if x % 2 == 0]

divison = [x for x in numbers if x % 3 == 0]

even_odd = ["even" if x % 2 == 0 else "odd" for x in numbers]

print(squares)
print(even)
print(even_squares)
print(divison)
print(even_odd)

# Exercise 2 — Dictionary

"""
Given:

names = ["Mahesh", "Rahul", "Amit", "Priya"]
marks = [85, 72, 91, 66]

Create:

{
    "Mahesh": 85,
    "Rahul": 72,
    "Amit": 91,
    "Priya": 66
}

Then create another dictionary containing only students with marks ≥ 75.

"""

names = ["Mahesh", "Rahul", "Amit", "Priya"]
marks = [85, 72, 91, 66]


student_marks ={name:marks for name,marks in zip(names,marks)}

distinction_students = {name:marks for name,marks in student_marks.items() if marks >= 75}

print(student_marks)
print(distinction_students)


# Exercise 3 — Set

"""
Given:

words = [
    "python",
    "django",
    "python",
    "redis",
    "django",
    "postgresql"
]

Create a set containing the lengths of unique words.

"""

words = [
    "python",
    "django",
    "python",
    "redis",
    "django",
    "postgresql"
]

len_words = {len(word) for word in words}

print(len_words)

# Exercise 4 — Nested

"""
Exercise 4 — Nested

Given:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Create:

1. flattened list
2. flattened even numbers
3. matrix with every value × 10
4. squares while preserving matrix structure

"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_list = [value for raw in matrix for value in raw]

print(flattened_list)

flattened_even = [value for raw in matrix for value in raw if value % 2 == 0]

print(flattened_even)

transform_matrix =[
    [value*10 for value in raw]
    for raw in matrix
]

print(transform_matrix)

transform_matrix_2 =[
    [value**2 for value in raw]
    for raw in matrix
]
print(transform_matrix_2)

# Exercise 5 — Backend-style 🔥

"""
Given:

users = [
    {"id": 101, "name": "Mahesh", "active": True},
    {"id": 102, "name": "Rahul", "active": False},
    {"id": 103, "name": "Amit", "active": True},
    {"id": 104, "name": "Priya", "active": False},
]

Create:

1. List of active users
2. List of active usernames
3. Dictionary: id → name for active users
4. Set of all usernames
5. Dictionary: id → "active"/"inactive"

This is particularly relevant because your previous backend work already involves transforming collections of records into filtered lists and lookup dictionaries.

"""
users = [
    {"id": 101, "name": "Mahesh", "active": True},
    {"id": 102, "name": "Rahul", "active": False},
    {"id": 103, "name": "Amit", "active": True},
    {"id": 104, "name": "Priya", "active": False},
]

list_of_active_users = [user["id"] for user in users if user["active"]]

print(list_of_active_users)

list_of_active_usernames = [user["name"] for user in users if user["active"]]

print(list_of_active_usernames)

active_users = {user["id"]:user["name"] for user in users if user["active"]}

print(active_users)

set_of_users = {user["name"] for user in users}

print(set_of_users)

dictionary = {user["id"]:"active" if user["active"] else "inactive" for user in users}

print(dictionary)


