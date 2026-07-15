## TODAY'S ASSIGNMENT

# Goal: Build an employee helper that proves you understand when to use a classmethod and when to use a staticmethod.

# Requirements (must complete all):

# - [ ] Create a class called `Employee` with a class variable `raise_amount = 1.04` and an `__init__` method that accepts `first_name`, `last_name`, `role`, and `monthly_salary`.

class Employee():

    raise_amount = 1.04

    def __init__(self, first_name, last_name, role, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.monthly_salary = monthly_salary
    
# - [ ] Add an instance method called `full_name` that returns the employee's first and last name together.

    def full_name(self):

        return f"{self.first_name} {self.last_name}" 

# - [ ] Add a `@classmethod` called `set_raise_amount(cls, amount)` that updates the class variable. Use `cls.raise_amount`, not `Employee.raise_amount`, inside the method.

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

# - [ ] Add a `@classmethod` called `from_string(cls, employee_string)` that accepts a string like `"Anita-Sharma-Developer-50000"`, splits it, and returns a new `Employee` object.

    @classmethod
    def from_string(cls, employee_string):
        first_name, last_name, role, monthly_salary = employee_string.split('-')

        return cls(first_name, last_name, role, monthly_salary)

# - [ ] Add another classmethod called `from_csv(cls, csv_string)` that accepts a string like `"Ravi,Kumar,Tester,45000"` and returns a new `Employee` object.

    @classmethod
    def from_csv(cls,csv_string):
        first_name, last_name, role, monthly_salary = csv_string.split(',')

        return cls(first_name, last_name, role, monthly_salary)
    


# - [ ] Add a `@staticmethod` called `is_workday(day_name)` that returns `False` for `"Saturday"` and `"Sunday"`, and `True` for other day names.

    @staticmethod
    def is_workday(day_name):
        if day_name == "Saturday" or day_name == "Sunday":
            return False
        return True

employee1 = Employee("Mahesh", "Biradar", "Software Engineer", "1020000")

employee2 = Employee.from_string("Anita-Sharma-Developer-50000")

print(f"Employee 1: full name: {employee1.full_name()}, role: {employee1.role}, monthly salary: {employee1.monthly_salary}")
print(f"Employee 2: full name: {employee2.full_name()}, role: {employee2.role}, monthly salary: {employee2.monthly_salary}")

Employee.set_raise_amount(1.05)

print(f"Employee 1 Raise amount: {Employee.raise_amount}")
print(f"Employee 1 Raise amount: {employee1.raise_amount}")
print(f"Employee 2 Raise amount: {employee2.raise_amount}")

print(F"Monday is workday: {Employee.is_workday('Monday')}")
print(F"Sunday is workday: {Employee.is_workday('Sunday')}")

# Stretch (optional — do only after main requirements done):

# - [ ] Add another classmethod called `from_csv(cls, csv_string)` that accepts a string like `"Ravi,Kumar,Tester,45000"` and returns a new `Employee` object.

employee3 = Employee.from_csv("Ravi,Kumar,Tester,45000")

print(f"Employee 3: full name: {employee3.full_name()}, role: {employee3.role}, monthly salary: {employee3.monthly_salary}")

## COMMUNICATION PRACTICE (15 min)

"""
I would use the class method instead of the static method when a method need to access or modify the data at class level.
The class level method receives the cls as its first parameter, so it can work with class variables that are shared by the every object of the class.
A static method does not receive cls or self, so it cannot access class or instance data unless it is passed explicitly. I use static method for utility functions that are related to the class but
do not depend on the class or any particula instance. I choose a classmethod when I need behavior that should apply to all objects of the class or when creating alternative constructors.
    
"""
## REVISION CHECK (answer these without looking — 2 min)

# 1. When code uses `self.raise_amount`, where does Python look first: the object or the class?

"""
The python look first in the object and if does not found in object then it looks in the class.

"""
# 2. Why should a shared employee counter be updated with `Employee.num_of_employees` instead of `self.num_of_employees`?

"""
num_of_employees is shared employee counter which means it is class variable and it is shared by all objects therefor it is updated with  Employee.num_of_employees insted of self.num_of_employees
bcz the self.num_of_employees is the instance variable does not shared by all the objects.

"""
## THEORY BLOCK (20 min)

"""
A computer network is a system that connects computers through wired or wireless communication so they can exchange data by following a common set of rules called protocols. 
Networking is divided into layers because each layer performs a specific function, making communication easier to design, understand, troubleshoot, and maintain. 
The OSI model helps engineers remember the different stages of network communication by organizing the entire process into seven separate layers.

"""




