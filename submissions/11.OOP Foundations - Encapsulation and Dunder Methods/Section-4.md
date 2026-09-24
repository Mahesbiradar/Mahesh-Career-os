
---

# 🐛 Section 4 — Debugging

For each problem:

1. Identify the error/bug.
2. Explain **why** it happens.
3. Give the corrected code.

---

### Q1 — Name Mangling

```python
class Employee:
    def __init__(self):
        self.__salary = 50000

e = Employee()

print(e.__salary)
```

What happens and how would you access the value correctly through a proper class interface?

---
# Ans: If we Execute above mentioned Code this will raise an attribute Error since we are trying to access the private attribute so to make it accessible correctly through a proper class interface we can use getters using @Property. 

 @property
    def salary(self):
        return self.__salary


### Q2 — Property Setter

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary must be positive")
        self.__salary = value

e = Employee(50000)
e.salary = 0
```

There is a logical bug.

Identify it and fix it.

---
# Ans: in this code the salary validation shoud be handle value equal and less than Zero but existing code only handles the values less tha zero. There for fixing 

if value <= 0:

will remove the logical bug.


### Q3 — Abstract Class

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    pass


car = Car()
```

Why does this fail?

Fix the code while preserving the abstract-class design.

---
# Ans: Here we have a abstarct class Vehicle and it has abstractmethod called start but here the derived class Car has not implemented the abstarct method which is defined in absract class without implementing the defined classes the object of the derived class not instantoated and throws typeerror.

to fix the above code we shoud implement the own start method in car class

class Car(Vehicle):
    def start(self):
        print("Car has been started")


### Q4 — `__len__`

```python
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return self.members

team = Team(["A", "B", "C"])

print(len(team))
```

This code produces an error.

Why?

Fix it.

---
# Ans: This code produces the TypeError because the __len__ dunder method is designed to return raw interger, but the code is returning a list(self.members)

When we run len(team), Python intercepts it, calls team.__len__(), and expects a whole number back. Because it gets ["A", "B", "C"] instead, the runtime system crashes.

To fix this , we shoud wrap the self.members inside pythons bultin function len() inside the method so that it retunr the count of items as an integer.

 def __len__(self):
        return len(self.members)

### Q5 — `__eq__`

```python
class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def __eq__(self, other):
        return self.employee_id == other.employee_id


e = Employee(101)

print(e == 101)
```

This implementation is not robust.

Why can this cause a problem?

Modify `__eq__` so comparing an `Employee` with an unrelated type is handled properly.

---
# Ans: The above implemented code is not robust because it assumes the other object will always have an employee_id attribute.

when we execute print(e == 101), the other object is an integer (101). since integers do not have an employee_id attribute, Python will crash with an AttributeError 

to make __eq__ robust, we must first verify the if other is an intance of the Employee class. if it is not we shoud return NotImplemented.instead of raising an error or returning False. Returning NotImplemented allows Python to gracefully fall back and let the other object handle the comparison, ultimately evaluating to False if neither class knows how to compare them.

 def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
            
        return self.employee_id == other.employee_id




 
