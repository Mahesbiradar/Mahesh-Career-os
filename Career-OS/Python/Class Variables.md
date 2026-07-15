# Class Variables vs Instance Variables (Python OOP)

## Why It Matters
- ⭐ **Why interviewers ask it**: Many bugs happen when developers accidentally store shared data on instances.
- **Backend usage**: global/shared config, counters, defaults used by all objects (e.g., limits, feature flags).
- **Production importance**: shared counters and defaults should update consistently for the whole class.

## Core Concepts
- **Class variable**: stored on the class, shared by all objects.
- **Instance variable**: stored on each object (`self.<name>`), separate per object.
- Python attribute lookup: when you use `self.raise_amount`, it checks:
  1) instance attribute first  
  2) then class attribute as fallback

So if you don’t override on an instance, it uses the class value.  
If you override on one instance, that one object uses the new value only.

## Important Syntax
```python
class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first_name, last_name, role, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.monthly_salary = monthly_salary
        Employee.num_of_employees += 1

    def apply_raise(self):
        self.monthly_salary *= self.raise_amount

e1 = Employee("A", "B", "Dev", 1000)
e2 = Employee("C", "D", "Dev", 2000)

Employee.raise_amount = 1.06  # affects objects that haven't overridden
e1.raise_amount = 1.10         # overrides only e1
```

## Memory Tricks
- **class variable = shared** (group-level)
- **instance variable = per object**
- **override = one object changes its own value**

## Interview Questions
**Basic**
1. What is a class variable?
2. What is an instance variable?
⭐ **Frequently Asked**
3. What does “override” mean with attributes?

**Intermediate**
4. If you change `Employee.raise_amount`, what happens to existing objects?
5. If you change `employee1.raise_amount`, does `employee2` change?

**Scenario-based**
6. You track `num_of_employees` for the whole app. Where should it live: instance or class?
7. You need default “raise percent” for all employees but one employee has a different raise. How do you model it?

## Common Mistakes
- Updating shared counters using `self.num_of_employees` (creates a per-instance counter).
- Expecting overriding to affect other objects automatically.
- Confusing class attribute with instance attribute behavior.

## Common Confusions ⚠ Common Confusion
- ⚠ “Changing one object’s field changes all”
  - It changes only if you changed the **class variable**, not the instance override.

## Real Backend Usage
- **Django**: class-level fields and defaults; model metadata is class configuration.
- **DRF**: serializer class attributes define behavior shared for that serializer.
- **FastAPI**: route handler classes/config often uses class-level defaults.
- **Production**: shared settings, feature flags, counters, constants.

## Diagram
```
Employee.raise_amount (class variable)
        |
        | fallback lookup
        v
employee1.raise_amount (override?) -> uses override if present
employee2.raise_amount (no override) -> uses class value
```

## Revision Box
- [ ] class variable shared across objects
- [ ] instance variable is per object (`self.x`)
- [ ] Python lookup: instance first, class second
- [ ] overriding on one object affects only that object

## Submission Review (your day-13.py)
- ✅ Good:
  - You correctly created `raise_amount` and `num_of_employees` as class variables.
  - You updated `Employee.num_of_employees` in `__init__`.
  - You demonstrated overriding `employee1.raise_amount = 1.10`.
- ⚠ Needs improvement:
  - `apply_raise()` in your submission converts salary using `int(self.monthly_salary * self.raise_amount)`. That truncates decimals and may fail precision expectations. Prefer multiplication without forcing `int` unless spec requires it.
  - Output labels for the earlier employee prints: your spec required exact labels like `Employee 1:` and `Employee 2:`, but your current prints included different label formatting.

## 30-Second Interview Revision
- Class variable = shared default on the class.
- Instance variable = data stored on each object.
- `self.attr` checks instance first, then class.
- Overriding `employee1.raise_amount` affects only `employee1`.
- Counters like `num_of_employees` usually belong on the class.
