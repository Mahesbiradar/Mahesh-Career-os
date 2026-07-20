# DAY 1 — Variables & Data Types
**Domain:** Python — Level 1  
**Phase:** 1 (Ignition)  
**Date:** 2026-06-26

---

## LESSON VIDEO

| | |
|---|---|
| **Course** | Python Programming with Mosh |
| **Platform** | Udemy Business |
| **Section** | Section 2 — Primitive Types |
| **Video Title** | Variables, Constants and Type Conversion |
| **Duration** | ~30 minutes (watch the full Section 2) |
| **Link** | Search "Python Programming with Mosh" on Udemy Business → Section 2 |

> **Can't find it?** Use this free alternative:  
> YouTube → search: `Corey Schafer Python Tutorial Variables` → watch Part 1 and Part 2 of his Python Beginner series (each ~20 min)

### What to Focus On While Watching
- How Python stores a value in memory when you write `x = 10`
- The difference between `int`, `float`, `str`, and `bool`
- What happens when you do `type(x)` — what does it return and why
- How `input()` always returns a string — even if the user types a number

---

## CONCEPT SUMMARY

> Read this AFTER watching the video.

A **variable** is a name you give to a value stored in memory. In Python, you do not declare the type — Python figures it out automatically.

```python
name = "Mahesh"      # str  (text)
age = 28             # int  (whole number)
salary = 6.5         # float (decimal number)
is_employed = False  # bool (True or False)
```

Python has four **primitive data types**:

| Type | Example | When You Use It |
|---|---|---|
| `int` | `28`, `100`, `-5` | Whole numbers, counts, IDs |
| `float` | `6.5`, `3.14`, `-0.5` | Decimal numbers, money, percentages |
| `str` | `"Mahesh"`, `"hello"` | Text — always in quotes |
| `bool` | `True`, `False` | Conditions, flags, yes/no |

### Checking the type
```python
x = 42
print(type(x))     # <class 'int'>
```

### Type Conversion
You can convert between types:
```python
age = "28"           # this is a string
age = int(age)       # now it's an integer
print(age + 2)       # 30  ← this works now
```

### Taking input from the user
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # must convert — input() always gives a string
```

### Common Mistake to Avoid
`input()` always returns a **string**. If you ask for a number and try to do maths with it, Python will throw an error. Always convert with `int()` or `float()`.

```python
age = input("Age: ")
print(age + 1)        # ERROR — can't add string and int
print(int(age) + 1)   # CORRECT — 29
```

### How This Connects to Your Goal
Every Django model field you write later (`name = CharField`, `age = IntegerField`) is built on these exact types. Understanding types now means you will never be confused by Django field choices.

---

## TODAY'S ASSIGNMENT

**Task:** Build a personal profile program  
**Time estimate:** 45 minutes  
**Difficulty:** Beginner  

### Requirements
Complete all of these:

- [ ] Create variables for: your name (str), your age (int), your years of experience (int), your target salary in LPA (float), and whether you are currently employed (bool)
- [ ] Print a formatted profile using f-strings that outputs all five values in one readable block (see expected output below)
- [ ] Ask the user to input a name and age using `input()`. Convert age to int. Print: "Hello [name], you will be [age+1] next year."
- [ ] Check the type of each of your five variables using `type()` and print them — confirm each is the type you expect
- [ ] **Stretch:** What happens if someone types "twenty" instead of a number in the age input? Try it. Note what error you get. Write a comment in your code explaining what the error means.

### Expected Output (for the profile block)
```
=== My Profile ===
Name: Mahesh Biradar
Age: 28
Experience: 8 years
Target Salary: 6.5 LPA
Currently Employed: False
```

### Rules During Assignment
- AI is **OFF**
- Python official docs allowed: docs.python.org/3/library/functions.html
- Re-read the Concept Summary above if stuck
- If stuck for 20+ minutes on one specific thing → note it and keep going

---

## HOW TO SUBMIT

When done, paste this in chat:

```
Submitting Day 1

[paste your complete Python code here]
```

**What AI will check:**
- [ ] All five variables created with correct types
- [ ] f-string used correctly in the profile output
- [ ] `input()` result converted with `int()` before arithmetic
- [ ] `type()` called on all variables and output matches expected type
- [ ] Stretch: error observed and commented — shows real curiosity

---

## REVISION CHECK

> No revision today — this is Day 1.  
> Starting from tomorrow, each lesson will have a quick recall question from 3 days earlier.

---

## COMMUNICATION PRACTICE (15 minutes)

**Today: Self Introduction**

Your self-introduction for SDE interviews needs to cover:
1. Your name and background (telecom — keep it brief)
2. Why you are transitioning to software engineering
3. What you are currently learning and building
4. What kind of role you are targeting

Draft it in writing first (3–4 sentences). Then say it out loud 3 times.

**Sample structure:**
*"Hi, I'm Mahesh Biradar. I have 8 years of experience in telecom network operations, which gave me a strong foundation in systems, debugging, and working under pressure. I'm now transitioning to software engineering — I'm currently building backend systems with Python and Django. I'm targeting backend developer or full-stack roles where I can apply both my systems thinking and my new development skills."*

This is just a sample. Write it in your own words. You will improve this every week.

---

*Next lesson: DAY 2 — Operators & Expressions*
