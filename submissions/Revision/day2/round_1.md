
---

# 🧠 DAY 2 ASSESSMENT

Now **don't look back at the revision while answering**.

We'll do this in **two rounds**, just like your previous assessments.

## ROUND 1 — Concepts + Short Problems

### Section A — Conceptual

**Q1.** What is the difference between:

```python
read()
readline()
readlines()
```

---
# Ans:

read()-reads teh entire file.
readline()-loads one line at time in string.
readlines()- loads every line and packages then into a list of strings.

**Q2.** Explain the difference between `"w"` and `"a"` file modes.

Give a practical example where `"a"` would be preferable.

---
# Ans:

w - write mode where it overiddes all the existing data of the file and append new data if any.

a - append mode append the new data after the last line of exiting content.

append mode is preferable where we need to append the data next to the existing content.

suppose i have file containig the existing adata and i want to add some data after the existing content ill use append mode.


**Q3.** Why is this generally preferred?

```python
with open("data.txt") as file:
    data = file.read()
```

over:

```python
file = open("data.txt")
data = file.read()
file.close()
```

Explain what a **context manager** is.

---
# Ans:

in above given two code blocks the first code block is preffered bcz the with statement uses context managers.

as in above mentiond code doent have the resource closoing statement bcz the content managers automatically handeles this.

there for the using first block over second is more prefarable which handels the resources efficinetly.

context managers manages the setup and cleanup of the resources effectively.



**Q4.** Explain the difference between:

```python
try
except
else
finally
```

Give the execution condition for each.

---
# Ans:

the try block we keep the code where exception may occure means this code my contain the potential error.

the except block handles the errors/ exceptions occured in the try block.

the else block is to execute if no exception ocurres in try then this will excecute.

the finnally block will execute all the time its for cleanup.


try can raise the exception,Except block handels the exceptions raised in try block,else executes if not exceptions occured in try, finaly will run all the times not dependent on any block.


**Q5.** What is the difference between:

```python
raise ValueError(...)
```

and simply allowing Python to naturally raise a `ValueError`?

---
# Ans:

Here explicitly raiseing the ValueError is good practice where we can handle the valueerror which can prevent the crashing of entire programm just because of this block.

whereas allowong python to naturally raise ValueError crashes the program and prevernt all the code block after this error will be not executed.

so explicity raising potential exception can be handled in good way rather than allowoing pythn to handle it naturally will crash the code.

**Q6.** Explain the difference between a **class** and an **object**.

Then explain the exact responsibility of `__init__`.

---
# Ans:

Class in nothing but bluprint/template defination.

object is instance created using the bluprint(class)

__init__ intializes the state of newly created object.


**Q7.** What is the difference between an **instance variable** and a **class variable**?

Use a student example.

---
# Ans:

intance variables are varibles where each object has it own state whereas the class varibales are shared amongst all the objects of that class unless its overidded by objects state.

suppose if we have class 

Class Student:

    collage_name = "ABC"

    def __init__(self,name):

        self.name = name

IN above block the name is instance varibels ans has its own state for each object but the collage_name is class varibels and its shared amongts all the object unless its overidded by object state.


**Q8.** Explain the difference between:

```python
self
cls
```

and when you would use:

```python
@staticmethod
```

---
# Ans: self is insatnce of current object cls is nothing but class itself.

self is used to asses the data belonging to one obejct and cls is used to access the data belonging to the entire class.

self is used in instance menthod and cls is used in class menthod.

@staticmethod is used when the method has functinality related to the class but dont need the access to self,class. or not dependent on the object or class state.


**Q9.** What is method overriding?

How is it related to polymorphism?

---

# Ans: The method overriding allows child classed to change or extent the implementation of the parent method.

method overriding is the primary way runtime polymorphism achived in oops.

polymorphism is nothing but many ways which provide same interface to objects with diffrent behaviour.

when we call the overriden method on a object the system determine which version of the method to execute at runtime based on the actull object type.


**Q10.** Explain these three terms in an interview:

```text
super()
MRO
isinstance()
```

Don't just give definitions — explain what each is used for.

---

# Ans:

super is in-built function that restunr the proxy object to call methods from parent or sibling class.it is used to reuse or extent the code from parent class without rewirting it.

MRO(Method Resolution Order)
The exact path that python follows to search method in class hierarchy. it is used by python to prevent the conflict or confution when diffremt classes have method with same name.

isinstance()
is a built in function that check if an object belongs to a specific class or subclass of it.

it is used for type checking and validation to make sure an object has the right tools and attributes before code tries to use it.




