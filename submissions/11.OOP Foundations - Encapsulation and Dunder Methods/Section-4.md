
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
# Ans: If we Execute above mentioned Code this will raise an attribute Error 


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
