## TODAY'S ASSIGNMENT

#Goal: Build a small class-based employee profile program that proves you understand classes, objects, attributes, and methods.

#Requirements (must complete all):

#1.- [ ] Create a class called `Employee` with an `__init__` method that accepts `first_name`, `last_name`, `role`, and `monthly_salary`, then stores all four as instance attributes.


class Employee():

    def __init__(self,first_name,last_name,role,monthly_salary):

        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.monthly_salary = monthly_salary

#2.- [ ] Add a method called `full_name` that returns the employee's first and last name together as one string.
        
    
    def full_name(self,):

        return f"{self.first_name} {self.last_name}"
    

#3.- [ ] Add a method called `annual_salary` that returns the monthly salary multiplied by 12.

    def annual_salary(self):

        return self.monthly_salary*12

# 6.- [ ] Add a method called `give_raise` that accepts a percentage number, increases that employee's monthly salary, and then print the new annual salary for one employee.

    def give_raise(self, percentage):
        raise_amount  = self.monthly_salary * (percentage / 100)

        self.monthly_salary += raise_amount

        return self.annual_salary()


#4.- [ ] Create two different `Employee` objects with different names, roles, and salaries. Print each employee using the labels `Employee 1:` and `Employee 2:` and include the full name, role, and annual salary in the output.

employee1 = Employee("Mahesh", "Biradar", "Software Engineer", 85000)

employee2 = Employee("Balu", "Patil", "Telecom Engineer", 90000)

print(f"Employee 1: full name: {employee1.full_name()}, role: {employee1.role}, annual salary: {employee1.annual_salary()}")
print(f"Employee 2: full name: {employee2.full_name()}, role: {employee2.role}, annual salary: {employee2.annual_salary()}")

#5. - [ ] Update only the first employee's `role`, then print both roles again using the labels `Updated Employee 1 role:` and `Employee 2 role still:` to prove the two objects keep separate data.

employee1.role = "fullstack Engineer"

print(f"Updated Employee 1 role: {employee1.role}")
print(f"Employee 2 role still: {employee2.role}")

#6.- [ ] Add a method called `give_raise` that accepts a percentage number, increases that employee's monthly salary, and then print the new annual salary for one employee.

employee1.give_raise(10)

print(f"Employee 1 Annual salary: {employee1.annual_salary()}")
print(f"Employee 2 Annual salary: {employee2.annual_salary()}")

## COMMUNICATION PRACTICE (15 min)

"""
class is blueprint which defines the structure and behavior os something.
object is real thing created using the blueprint of the class.

Instnace is another name to object created from class. an Attributes is piece of
data stored inside the object.

An method if function defined in the class that describes what object can do.
By creating multiple object from same class. each instace can have its own unique attributes while sharing the same method.

"""

## REVISION CHECK (answer these without looking — 2 min)

# 1. In a `try` / `except` / `else` / `finally` structure, when does the `else` block run?

#Forgotted then seen last times works now got it the else block runs if now exception occurred

#2.Why is `except ValueError` better than a bare `except` when converting user input to an integer?

"""
except ValueError is better than the bare except because it catches only the expected error when converting invalid input to an integer.
a bare except cathes all the exceptions. including unrelated programming errors. which can hide bugs and make debugging more difficult.
"""
## THEORY BLOCK (20 min)

"""

my version
An operating system provides the interface between the user applications and the hardware.
Since applications cannot access the hardware directly therefor operating system acts like bridge between the applications and hardware.
The main functions or OS is to manage the harware,Process management,storage management,memory management,File management.

got in chatgpt
An operating system is the software that acts as a bridge between the computer's hardware and the applications, making it possible for programs to run smoothly. 
Applications need the operating system because it provides essential services such as accessing memory, reading and writing files, and communicating with hardware 
devices instead of interacting with the hardware directly. The operating system manages resources by scheduling CPU time, allocating memory, organizing files, 
and controlling input/output devices so that multiple programs can run efficiently and safely.

"""


