"""
ROUND 2 — Coding + Output

Don't solve these mentally only. Actually write/run the code if possible.


Q16 — Coding

Write a function:

frequency_count(numbers)

that takes:

[1, 2, 2, 3, 3, 3]

and returns:

{
    1: 1,
    2: 2,
    3: 3
}

You may use a dictionary.


"""

def frequency_count(numbers):

    freq_count = {}

    for i in numbers:

        freq_count[i]= freq_count.get(i,0)+1

    return freq_count

print(frequency_count([1, 2, 2, 3, 3, 3]))


"""

Q17 — Coding

Write:

def calculate_total(*args, **kwargs):

It should:

add all positional numeric values
print the customer's name from kwargs
return the total

Example:

calculate_total(100, 200, 50, name="Mahesh")

Expected:

Customer: Mahesh
Total: 350

"""

def calculate_total(*args, **kwargs):

    total = 0

    custumer_name = kwargs.get("name")

    for i in args:

        total += i

    return f"Customer: {custumer_name}\nTotal: {total}"

print(calculate_total(100, 200, 50, name="Mahesh"))


"""
Q18 — Coding

You have:

students = [
    ("Mahesh", 82),
    ("Rahul", 95),
    ("Amit", 72),
    ("Priya", 88)
]

Using lambda, find:

student with highest marks
students sorted by marks

"""
students = [
    ("Mahesh", 82),
    ("Rahul", 95),
    ("Amit", 72),
    ("Priya", 88)
]

highest_student  = max(students,key= lambda x:x[1])

sorted_students = sorted(students,key=lambda x:x[1])

print("Student with highest marks:")
print(f"Name: {highest_student[0]}, Marks: {highest_student[1]}\n")

print("Students sorted by marks:")
for name, marks in sorted_students:
    print(f"Name: {name}, Marks: {marks}")


"""
Q19 — Output Prediction

What is the output?

numbers = [1, 2, 3]

result = numbers.append([4, 5])

print(numbers)
print(result)

Explain why.

"""

# [1, 2, 3,[4, 5]]
None

# Here intailly i thought the result also produces same value as numbers but i got when read now i was not aware of this.

# In python most of the methods which modify the mutable collaction inplace do not retunrns the updated collection they explecitely returns None.

## There for the result consist of None


"""
Q20 — Output Prediction 🔥

What is the output?

def test(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

test(10, 20, 30, name="Mahesh", age=25)

"""
10
(20, 30)
{name="Mahesh", age=25}

"""
Q21 — Debugging

What's wrong here?

data = {
    ["name", "Mahesh"]
}

How would you fix it if your intention was to create:

{
    "name": "Mahesh"
}

"""

# In above code the dict cosist of list but not gaving any key for the same. which is wrong.
# Ans i woud remove brackets and then in place of , ill use : so the first string will be the key and second will be the value.

"""

Q22 — Debugging

A developer writes:

numbers = [3, 1, 2]

result = numbers.sort()

print(result)

They expect:

[1, 2, 3]

Why don't they get that?

"""
# The devoloped not gets the expected o/p bcz sort function modifies inplace and retunrs none instead of returning list.

# to make this happend we shoud use result = sorted(numbers) which return the new modifies list and not modifies the original list


"""

Q23 — Practical Backend Question

You have:

myproject/
    app.py
    database.py
    users.py

app.py needs a function from database.py.

Show two valid ways to import it.

"""

#inside the app.py

1.# Specific function import

from database import example_function

#Calling the function
connect_to_db()

2.#Module import 

import database

#Calling the function

database.connect_to_db()


"""

Q24 — Final Integration 🔥

Explain this entire flow in your own words:

Python project
      ↓
virtual environment
      ↓
pip
      ↓
requirements.txt
      ↓
packages
      ↓
modules
      ↓
imports
      ↓
application

I want you to explain what each component does and how they relate to each other.


"""

The First step in the above flow is the Folder which consist the propject files.

virtual environment creates the isolated python environment for this project withoud conflicting with global or any other project.students

pip is python package installer helps in installing the ecternal packages required for the project.students

requirements.txt file contains the all teh dependencies of the project and we can install all these dependencies using the pip.

package provides a way to organize all the realted modules in directory staructure.

modules are teh python files consisting the python code.

using imports we can resuse the code from diffrent modules and packages. to run a specific application.

