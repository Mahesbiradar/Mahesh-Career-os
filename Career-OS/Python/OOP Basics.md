# OOP Basics: Classes & Instances (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Most backend frameworks use OOP patterns (models, views, serializers).
- **Backend usage**: You encapsulate behavior + data in objects (clean architecture).
- **Production importance**: Understanding `self` and instance data prevents broken state and confusing bugs.

## Core Concepts
- A **class** is a blueprint (structure + methods).
- An **object** (instance) is a real created thing from that blueprint.
- `__init__` runs when the object is created. This is where instance attributes are set.
- `self` inside instance methods refers to the current object.
- **Instance attributes** (like `self.role`) belong to each object separately.
- **Methods** are functions defined inside the class that operate on an object’s data.

## Important Syntax
```python
class Employee:
    def __init__(self, first_name, last_name, role, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.monthly_salary = monthly_salary

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def annual_salary(self):
        return self.monthly_salary * 12

e1 = Employee("A", "B", "Engineer", 5000)
print(e1.full_name())
```

## Memory Tricks
- **class = blueprint**
- **instance = made object**
- **`__init__` = initialization when object is created**
- **`self` = “this object’s data”**

## Interview Questions
**Basic**
1. What is a class?
2. What is an instance/object?
⭐ **Frequently Asked**
3. What does `__init__` do?

**Intermediate**
4. Why do we use `self` in instance methods?
5. Why doesn’t changing one object’s attribute change another object’s attribute?

**Scenario-based**
6. You need behavior that depends on per-user data (role, permissions). Where do you store it: global vars or instance attrs?
7. In Django-like design, why would a method on a model be useful?

## Common Mistakes
- Forgetting `self` in method definitions.
- Accidentally using class variables when you meant instance variables.
- Expecting method to “update other objects” automatically (it won’t).

## Common Confusions ⚠ Common Confusion
- ⚠ `self` in the method body
  - `self.role` means “role attribute on this specific object”.
- ⚠ Methods vs attributes
  - Methods are callable; attributes are data fields.

## Real Backend Usage
- **Django**: model methods operate on instance data.
- **DRF**: serializers/mixins often use class-based patterns.
- **FastAPI**: OOP used for service classes and dependency objects.
- **Production**: encapsulate business logic into classes with instance state.

## Diagram
```
Employee (class blueprint)
      |
      |  create
      v
employee1 (object) has its own self.first_name, self.role, ...
employee2 (object) has its own values
```

## Revision Box
- [ ] class = blueprint
- [ ] object/instance = created from class
- [ ] `__init__` sets initial attributes
- [ ] `self` = current object
- [ ] instance attributes are per-object

## Submission Review (your day-12.py)
- ✅ Good:
  - Correct `Employee` class with `__init__`.
  - Used methods `full_name()` and `annual_salary()`.
  - Demonstrated `give_raise` changing only `employee1`.
- ⚠ Needs improvement:
  - Some print labels don’t exactly match the spec checklist (spec expects exact phrases).
  - `apply` naming: spec uses `apply_raise`; your method naming is fine as your stretch is different, but keep alignment when required.

## 30-Second Interview Revision
- A class is a blueprint; an object is created from it.
- `__init__` initializes each object’s instance attributes.
- `self` refers to the current object.
- Methods use `self` to read/update instance data.
- Two objects created from the same class keep separate state.
