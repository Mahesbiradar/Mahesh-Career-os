"""

# Section 3 — Mini Project ⭐⭐⭐

This project combines **all the topics you've completed so far**:

* Variables
* Input/Output
* Control Flow
* Lists
* Tuples
* Dictionaries
* Sets
* Loops
* Conditions

## Mini Project: Student Result Management System

Imagine you're building the backend logic for a small coaching institute.

### Initial Data

```python
students = {
    "Mahesh": [85, 90, 88],
    "Rahul": [72, 68, 75],
    "Anjali": [95, 91, 93],
    "Sneha": [60, 65, 70],
    "Amit": [88, 90, 92]
}
```

Each student's list contains marks in **Maths, Science, and English**.

---

## Your Tasks

### Part A – Student Report

For every student:

* Print the student's name.
* Print all three marks.
* Calculate the total.
* Calculate the average.
* Print:

```
Pass
```

if average ≥ 40, otherwise

```
Fail
```

---

### Part B – Class Statistics

Print:

1. Total number of students.
2. Highest average.
3. Name(s) of the topper(s).
4. Lowest average.
5. Class average.

---

### Part C – Grade System

Assign grades:

```
Average >= 90   → A
Average >= 75   → B
Average >= 60   → C
Else            → D
```

Print:

```
Mahesh -> B
Rahul -> C
...
```

---

### Part D – Sets

Create a set containing **all unique marks** from every student.

Example:

```
{60, 65, 68, 70, 72, ...}
```

Then print:

* Number of unique marks.
* Whether mark `100` exists.
* Whether mark `91` exists.

---

### Part E – Challenge

Create a dictionary called `grade_count` like:

```python
{
    "A": 1,
    "B": 2,
    "C": 2,
    "D": 0
}
```

This counts how many students received each grade.

---

## Rules

* ❌ Don't use `sum()`, `max()`, `min()`, `Counter`, or any advanced libraries.
* ✅ Solve everything using loops, dictionaries, lists, sets, and conditions.
* ✅ Write clean, readable code with meaningful variable names.

This project is intentionally a bit longer because it simulates the kind of logic you'll implement in real backend applications. Once you finish it, I'll review it like a senior engineer reviewing a pull request, covering correctness, readability, edge cases, time complexity, and opportunities to make it more Pythonic.

"""

## Mini Project: Student Result Management System

students = {
    "Mahesh": [85, 90, 88],
    "Rahul": [72, 68, 75],
    "Anjali": [95, 91, 93],
    "Sneha": [60, 65, 70],
    "Amit": [88, 90, 92]
}

"""
### Part A – Student Report

For every student:

* Print the student's name.
* Print all three marks.
* Calculate the total.
* Calculate the average.
"""

def student_report(data):

    for name,marks in data.items():

        print(name,marks)

        total_marks = 0

        for mark in marks:

            total_marks += mark

        average = int(total_marks/len(marks))

        print(f"Total Marks: {total_marks}")
        print(f"Average: {average}")

        if average >= 40:
            print("Pass")
        else:
            print("Fail")


student_report(students)


"""
### Part B – Class Statistics

Print:

1. Total number of students.
2. Highest average.
3. Name(s) of the topper(s).
4. Lowest average.
5. Class average.

"""

def class_statistics(data):

    if not data:
        print("Data not available")
        return

    # 1. Total number of students.

    total_students = len(data)
    print(f"1. Total number of students: {total_students}")



    highest_average = 0
    lowest_average = float('inf')
    average = 0
    topper = None

    for name,marks in data.items():

        total_marks = 0

        for mark in marks:

            total_marks += mark

        student_average = int(total_marks/len(marks))

        average += student_average

        if student_average > highest_average:
            highest_average = student_average
            topper = name

        if student_average < lowest_average:
            lowest_average = student_average

    class_average  = average / total_students


    # 2. Highest average.

    print(f"2. Highest average: {highest_average}")
    print(f"3. Name(s) of the topper(s): {topper}")
    print(f"4. Lowest average: {lowest_average}")
    print(f"5. Class average: {class_average}")


class_statistics(students)

### Part C – Grade System

"""
Assign grades:

```
Average >= 90   → A
Average >= 75   → B
Average >= 60   → C
Else            → D
```

Print:

```
Mahesh -> B
Rahul -> C

"""
def grade_system(data):

    for name,marks in data.items():


        total_marks = 0

        for mark in marks:

            total_marks += mark

        average = int(total_marks/len(marks))

        grade = None

        if average >= 90 and average <= 100:
            grade = "A"
        elif average >= 75 and average <= 89:
            grade = "B"
        elif average >= 60 and average <= 74:
            grade = "C"
        else:
            grade = "D"

        print(f"{name} -> {grade}")

grade_system(students)
        

### Part D – Sets

"""

Create a set containing **all unique marks** from every student.

Example:

```
{60, 65, 68, 70, 72, ...}
```

Then print:

* Number of unique marks.
* Whether mark `100` exists.
* Whether mark `91` exists.
  
"""

def sets(data):

    students_unique_marks = set()

    for name,marks in data.items():

        

        for mark in marks:

            students_unique_marks.add(mark)

    print(f"Number of unique marks: {len(students_unique_marks)}")

    if 100 in students_unique_marks:
        print(f"Whether mark `100` exists: Yes")
    else:
        print(f"Whether mark `100` exists: No")

    if 91 in students_unique_marks:
        print(f"Whether mark `91` exists: Yes")
    else:
        print(f"Whether mark `91` exists: No")


sets(students)


### Part E – Challenge

"""
Create a dictionary called `grade_count` like:

```python
{
    "A": 1,
    "B": 2,
    "C": 2,
    "D": 0
}
```

This counts how many students received each grade.


"""        

def grade_counts(data):

    grade_count = {}

    for name,marks in data.items():


        total_marks = 0

        for mark in marks:

            total_marks += mark

        average = int(total_marks/len(marks))

        grade = None

        if average >= 90 and average <= 100:
            grade = "A"
        elif average >= 75 and average <= 89:
            grade = "B"
        elif average >= 60 and average <= 74:
            grade = "C"
        else:
            grade = "D"

        grade_count[grade] = grade_count.get(grade,0)+1


    return grade_count

print(grade_counts(students))




