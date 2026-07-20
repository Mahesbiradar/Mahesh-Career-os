# Exception Handling (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Robust systems must fail gracefully when input is invalid or external resources fail.
- **Backend usage**: converting/validating request data (e.g., `"age": "twenty"`) and handling parsing errors.
- **Production importance**: catching the right exception avoids hiding real bugs.

## Core Concepts
- An **exception** happens at runtime when something goes wrong (e.g., `int("abc")`).
- Structure:
  - `try`: code that may fail
  - `except`: handle a specific failure
  - `else`: runs only if no exception happened
  - `finally`: runs always (success or failure)

### Why keep `try` small
Only the risky line should be inside `try`, so you don’t accidentally hide bugs in unrelated code.

## Important Syntax
```python
try:
    num = int(value)
except ValueError:
    skipped_values.append(value)
    print(f"Skipped invalid score: {value}")
else:
    valid_scores.append(num)
    print(f"Accepted score: {num}")
finally:
    print(f"Finished checking: {value}")
```

### `raise` (manual errors)
```python
if num > 100 or num < 0:
    raise ValueError
```

## Memory Tricks
- `except ValueError` = “catch **conversion** problems”
- `else` = “success path”
- `finally` = “always runs”

## Interview Questions
**Basic**
1. What is an exception in Python?
2. What does `finally` run for?
3. When does `else` run?

⭐ **Frequently Asked**
4. Why catch `ValueError` instead of `except:`?

**Intermediate**
5. What happens if the error is not a `ValueError`?
6. Why should `try` block be small?

**Scenario-based**
7. You parse `"85"`, `"90"`, and `"absent"` from an API. How do you avoid crashing?
8. You validate numeric bounds and want to return `400 Bad Request`. Where do you use `raise`?

## Common Mistakes
- Using bare `except:` and hiding real bugs.
- Putting too much code inside `try`, which makes debugging harder.
- Forgetting `finally` runs even on failures.

## Common Confusions ⚠ Common Confusion
- ⚠ `else` is not “finally”
  - `else` runs only when there is **no exception**
  - `finally` runs **always**
- ⚠ `except` catches specific errors
  - A `ValueError` won’t catch everything.

## Real Backend Usage
- **Django/DRF**: serializers raise validation errors (your Python `ValueError` logic maps to validation).
- **FastAPI**: validation often handled by Pydantic, but you still use try/except for custom conversions.
- **APIs**: invalid request payload should not crash the server; it should become a controlled error response.

## Diagram
```
try  ---> [success] ----> else
  \-> [failure ValueError] -> except
finally runs in both paths
```

## Revision Box
- [ ] `try/except/else/finally` roles
- [ ] `except ValueError` for conversion issues
- [ ] `else` = success only
- [ ] `finally` = always
- [ ] Use `raise` for manual validation failures

## Submission Review (your day-11.py)
- ✅ Good:
  - Correct use of `try` + `except ValueError`
  - Collected `valid_scores` and `skipped_values`
  - Used `finally` to print “Finished checking...”
- ⚠ Needs improvement:
  - Stretch section: you added `"105"` but the spec expects skipping it the same way as text errors (print `Skipped invalid score: <value>` style). Your stretch currently prints the exception object, not the required message.
  - Average score calculation must guard against empty `valid_scores` in real cases (interviews may ask this).

## 30-Second Interview Revision
- Exceptions happen during runtime failures.
- Use `try` for risky code and `except` for expected failures.
- Prefer specific exceptions (`ValueError`).
- `else` runs only when no exception occurred.
- `finally` runs always (cleanup/final logs).
