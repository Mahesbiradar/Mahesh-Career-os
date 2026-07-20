# Control Flow (if/elif/else) & Loops (for/while) — Python

## Why It Matters
- ⭐ **Why interviewers ask it**: Branching and looping are where most logic bugs live (off-by-one, wrong conditions, wrong skip behavior).
- **Backend usage**: Looping is used in pagination, processing records, retry logic, iterating over request items, and building data transformations.
- **Production importance**: `break/continue` and short-circuiting help performance and correct behavior.

## Core Concepts
### 1) `if / elif / else`
- Only one branch runs: the **first** matching condition (True) wins.
- If no branch matches and `else` exists, `else` runs.

Example:
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
```

### 2) Short-circuit evaluation (`and` / `or`)
- `and`: if left side is falsy → right side is **not evaluated**
- `or`: if left side is truthy → right side is **not evaluated**

### 3) Falsy values (used heavily)
These evaluate to `False` in conditions:
- `0`, `""`, `[]`, `{}`, `None`, `False`

So:
```python
if []: ...
# does not run
```

### 4) `for` loop + `range()`
- `range(start, stop)` counts up to but **not including** `stop`.
```python
for i in range(1, 11):  # 1..10
    ...
```

### 5) `while` loop
- Repeats until condition becomes false.
```python
while x > 0:
    x -= 1
```

### 6) `break` vs `continue`
- `break`: exits the loop completely
- `continue`: skips to the next iteration immediately

Correct `continue` pattern:
```python
for num in range(1, 26):
    if num % 2 == 0:
        continue
    print(f"Odd: {num}")
```

## Important Syntax
```python
if condition:
    ...

elif condition:
    ...

else:
    ...

for i in range(1, 11):
    break
    continue

while condition:
    ...
```

## Memory Tricks
- **`break` = “stop forever”**
- **`continue` = “skip this time, try next time”**
- **`range(stop)` stops before stop** (exclusive stop)

## Interview Questions
**Basic**
1. What’s the difference between `for` and `while`?
2. What values does `range(1, 5)` generate?
3. What does `break` do?

**Intermediate**
4. Why does `continue` matter for performance and correctness?
5. What does short-circuit mean for `and`?

**Scenario-based**
6. You need to skip even numbers while printing odds. Where should `continue` be placed?
7. When validating input: how do you structure early exit using `break`?

⭐ **Frequently Asked**
8. `if my_list:` vs `if len(my_list) == 0:` — which is preferred and why?

## Common Mistakes
- Off-by-one with `range()` (stop is exclusive)
- Putting `print` inside the wrong `if` and breaking required output
- Using `if not ... != ""` style instead of direct falsy checks
- Writing `continue` but still letting code run above/below incorrectly

## Common Confusions ⚠ Common Confusion
- ⚠ **Skip logic**
  - `if condition: print()` is not the same as `continue`
  - `continue` skips the rest of the loop body for that iteration

## Real Backend Usage
- **Django/DRF/FastAPI**: iterate over queryset/results; filter with conditions; early exit when conditions are met.
- **APIs**: pagination loops, processing batch requests, retry loops.
- **Production**: `continue` patterns reduce nested if-statements and make code more readable.

## Diagram
```
for each item:
   if item should be skipped:
       continue  -> next item
   process item
   if stop condition met:
       break -> exit loop
```

## Revision Box
- [ ] `range` stop is exclusive
- [ ] Falsy values: `0, "", [], {}, None, False`
- [ ] `and/or` short-circuit
- [ ] `break` exits loop, `continue` skips iteration

## Submission Review (your day-05.py / day-06.py / day-04.py)
- ✅ Good:
  - Used `for`/`while`, `break`, and `continue` in the right places across attempts.
  - Correctly practiced falsy checks with empty lists (`if nums:`).
- ⚠ Needs improvement:
  - Output formatting must be exact (`Found: <item>` vs `Found: item`, labels/spaces).
  - `continue` requirement is behavior-specific, not just matching output—structure matters.
- ⭐ Interview Tip: Always structure loop body so the “normal work” runs **after** `continue` checks.

## 30-Second Interview Revision
- `if/elif/else`: first True branch runs.
- Short-circuit: `and`/`or` skip evaluation when result is known.
- Falsy: `0, "", [], {}, None, False`.
- `range(a, b)` generates `a..b-1`.
- `break` exits loop; `continue` skips rest of current iteration.
