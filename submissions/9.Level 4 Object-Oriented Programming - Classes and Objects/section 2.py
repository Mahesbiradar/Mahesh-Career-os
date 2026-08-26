"""
---

# 🟡 SECTION 2 — Coding Assignments

Now let's move from definitions to actual implementation.

## 🟢 Assignment 1 — Easy

### `Employee` Class

Create an `Employee` class with:

```text
name
salary
```

Requirements:

1. Use `__init__`.
2. Store `name` and `salary` as instance variables.
3. Create an instance method:

```python
display_details()
```

which prints:

```text
Name: Mahesh
Salary: 50000
```

4. Create two employees with different values.
5. Demonstrate that each object maintains its own data.

---

"""

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_details(self):

        print(f"Name: {self.name}\nSalary: {self.salary}")

emp1 = Employee("Mahesh",60000)
emp2 = Employee("Sumit",55000)


emp1.display_details()
emp2.display_details()

print(emp1.name)
print(emp1.salary)


"""
# 🟡 Assignment 2 — Medium

### Class Variable + Class Method

Create:

```python
class Employee:
```

with:

```text
company = "ABC Technologies"
```

as a class variable.

The class should have:

```python
__init__(self, name, salary)
display_details(self)
change_company(cls, new_company)
```

Requirements:

1. `name` and `salary` → instance variables.
2. `company` → class variable.
3. `display_details()` → instance method.
4. `change_company()` → class method.
5. Create two employees.
6. Change the company using the class method.
7. Demonstrate that both employees now see the new company.

---

"""
# 🟡 Assignment 2 — Medium


class Employee:

    company = "ABC Technologies"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_details(self):

        print(f"Name: {self.name}\nSalary: {self.salary}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    

emp1 = Employee("Mahesh",60000)
emp2 = Employee("Sumit",55000)

print(emp1.company)
print(emp2.company)

Employee.change_company("XYZ Technologies")


print(emp1.company)
print(emp2.company)

"""

# 🔴 Assignment 3 — Hard

### Employee Validation System

Create:

```python
class Employee:
```

with:

```text
name
salary
employee_id
company
```

Requirements:

### Instance variables

```text
name
salary
employee_id
```

### Class variable

```text
company = "ABC Technologies"
```

### Instance method

```python
display_details()
```

### Class method

```python
change_company(cls, new_company)
```

### Static method

```python
is_valid_salary(salary)
```

The static method should return:

```text
True
```

if salary is greater than `0`, otherwise:

```text
False
```

Then your program should:

1. Create at least two employees.
2. Display their details.
3. Validate salaries using the static method.
4. Change the company using the class method.
5. Show that the company changed for both employees.
6. Demonstrate that their individual names/salaries remain different.

### Extra challenge

Add:

```python
@classmethod
def from_string(cls, data):
```

where:

```text
data = "Mahesh,50000,E101"
```

creates an `Employee` object.

This tests whether you understand why a **class method can be used as an alternative constructor**.

---

"""


class Employee:

    company = "ABC Technologies"

    def __init__(self,name,salary,employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id


    def display_details(self):

        print(f"Name: {self.name}\nSalary: {self.salary}\nEmployee Id: {self.employee_id}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def is_valid_salary(salary):

        return True if salary > 0 else False

    @classmethod
    def from_string(cls, data):
        name,salary,employee_id = data.split(",")
        return cls(name,salary,employee_id)


# 1. Create at least two employees.

emp1 = Employee("Mahesh",56000,"E101")
emp2 = Employee("Sukesh",50000,"E102")

# 2. Display their details.


emp1.display_details()
emp2.display_details()

# 3. Validate salaries using the static method.

print(Employee.is_valid_salary(emp1.salary))
print(Employee.is_valid_salary(emp2.salary))

# 4. Change the company using the class method.

Employee.change_company("XYZ Technologies")

# 5. Show that the company changed for both employees.

print(emp1.company)
print(emp2.company)


# 6. Demonstrate that their individual names/salaries remain different.

print(emp1.name)
print(emp1.salary)
print(emp2.name)
print(emp2.salary)


### Extra challenge


data = "rukesh,51000,E103"

emp2= Employee.from_string(data)

emp2.display_details()

