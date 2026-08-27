
---

# 🎤 SECTION 6 — OOP Interview Round

---

## 🎤 Q1 — Class vs Object

> "Explain class and object to me without using the phrase 'class is a blueprint'."

I want a technical definition.

---
# Ans:

Class is structure used to craete the real objects and objects are the intances created using the structure defined in class.

Ex: Collage is the class where all the template,structure were created and students are the object they study and learn the subject usingb the template or structure defined by collage.


## 🎤 Q2 — Instance vs Class Variables

Suppose you have:

```python
class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

Why are:

```text
name
salary
```

instance variables, while:

```text
company
```

is a class variable?

And give me one situation where `company` **should instead be an instance variable**.

---
# Ans:

the name and salry is instance variables bcz there are initilized after every object creation and each instrance has ist own distict state where as the company has state which is global and shared by all objects unles overidded by obeject state. Therefor the company is class varible.

1. To make company as intance variable we shoude intialized after the object creating so it shoud contains it own distint state with each object. or overidding the state of class variable for object and therefor the company will be isntrance varianle for that specific object.


## 🎤 Q3 — `self` vs `cls`

This is a very important interview question:

> **"What is the difference between `self` and `cls`?"**

Don't just say:

```text
self = object
cls = class
```

Explain what they allow the method to access and why they are passed automatically.

---
# Ans:

self is current intance and passed to instance method automatically as first argumet where as cls is class which is passed automatically to class methods as first argument.


## 🎤 Q4 — Three Method Types

Imagine I give you:

```text
Employee
```

and ask you to implement:

```text
1. calculate_salary()
2. change_company()
3. validate_employee_id()
```

Which would you make:

* Instance method?
* Class method?
* Static method?

You decide the design and explain **why**.

---

# Ans:

Here ill make calculate_salary() as * Instance method? bcz each object has its own distict state therefor ill use this method as Instance method. similarly ill use change_company() as class method as most of the employees share same state and to change the state of class varibel ill use this method as class method.

And finnaly ill use the validate_employee_id() as static method since ist doent depends on instance or class state but related to the class therefor ill use this method as static method.



## 🎤 Q5 — Real Interview Scenario 🔥

You're designing a backend application with:

```python
class Vehicle:
```

Every vehicle has:

```text
vehicle_number
model
price
```

The company has:

```text
company_name
```

You need:

```text
display_details()
change_company()
is_valid_vehicle_number()
```

Explain how you would design the class.

I want you to tell me:

```text
vehicle_number → ?
model          → ?
price          → ?
company_name   → ?

display_details()       → ?
change_company()        → ?
is_valid_vehicle_number() → ?
```

And explain **why** you chose each type.

---

Here ill use:vehicle_number,model,price as instance variable bcz each object will have distince state for these variable.
company_name as class variable bcz its shared by all instances therefor no need to use as instance variable.

display_details() as instance method where we pass current instace for showing related data of that object by passing current instance as self.

change_company() as class method to change the state of the class variable.

is_valid_vehicle_number() as static method bcz it doent required any instance or class states.
