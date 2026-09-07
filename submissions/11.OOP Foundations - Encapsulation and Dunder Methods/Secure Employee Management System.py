"""
# Section 3 — Mini Project

## 🏦 Secure Employee Management System

Build a small employee management system combining:

* Encapsulation
* Properties
* Abstraction
* Inheritance
* Polymorphism
* Dunder methods
* Exception handling
* At least one previous OOP concept naturally where useful

### Requirements

Create an abstract class:

```python
Employee(ABC)
```

It should have:

* private employee ID
* public name
* private salary
* `salary` property
* abstract method `calculate_bonus()`

Create at least:

```python
Developer
Manager
```

### Salary

Salary must always be:

```text
> 0
```

Invalid salary → `ValueError`.

### Bonus

Different employee types should calculate bonus differently.

For example:

```text
Developer → 10%
Manager   → 20%
```

The exact percentages are up to you.

Use **polymorphism**:

```python
employees = [
    Developer(...),
    Manager(...)
]

for employee in employees:
    print(employee.calculate_bonus())
```

### Dunder methods

Implement:

```python
__str__()
__repr__()
__eq__()
```

Two employees should be equal when their **employee IDs** are equal.

### Encapsulation requirement

Outside code should be able to:

```python
employee.salary
```

but salary modifications must go through your property validation.

### Exception handling

Create/use an appropriate exception for at least one business-specific error, such as:

```text
InvalidEmployeeIDError
```

or another meaningful exception of your choice.

### Final requirement

Create several employees and demonstrate:

* valid salary
* invalid salary
* salary update
* bonus calculation
* equality
* `str()`
* `repr()`
* polymorphism
* exception handling

**Don't over-engineer it.** I want to see whether you can combine the concepts cleanly.

---

"""

class InvalidEmployeeIDError(Exception):
    pass

from abc import ABC,abstractmethod

class Employee(ABC):

    def __init__(self,employee_id,name,salary):

        if not employee_id or not isinstance(employee_id, str):
            raise InvalidEmployeeIDError("Employee ID must be a non-empty string.")

        self.__employee_id = employee_id
        self.name = name
        self.salary = salary


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):

        if value <= 0:
            raise ValueError("Salary must be greater than 0.")
        self.__salary = value

    @abstractmethod
    def calculate_bonus(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(ID: {self.__employee_id}, Name: {self.name}, Salary: {self.salary})"


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__employee_id}', '{self.name}', {self.salary})"

    def __eq__(self, other):
        return self.__employee_id == other.__employee_id



class Developer(Employee):

    def calculate_bonus(self):
        return self.salary*0.10
 

class Manager(Employee):

    def calculate_bonus(self):
        return self.salary*0.20




# Final requirement


print("--- 1. Valid Salary, Polymorphism, str(), and repr() ---")


employees = [
    Developer("D101","Mahesh",1000),
    Developer("D102","Rahul",2000),
    Manager("M101","Prashant",4000),
    Manager("M102","Arun",5000),
]

for employee in employees:
    print(f"str():  {employee}")
    print(f"repr(): {repr(employee)}")
    print(f"Bonus:  {employee.calculate_bonus()}")
    print("-" * 20)


print("\n--- 2. Salary Update & Validation Guard ---")

d3=Developer("D103","Suresh",2000)
print(f"Original Salary: {d3.salary}")

d3.salary = 40000
print(f"Updated Salary: {d3.salary}")

try:
    d3.salary = -1000
except ValueError as e:
    print(f"Caught Expected Error: {e}")

print("\n--- 3. Equality Checks (__eq__) ---")

d4 = Developer("D104","Karan",2000)
d5 = Developer("D104","Rahul",2000)

print(f"Is d4 equal to d5? {d4 == d5}")

print("\n--- 4. Exception Handling (Invalid ID & Invalid Salary on Creation) ---")

try:
    bad_id_emp = Developer("","Rahul",1000)
except InvalidEmployeeIDError as e:
    print(f"Caught Expected ID Error: {e}")

try:
    bad_sal_emp = Manager("M001","Sukesh",-1000)
except ValueError as e:
    print(f"Caught Expected Salary Error: {e}")
