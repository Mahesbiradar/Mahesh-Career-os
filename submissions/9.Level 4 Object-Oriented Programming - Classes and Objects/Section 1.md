
---

# 🟢 SECTION 1 — 10 OOP Questions

Difficulty increases from easy → hard.

### Q1 — Class vs Object

What is the difference between a **class** and an **object**?

Use a simple real-world example and then explain the Python relationship.

---

# Ans: A class is nothing but structure or bluprint to create an instance and the object is a intance of a class.

Ex: Suppose a Company manufactures cars and the company has design and structure to produce the cars so we can call it as class and a real produced car by using the bluprint or structure of the company is a object.


### Q2 — Attributes vs Methods

Consider:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("Studying")
```

Identify:

1. The attributes
2. The method
3. The instance variables
4. What `self` represents

---

# Ans: 
1. self.name and age are the attributes which contains the data or state of the objects.
2. study is the Method which defines the behaviour.
3.self.name and self.age are the intance variable.
4. self represents the current data or state of the newly created object.

### Q3 — `__init__` and `self`

Explain what happens when this executes:

```python
student = Student("Mahesh", 25)
```

Specifically:

* When is `__init__` called?
* What does `self` refer to?
* Where is `"Mahesh"` stored?
* Where is `25` stored?

---
# Ans:
1.the init method is called to intialize the current state of newly created object.
2.self referse to current instance.
3. "Mahesh" is the current instance value stored in the variable called name.
3."25" is stored as age. 


### Q4 — Instance Variable

What is the output?

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

Explain **why** the two values are different.

---
# Ans:
Amit
Rahul

The values are chnaged bcz we are assignimg the new name to the intance varible name for the student s1.

### Q5 — Class Variable

What is the output?

```python
class Student:

    school = "ABC School"


s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)

Student.school = "XYZ School"

print(s1.school)
print(s2.school)
```

Explain what happens to the class variable.

---
# Ans:
O/P
ABC School
ABC School
XYZ School
XYZ School

Here the School is class variable and shared amongs the all instnaces and Here in above program we have set class school as value "ABC School" and then we have reassigned a diffrent value to that class varibel therefor since class variobels ar shared amongst all the instances until override. and again we have chnaged the value of that class Therfor the the accessing class varibles value over instance will give updated value only.

### Q6 — Class Variable Trap

Consider:

```python
class Student:

    school = "ABC"


s1 = Student()
s2 = Student()

s1.school = "XYZ"

print(s1.school)
print(s2.school)
print(Student.school)
```

What is the output?

**Most importantly, explain why `s1.school` is different from `s2.school`.**

---
## Ans:

O/p:
XYZ
ABC
ABC

# Here initially the the class variable value is ABC and then we created two instance therefor these two instance shared same value of class varibles but later on we overides the class varible value on s1 instance with differnt value therefor the s1.school is diffrent from s2.school.


### Q7 — Instance Method

Consider:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


student = Student("Mahesh")
student.introduce()
```

Explain what happens conceptually when:

```python
student.introduce()
```

is called.

What is the role of `self`?

---
# Ans: Here when the we are calling a introduce method on the object called(student). The introduce method takes self as argument and prints My name is {self.name} Here self is nothing but the current instance which is student . and this statement is same like Student.introduce(student) so the methos taking a student as argument and printing somthing which is in print statement. So the role of self is passing the current instance so no need to pass the current instance as argument while calling the method on instance.

### Q8 — Class Method vs Instance Method

Explain the difference between:

```python
def change_name(self, name):
    ...
```

and:

```python
@classmethod
def change_school(cls, school):
    ...
```

Specifically explain:

* `self`
* `cls`
* What each method can access
* When you would use each one

---
# Ans: The basic diffrence b/w these two methods is change_name is instance/normal method and change_school is class method.

Here self is the current instance passed to as firts argument to the instance method.
'cls' is current class level varible passed as fist argument to the class method.
the change_name has access to the instance level data. and the change_school has access to the class level varibles.
When i want to access the instance level state ill use self and the when i want a access to the class level state then ill use cls.

### Q9 — Static Method

Why would we use:

```python
@staticmethod
def is_valid_email(email):
    ...
```

instead of a normal instance method?

What makes a static method different from an instance method and class method?

---
# Ans:

Here in above code is_valid_email dont need access isnatance or class level state therefor we use staticmethod.
the static method is logically belongs to class but dont required access to instance or class level state and it not use self or cls as first argument.


### Q10 — Hard: Design Decision

You're building a `BankAccount` class.

You have:

```text
account_number
balance
bank_name
deposit()
withdraw()
is_valid_account_number()
change_bank_name()
```

Decide which should be:

* Instance variable
* Class variable
* Instance method
* Class method
* Static method

Explain **why** for each.

---
# Ans:

* Instance variable - account_number,balance  Here each object have dicticnt account number and balance Therfor these tow are instance variables. 
* Class variable - here bank_name is class variable bcz bank name shoud be shared amongst all the customers(objects) of that bank so creating a class varible can have shared access to all the instances of that class.
* Instance method - deposit(), withdraw() These are instance methods bcz here we need instance level state. Suppose one customer deposits x amout that doent not relate to any other cutometrs so it instnace specific. similar the withdraw() also a instance specific.
* Class method - change_bank_name() is class method bcz here we need acess to the class variable bank_name for modification of cutomer bank name. Therfor change_bank_name() access to class level state.
* Static method - is_valid_account_number() Here we dont need any instance or class level state therefor this is static methos. which related to the class but dont required accees to instance or class level state ex self,cls.











