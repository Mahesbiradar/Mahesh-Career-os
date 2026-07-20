# Strings (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Strings are everywhere in backend work (request/response, parsing, validation, formatting).
- **Backend usage**: You clean inputs (`strip`), split tokens (`split`), transform (`upper/lower`), and search (`find/in`).
- **Production importance**: Strings are immutable → bugs happen when you “modify” thinking it changes original.

## Core Concepts
- A **string** is an ordered sequence of characters.
- Strings are **immutable**: you cannot change a character in place. Methods return a **new string**.
- Indexing:
  - `s[0]` = first character
  - `s[-1]` = last character
- Slicing: `s[start:stop:step]`
  - `start` inclusive, `stop` exclusive
  - omit values: `s[:stop]`, `s[start:]`, `s[::]`
- Common methods:
  - `.strip()` removes leading/trailing whitespace
  - `.upper()` / `.lower()` return transformed copies
  - `.replace(old, new)` returns a new string
  - `.split(sep=None)` returns a list of words/tokens
  - `.join(list)` returns a string by joining items
  - `.find(sub)` returns index or `-1` if not found
  - `.startswith(prefix)` returns `True/False`
- f-strings:
  - `f"Hello {name}"` evaluates `{...}` at runtime and inserts result.

## Important Syntax
```python
s = "  Python is a powerful programming language  "

s2 = s.strip()
word = s2[s2.find("powerful"):s2.find("powerful")+len("powerful")]

print(s2.upper())
print(s2.lower())

replaced = s2.replace("powerful", "beautiful")

words = s2.split()
count = len(words)
```

## Memory Tricks
- **strip = spaces killer**
- **split = list maker**
- **join = list to string**
- **strings don’t change** → methods return new strings

## Interview Questions
**Basic**
1. What does `"  hello  ".strip()` return?
2. Does `strip()` change the original string?
⭐ **Frequently Asked**
3. Difference between slicing and indexing in Python?

**Intermediate**
4. What does `s.find("x")` return when substring isn’t present?
5. Why is immutability helpful for reasoning/debugging?

**Scenario-based**
6. You receive `"  username  "` from an API. Where would `strip()` be used?
7. You split a CSV line with `.split(",")`. How do you get the number of fields?

## Common Mistakes
- Thinking `upper()` / `replace()` modifies original string.
- Wrong slice boundaries (stop is exclusive).
- Using wrong f-string labels/format spec.

## Common Confusions ⚠ Common Confusion
- ⚠ **Immutability confusion**
  - `s.upper()` → new string, original `s` unchanged.
- ⚠ **`strip` vs `lstrip/rstrip`**
  - `strip` removes both ends.
- ⚠ **`find` returns index**
  - `find()` doesn’t return substring; it returns where it starts.

## Real Backend Usage
- **Django/DRF/FastAPI**: normalize user input (strip whitespace), validate string formats.
- **APIs**: split and parse paths/query-like strings, clean tokens before DB operations.
- **Production**: search strings safely; when not found, handle `-1` or prefer `"x" in s`.

## Diagram
```
Original string:  "  hello  "
        |
        v
s2 = s.strip() -> "hello"   (new string; original unchanged)
```

## Revision Box (1 screen)
- [ ] Strings are immutable
- [ ] Slicing: start inclusive, stop exclusive
- [ ] `.strip()`, `.find()`, `.upper()`, `.lower()`, `.replace()`, `.split()`
- [ ] f-strings evaluate `{}` expressions

## Submission Review (your day-03.py)
- ✅ Good:
  - Correct use of `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.split()`, `len(...)`.
- ⚠ Needs improvement:
  - Stretch/requirements require careful label discipline and exact slicing by correct position.
  - Your slicing uses fixed indices (`[12:20]`). It can be fragile; prefer computing index via `find()` then slicing from there.
  - In revision check, ensure you clearly explained short-circuit and division operators with correct terms.

⭐ **Interview Tip**
- When asked “strings are immutable”, always say: **methods return a new string**.

## 30-Second Interview Revision
- Strings are immutable.
- `strip()` removes leading/trailing whitespace.
- Slicing uses `start:stop` where stop is exclusive.
- `.replace()` and `.upper()` return new strings.
- `.split()` returns a list; `.join()` reverses it.
- f-strings insert evaluated expressions inside `{}`.
