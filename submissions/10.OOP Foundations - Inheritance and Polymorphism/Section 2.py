# # 🟡 SECTION 2 — Coding Assignments

# These will focus primarily on **Inheritance + Polymorphism**, with earlier concepts appearing naturally where useful.

# ---

"""
## 🟢 Assignment 1 — Basic Inheritance

Create:

```python
class Vehicle:
```

with:

```python
def __init__(self, brand):
    ...
```

Store:

```text
brand
```

as an instance variable.

Create an instance method:

```python
def start(self):
    ...
```

that prints:

```text
Toyota vehicle started
```

if the brand is Toyota.

Then create:

```python
class Car(Vehicle):
```

with an additional instance variable:

```text
doors
```

and a method:

```python
def drive(self):
    ...
```

that prints:

```text
Toyota car is driving
```

### Requirements

Demonstrate that the `Car` object can use:

```python
car.start()
car.drive()
```

---

"""
class Vehicle:

    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started")

class Car(Vehicle):

    def __init__(self,brand,doors):
        super().__init__(brand)
        self.doors = doors


    def drive(self):
        print(f"{self.brand} vehicle started")  # Since start alos has same print statemebt so we can use super() and method start() to print the same

car = Car("Toyata",2)

car.start()
car.drive()


"""

# 🟡 Assignment 2 — Inheritance + `super()` + Overriding

Create:

```python
class Employee:
```

with:

```text
name
salary
```

and an instance method:

```python
display_details()
```

Then create:

```python
class Manager(Employee):
```

Add:

```text
team_size
```

Use `super()` in the `Manager` constructor.

Then override:

```python
display_details()
```

The Manager's implementation should display:

```text
Name: Mahesh
Salary: 80000
Team Size: 5
Role: Manager
```

### Important requirement

Inside the overridden method, use:

```python
super().display_details()
```

to reuse the parent's implementation.

Then add the Manager-specific information.

This tests whether you understand the difference between:

```text
overriding
```

and:

```text
completely replacing parent functionality
```

---

"""

# 

class Employee:
    def __init__(self,name,salary):

        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")
        


class Manager(Employee):

    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}\nRole: Manager")


mgr1= Manager("Mahesh",160000,10)

mgr1.display_details()


"""
# 🔴 Assignment 3 — Polymorphism

Create a base class:

```python
class Payment:
```

with:

```python
def process(self):
    ...
```

Create three child classes:

```text
UPIPayment
CardPayment
CashPayment
```

Each should override:

```python
process()
```

with different output.

For example:

```text
Processing UPI payment
Processing Card payment
Processing Cash payment
```

Then create:

```python
payments = [
    UPIPayment(),
    CardPayment(),
    CashPayment()
]
```

Write:

```python
def process_payments(payments):
    ...
```

which processes every payment **without checking the concrete class**.

### Important restriction

Don't do:

```python
if isinstance(payment, UPIPayment):
    ...
elif isinstance(payment, CardPayment):
    ...
```

The whole purpose is to demonstrate **polymorphism**.

The function should simply rely on:

```python
payment.process()
```

### Bonus

Add:

```python
isinstance()
```

checks outside the processing function to demonstrate that you understand the difference between:

> **using polymorphism**

and:

> **checking an object's type**.
"""

class Payment:

    def process(self):
        print("Processing Payment")

class UPIPayment(Payment):

    def process(self):
        print("Processing UPI Payment")

class CardPayment(Payment):
    def process(self):
        print("Processing Card Payment")

class CashPayment(Payment):

    def process(self):
        print("Processing Cash Payment")


payments = [
    UPIPayment(),
    CardPayment(),
    CashPayment()
]

def process_payments(payments):

    for payment in payments:

        payment.process()


process_payments(payments)


print(issubclass(UPIPayment,Payment))

print(isinstance(CardPayment,Payment))
