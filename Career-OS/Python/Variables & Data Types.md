# Variables & Data Types (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Most beginner backend bugs come from wrong types and wrong assumptions about input formats.
- **Backend usage**: API inputs (query params, JSON fields) often arrive as strings → you must convert to `int/float` before computations.
- **Production importance**: Clean type conversion + validation avoids runtime crashes and enables proper error responses (400).

## Core Concepts
- A **variable** is a name that points to a value in memory.
- Python is **dynamically typed**: you don’t declare types; Python infers them at runtime.
- Common primitive types in backend code:
  - `int`: whole numbers (counts, IDs)
  - `float`: decimal numbers (money, percentages)
  - `str`: text (always in quotes)
  - `bool`: `True/False` (flags and conditions)
- `type(x)` prints the runtime type.
- **Type conversion** is explicit:
  - `int("28")` → `28`
  - `float("6.5")` → `6.5`
- **`input()` always returns a string**.
  - Even if the user types `28`, you still get `"28"` (type `str`).

### Small example
```python
age_str = input("Age: ")   # always str, e.g. "28"
age = int(age_str)         # convert to int
print(age + 1)            # safe arithmetic
```

## Important Syntax
```python
type(x)

age = int(input("Age: "))
salary = float(input("Salary: "))

# Convert string to int/float explicitly
age = int("28")
```

## Memory Tricks
- **Input → string**: `input()` is a “string machine”.
- `int` sounds like “integer”, `str` sounds like “string”, `bool` is binary.

## Interview Questions
**Basic**
1. What does `type("hello")` return?
2. What does `input()` return, regardless of what the user types?
3. Why can `"28" + 1` fail?

**Intermediate**
4. In a backend endpoint, why might `"age"` from request data be a string?
5. When would you use `float()` vs `int()`?

**Scenario-based**
6. API receives `"price": "19.99"` as a string. How do you compute totals safely?
7. A user enters `"twenty"` when you expect a number. How do you prevent crashing?

⭐ **Frequently Asked**
8. What does `int("twenty")` do? What error do you get?

## Common Mistakes
- Forgetting to convert `input()` result before arithmetic.
- Assuming Python will auto-convert `"28"` to `28` automatically.
- Confusing formatting with types (e.g., printing is not conversion).

## Common Confusions ⚠ Common Confusion
- ⚠ **`input()` vs actual numeric types**
  - `input()` → `str`
  - arithmetic needs numeric types (`int/float`)
- ⚠ **Conversion is explicit**
  - Python does not silently convert `"28"` into `28`.

## Real Backend Usage
- **Django / DRF**: request fields arrive as strings; serializers/validators convert and validate.
- **FastAPI**: Pydantic validates/coerces types (but invalid values still raise errors).
- **REST APIs**: query params are strings by default → convert before filtering or calculations.
- **Production**: type conversion errors should become clear client-facing messages (HTTP 400).

## Diagram
```
User types: "28"
        |
        v
input()  -> "28"  (type: str)
        |
        v
int("28") -> 28  (type: int)
```

## Revision Box
- [ ] `input()` always returns `str`
- [ ] `type(x)` shows runtime type
- [ ] `int()` / `float()` convert explicitly
- [ ] Invalid conversion throws runtime errors (handle/validate)

## Submission Review
- ✅ You correctly handled the **“twenty” → ValueError** stretch by showing the error output.
- ⚠ Main missing part: you didn’t implement the required **interactive input + age+1 print** (Task 3).
- ⭐ Interview tip: always practice the exact `input()` conversion pattern with real arithmetic.

## 30-Second Interview Revision
- Python is dynamically typed.
- `input()` always returns a string.
- Convert with `int()` / `float()` before arithmetic.
- `type(x)` tells runtime type.
- Invalid conversions (e.g., `int("twenty")`) raise exceptions.
