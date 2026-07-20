## TODAY'S ASSIGNMENT

# Goal: Build a small inheritance hierarchy and prove—via exact printed output—that subclasses inherit and override behavior correctly.

# Requirements (must complete all):

# - [ ] Create a `Person` parent class with an `__init__(self, name)` storing `self.name`

class Person():

    def __init__(self,name):
        self.name = name
    def info(self):
        return f"Person: {self.name}"

# - [ ] Create a `Employee(Person)` subclass that adds `self.employee_id` and includes an `info()` method that returns a string like `Employee: <name> (<employee_id>)`

# - [ ] Override `info()` in the subclass (do not just inherit a parent implementation)

# - [ ] Demonstrate `super()` usage by calling the parent initializer inside `Employee.__init__`

class Employee(Person):

    def __init__(self,name,employee_id):
        super().__init__(name)
        self.employee_id = employee_id
    
    def info(self):

        return f"Employee: {self.name} ({self.employee_id})"
    


# - [ ] In a short main/test section, create **two** employees with different values and print exactly two lines (one per employee) using `info()`

emp1 = Employee("Mahesh", "001")
emp2 = Employee("Rahul", "002")

print(emp1.info())
print(emp2.info())


# Stretch (optional — do only after main requirements done):


class Manager(Employee):

    def __init__(self,name,employee_id,team_size):
        super().__init__(name,employee_id)
        self.team_size = team_size
    
    def info(self):
        
        return f"{super().info()} | Team Size: {self.team_size}"

mgr1 = Manager("Balu", "003", "5")

print(mgr1.info())
    

## COMMUNICATION PRACTICE (15 min)


"""
The inheritance lets a python class to reuse the behaviour of another class.
Therefor your avoided to copy paste same code multiple times. 
The child class automatically inherits all the methods and attributes from parent class.
Child class can modify or extent the methods inherited from parent class and these methods will override the parent method inside the child subclass.
The child class can invoke the logic defined by parent calls safely by using super() function.
"""
## REVISION CHECK (answer these without looking — 2 min)

# 1. What is the difference between `classmethod` and `staticmethod` in Python?

"""
The 'classmethod' are dependent on the class level data and classmethods shared by all objects in the class and the classmethod used 'cls' as the first parameter. The staticmethod is not dependent on class level data they are used for uitility functions related to the class and the static method don't recives any parameter like 'self','cls' which is passed in isntance,class method.
"""
# 2. What is a common output-label mistake that can cause your checklist to fail even if the logic is correct?

"""
The main mistakes are The Exact label given for the print statement and using Double Quotes inside the F-string

"""

## THEORY BLOCK (20 min) — CN: TCP/IP Model vs OSI

"""
The OSI Model is consist of 7 layrs including(Physical,Data link,Netwok,Transport,session,presentation,Application) and the OSI model is fundamental concept.
TCP/IP model is also called internet protocol suit it consist of 4 layers including(Network access layer,Internet Layer,Transport, Applicaction layer) and this model is impletemented model.
The OSI model is devoloped by ISI whereas the TCP/IP  model is devoloped bt ASPANET.
"""



