
"""
# 🔥 SECTION 3 — Mini Project

Now we're going to combine today's topic with your previous topics:

* Variables
* Strings
* Lists
* Dictionaries
* Sets
* Loops
* Functions
* `with`
* Exceptions
* Custom exceptions

## Mini Project: **Student Record Manager**

Create a Python program that reads student records from a file.

### Input file

```text
Mahesh,85,Python
Rahul,72,Python
Amit,91,Java
Priya,66,Python
```

Your program should provide:

### 1. Read the file

Use:

```python
with open(...)
```

---

### 2. Parse the data

Create a dictionary such as:

```python
{
    "Mahesh": {"marks": 85, "course": "Python"},
    "Rahul": {"marks": 72, "course": "Python"}
}
```

---

### 3. Functions

Create separate functions:

```python
load_students(filename)
calculate_average(students)
find_top_student(students)
get_students_by_course(students, course)
```

---

### 4. Error handling

Handle:

```text
FileNotFoundError
ValueError
```

---

### 5. Custom exception

Create:

```python
class InvalidStudentRecordError(Exception):
    pass
```

Raise it when a record is malformed.

For example:

```text
Mahesh,85
```

is invalid because the course is missing.

---

### 6. Course filtering

If the user enters:

```text
Python
```

return:

```text
Mahesh
Rahul
Priya
```

This gives you practice with strings, dictionaries, loops and functions from previous topics.

---

### 7. Final output

Your program should be able to produce something conceptually like:

```text
Total Students: 4
Average Marks: 78.5
Top Student: Amit
Python Students: Mahesh, Rahul, Priya
```

### Important constraint

**Don't try to make this production-level.**

I want to see your Python fundamentals.

"""

def calculate_average(students):

    total_marks = 0

    for student,info in students.items():

        total_marks += info["marks"]

    return total_marks / len(students)


def find_top_student(students):


    top_students = []
    top_marks = float('-inf')

    for student,info in students.items():

        if info["marks"] > top_marks:
            top_marks = info["marks"]
            top_students = [student]
        elif info["marks"] == top_marks:
            top_students += [student]

    return top_students if len(top_students) > 1 else top_students[0]


def get_students_by_course(students, course):

    students_list = []

    for student, info in students.items():

        if course == info["course"]:

            students_list.append(student)

    return students_list if students_list else None


class InvalidStudentRecordError(Exception):
    pass


def load_students(filename):


    try:
        with open(filename,"r") as file:

            students = {}

            for line in file:

                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                data = cleaned_line.split(",")

                if len(data) != 3:
                    raise InvalidStudentRecordError(f"Skipping invalid data format line: {cleaned_line}")
               
                else:

                    name = data[0].strip()
                    subject = data[2].strip()

                    try:
                        marks = int(data[1].strip())
                    except ValueError:
                        raise InvalidStudentRecordError(f"Invalid marks format for student: {name}")
                    
                    students[name] = {"marks":marks, "course":subject}


            # total_students = len(students)
            # average_marks = calculate_average(students)
            # top_student = find_top_student(students)
            # subject_name = input("Enter the Subject Name:")
            # filter_students = get_students_by_course(students,subject_name)

            return students

             
    except FileNotFoundError:
        print("File not Found")
        return None
    except InvalidStudentRecordError as e:
        print(f"Student record error: {e}")
        return None



student_file = r"submissions\input.txt"

student_data = load_students(student_file)

if student_data is not None:

    total_student = len(student_data)

    average_marks = calculate_average(student_data)

    top_student = find_top_student(student_data)

    course_name  = input("Enter the Subject Name:")

    course_students  = get_students_by_course(student_data,course_name)

    print(f"Total Students: {total_student}")
    print(f"Average Marks: {average_marks}")
    print(f"Top Student: {top_student}")
    if course_students:
        print(f"{course_name} Students: {course_students}")
    else:
        print(f"No students found for {course_name}")
else:

    print("Student data could not be loaded.")

    








