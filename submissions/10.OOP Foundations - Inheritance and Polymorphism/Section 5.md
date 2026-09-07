---

# 🔵 SECTION 5 — Output Prediction

**Do not run these.**
Give me the exact output and explain why.

These are primarily **Inheritance + Polymorphism** questions.

---

## Q1 — Basic Inheritance

```python
class Vehicle:

    def start(self):
        print("Vehicle")


class Car(Vehicle):
    pass


car = Car()
car.start()
```

What is printed?

Why can `Car` access `start()`?

---
# Ans:
Vehicle

Car is child class of Vehicle class therefor Car can access all the methods and attributed of parent class therfor Carcan access start().

## Q2 — Overriding

```python
class Vehicle:

    def start(self):
        print("Vehicle")


class Car(Vehicle):

    def start(self):
        print("Car")


vehicle = Vehicle()
car = Car()

vehicle.start()
car.start()
```

What is the exact output?

Why doesn't `car.start()` call the parent's method?

---
# Ans: O/P
Vehicle
Car

Since Car class has ist own start() method therfore its not calling the parent's method unless explicitly delegating call using the super().

## Q3 — `super()`

```python
class Vehicle:

    def start(self):
        print("Vehicle")


class Car(Vehicle):

    def start(self):
        super().start()
        print("Car")


Car().start()
```

What is the output?

Explain the execution order.

---
# Ans: O/p
Vehicle
Car

Here once the Car().start() executes in the start method in Car class first it calling the parent start class which prints Vehicle and then the start method has one more print stetment which prints Car.

## Q4 — Polymorphism

```python
class Dog:

    def speak(self):
        return "Bark"


class Cat:

    def speak(self):
        return "Meow"


def speak(animal):
    print(animal.speak())


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    speak(animal)
```

What is the exact output?

What OOP concept is being demonstrated?

---
# Ans: O/P
Bark
Meow
Bark

This code block demonstares the Polymorphism concept of oops.

Where Polymorphism provide same operation/Interface on differmt types of objcets or objects with differen behaviour.

# Ans:
## Q5 — `isinstance()` 🔥

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()

print(isinstance(car, Car))
print(isinstance(car, Vehicle))
print(isinstance(Car, Vehicle))
print(issubclass(Car, Vehicle))
```

Give all four outputs **in order**.

Be especially careful with the third one.

---
# Ans O/P
True
True
False  """ Here isinstance check object-class inheritance relationship in python after    
       all everythging is object and Car as object doent belongs or inherits from Vehicle therefor False.""
True

## Q6 — MRO

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


print(D.__mro__)
D().show()
```

You don't need to reproduce the exact representation of the `__mro__` tuple.

Tell me the **class order** in the MRO and what `D().show()` prints.

---
# Ans: O/P
B

Here ho method resolution order takes place is fist the class is being searched in own class if not exist then check with parent class here b is first parent and c is second parent therfor first the method is searched in class b if exist then executed else searches in class c and if not exist in both parent class b and c then it will to nect heirachy where b and c are child class of a. But in above code.


## Q7 — `super()` in a Chain

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(B):

    def show(self):
        super().show()
        print("C")


C().show()
```

What is the exact output order?

Explain the chain.

---
# Ans: O/P

A
B
C

Here C has its own method which exting the implementation of parent class method b and b also extending the implementation in method show() first the class a method prints A then class b prints b  and finaaly class c method show() prints C

## Q8 — Polymorphism + Overriding

```python
class Employee:

    def calculate_bonus(self):
        return 1000


class Manager(Employee):

    def calculate_bonus(self):
        return 3000


class Intern(Employee):

    def calculate_bonus(self):
        return 500


employees = [
    Employee(),
    Manager(),
    Intern()
]

for employee in employees:
    print(employee.calculate_bonus())
```

What is the output?

Why is this polymorphism?

---
# Ans:
1000
3000
500

Here in lopp we are calling the method of diffrenr class and each method has diffrenr behaviour still the python providing interface in same way. even all methods has different behaviour.


## Q9 — `issubclass()` 🔥

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


class ElectricCar(Car):
    pass


print(issubclass(ElectricCar, Car))
print(issubclass(ElectricCar, Vehicle))
print(issubclass(Car, ElectricCar))
```

What is the output?

Explain each one.

---
# Ans:
True
True
False

Here issubclass checks Class to class relationship. and Since ElectricCar is subclass of Car( Bcz it inherts from Car) Therfor its True. and in second ElectricCar is subclass of Vehicle bcz ElectricCar is inheriting from Car and Car inherting From Vehicle.

and In last Car is subclass of Vehicle not the subclass of ElectricCar threfor it gives False



## Q10 — Hard

```python
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):
        print("Dog")
        super().speak()


class Puppy(Dog):

    def speak(self):
        print("Puppy")
        super().speak()


Puppy().speak()
```

What is the exact output?

Draw the execution mentally:

```text
Puppy.speak()
     ↓
?
     ↓
?
     ↓
?
```

---

# Ans:
Puppy
Dog
Animal

Puppy.speak() ->
        ↓
   print("Puppy")
        ↓
   super().speak()
        ↓
   print("Dog")
        ↓
   super().speak()
        ↓
   print("Animal")




