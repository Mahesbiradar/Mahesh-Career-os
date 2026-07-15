# Functions (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Functions test your understanding of input/output, `return` vs `print`, and default parameters.
- **Backend usage**: Business logic is typically packaged into functions (parsing, validation, computing, mapping DTOs).
- **Production importance**: Correct return values make code composable and testable.

## Core Concepts
### 1) `print()` vs `return`
- `print()` displays output, but returns `None`.
- `return` gives a value back to the caller.

### 2) Function calling
- Call using `name(args...)`.
- Returned value can be stored or used in expressions.

### 3) Default parameters
Example:
```python
def power(base, exponent=2):
    return base ** exponent
```
- `power(3)` uses `exponent=2`
- `power(3, 4)` overrides the default

### 4) Functions calling other functions
A function can call another function inside its body:
```python
def greet(name): ...
def introduce(name, age):
    greeting = greet(name)
    return f"{greeting} Age: {age}"
```

## Important Syntax
```python
def greet(name):
    return f"Hello, {name}!"

def power(base, exponent=2):
    return base ** exponent

result = greet("Mahesh")
```

## Memory Tricks
- **return = “give back”**
- **print = “show on screen”**
- **default param = fallback when argument is missing**

## Interview Questions
**Basic**
1. What happens if a function has no `return`?
2. Difference between `print(x)` and `y = print(x)`?

**Intermediate**
3. How do default parameters work in Python?
⭐ **Frequently Asked**
4. Why does `result = my_function()` become `None` when function only prints?

**Scenario-based**
5. You want to validate input and then compute a value. Where do you put logic?
6. You need to build a `introduce()` message using `greet()`. How do you avoid duplication?

## Common Mistakes
- Using `print()` inside a function when the caller expects a returned value.
- Forgetting to use default parameters correctly.
- Duplicating code instead of composing functions.

## Common Confusions ⚠ Common Confusion
- ⚠ **Returning vs printing**
  - A function that only prints returns `None`.
- ⚠ **Default vs overridden arguments**
  - Missing argument uses default; provided argument overrides.

## Real Backend Usage
- **Django/DRF/FastAPI**: service/helper functions for validation and transformation.
- **APIs**: parse request data → convert types → return computed response structures.
- **Production**: pure functions (`return` values) are easier to unit test.

## Diagram
```
Caller -> calls function -> function computes -> returns value
           (optional) -> function may call another helper function
```

## Revision Box
- [ ] `return` sends value back; `print` does not
- [ ] Default parameter used only if omitted
- [ ] Functions can call other functions
- [ ] Returned value can be printed or used elsewhere

## Submission Review (your day-07.py)
- ✅ Good:
  - Correct `greet`, `add`, `power`, `square`, `total` structure conceptually.
  - You used `return` for most functions.
- ⚠ Needs improvement:
  - Stretch/main outputs were repeated with extra prints in places (spec requires exact labels).
  - `power` function output format can be stricter: `Result: 9` required exact matching.

⭐ **Interview Tip**
- When interview asks “write a function”, always specify: input parameters → return value → no side effects unless required.

## 30-Second Interview Revision
- Functions are reusable logic blocks.
- `return` is for values; `print` is for displaying.
- Default parameters provide fallback values.
- A function can call other functions (composition).
