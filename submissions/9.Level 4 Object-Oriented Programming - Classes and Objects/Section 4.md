
---

# 🟠 SECTION 4 — DEBUGGING

For each question answer:

1. What is wrong?
2. Why does it happen?
3. What happens when the code runs?
4. How would you fix it?

---

## 🐛 Debug Q1 — `self` vs Class Variable

```python
class Employee:

    company = "ABC"

    def __init__(self, name):
        name = name

    def display(self):
        print(self.name)
        print(self.company)


emp = Employee("Mahesh")
emp.display()
```

The programmer expects:

```text
Mahesh
ABC
```

What is wrong?

---

# Ans: Here while intializing the object state the objects curremt intance expects self.name but only name exists Therefor Attribute Error raises.

When code runs python raises attribute Error. Here while initilizing objects state we have add the reference for the current instance which self.  self.name = name


## 🐛 Debug Q2 — Class Method

```python
class Employee:

    company = "ABC"

    @classmethod
    def change_company(self, new_company):
        self.company = new_company


Employee.change_company("XYZ")

print(Employee.company)
```

This code may appear to work.

But the programmer has used the wrong terminology/convention.

What should the first parameter of a class method be called?

What should the corrected code look like?

---
Here self is used as first paramenter for the class method but self is used for the instance method here we shoud use cls as convestion for the class method as first parameter.

corrected code 

def change_company(cls, new_company):
        cls.company = new_company

## 🐛 Debug Q3 — Class Variable vs Instance Variable

```python
class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Mahesh")
emp2 = Employee("Rahul")

emp1.company = "XYZ"

print(emp1.company)
print(emp2.company)
print(Employee.company)
```

The programmer expected all three to print `"XYZ"`.

Why doesn't that happen?

---

# Ans: Here initailly the class variable contains the value as ABC and this is shared amongst all the instances but here in code the value of the global varibels company is overidded for the only emp1 object now the overidded value is set only for that specific object and all other objects and class varible contains the same value. Value therefor still XYZ not printed for other objects and class variable value except emp1 object.

If we need to change the value of class variable then we shoud change the value of class varible only 

Employee.company = "XYZ"

for changing the class varibels value we shoud assign value to the class variable.

## 🐛 Debug Q4 — Exception Inside a Loop

```python
def process_numbers(numbers):

    try:
        results = []

        for number in numbers:
            results.append(int(number))

        return results

    except ValueError:
        print("Invalid number")


numbers = ["10", "20", "abc", "40"]

result = process_numbers(numbers)

print(result)
```

The programmer wants:

```text
[10, 20, 40]
```

and wants invalid values to be skipped.

What is wrong with the exception structure?

How would you fix it?

---

# Ans: Here the existing structure of exception handling is outside the loop and to skip if nay inavlid numbers we shoud use this structure indixe the loop if any non int number exist we can skip and continue with other records. bcz the exition block outsize the loop the loop exits immdeatly after error occurs the remaining record will not processed.


def process_numbers(numbers):
    results = []
    for number in numbers:
        try:
            results.append(int(number))
        except ValueError:
            print(f"Skipping invalid number: {number}")
    return results

numbers = ["10", "20", "abc", "40"]
result = process_numbers(numbers)
print(result)


## 🐛 Debug Q5 — Custom Exception + OOP

```python
class InvalidSalaryError(Exception):
    pass


class Employee:

    def __init__(self, name, salary):
        if salary <= 0:
            raise InvalidSalaryError("Salary must be positive")

        self.name = name
        self.salary = salary


try:
    emp = Employee("Mahesh", -50000)

except ValueError:
    print("Invalid salary")
```

The programmer expects:

```text
Invalid salary
```

to be printed.

What is wrong?

How should the exception be handled?

---
# Ans: Here once the program runs the ans raises the error the code attempts to catch a valueError, but the InvalidSalaryError doent inherits from the valueError therfor the InvalidSalaryError exeption goes unhandeled and the program crashes. with the traceback insted of printing the the expected error message.

class InvalidSalaryError(Exception):
    pass


class Employee:

    def __init__(self, name, salary):
        if salary <= 0:
            raise InvalidSalaryError("Salary must be positive")

        self.name = name
        self.salary = salary


try:
    emp = Employee("Mahesh", -50000)

except InvalidSalaryError:  # Caught the correct custom exception
    print("Invalid salary")



