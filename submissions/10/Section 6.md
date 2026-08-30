# 🎤 SECTION 6 — Interview Round

Answer these as you would in a junior Python/backend interview.

---

## Q1 — Inheritance vs Composition

You've learned inheritance.

Suppose you have:

```text
Car
Engine
```

Would you model this as:

```python
class Car(Engine):
```

or:

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

Which relationship does each represent?

Which would normally make more sense for a car and an engine?

Explain why.

---
# Ans:
In above given code the first statement shows the relationship of inheritance. Where Car class inhering from the Engine class. And in second relationship then the engine is attribute of car class and it contains the value of Engine class.

The first relationship is make more sense bcz Engine is part of vehicle and each vehicle contains the distict engine so inheriting from base class and then extending functionality makes more sense. Here we can Inherit base class data and behaviour and add on own things for car class.


## Q2 — `super()`

An interviewer asks:

> **"Does `super()` mean 'call my parent class'?"**

Would you say yes or no?

Give me a technically accurate explanation.

---
# Ans:
Yes super() mean call my parent class in littrela sense.

seince we access the parent class attributes and behaviour when the child class has itw own implementation and when it want to add top of the base of parent class data and behavour super() helps to do so.

Suppose parent class has some base functionlaity and when child class want to extend that functionality instead of copy pasting thw whole code we can simply using super method access the parent class base functionality and then we can add to the base functionlaity and name application specific functionality wich make the code more maintanable and readable.

## Q3 — Method Overriding

An interviewer asks:

> **"If a child class overrides a method, is the parent's method gone?"**

Explain what actually happens.

Also explain how you can still access the parent implementation.

---
# AnS:

If child class overides a method then parent's method will be not affected at all. Here when the child class overides method it means it simply creates a its own method which shadows the parent method. and the child class still access the parent implementation using the super() method and extends the functionality.

## Q4 — Polymorphism

Explain polymorphism using this example:

```python
class Payment:
    def process(self):
        ...


class UPI(Payment):
    ...


class Card(Payment):
    ...
```

The interviewer asks:

> "Why is polymorphism useful in a backend system instead of simply using `if/elif` based on payment type?"

Give a practical answer.

---
# Ans: The polymorphism useful in backend system instead of simply using `if/elif` bcz now let take example of above mentioned code where we have different payemnt mode like we have objects of diffrent type or we can say objects have diffrent behaviour but they all need to process the paymennt means all the methods of will process the payment now if we use if/else and assume we have n payment modes so inteand writing n if else conditions here the maintiningbilty issue is there in future there may new payment modes may arrive but all are performing same operation so here polymorphism is useful which simply provides same operations or ingterface on diffrent types of objects or objects with diffrent behaviour. with polymorphism we simply reduce lines code where all if else contions were writen and main thing is maintainibility.


## Q5 — `isinstance()` vs `issubclass()` 🔥

Explain this to me without looking at notes:

```python
isinstance(obj, Class)
```

vs:

```python
issubclass(Child, Parent)
```

Then explain why this is wrong:

```python
isinstance(Car, Vehicle)
```

when `Car` is defined as:

```python
class Car(Vehicle):
    pass
```

And what should be written instead to test the two different relationships?

---
# Ans:

Here in python both isinstance() and issubclass() are used for diffrent functionlaity.

isinstance check the obj - class relations which means does the object belongs to the clas or subclass. and the issubclass checks the class to class relation which means it checks wheather Child class inherits from the parent class or not.


isinstance(obj, Class) here this statement check does the obj belongs to Class or its subclasses.

issubclass(Child, Parent) Here the statementr checks does the child class related to the parent class or not which simpy meand inherited from parent or not.


isinstance(Car, Vehicle)
```

when `Car` is defined as:

```python
class Car(Vehicle):
    pass

In abive menbtioned code in parenthesis the python consider Car as object and cheks the relationship with clas Vehicle but here in actull implementation Car is not an object Vehicle class or its subclass. the Car is class to check the class to class relationship issubclass() shoud be used.