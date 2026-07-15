# Day 14 — classmethods & staticmethods — Python Level 2
Phase: Ignition
Estimated time: 2 hours

---
## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python OOP Tutorial |
| Section/Video | Python OOP Tutorial 3: classmethods and staticmethods |
| Duration | ~15 min |
| Link | https://youtu.be/rq8cL2XMM5M |

What to focus on while watching:
- How a normal method receives `self`, but a classmethod receives `cls`
- Why classmethods are useful for changing class-level data like `raise_amount`
- How a classmethod can be used as an alternate constructor, such as building an object from a string
- Why a staticmethod belongs inside a class only when the function is related to the class but does not need object or class data

---
## CONCEPT SUMMARY (read AFTER video, not before)

A regular instance method works with one object, so it receives `self`.
A classmethod works with the class itself, so it receives `cls` and can update class variables or create new objects.
The `@classmethod` decorator is often used for alternate constructors, where you take data in another format and return a ready-made object.
Using `cls` instead of writing `Employee` directly keeps the method flexible if you later create subclasses.
A staticmethod does not receive `self` or `cls`; it is just a helper function placed inside the class because it logically belongs there.
The common beginner mistake is using `@staticmethod` for code that actually needs object data or class data.
In Django later, you will see class-level patterns in managers, model helpers, and reusable constructors.

---
## TODAY'S ASSIGNMENT

Goal: Build an employee helper that proves you understand when to use a classmethod and when to use a staticmethod.

Requirements (must complete all):
- [ ] Create a class called `Employee` with a class variable `raise_amount = 1.04` and an `__init__` method that accepts `first_name`, `last_name`, `role`, and `monthly_salary`.
- [ ] Add an instance method called `full_name` that returns the employee's first and last name together.
- [ ] Add a `@classmethod` called `set_raise_amount(cls, amount)` that updates the class variable. Use `cls.raise_amount`, not `Employee.raise_amount`, inside the method.
- [ ] Add a `@classmethod` called `from_string(cls, employee_string)` that accepts a string like `"Anita-Sharma-Developer-50000"`, splits it, and returns a new `Employee` object.
- [ ] Add a `@staticmethod` called `is_workday(day_name)` that returns `False` for `"Saturday"` and `"Sunday"`, and `True` for other day names.
- [ ] Create one employee normally and one employee using `Employee.from_string(...)`. Print the exact labels `Employee 1:`, `Employee 2:`, `Raise amount:`, `Monday is workday:`, and `Sunday is workday:`.

Stretch (optional — do only after main requirements done):
- [ ] Add another classmethod called `from_csv(cls, csv_string)` that accepts a string like `"Ravi,Kumar,Tester,45000"` and returns a new `Employee` object.

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.
- Output labels must match the checklist exactly.

---
## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-14.py
2. Come back to the AI chat
3. Type: "Submitting Day 14" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---
## COMMUNICATION PRACTICE (15 min)

Today's task: In 6 polished sentences, answer this interview-style question: "When would you use a classmethod instead of a staticmethod?" Include the words `classmethod`, `staticmethod`, `cls`, `self`, and `object`. Before submitting, proofread once for complete sentences, capital `I`, correct spelling of "method", "static", "class", "object", and "separate", and spaces after commas.
Save output as: communication/day-14_comm.md (optional)
Paste it with your code submission for evaluation.

---
## REVISION CHECK (answer these without looking — 2 min)

1. When code uses `self.raise_amount`, where does Python look first: the object or the class?
2. Why should a shared employee counter be updated with `Employee.num_of_employees` instead of `self.num_of_employees`?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---
## THEORY BLOCK (20 min)

Subject: CN
Resource: Gate Smashers YouTube — "Lec-2: Introduction to Computer Network | OSI MODEL in easiest Way in Hindi"
Link: https://youtu.be/4D55Cmj2t-A
Topic today: What is a Network + OSI Model intro

After watching, write 3 sentences in your own words explaining what a computer network is, why networking is divided into layers, and what the OSI model helps engineers remember.
Include this with your submission.
