# Class vs Instance vs Static Methods (Python)

## Why It Matters
- Interviewers ask this because it proves whether you know where method data comes from: the object, the class, or neither.
- Backend code uses these patterns in service classes, Django models, managers, serializers, factories, and helper utilities.
- Choosing the wrong method type can make code harder to reuse, especially when subclasses are added later.

## Core Concepts
- An instance method works with one object and receives `self`.
- A classmethod works with the class itself and receives `cls`.
- A staticmethod belongs inside a class for organization, but it receives neither `self` nor `cls`.
- Use an instance method when the logic needs object-specific data.
- Use a classmethod when the logic needs class-level data or should create an object from another format.
- Use a staticmethod when the logic is related to the class but does not need object or class state.

```python
class Employee:
    raise_amount = 1.04

    def full_name(self):
        return self.name

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
```

## Important Syntax
```python
def method(self): ...

@classmethod
def method(cls): ...

@staticmethod
def method(): ...
```

## Memory Tricks
- `self` means "this object."
- `cls` means "this class."
- static means "no object data and no class data."

## Interview Questions
- ⭐ What is the difference between an instance method, classmethod, and staticmethod?
- ⭐ When would you use a classmethod instead of a staticmethod?
- Why should classmethods use `cls` instead of the class name directly?
- What is an alternate constructor?
- When is `@staticmethod` useful?
- Scenario: You receive `"Anita-Sharma-Developer-50000"` and need to create an employee object. Which method type fits best?

## Common Mistakes
- Using `@staticmethod` for logic that needs class data.
- Using the class name directly inside a classmethod instead of `cls`.
- Forgetting that instance methods automatically receive `self`.
- Calling an instance method on the class without an object.
- Missing exact output labels even when the method logic is correct.

## Common Confusions ⚠
- Instance method vs classmethod: instance methods work with one object's data; classmethods work with class-level data or class construction.
- Classmethod vs staticmethod: classmethods receive `cls`; staticmethods receive neither `self` nor `cls`.
- Class variable vs classmethod: a class variable stores shared data; a classmethod is behavior that can read or change class-level data.
- Alternate constructor vs normal constructor: `__init__` initializes an object; a classmethod can parse input and return a new object.

## Real Backend Usage
- Django managers and query helpers often use class-level patterns.
- Model or serializer helper methods may use instance methods when they depend on one record's data.
- Classmethods are useful for factories, such as creating objects from JSON, CSV, or API payloads.
- Staticmethods are useful for small validation helpers that logically belong with a class but do not need stored state.

## 30-Second Interview Revision
- Instance method receives `self` and works with one object.
- Classmethod receives `cls` and works with the class.
- Staticmethod receives neither `self` nor `cls`.
- Use classmethods for class data and alternate constructors.
- Use staticmethods only when the helper is related to the class but does not need object or class state.
