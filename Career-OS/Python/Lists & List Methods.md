# Lists & List Methods (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Lists are the most common mutable structure; methods often have subtle behavior (`remove` vs `pop`).
- **Backend usage**: store ordered items like records, query results, parsed tokens, batches of events.
- **Production importance**: mutability means in-place changes can affect other references—need to understand it.

## Core Concepts
### List basics
- Written as: `["a", "b", "c"]`
- **Mutable**: list methods change the list in place.

### Common methods
- `append(x)`: adds to the end
- `insert(i, x)`: inserts at index `i`, shifting later elements
- `remove(x)`: deletes the **first occurrence** of value `x`
- `pop(i)`: deletes by **index** and returns removed item (if `i` omitted, pops last)

### Indexing & slicing
- `movies[0]` first item, `movies[-1]` last
- `movies[start:stop]` returns a new list
  - `start` inclusive, `stop` exclusive

### enumerate()
- `enumerate(list, start=1)` gives `(index, value)` while iterating.

## Important Syntax
```python
movies = ["Inception", "Interstellar"]

movies.append("Dunkirk")
movies.insert(0, "Memento")

movies.remove("Inception")  # removes first matching value

for i, m in enumerate(movies, start=1):
    print(f"{i}. {m}")

top3 = movies[0:3]
```

## Memory Tricks
- `append` = **end**
- `insert` = **index**
- `remove` = **value** (first match)
- `pop` = **index** (and returns)

## Interview Questions
**Basic**
1. Is a list mutable or immutable?
2. Difference between `append` and `insert`?
3. Difference between `remove` and `pop`?

⭐ **Frequently Asked**
4. What does slicing `a[1:4]` return?

**Intermediate**
5. When would you use `enumerate()` instead of manual counters?

**Scenario-based**
6. You loop through API results and need “1., 2., 3.” numbering. How?
7. You want the first 3 items from a list without changing the original. How?

## Common Mistakes
- Thinking `remove()` removes by index (it removes by value).
- Confusing `insert(i, x)` index ordering.
- Expecting slicing to modify the original list (it does not).

## Common Confusions ⚠ Common Confusion
- ⚠ **`remove` vs `pop`**
  - `remove(x)` uses value
  - `pop(i)` uses index
- ⚠ **Mutability**
  - list operations change the same list object.

## Real Backend Usage
- **Django/DRF**: lists hold serialized items; you often loop using `enumerate`.
- **FastAPI**: convert input strings into token lists (`split`) and process.
- **Production**: slicing creates a new list for safe “view” of first N items.

## Diagram
```
List (mutable)
[0] [1] [2] [3]
  | append -> adds at end
  | insert(i) -> shifts right
  | remove(x) -> deletes first match
```

## Revision Box
- [ ] Lists are mutable
- [ ] `append` end, `insert` at index
- [ ] `remove` by value, `pop` by index
- [ ] `start:stop` stop is exclusive
- [ ] `enumerate(..., start=1)` for numbering

## Submission Review (your day-08.py)
- ✅ Good:
  - Correctly used `append`, `insert(0, ...)`, `remove`, and `enumerate`.
  - You printed the final list with numbering starting at 1.
- ⚠ Needs improvement:
  - Requirement labels: some outputs used the wrong label formatting:
    - Day spec wants exact labels like `After insert:` and `After remove:` (you missed the trailing `:` in one label).
  - `print` f-string formatting must match exact spec (avoid extra commas/spacing differences).
  - You mixed in non-needed “communication practice” into the same file; keep assignment code clean.

⭐ **Interview Tip**
- When a spec demands “exact output”, treat it like an API contract: spacing and punctuation are part of the behavior.

## 30-Second Interview Revision
- Lists are mutable.
- `append` adds to end; `insert(i, x)` inserts at index.
- `remove(x)` deletes by value; `pop(i)` deletes by index.
- Slicing returns a new list.
- `enumerate()` gives index + value (great for numbering).
