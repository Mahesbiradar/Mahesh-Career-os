# Dictionaries (Python)

## Why It Matters
- ⭐ **Why interviewers ask it**: Dicts are the core structure for key-value access.
- **Backend usage**: user profiles, JSON parsing, configuration maps, headers, query parameters.
- **Production importance**: dict mistakes cause KeyErrors and wrong data returned to clients.

## Core Concepts
- A dictionary stores `key: value` pairs.
- Keys must be unique.
- If you assign the same key again, the value is replaced.
- Two main ways to read:
  - `d["key"]` → crashes with `KeyError` if missing
  - `d.get("key", default)` → safe for missing keys
- Loop:
  - `for k, v in d.items():` gives key and value.

## Important Syntax
```python
student = {"name": "Mahesh", "age": 28, "course": "Python", "city": "Bangalore"}

print(student["name"])                       # direct access (KeyError if missing)

print(student.get("phone", "Not provided"))  # safe default

student["city"] = "Mysore"                  # update
student["email"] = "abc@gmail.com"          # add

del student["age"]                          # delete key

for key, value in student.items():
    print(key, value)
```

## Memory Tricks
- **dict = dictionary = label → value**
- `[]` read requires key to exist
- `.get()` is “**get or default**”

## Interview Questions
**Basic**
1. What is a dictionary in Python?
2. Difference between `d["x"]` and `d.get("x")`?

⭐ **Frequently Asked**
3. What happens when you do `del d["missing_key"]`?

**Intermediate**
4. How do you iterate key + value using one loop?

**Scenario-based**
5. You parse an API payload and some fields are optional. How do you read them safely?
6. You need to delete a field before saving to DB.

## Common Mistakes
- Using `d["missing"]` and crashing with `KeyError`.
- Forgetting `del d["key"]` deletes the key (not just a value in variable).
- Misunderstanding `.items()` (it returns pairs).

## Common Confusions ⚠ Common Confusion
- ⚠ `{}` is an empty dictionary, not an empty set.
- ⚠ `dict.keys()` vs `dict.items()`
  - `keys()` gives only labels
  - `items()` gives label + value

## Real Backend Usage
- **Django/DRF**:
  - serializer output is dict-like JSON.
  - request payload often becomes Python dicts.
- **FastAPI**:
  - request bodies convert to dict models (or Pydantic objects).
- **APIs**:
  - headers and query params are naturally key-value mappings.

## Diagram
```
Dictionary:
{
  "name": "Mahesh",
  "age": 28
}

Access:
student["name"]  -> "Mahesh"
student.get("phone","Not provided") -> default
```

## Revision Box
- [ ] dict = key → value
- [ ] `d["key"]` raises KeyError if missing
- [ ] `d.get("key", default)` is safe
- [ ] `.items()` loops key and value

## Submission Review (your day-10.py)
- ✅ Good:
  - Correct keys: `name, age, course, city`
  - Used `.get()` for missing `phone`
  - Removed `age` and looped through `student.items()`
- ⚠ Needs improvement:
  - You printed `Final profile:` inside the loop, but you also printed the full dict after loop. Specs may want only one style of output.
  - Keep f-string formatting consistent (`key:value` vs `key, value`).

## 30-Second Interview Revision
- Dict stores key-value pairs.
- Keys are unique; reassign replaces value.
- `d["x"]` requires key exists; `.get()` provides default.
- Use `for k,v in d.items()` to iterate through records.
