
---

# 🐛 SECTION 4 — DEBUGGING ROUND

For each question answer:

**1. What's wrong?**
**2. Why?**
**3. What happens?**
**4. How would you fix it?**

Don't just give the corrected code—explain the underlying OOP concept.

---

## 🐛 Debug Q1 — `super()`

```python
class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, team_size):
        self.team_size = team_size
```

Then:

```python
manager = Manager("Mahesh", 5)

print(manager.name)
```

The programmer expects:

```text
Mahesh
```

What is wrong?

Why would `super()` be useful here?

---

# Ans: Here in the child class the in initializer method we have not delegating the parent instnace atribute name. to deligate the parent instance atribute super() method is useful.
here is the fix.

    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

## 🐛 Debug Q2 — Overriding

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Bark")

        super().speak()
```

The programmer expected only:

```text
Bark
```

but gets:

```text
Bark
Animal sound
```

Is the code actually wrong?

Explain what `super()` is doing and how you would change it **if only `Bark` should be printed**.

---
# Ans: Here the code is not wrong but in child class the using super method class method is deligated therefor both Bark and Animal sound is printed if the user want to print only Bark then we shoud remove super().speak()

Here once we call the speak  method on the object created using the child class Dog. Here the speak() method exist in both parent class and child class. so when we call it as per above code the method first print the Bark and then call the parent class bcz we have delegated parent method using super() method and the parent method prints Animal sound.
if we need only the Bark we shoud comment out the class method delegated stetment super().speak()




## 🐛 Debug Q3 — `isinstance()` Trap

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


print(isinstance(Car, Vehicle))
```

The programmer expects:

```text
True
```

because `Car` inherits from `Vehicle`.

What's wrong with their reasoning?

How would you correctly check the inheritance relationship?

And how would you correctly check whether a `Car` object is an instance of `Vehicle`?

---

# Ans: Here Car is child class of parent class Vehicle but Car is not an intance. isinstance checks the object to Class relationship. since Car is class so we can use issubclass to check class to class inheritance relationship.

to check the inheritance relationship we can use below statement.

print(issubclass(Car, Vehicle))  

and to correctly check wheatger a Car objcet is and instance of Vehicle the we can creat one object and then we can check inheritance relationship

mycar = Car()

print(isinstance(mycar,Vehicle))



## 🐛 Debug Q4 — Polymorphism Broken

```python
class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


def make_sound(animal):

    if isinstance(animal, Dog):
        animal.speak()

    elif isinstance(animal, Cat):
        animal.speak()
```

The programmer says:

> "I'm using polymorphism."

Do you agree?

What's unnecessarily wrong with this design?

How would you rewrite `make_sound()` to properly demonstrate polymorphism?

---
# Ans: Here ill Not agress with programer bcz polymorphism is about same operation/interface with diffrent type of object or objcets with diffrent behaviours.

in the main function regardless of instance inheritance relationship the mthod shoud work for all objects then only we can conclude its polymorphism.

to properly demonstrate polymorphism ill simply run the method on object.


def make_sound(animal):
    animal.speak()


## 🐛 Debug Q5 — Multiple Inheritance + MRO 🔴

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


d = D()
d.show()
```

The programmer says:

> "Python will be confused because both B and C have `show()`."

Is that correct?

What gets printed?

Why?

And what concept determines which method Python finds first?

---

# Ans:

for the first quetion here python will not confuse it uses mro to resolve the methods order.

since class D donnt have any show method on its own python then checksthis method from the parent class since D inhering in order first from B and then C and both has this method therefor the methods ib class B excuted bcz of first order. and B is printed.

Here why Method in B gets Excuted comes from MRO method resulution order. Which determines when multiple methods with same name exist in child or parent class which methid shoud be executed.Here if the class consist of own method then it will executed if not then pythin checks with is parent class in order.




