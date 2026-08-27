
---

# 🔵 SECTION 5 — OOP Output Prediction

---

## 🧪 Q1 — Instance Variables

```python
class Student:

    def __init__(self, name):
        self.name = name


s1 = Student("Mahesh")
s2 = Student("Rahul")

s1.name = "Amit"

print(s1.name)
print(s2.name)
```

What is the output?

Why doesn't changing `s1.name` affect `s2.name`?

---
# Ans: O/P
Amit
Rahul

Here we have chnaged the state of spefic object which is s1 there for it doesnot affects any other objects.



## 🧪 Q2 — Class Variable Shadowing

```python
class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name


e1 = Employee("Mahesh")
e2 = Employee("Rahul")

e1.company = "XYZ"

print(e1.company)
print(e2.company)
print(Employee.company)
```

What is the output?

Explain exactly where each value is coming from.

---

# Ans: O/P
XYZ
ABC
ABC

Here the we have  overidded the state of class variable for e1 object Therefor the value remains same for cls variable for all other objects and class varible itself excepts e1 object.

## 🧪 Q3 — Class Method

```python
class Employee:

    company = "ABC"

    @classmethod
    def change_company(cls, name):
        cls.company = name


e1 = Employee()
e2 = Employee()

e1.change_company("XYZ")

print(e1.company)
print(e2.company)
print(Employee.company)
```

What is the output?

Why can calling the class method through `e1` still change the class variable?

---

# Ans: O/P

XYZ
XYZ
XYZ

Here we are running the class method on e1 object still the class varible state is changed globally bcz the class method changingb the state of the class varible not not the object state.

## 🧪 Q4 — Instance vs Class Method

```python
class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

    @classmethod
    def show_company(cls):
        print(cls.company)


e = Employee("Mahesh")

e.show_name()
e.show_company()
```

What is the output?

For each method, tell me whether it receives:

```text
self
```

or:

```text
cls
```

---

# Ans: O/P
Mahesh
ABC

THE Instance method show_name receives self and the class method show_company receives the cls.


## 🧪 Q5 — Static Method

```python
class Employee:

    def __init__(self, salary):
        self.salary = salary

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


e = Employee(50000)

print(e.is_valid_salary(100))
print(Employee.is_valid_salary(-10))
```

What is the output?

Why doesn't `is_valid_salary()` need `self`?

---
# Ans: O/P
True
False

is_valid_salary() doent need the self bcz its static method and static method doent except self/cls automatically as first argument. 


## 🧪 Q6 — Hard: Attribute Lookup

```python
class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name


e = Employee("Mahesh")

print(e.company)

e.company = "XYZ"

print(e.company)

del e.company

print(e.company)
```

What is the output?

Most importantly, explain what happens after:

```python
del e.company
```

---

# Ans: O/P
ABC
XYZ
ABC

Here execution of  del e.company delted the current state of that objecst but still the class variable doesnt affect from this therefor printing again print(e.company) wll prints ABC.


## 🧪 Q7 — Class Variable Mutation

```python
class Counter:

    count = 0

    def __init__(self):
        Counter.count += 1


a = Counter()
b = Counter()
c = Counter()

print(Counter.count)
print(a.count)
print(b.count)
```

What is the output?

Why can `a.count` access `count` even though `count` wasn't created using `self`?

---
# Ans: O/P
3
3
3

Here creting objects and initialiing object mutating the global varible count which incrementing by with each object creating . count is class varible therefor its shared by all objects of the class therfor the object also access the count.


## 🧪 Q8 — Method Binding

```python
class Student:

    def greet(self):
        print("Hello", self)


s = Student()

s.greet()
Student.greet(s)
```

What happens?

Will both calls work?

Why are they effectively related?

---
# Ans: O/P

Hello <object>  
Hello <object>

Here we have created object s and then running instance method on object and then claaing the method by passing object.
Yes both calls work.
The thisr question not sure.

## 🧪 Q9 — Class Method + Instance Attribute

```python
class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, company):
        cls.company = company


e1 = Employee("A")
e2 = Employee("B")

e1.company = "Personal"

Employee.change_company("XYZ")

print(e1.company)
print(e2.company)
print(Employee.company)
```

What is the output?

This is testing whether you can distinguish:

```text
instance attribute
vs
class attribute
```

---

# Ans: O/P
Personal
XYZ
XYZ

Now here we have we have created a class variable company with value "ABC" then we have changed the state of e1 object for class varibel value and the we have changed the value of class variable through the class method now the state current state of class variable is shared by all object but the e1 object state of company was overidded therefor chaning the class state doent change this object state.

company is class attribute but self.name = name is teh intance attribute

## 🧪 Q10 — Hardest

```python
class Employee:

    company = "ABC"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_default():
        return Employee("Unknown")

    @classmethod
    def create(cls, name):
        return cls(name)


e1 = Employee.create_default()
e2 = Employee.create("Mahesh")

print(e1.name)
print(e2.name)
print(type(e1).__name__)
print(type(e2).__name__)
```

What is the output?

And explain the conceptual difference between:

```python
Employee(...)
```

inside the static method and:

```python
cls(...)
```

inside the class method.

---

# Ans:

O/P

Unknown
Mahesh
Employee
Employee


Here both the method calling the class Employee.

in static method calling Employee Class by passing the defualt name Unknown to create object. and the class method also claaing the Employee class by passing the user given name.

