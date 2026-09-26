
# Section 3 — Mini Project


### **25 marks**

## Employee Analytics System

"""
Build a small **Employee Analytics System** using the concepts you've learned so far.

This is intentionally designed to combine today's comprehensions with your earlier knowledge of:

* variables and data types
* lists/dictionaries/sets
* loops and conditions
* functions
* `zip()`
* string manipulation
* exceptions
* OOP concepts where useful

You **do not have to use every previous topic**. Use them naturally.

---

### Given data

```python
employees = [
    {
        "id": 101,
        "name": "Mahesh",
        "department": "Backend",
        "salary": 65000,
        "skills": ["Python", "Django", "PostgreSQL"],
        "active": True
    },
    {
        "id": 102,
        "name": "Rahul",
        "department": "Frontend",
        "salary": 55000,
        "skills": ["React", "JavaScript", "CSS"],
        "active": True
    },
    {
        "id": 103,
        "name": "Amit",
        "department": "Backend",
        "salary": 80000,
        "skills": ["Python", "Django", "Redis"],
        "active": False
    },
    {
        "id": 104,
        "name": "Priya",
        "department": "QA",
        "salary": 50000,
        "skills": ["Python", "Selenium", "SQL"],
        "active": True
    },
    {
        "id": 105,
        "name": "Kiran",
        "department": "Backend",
        "salary": 72000,
        "skills": ["Python", "FastAPI", "PostgreSQL"],
        "active": True
    }
]
```

---

## Your task

Create a program that produces the following analytics.

### Part A — Active Employees

Create a list containing the **names of all active employees**.

Expected structure:

```text
["Mahesh", "Rahul", "Priya", "Kiran"]
```

Use a comprehension.

---

### Part B — Backend Employees

Create a dictionary:

```text
employee_id → employee_name
```

for **active Backend employees only**.

Expected:

```python
{
    101: "Mahesh",
    105: "Kiran"
}
```

Use a dictionary comprehension.

---

### Part C — Salary Analysis

Create a list containing the salaries of employees earning **₹60,000 or more**.

Then create another list containing those salaries after applying a **10% increase**.

For example:

```text
original:
[65000, 80000, 72000]

after increase:
[71500.0, 88000.0, 79200.0]
```

Use comprehensions.

---

### Part D — Departments

Create a set containing all unique departments.

Then create a dictionary:

```text
department → number of employees
```

For the second part, you may use a normal loop **or** a comprehension combined with something you've previously learned.

The important thing is that the result should correctly count employees in each department.

---

### Part E — Skills

Create a set containing **all unique skills** across all employees.

For example, the result should contain things like:

```text
Python
Django
PostgreSQL
React
JavaScript
...
```

Since each employee has a list of skills, this requires thinking carefully about a **nested comprehension**.

---

### Part F — Employee Status

Create:

```text
employee_id → "active"/"inactive"
```

using a dictionary comprehension.

---

### Part G — Function

Put the analytics into a function:

```python
def generate_employee_report(employees):
    ...
```

The function should return a dictionary containing your major results.

Something like:

```python
{
    "active_employees": ...,
    "backend_employees": ...,
    "high_salary": ...,
    "salary_after_raise": ...,
    "departments": ...,
    "skills": ...,
    "employee_status": ...
}
```

---

### Part H — Error Handling

What should your function do if `employees` is not a list?

For example:

```python
generate_employee_report("employees")
```

Handle this appropriately using an exception.

You don't need to build a sophisticated custom exception unless you want to. A normal built-in exception is sufficient.

---

### Part I — Engineering Question

After writing your solution, answer:

> **Which parts of your program should use comprehensions, and which parts should use normal loops? Why?**

I specifically want to see whether you understand that:

> **"I know comprehensions" ≠ "I should use comprehensions everywhere."**

---

### Section 3 scoring

| Component                 |  Marks |
| ------------------------- | -----: |
| A — Active employees      |      2 |
| B — Backend lookup        |      3 |
| C — Salary transformation |      3 |
| D — Department analytics  |      3 |
| E — Nested skills         |      3 |
| F — Status dictionary     |      2 |
| G — Function integration  |      3 |
| H — Exception handling    |      2 |
| I — Engineering reasoning |      4 |
| **Total**                 | **25** |

---

"""


employees = [
    {
        "id": 101,
        "name": "Mahesh",
        "department": "Backend",
        "salary": 65000,
        "skills": ["Python", "Django", "PostgreSQL"],
        "active": True
    },
    {
        "id": 102,
        "name": "Rahul",
        "department": "Frontend",
        "salary": 55000,
        "skills": ["React", "JavaScript", "CSS"],
        "active": True
    },
    {
        "id": 103,
        "name": "Amit",
        "department": "Backend",
        "salary": 80000,
        "skills": ["Python", "Django", "Redis"],
        "active": False
    },
    {
        "id": 104,
        "name": "Priya",
        "department": "QA",
        "salary": 50000,
        "skills": ["Python", "Selenium", "SQL"],
        "active": True
    },
    {
        "id": 105,
        "name": "Kiran",
        "department": "Backend",
        "salary": 72000,
        "skills": ["Python", "FastAPI", "PostgreSQL"],
        "active": True
    }
]



def generate_employee_report(employees):


        if not isinstance(employees,list):

            raise TypeError(f"Expected input type 'list', but received '{type(employees).__name__}'.")

        # Part A — Active Employees
        active_employees = [employee["name"] for employee in employees if employee["active"]]

        # Part B — Backend Employees

        backend_employees = {employee["id"]:employee["name"] for employee in employees if employee["department"]=="Backend"}

        # Part C — Salary Analysis

        high_salary = [employee["salary"] for employee in employees if employee["salary"] >=60000]

        salary_after_raise = [employee["salary"]*1.10 for employee in employees if employee["salary"] >=60000]

        # Part D — Departments

        unique_departments = {employee["department"] for employee in employees}

        departments = {}

        for employee in employees:

            departments[employee["department"]] = departments.get(employee["department"],0)+1


        # Part E — Skills

        skills = {skill for employee in employees for skill in employee["skills"]}

        # Part F — Employee Status

        employee_status ={employee["id"]:"active" if employee["active"] else "inactive" for employee in employees}


        return {

            "active_employees" : active_employees,
            "backend_employees": backend_employees,
            "high_salary": high_salary,
            "salary_after_raise": salary_after_raise,
            "departments": departments,
            "skills": skills,
            "employee_status": employee_status
        }


try:
    data = employees
    report = generate_employee_report(data)
    print(report)

except TypeError as e:
    print(f"Data Processing Error: {e}")


# Part I — Engineering Question

# Which parts of your program should use comprehensions, and which parts should use normal loops? Why?

# In this program the D part shoud use normal loop and remaining parts shoud use comprehensions.

# Bcz is use comprehensions in d part then readiblity and debuging will be complicated that what is felt for remaining part it has transfomation and filtering so we can use comprehensions efficeently.

