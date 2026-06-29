# DAY 2 — Operators & Expressions
**Domain:** Python — Level 1  
**Phase:** 1 (Ignition)  
**Date:** 2026-06-27

---

## LESSON VIDEO

| | |
|---|---|
| **Course** | Corey Schafer Python Beginner Series |
| **Platform** | YouTube |
| **Video Title** | Python Tutorial for Beginners 3 — Integers and Floats |
| **Duration** | ~15 minutes |
| **Link** | Search on YouTube: `Corey Schafer Python Beginners Integers Floats` |

> Also watch: `Corey Schafer Python Tutorial Comparisons and Booleans` (~10 min)  
> Both together cover all operators you need today.

### What to Focus On While Watching
- The difference between `/` (true division) and `//` (floor division) — they do NOT behave the same
- What the `%` (modulo) operator actually does — this is used in FizzBuzz and many real problems
- How `and` / `or` return actual values, not just `True`/`False` — this surprises most beginners
- Why `is` and `==` are different — Python caches small integers, which makes `is` behave unexpectedly

---

## CONCEPT SUMMARY

> Read this AFTER watching the video.

**Operators** are symbols that tell Python to perform an operation on values.

### Arithmetic Operators
```python
print(10 + 3)    # 13  — addition
print(10 - 3)    # 7   — subtraction
print(10 * 3)    # 30  — multiplication
print(10 / 3)    # 3.333...  — true division (always returns float)
print(10 // 3)   # 3   — floor division (rounds DOWN to nearest int)
print(10 % 3)    # 1   — modulo (remainder after floor division)
print(10 ** 3)   # 1000 — exponent (10 to the power of 3)
```

### Comparison Operators
```python
print(10 == 10)   # True  — equal
print(10 != 9)    # True  — not equal
print(10 > 9)     # True  — greater than
print(10 < 9)     # False — less than
print(10 >= 10)   # True  — greater than or equal
print(10 <= 9)    # False — less than or equal
```

### Logical Operators (short-circuit evaluation)
```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Short-circuit: Python stops evaluating as soon as the result is known
# In "and", if the first value is falsy — Python returns it immediately without checking the second
# In "or", if the first value is truthy — Python returns it immediately
print(0 and 10)     # 0   (returned 0 immediately — no point checking 10)
print(5 or 10)      # 5   (returned 5 immediately — already truthy)
```

### Assignment Operators
```python
x = 10
x += 3    # same as x = x + 3  → x is now 13
x -= 2    # x = 11
x *= 2    # x = 22
x //= 3   # x = 7
```

### Identity vs Equality
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)    # True  — same values
print(a is b)    # False — different objects in memory

# Small integers are cached by Python (usually -5 to 256)
x = 100
y = 100
print(x is y)    # True  — Python reuses the same object for small ints

x = 1000
y = 1000
print(x is y)    # False — Python creates separate objects for large ints
```

### Common Mistake to Avoid
Using `=` instead of `==` inside a condition. `=` assigns a value. `==` compares values. Writing `if x = 5:` is a SyntaxError in Python.

### How This Connects to Your Goal
Operators are used in every single Django view you will write — filtering querysets (`age >= 18`), checking permissions (`user.is_admin == True`), building conditions for business logic. Getting these solid now means zero confusion later.

---

## TODAY'S ASSIGNMENT

**Task:** Operators demonstration script  
**Time estimate:** 45 minutes  
**Difficulty:** Beginner  

### Requirements
Complete all of these:

- [ ] Demonstrate all 7 arithmetic operators with print statements showing inputs and outputs
- [ ] Show the difference between `/` and `//` clearly — use an example where the result is different (e.g. `7/2` vs `7//2`)
- [ ] Show short-circuit evaluation for `and` and `or` — use print statements that prove Python stopped early (hint: `0 and print("this should not print")`)
- [ ] Show the difference between `==` and `is` — use a list example where `==` is `True` but `is` is `False`
- [ ] **Stretch:** What does `bool(0)`, `bool("")`, `bool([])`, `bool(None)` return? Print all four and write a comment explaining what "falsy" means

### Rules During Assignment
- AI is **OFF**
- Official docs allowed: docs.python.org/3/library/stdtypes.html
- Re-read the Concept Summary above if stuck
- If stuck for 20+ minutes on one thing → note it and keep going

---

## HOW TO SUBMIT

When done, come back and say:

```
Submitting Day 2
```

Then paste your complete Python file.

**What AI will check:**
- [ ] All 7 arithmetic operators demonstrated with correct outputs
- [ ] `/` vs `//` distinction is clear and correctly explained
- [ ] Short-circuit evaluation actually demonstrated (not just mentioned)
- [ ] `==` vs `is` shown with correct understanding
- [ ] Stretch: falsy values listed and a comment explaining the concept

---

## REVISION CHECK

> Answer this before starting the video. Takes 2 minutes.  
> Topic from Day 1: **Variables & Data Types**

**Question:** Without looking at your Day 1 code — what does `type("hello")` return? What does `int("28")` do? And what error do you get if you call `int("twenty")`?

Write your answer out loud or in a comment in today's file before you begin.

---

## COMMUNICATION PRACTICE (15 minutes)

**Today: Refine your self-introduction**

You wrote a version on Day 1. Today, say it out loud 3 times without reading it.

Then answer this out loud (60 seconds):  
*"Operators in Python are ___. The one that surprised me was ___ because ___."*

This is technical explanation practice — you will be asked to explain code concepts in interviews. The habit starts now.

**Pronunciation drill (say each term 3 times):**  
Django (JANG-go) · PostgreSQL (post-GRESS-Q-L) · API (A-P-I) · HTTP (H-T-T-P) · Python (PIE-thon)

---

*Next lesson: DAY 3 — Strings (methods, slicing, f-strings, immutability)*
