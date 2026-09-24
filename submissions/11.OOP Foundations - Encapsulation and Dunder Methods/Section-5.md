
---

# 🎯 Section 5 — Output Prediction

**Don't execute the code.** Predict the exact output/error and explain why.

### Q1 — Name Mangling

```python
class Employee:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary


e = Employee()

print(e.get_salary())
print(hasattr(e, "__salary"))
print(hasattr(e, "_Employee__salary"))
```

What is printed?

---
# Ans: O/P

50000
False
True


### Q2 — Property

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        print("Setter called")
        self.__salary = value


e = Employee(50000)

print(e.salary)

e.salary = 60000

print(e.salary)
```

Give the exact output and explain when the getter/setter runs.

---
# Ans: O/P

50000
Setter called
60000

Here intially when the print(e.salary) this line executed getter is called which retunr the __salary and when the e.salary = 60000 is executes setter is called. again when print(e.salary)
is called the getter runs.


### Q3 — `__str__` and `__repr__`

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee: {self.name}"

    def __repr__(self):
        return f"Employee({self.name!r})"


e = Employee("Mahesh")

print(e)
print(str(e))
print(repr(e))
```

What is the output?

---
# Ans: O/P
Employee: Mahesh
Employee: Mahesh
Employee('Mahesh')


### Q4 — Equality

```python
class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.employee_id == other.employee_id


e1 = Employee(101)
e2 = Employee(101)
e3 = Employee(102)

print(e1 == e2)
print(e1 == e3)
print(e1 == 101)
```

Predict all three outputs.

---
# Ans: O/P

True
False
False


### Q5 — Abstract Class + Polymorphism

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

print(isinstance(animals[0], Animal))
print(issubclass(Dog, Animal))
```

What is printed?

---
# Ans: O/P
Bark
Meow
True
True
