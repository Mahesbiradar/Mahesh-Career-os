### Section B — Short coding
"""
**Q11. File Handling**

Write a function:

```python
def count_lines(filename):
    ...
```

It should open a text file and return the number of lines.

Use a context manager.

---

"""

# Ans:

def count_lines(filename):
    
    with open(filename,"r") as file:

        lines = file.readlines()

        return len(lines)



"""
**Q12. Exceptions**

Write a function:

```python
def divide(a, b):
    ...
```

Requirements:

* Return `a / b`
* Handle division by zero
* Print a meaningful message
* Use `try/except`

---

"""
# Ans:

def divide(a, b):

    try:

        return a / b

    except ZeroDivisionError:
        print("Cannot Divide by zero Pls enter Valid Number")

        return None

print(divide(10,0))

"""

**Q13. OOP**

Create:

```python
class BankAccount
```

Requirements:

* `owner`
* `balance`
* `deposit(amount)`
* `withdraw(amount)`
* Don't allow withdrawal greater than balance.

Keep it simple. No need for property yet.

---
"""

class BankAccount:

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited amount in Account is: {amount}"
        return "Invalid deposit amount."

    def withdraw(self,amount):

        if amount > self.balance:
            print("Unable to process request due to insufficient balance")
        elif amount <= 0:
            print("Please enter a valid withdrawal amount.")
        else:
            self.balance -= amount
            return f"Withdrew: {amount}"



"""
## Section C — Debugging

**Q14.**

What's wrong with this?

```python
with open("data.txt", "r") as file:
    data = file.read()

print(file.read())
```

Explain the problem.

---

"""

# Ans: In above code the context manager opened the file in read mode and then all the data of file is kept in data variable as string.

# but the print(file.read()) statement is written outsie the cobtexr manager/ file handling. therefor it will raise and error if we want to print the contnt of the file then we can use varibale name in print statement this prints the data.



"""
**Q15.**

What's wrong with this?

```python
class Student:

    college = "ABC"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_name(cls, name):
        cls.name = name
```

The developer wants to change the student's name.

What conceptual mistake has been made?

---

"""
# Ans:
# In above given code block the developer has built the class method to chnage the state of the object where as the class methods are used to changes the state of attributes at class level not object level.BankAccount
# to change the students name we shoud use instance method as follow

def change_name(self, name):
        self.name = name

"""
**Q16.**

Find the problem:

```python
class Dog:

    def __init__(self, name):
        self.name = name

class Puppy(Dog):

    def __init__(self, name, age):
        self.age = age
```

What happens to `name`?

How would you fix it using `super()`?

---
"""
# Ans:

# In the original code, the Puppy class overrides the parent's __init__ method but does not call it. Because of this, the parent's initialization logic is skipped, and the name attribute is never created on the object. Trying to access p1.name will throw an AttributeError.

# # Here is the fixed version

class Dog:

    def __init__(self, name):
        self.name = name

class Puppy(Dog):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

p1 = Puppy("indi",5)

print(p1.name)


"""
## Section D — Output Prediction

**Q17.**

What is the output?

```python
class Student:

    college = "ABC"

    def __init__(self, name):
        self.name = name

s1 = Student("A")
s2 = Student("B")

s1.college = "XYZ"

print(s1.college)
print(s2.college)
print(Student.college)
```

Explain **why**.

---
"""
# Ans:

# XYZ
# ABC
# ABC

# Here intilly the objects were created and they has shared access to the class variable called college and then s1.college = "XYZ" overidded the object state for this variable called collage.

# There for claaing the collage atribute on s1 given XYZ and s2 still sharing the same state as the class attribute that why calling collage on s2 gives ABC and same with overiddeing the object level state doent impact on class level attribute therdir Student.collage alos gives ABC.


"""
**Q18.**

What is the output?

```python
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):
        print("Dog")


animal = Animal()
dog = Dog()

animal.speak()
dog.speak()
```

Explain the OOP concept involved.

---

"""

# Ans:

# In above given code the the parent class and child class have the same method name but the child class has extent its own implementation which class method overidding in OOPS.print

# Where Child inherits from paremnt and can extent its own imeplemenstation.


"""
## Section E — Interview Questions

**Q19.**

You're asked:

> "Why should we use exception handling instead of simply letting the application crash?"

Answer as if you're interviewing for a backend developer position.

---

"""

# As Backend Devoloper letting the application crash in production is a major issue. we use exception handling for four main reasons.print

# 1.Keep the application running: if one user causes the error(given bad input) the application shoud not be down for everyone else. Exception handling isolates the error so the server stays up.print
# 2.Better User Experiance: intead of app freezing or black screen we can catch the exception and send back the User Frednly error message.
# 3.Security: Application crashing prints the details trackeback of the code. if a hacker sees this.they get a map of our internal database and server structure.we catch exceptions to hide this sensitive information.
# 4.Debbugging: Caching the error allows us to silently log the errors so backend team works on this to fix the same.

# This answer i have read online and then written its not my own answer as of now.

"""
**Q20.**

You're asked:

> "Explain encapsulation in Python. Does Python have truly private variables?"

Give me an interview-quality answer.

---

"""

# Ans:

# Encapsulation means exposing the essential and hiding the actull imepementations for example the capsule is good example of encapsulation where the actull drug and ingredients are hiddent inside the capsule but user just seen the outer structure.print

# similary in pythin encapsulation allows us to expose only eseentials and hindes the actull implementations.


# Python truly not have a private varibales. In python we have convenstions and the Name mangling.

# The pythin convenstions are varible referce to public variable _variable means protected where its for internal use and __variable means name manglong where python alters the name of variable once it sees the __ and chnages it to _Classname__varibele name to prevent the accidentale name collision and variable overidiing.print

# Here its my own explanation.