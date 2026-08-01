# Day 17 — Polymorphism & Abstract Base Classes — Python Level 4

---
## TODAY'S VIDEO

| Field | Detail |
|---|---|
| Instructor | Pybites |
| Platform | YouTube (free) |
| Video Title | Python abstract base class (ABC) example |
| Duration | ~12 min |
| Link | https://youtu.be/hEW-IWGluG4 |

What to focus on while watching:
- How `ABC` and `@abstractmethod` force child classes to implement specific methods
- The difference between duck typing ("if it walks like a duck...") and using `isinstance()` with ABCs
- Why ABCs are useful for defining shared interfaces across unrelated classes
- What happens if you try to instantiate a class that has an unimplemented abstract method

---
## CONCEPT SUMMARY (read AFTER video, not before)

Polymorphism means the same method call behaves differently depending on which object receives it. In Python, this happens naturally through duck typing — you don't need inheritance for two objects to be "polymorphic." If both have a `.speak()` method, you can call `.speak()` on either without checking their type.

Abstract Base Classes (ABCs) add structure to this flexibility. They define a contract: any class that inherits from an ABC must implement all abstract methods, or it cannot be instantiated. This is how Python creates "interfaces" without true interface syntax. Use `abc.ABC` as the base and `@abc.abstractmethod` on methods that subclasses must override.

The key interview trap: Python prefers duck typing over `isinstance()` checks. ABCs are a middle ground — they let you enforce structure while still supporting polymorphism.

---
## TODAY'S ASSIGNMENT

Goal: Create a `Shape` ABC with an abstract `area()` method, then build `Rectangle` and `Circle` subclasses that implement it, demonstrating polymorphism through a shared function.

Requirements (must complete all):
- [ ] Import `ABC` and `abstractmethod` from the `abc` module
- [ ] Create an abstract class `Shape` that inherits from `ABC`, with an abstract method `area(self)`
- [ ] Create a `Rectangle` class that inherits from `Shape`, with `__init__(self, width, height)` and an `area()` method that returns `width * height`
- [ ] Create a `Circle` class that inherits from `Shape`, with `__init__(self, radius)` and an `area()` method that returns `3.14 * radius * radius`
- [ ] Create a standalone function `print_area(shape)` that accepts any `Shape` object and prints the exact line: `Area: {value}` (replace `{value}` with the actual area)
- [ ] Create one `Rectangle(4, 5)` and one `Circle(3)`, pass both to `print_area()`, and verify the output lines are exactly: `Area: 20` and `Area: 28.26`

Stretch (optional — only after main requirements done):
- [ ] Try to instantiate `Shape()` directly, catch the `TypeError`, and print the exact line: `Cannot instantiate abstract class`

Rules:
- No AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.
- Exact output labels matter — match them character for character.

---
## HOW TO SUBMIT

When done:
1. Save your file as: `submissions/day-17.py`
2. Come back to the AI chat
3. Paste PROMPT 2 and paste your entire file content below it

---
## REVISION CHECK (answer without looking — 2 min)

1. What is the difference between a regular method and a `@property` decorated method when accessing it on an instance?
2. In Day 16's assignment, what exact error message should the `@balance.setter` raise when a negative value is passed?
