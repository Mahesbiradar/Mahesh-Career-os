
# 💻 Section 2 — Coding Assignments

### Assignment 1 — Easy: Encapsulation

"""
Create a class:

```python
class Employee:
```

Requirements:

* Store `name` publicly.
* Store `salary` using a private attribute.
* Provide a property called `salary`.
* Salary must be greater than `0`.
* Assigning an invalid salary should raise `ValueError`.

Example expected behavior:

```python
e = Employee("Mahesh", 50000)

print(e.name)
print(e.salary)

e.salary = 60000
print(e.salary)

e.salary = -1000    # should raise ValueError
```

---

"""

class Employee:

    def __init__(self,name,salary):

        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):

        if value < 0:
            raise ValueError("Salary must be positive")

        self.__salary = value


e = Employee("Mahesh", 50000)

print(e.name)
print(e.salary)

e.salary = 60000

print(e.salary)

# e.salary = -1000

# print(e.salary)

### Assignment 2 — Medium: Dunder Methods


        

"""
Create a class:

```python
class Book:
```

It should contain:

* `title`
* `author`
* `pages`

Implement:

```python
__str__()
__repr__()
__len__()
__eq__()
```

Requirements:

* `str(book)` → human-readable description.
* `repr(book)` → developer/debug representation.
* `len(book)` → number of pages.
* Two books are equal when their **title and author** are the same.

For example:

```python
b1 = Book("Python Basics", "John", 300)
b2 = Book("Python Basics", "John", 350)

print(b1)
print(repr(b1))
print(len(b1))
print(b1 == b2)
```

---

"""
class Book:

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def __repr__(self):

        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"
    def __eq__(self, other):

        return self.title == other.title and self.author == other.author

    def __len__(self):
        return self.pages



b1 = Book("Python Basics", "John", 300)
b2 = Book("Python Basics", "John", 350)

print(b1)
print(repr(b1))
print(len(b1))
print(b1 == b2)


### Assignment 3 — Hard: Abstraction + Encapsulation + Polymorphism
"""
Create an abstract class:

```python
class Payment(ABC):
```

It should have an abstract method:

```python
pay(amount)
```

Create at least two concrete classes:

```python
class CreditCardPayment(Payment):
class UPIPayment(Payment):
```

Requirements:

1. `Payment` cannot be instantiated directly.
2. Each payment type implements `pay()`.
3. `amount` must be greater than `0`.
4. Store an appropriate internal/private piece of payment information.
5. Use polymorphism so that this works:

```python
payments = [
    CreditCardPayment(...),
    UPIPayment(...)
]

for payment in payments:
    payment.pay(1000)
```

6. Add a useful `__str__()` to the payment classes.

**Important:** Keep the design reasonably clean. Don't add unnecessary complexity.

"""

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass


class CreditCardPayment(Payment):

    def __init__(self,card_number):
        self.__card_number = f"****-****-****-{card_number[-4:]}"

    def pay(self,amount):

        if amount < 0:
            raise ValueError("Payment amount must be greater than 0.")
        print(f"Successfully processed ${amount:.2f} using Credit Card ({self.__card_number}).")

    def __str__(self):
        return f"Credit Card Payment Method ({self.__card_number})"


    

class UPIPayment(Payment):

    def __init__(self,upi_id):

        self.__upi_id = upi_id


    def pay(self,amount):
        if amount < 0:
            raise ValueError("Payment amount must be greater than 0.")

        print(f"Successfully processed ${amount:.2f} using UPI ID({self.__upi_id})")

    def __str__(self):

        return f"UPI Payment Method ({self.__upi_id})"



try:
    ghost_payment = Payment()

except TypeError as e:

    print(f"Correctly blocked abstract instantiation: {e}\n")

payments = [
    CreditCardPayment("1234567890123456"),
    UPIPayment("mahesh@okaxis")
]

# Print out the user-friendly __str__ representations
print("--- Registered Methods ---")

for payment in payments:

    print(payment)


print("\n--- Processing Payments ---")

for payment in payments:

    payment.pay(1000)

print("\n--- Testing Edge Case Validation ---")

try:

    payments[0].pay(-50)
except ValueError as e:

    print(f"Validation works perfectly: {e}")