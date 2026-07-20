# Day 16 — Encapsulation & Property Decorators — Python Level 4

---
## TODAY'S VIDEO

| Field | Detail |
|---|---|
| Instructor | Corey Schafer |
| Platform | YouTube (free) |
| Video Title | Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters |
| Duration | ~18 min |
| Link | https://youtu.be/jCzT9XFZ5bw |

What to focus on while watching:
- How `@property` turns a method into an attribute-like access (no parentheses needed)
- The difference between direct attribute access and using a getter/setter pattern
- How `@name.setter` and `@name.deleter` work — notice they share the same method name
- Why Python prefers convention (`_name`) over strict enforcement for "private" attributes

---
## CONCEPT SUMMARY (read AFTER video, not before)

Python does not have true private variables. Instead, it uses a single underscore `_name` as a convention meaning "this is internal, don't touch it." The double underscore `__name` triggers name mangling, which makes it harder to access from outside — but it's still not truly private.

The `@property` decorator lets you define a method that behaves like an attribute. You access it without parentheses. The matching `@name.setter` lets you control what happens during assignment (e.g., validation). The `@name.deleter` runs cleanup logic when the attribute is deleted with `del`.

The big idea: you can start with a simple public attribute, and later add `@property` + `@setter` to add logic without breaking existing code that reads or writes that attribute.

---
## TODAY'S ASSIGNMENT

Goal: Build a `BankAccount` class that uses `@property`, `@setter`, and `@deleter` to control access to the account balance with validation and logging.

Requirements (must complete all):
- [ ] Create a `BankAccount` class with a private-by-convention attribute `_balance` initialized in `__init__` (default 0)
- [ ] Define a `@property` named `balance` that returns the current `_balance` value
- [ ] Define a `@balance.setter` that only allows setting `_balance` to a non-negative number; if a negative value is passed, raise a `ValueError` with the exact message: `Balance cannot be negative`
- [ ] Define a `@balance.deleter` that prints the exact line: `Balance deleted for account`
- [ ] After creating an account, set the balance to `500`, then print the exact line: `Current balance: 500`
- [ ] (Stretch) Try to set the balance to `-100`, catch the `ValueError`, and print the exact line: `Error: Balance cannot be negative`

Rules:
- No AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.
- Exact output labels matter — match them character for character.

---
## HOW TO SUBMIT

When done:
1. Save your file as: `submissions/day-16.py`
2. Come back to the AI chat
3. Paste PROMPT 2 and paste your entire file content below it

---
## REVISION CHECK (answer without looking — 2 min)

1. In inheritance, what does `super().__init__(...)` do inside a child class's `__init__` method?
2. Why is exact output label matching important? (Think back to Day 14's `Raise amount:` gap.)
