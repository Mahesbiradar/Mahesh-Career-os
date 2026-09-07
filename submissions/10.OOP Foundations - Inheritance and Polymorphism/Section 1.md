

# 🟢 SECTION 1 — 10 Interview/Concept Questions

Difficulty progresses from easy → hard.

### Q1 — Basic Inheritance

What is inheritance in Python?

Explain:

1. What the parent class provides.
2. What the child class gets from the parent.
3. Why inheritance is useful.

Give a small example.

---
# Ans:

inheritance in python allows the child class to reuse and extend functionality of parent class.

1.Parent Class provides the state(attributes) and Behaviour(Methods) to child class.
2.child class gets the code and behaviour of its parent class.
3. Inheritance is useful bcz of code reusiblity,Extending therr behaviour, support polymorphism.


Class Vehicle:

    def work(self):

        print("Vehicle is running")


Class Car(Vehicle):

    Pass

Here above example the Child class car inherits the behaviour of parent class Vehicle and can extent its behaviour. so no need to write the same code at two time simply use the same code the parent has and can extent also.

### Q2 — Parent vs Child

Consider:

```python
class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")
```

Answer:

1. What is the parent class?
2. What is the child class?
3. Which methods can a `Car` object access?
4. Does `Vehicle` get `drive()` from `Car`?

Explain why.

---
# Ans:
1.Vehicle is the parent class for the Car child class.
2.Car is the child class of Vehicle.
3.Car can access all its parent class methods as well as it own methods also.ex: start,drive.
4.No bcz in above code the Car is inheriting from vehicle but vehicle not inherting from the car. therefor Vehicle cannot access the drive() from Car.

### Q3 — `super()`

Consider:

```python
class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size
```

Why do we use:

```python
super().__init__(name)
```

instead of simply writing:

```python
self.name = name
```

inside `Manager`?

---
# Ans:

here in python super() method is used to inherit the attributes and methods from the parent class when both parent and chils class has same methods.

we cant simply write self.name = name bcz we we need to inherit then we shoud use super() or if we use self.name = name
then this shadows the state of attrubute if parent class. and we cant inherit from parent class.


### Q4 — Method Overriding

What is **method overriding**?

Consider:

```python
class Animal:

    def speak(self):
        print("Some sound")


class Dog(Animal):

    def speak(self):
        print("Bark")
```

What happens when:

```python
dog = Dog()
dog.speak()
```

is executed?

Which `speak()` implementation is used and why?

---
# Ans:
When dog.speak() is executed the speak() method defined in the Dog class is executed bcz in python when the method overiding occures MRO Has resultion order it searches the method in own class then parent class. in this odrder the method executes if exist.
 

### Q5 — `super()` + Overriding

Consider:

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        super().speak()
        print("Bark")
```

What will:

```python
Dog().speak()
```

print?

And explain what `super().speak()` is doing.

---
# Ans:
once the Dog().speak() executes it prints.
Animal sound
Bark

Here super().speak() method inherting the implementation of parent class. and the when the Dog().speak() excecutes since it has its own speak() method and inside this method it inherting the same method from parent class there for here first the Animal sound prints the Bark prints.


### Q6 — Polymorphism

What is **polymorphism** in Python?

Consider:

```python
class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


def make_sound(animal):
    animal.speak()
```

Why can this work?

```python
make_sound(Dog())
make_sound(Cat())
```

Even though `Dog` and `Cat` are different classes?

---
# Ans:

In python polymorphism provides the same  interface/operation for diffrent types of bojects of bojects with diffrent behaviours.

Here the make_sound provides the same interface for different classes dog and cat. 


### Q7 — Polymorphism + Inheritance

Consider:

```python
class Payment:

    def process(self):
        print("Processing payment")


class UPI(Payment):

    def process(self):
        print("Processing UPI")


class Card(Payment):

    def process(self):
        print("Processing Card")
```

Then:

```python
payments = [UPI(), Card(), Payment()]

for payment in payments:
    payment.process()
```

Explain why the same:

```python
payment.process()
```

can produce different behavior.

What OOP concept is demonstrated here?

---
# Ans: Here payment.process() can produce different behavior bcz this phenomenon cladded in python as Polymorphism + inheritance. Here both the subclasses upi and card inherits the behaviour from parent class Payment and these subclasses extended the behavour of parent method process()

in this code block Polymorphism + inheritance is demonstrated.


### Q8 — `isinstance()`

Consider:

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()
```

Predict:

```python
isinstance(car, Car)
isinstance(car, Vehicle)
isinstance(car, object)
```

Will all three be `True`?

Explain **why**.

---
# Ans:

Will all three be `True`? Yes.

Here isinstance check the relationship of object -> class threfor the firt statement checking that car objects belongs to Car class which is true. and in second statement checking the wheather car object belongs to Vehicle class which is true bcz here the car object is belongs to Car class which is child class of Vehicle. and in third statement isinstance checjing car is wheather object or not and its True car is object.

### Q9 — `issubclass()` vs `isinstance()`

Given:

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()
```

Explain the result of:

```python
issubclass(Car, Vehicle)
issubclass(Vehicle, Car)

isinstance(car, Car)
isinstance(Car, Vehicle)
```

Be careful here: some are checking **class relationships**, while others are checking **object relationships**.

---
# Ans:
issubclass(Car, Vehicle) - True  Bcz issubclass checks relationship b/w class to class and here Car class is subclass of Vehicle.
issubclass(Vehicle, Car) - False Here Vehicle is not subclass of Car Class.

isinstance(car, Car) - True bcz car is object and its instance of Car class.
isinstance(Car, Vehicle) - False bcz Car is class not an instance of Vehicle Class.



### 🔴 Q10 — Multiple Inheritance + MRO

Consider:

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
```

Now:

```python
d = D()
d.show()
```

Which version of `show()` will execute?

Explain **why Python chooses that method**.

You don't need to give the complete MRO algorithm yet, but explain what you understand about the method lookup order.

---

# Ans:

Here once the d.show() executes the method of Class b executes.

In Python MRO Takes place when executing the methods or accesing the attribute state.

Here the when we are calling the show() method on obejct d this object is istnace of Class D then python searches the show method in D Class in above code The D class doent have its own show method then python searches in it parent class since D inhertis from two parent classes and in the order of Class B first and Class C next therefor python search the show method in B class first and the method exist in this B class and class the method and it prints B . This takes place as Method resolution order.

