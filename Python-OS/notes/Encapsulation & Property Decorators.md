# Encapsulation & Property Decorators (Python)

## Why It Matters
- Interviewers ask about encapsulation because it shows whether you can protect object data and design clean class APIs.
- In backend code, properties are useful when model or service attributes need validation, formatting, or cleanup without changing how other code reads the value.
- Django and API code often need controlled assignment, such as preventing negative prices, invalid statuses, or unsafe user data.

## Core Concepts
- Encapsulation means keeping internal object data controlled instead of letting every part of the program change it freely.
- Python uses `_name` as a convention for "internal use" attributes. It is not truly private, but it tells other developers not to access it directly.
- `@property` lets a method behave like an attribute, so callers can use `obj.balance` instead of `obj.balance()`.
- A setter validates or transforms a value before saving it.
- A deleter runs logic when an attribute is deleted with `del`.

```python
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
```

## Important Syntax
```python
@property
def value(self): ...

@value.setter
def value(self, new_value): ...

@value.deleter
def value(self): ...
```

## Memory Tricks
- `_balance` is the storage box.
- `balance` is the public counter window.
- The setter is the security guard that checks values before they enter.

## Interview Questions
- ⭐ What is encapsulation in Python?
- ⭐ What does `@property` do?
- What is the difference between `_name` and `__name`?
- Why does Python use conventions instead of strict private variables?
- When would you use a setter instead of directly assigning an attribute?
- Scenario: A product price should never be negative. How would you enforce that in a class?

## Common Mistakes
- Writing `account.balance()` after using `@property`; property access should be `account.balance`.
- Setting `_balance` directly from outside the class and bypassing validation.
- Forgetting that the setter method name must match the property name.
- Raising an error with the wrong message when exact validation output matters.
- Initializing a value directly when the assignment specifically needs to demonstrate setter behavior.

## Common Confusions ⚠
- `_balance` vs `balance`: `_balance` stores the real value; `balance` is the controlled public interface.
- `@property` vs normal method: a property is read like an attribute, while a normal method uses parentheses.
- Setter vs constructor: `__init__` creates the object; a setter controls later assignment.
- Encapsulation vs true privacy: Python encourages controlled access by convention, but it does not fully hide attributes.
- `raise` vs `print`: `raise ValueError(...)` creates an error; `print(...)` only displays text.

## Real Backend Usage
- A Django model can use property methods to expose calculated values such as `full_name`, `total_price`, or `is_expired`.
- A service class can use setters to reject invalid business data before it reaches the database.
- API validation often follows the same idea: check input early, raise a clear error, and prevent invalid state.
- Properties help keep old calling code stable because `user.full_name` can stay the same even if the calculation changes internally.

## 30-Second Interview Revision
- Encapsulation controls how object data is accessed and changed.
- `_attribute` means internal by convention, not truly private.
- `@property` makes a method readable like an attribute.
- `@name.setter` validates or transforms assignment to `obj.name`.
- In backend work, properties and setters help protect models, service objects, and API data from invalid state.
