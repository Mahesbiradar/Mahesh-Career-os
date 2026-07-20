# Tuples & Sets (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Tuples and sets have “special rules” (immutability, uniqueness, no indexing) that often break code.
- **Backend usage**: tuples for fixed data, sets for deduplication and fast membership checks.
- **Production importance**: using lists when you want immutability, or sets when you need duplicates, causes subtle logic bugs.

## Core Concepts
### Tuples
- Written with parentheses: `(1, 2, 3)`
- **Immutable**: you can’t append/remove/update items.
- Great for fixed groups of values (coordinates, return multiple values).
- Unpacking:
  
```python
  x, y, z = coordinates
  ```

### Sets
- Written with `{}` but with unique values: `{"a", "b"}`
- **Unique**: duplicates are automatically removed.
- **Unordered**: indexing doesn’t exist (`my_set[0]` fails).
- Set operations:
  - intersection: `a & b`
  - union: `a | b`
  - difference: `a - b`

### Two common rules
- Empty set must be `set()` (not `{}`)
- One-item tuple must be `(5,)` (comma is required)

## Important Syntax
```python
coordinates = (10, 15, 20)

print(coordinates)         # tuple
x, y, z = coordinates     # unpack

python_skills = {"List", "Dict", "Set", "Tuple"}
java_skills = {"Array", "Dict", "Set", "String"}

common = python_skills & java_skills
all_ = python_skills | java_skills
only_python = python_skills - java_skills
```

## Memory Tricks
- **Tuple = “fixed bundle”** (immutable)
- **Set = “unique bag”** (no duplicates, no order)

## Interview Questions
**Basic**
1. Are tuples mutable or immutable?
2. Can you index a set like `my_set[0]`?
⭐ **Frequently Asked**
3. What is the difference between `{}` and `set()`?

**Intermediate**
4. What does `python_skills & java_skills` return?
5. Why is tuple unpacking useful?

**Scenario-based**
6. You need to deduplicate tags from user input. Which type helps?
7. You need to return `(status, message)` from a function. Should it be list or tuple and why?

## Common Mistakes
- Using `{}` thinking it creates an empty set (it creates a dict).
- Trying to modify a tuple.
- Expecting sets to preserve order.

## Common Confusions ⚠ Common Confusion
- ⚠ **One-item tuple**
  - `(5)` is an `int`
  - `(5,)` is a tuple
- ⚠ **set uniqueness**
  - duplicates vanish automatically

## Real Backend Usage
- **Django / DRF**: sets for deduping IDs/tags; tuples for fixed multi-value returns.
- **FastAPI**: validate inputs, then convert to set when deduplication is needed.
- **Production**: membership checks (`x in some_set`) are fast conceptually.

## Diagram
```
Tuple (fixed)      Set (unique)
(1,2,3)           {1,2,3}  (duplicates removed)
Immutable         Unordered, no indexing
```

## Revision Box
- [ ] Tuples are immutable
- [ ] Tuples unpack into variables
- [ ] Sets store unique values
- [ ] No set indexing
- [ ] Set ops: `&`, `|`, `-`

## Submission Review (your day-09.py)
- ✅ Good:
  - Correct tuple creation and unpacking.
  - Correct set operations for `&` and `|`.
- ⚠ Needs improvement:
  - Label discipline: you printed required labels correctly, but keep output strictly spec-matching (exact text).
  - Stretch wasn’t required, but you implemented the difference correctly—good.

## 30-Second Interview Revision
- Tuple = immutable fixed sequence.
- Unpacking: `x, y = t`.
- Set = unique collection, no duplicates, no indexing.
- Set ops: `&` common, `|` all unique, `-` difference.
