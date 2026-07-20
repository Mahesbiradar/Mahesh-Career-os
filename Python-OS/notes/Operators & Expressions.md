# Operators & Expressions (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Operator behavior is a common source of logic bugs (especially `/` vs `//`, `==` vs `is`, `and/or` returning values).
- **Backend usage**: Filtering, permissions, validation rules, and computing derived fields all rely on operator semantics.
- **Production importance**: Wrong operator choice can cause incorrect grades, wrong money calculations, or broken conditions.

## Core Concepts
### 1) Arithmetic operators
- `/` **true division** always returns a `float`
- `//` **floor division** rounds **down** to the nearest integer
- `%` modulo is the remainder
- `**` exponent

Example:
```python
print(7 / 2)   # 3.5
print(7 // 2)  # 3
```

### 2) Comparison operators
- `==` compares values
- `!=` not equal
- `>`, `<`, `>=`, `<=` for ordering

### 3) Logical operators + short-circuit
- `and`: stops as soon as it knows the result is `False`
- `or`: stops as soon as it knows the result is `True`
- Important: `and/or` return the **actual operands**, not only `True/False`

Example:
```python
result = 0 and print("runs")  # print won't execute
```

### 4) `==` vs `is` (identity vs equality)
- `==` checks value equality
- `is` checks whether two references point to the **same object** in memory

Example:
```python
a = [1,2,3]
b = [1,2,3]
print(a == b)  # True (same values)
print(a is b)  # False (different objects)
```

### 5) Falsy / Truthiness (used in real code)
In `if ...:` checks, these evaluate to `False`:
- `0`, `""`, `[]`, `{}`, `None`, `False`

So:
```python
if []: 
    ...
else:
    ...
```

## Important Syntax
```python
x = 7 / 2      # float
x = 7 // 2     # int (floor)
x = 7 % 2      # remainder
x = 2 ** 3     # exponent

a == b
a is b

# short-circuit
a and b
a or b
not a

# truthiness
if some_list:
    ...
```

## Memory Tricks
- `/` gives “**real** number division”
- `//` gives “**integer** division”
- `==` sounds like “**equals**”
- `is` sounds like “**identity**”
- Falsy list: **0 empty None False**

## Interview Questions
**Basic**
1. What’s the difference between `/` and `//`?
2. What does `%` return?
3. What’s the difference between `==` and `is`?
⭐ **Frequently Asked**
4. What does `input()` return and why does it matter for operators?

**Intermediate**
5. Why can `x = 0 and expensive()` be used to skip function calls?
6. In expressions like `A and B`, what value is returned when `A` is falsy?

**Scenario-based**
7. You parse `"age": "28"` from an API and want to check `age >= 18`. What conversions and operators do you need?
8. You must detect invalid input. How would you use truthiness + comparisons safely?

## Common Mistakes
- Using `is` where you meant `==`
- Printing “expected math” but labels are mismatched
- Assuming `and/or` return only boolean values
- Doing arithmetic with string inputs

## Common Confusions ⚠ Common Confusion
- ⚠ **`and/or` vs boolean logic**
  - `and/or` returns operands, not necessarily `True/False`
- ⚠ **`is` vs `==`**
  - `is` checks identity (same object), which can surprise you with caching for small integers

## Real Backend Usage
- **Django/DRF**: conditions like `if user.is_admin` and validation checks
- **FastAPI**: comparisons for bounds checks and rejection rules
- **REST APIs**: query filters using comparisons (`>=`, `<`, `!=`)
- **Production**: use clear operator semantics to avoid subtle bugs

## Diagram
```
Short-circuit:
(A) and (B)
  |
  | if A is falsy -> B is skipped
  v
result is A

(A) or (B)
  |
  | if A is truthy -> B is skipped
  v
result is A
```

## Revision Box
- [ ] `/` vs `//`
- [ ] `%` is remainder
- [ ] `and/or` short-circuit and return operands
- [ ] `==` value equality, `is` identity
- [ ] Falsy values: `0, "", [], {}, None, False`

## Submission Review (your day-02.py)
- ✅ You demonstrated:
  - all 7 arithmetic operators
  - `/` vs `//`
  - a short-circuit example (indirectly via `if/else`)
  - `==` vs `is` using lists
  - falsy outputs using `bool(...)`
- ⚠ Needs improvement:
  - In multiple places your f-string labels had mismatches (e.g., labels like `x - y` for addition output).
  - Short-circuit “proof” spec is better with a direct expression (not just if/else).
  - For the `bool(...)` stretch, you should print exactly `bool(0)`, `bool("")`, `bool([])`, `bool(None)` results (you did it, but also included extra values like dict).

## 30-Second Interview Revision
- `/` true division → `float`
- `//` floor division → rounds down to `int`
- `%` remainder, `**` exponent
- `==` compares values, `is` compares identity
- `and/or` short-circuit (and returns operands)
- Falsy: `0, "", [], {}, None, False`
