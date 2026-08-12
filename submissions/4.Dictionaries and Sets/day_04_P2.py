
# Assignment 1 — Easy ⭐

"""
## Student Record Manager

You are given the following dictionary:

```python
student = {
    "name": "Mahesh",
    "age": 22,
    "branch": "ENTC",
    "cgpa": 8.64
}
```

### Perform the following operations:

1. Print the student's name.
2. Update the CGPA to `8.80`.
3. Add a new key:

```python
"city": "Bangalore"
```

4. Remove the `"age"` key.
5. Print all keys.
6. Print all values.
7. Print every key-value pair in this format:

```
name -> Mahesh
branch -> ENTC
cgpa -> 8.80
city -> Bangalore
```

---
"""
student = {
    "name": "Mahesh",
    "age": 22,
    "branch": "ENTC",
    "cgpa": 8.64
}

print(f"name -> {student['name']}")

student["cgpa"] = 8.80

student["city"] = "Bangalore"

del student["age"]

for key in student.keys():
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(f"{key} -> {value}")

"""

# Assignment 2 — Medium ⭐⭐

## Word Frequency Counter

Write a program that counts the frequency of each word in a sentence.

Example:

```python
sentence = "python is easy python is powerful"
```

Expected Output:

```
python : 2
is : 2
easy : 1
powerful : 1
```

### Requirements

* Use a dictionary.
* Do **not** use `Counter`.
* Convert the sentence into words using `split()`.
* Handle repeated words correctly.

### Bonus Challenge

Print only the words whose frequency is greater than `1`.

---
"""

sentence = "python is easy python is powerful"

sentence_list = sentence.split()

words_freq = {}

for i in sentence_list:
    words_freq[i] = words_freq.get(i,0)+1

for key,value in words_freq.items():

    if value > 1:

        print(f"{key} : {value}")


"""

# Assignment 3 — Hard ⭐⭐⭐

## Student Marks Management System

You are given the following dictionary:

```python
students = {
    "Mahesh": 85,
    "Rahul": 72,
    "Anjali": 91,
    "Sneha": 68,
    "Amit": 91
}
```

### Write a program to:

1. Print all student names.
2. Print all marks.
3. Find the student(s) with the highest marks.
4. Find the average marks.
5. Print all students who scored more than the average.
6. Create a **set** containing all unique marks.
7. Check whether the mark `91` exists using the set.
8. Print the number of unique marks.

### Expected Skills Tested

* Dictionary traversal
* `keys()`, `values()`, `items()`
* Loops
* Conditions
* Variables
* Sets
* Membership testing
* Basic calculations

---

"""

## Submission Format

students = {
    "Mahesh": 85,
    "Rahul": 72,
    "Anjali": 91,
    "Sneha": 68,
    "Amit": 91
}

# 1. Print all student names.

for key in students.keys():

    print(key)

# 2. Print all marks.

for value in students.values():

    print(value)

# 3. Find the student(s) with the highest marks.

heighest_Marks = 0

for value in students.values():

    heighest_Marks = max(heighest_Marks,value)

print("Topper(s):")

for key,value in students.items():

    if value == heighest_Marks:
        print(key)

# 4. Find the average marks.

total_marks = 0
total_students = len(students)

for value in students.values():

    total_marks += value

average_marks = total_marks / total_students


# 5. Print all students who scored more than the average.

print("Students Scored more than Average marks: ")

for key,value in students.items():

    if value > average_marks:
        print(key)
# 6. Create a **set** containing all unique marks.

unique_marks  = set()

for value in students.values():
    unique_marks.add(value)

# 7. Check whether the mark `91` exists using the set.

if heighest_Marks in unique_marks:
    print("True")
else:
    print("False")

# 8. Print the number of unique marks.

print(unique_marks)

