# Inheritance (Python)

## Why It Matters
- Interviewers ask about inheritance because it tests whether you understand parent-child class relationships and method overriding.
- Backend frameworks use inheritance heavily in Django class-based views, forms, models, serializers, exceptions, and reusable base classes.
- Good inheritance reduces repeated code, but careless inheritance can make behavior hard to trace.

## Core Concepts
- Inheritance lets one class reuse attributes and methods from another class.
- The original class is the parent class or base class.
- The new class is the child class or subclass.
- A child class can add new attributes, add new methods, or override parent methods.
- `super()` calls the parent implementation, commonly inside the child constructor.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
```

## Important Syntax
```python
class Child(Parent): ...

super().__init__(value)

def method(self): ...  # child version overrides parent version
```

## Memory Tricks
- Parent class = shared base behavior.
- Child class = specialized version.
- `super()` means "reuse the parent part instead of rewriting it."

## Interview Questions
- ⭐ What is inheritance in Python?
- ⭐ Why is `super()` used inside a child class constructor?
- What is method overriding?
- What is the difference between a parent class and a child class?
- Why should a subclass override a method instead of copying the parent implementation?
- Scenario: `Manager` and `Developer` share employee details but have different extra behavior. How would inheritance help?

## Common Mistakes
- Forgetting to call `super().__init__(...)`, so parent attributes are never initialized.
- Copying the parent constructor instead of reusing it with `super()`.
- Thinking override means changing the parent method; it only changes behavior for the child class.
- Adding extra printed output when the assignment asks for exact output lines.
- Using inheritance when simple composition would be clearer.

## Common Confusions ⚠
- Inheritance vs object creation: inheritance connects classes; object creation makes an instance from a class.
- Override vs overload: overriding replaces parent behavior in a child class; Python does not use Java-style method overloading by signature.
- Parent class vs child object: the child class inherits code, but each created object still has its own instance data.
- `super().__init__()` vs inheriting methods: `super().__init__()` calls parent initialization; inherited methods are available because of the class relationship.

## Real Backend Usage
- Django class-based views inherit from base view classes and override methods like `get()` or `post()`.
- Django models inherit from `models.Model`.
- DRF serializers and viewsets inherit shared behavior and override specific hooks.
- Custom exceptions often inherit from a base exception class.
- Shared service classes can define common behavior while subclasses specialize business rules.

## 30-Second Interview Revision
- Inheritance lets a child class reuse parent class code.
- Parent/base class holds shared behavior; child/subclass specializes it.
- `super().__init__(...)` calls the parent constructor to initialize parent attributes.
- Overriding means the child provides its own version of a parent method.
- Backend frameworks use inheritance in views, serializers, models, forms, and exceptions.
