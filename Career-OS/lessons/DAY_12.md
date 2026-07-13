# Day 12 — OOP Basics — Python Level 2
Phase: Ignition
Estimated time: 2 hours

---
## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python OOP Tutorial |
| Section/Video | Python OOP Tutorial 1: Classes and Instances |
| Duration | ~16 min |
| Link | https://youtu.be/ZDa-Z5JzLYM |

What to focus on while watching:
- How a `class` acts like a blueprint, while each object is a separate instance made from that blueprint
- Why `__init__` is used to set starting data for each new object
- What `self` means inside instance methods and why Python passes the object into the method
- How instance attributes like `name`, `role`, or `salary` belong to one object, not automatically to every object

---
## CONCEPT SUMMARY (read AFTER video, not before)

Object-oriented programming lets you group related data and behavior together.
A class is the blueprint; an object is one real thing created from that blueprint.
`__init__` runs when a new object is created, so it is the right place to store starting values.
`self` means "this specific object", which is why `self.name` for one object can be different from `self.name` for another object.
Instance attributes store data, and instance methods perform actions using that object's data.
The common beginner mistake is forgetting `self` in a method definition or using a variable name without `self.` when you meant the object's attribute.
In Django later, models, views, forms, and serializers all use class-based patterns, so this is a foundation topic.

---
## TODAY'S ASSIGNMENT

Goal: Build a small class-based employee profile program that proves you understand classes, objects, attributes, and methods.

Requirements (must complete all):
- [ ] Create a class called `Employee` with an `__init__` method that accepts `first_name`, `last_name`, `role`, and `monthly_salary`, then stores all four as instance attributes.
- [ ] Add a method called `full_name` that returns the employee's first and last name together as one string.
- [ ] Add a method called `annual_salary` that returns the monthly salary multiplied by 12.
- [ ] Create two different `Employee` objects with different names, roles, and salaries. Print each employee using the labels `Employee 1:` and `Employee 2:` and include the full name, role, and annual salary in the output.
- [ ] Update only the first employee's `role`, then print both roles again using the labels `Updated Employee 1 role:` and `Employee 2 role still:` to prove the two objects keep separate data.

Stretch (optional — do only after main requirements done):
- [ ] Add a method called `give_raise` that accepts a percentage number, increases that employee's monthly salary, and then print the new annual salary for one employee.

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---
## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-12.py
2. Come back to the AI chat
3. Type: "Submitting Day 12" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---
## COMMUNICATION PRACTICE (15 min)

Today's task: In 5 polished sentences, explain the difference between a class and an object to a beginner. Include the words `class`, `object`, `instance`, `attribute`, and `method`. Before submitting, proofread once for complete sentences, capital `I`, correct spelling of "instance" and "attribute", and spaces after commas.
Save output as: communication/day-12_comm.md (optional)
Paste it with your code submission for evaluation.

---
## REVISION CHECK (answer these without looking — 2 min)

1. In a `try` / `except` / `else` / `finally` structure, when does the `else` block run?
2. Why is `except ValueError` better than a bare `except` when converting user input to an integer?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---
## THEORY BLOCK (20 min)

Subject: OS
Resource: Gate Smashers YouTube — "L-1.1: Introduction to Operating System and its Functions"
Link: https://youtu.be/WJ-UaAaumNA
Topic today: What is an OS

After watching, write 3 sentences in your own words explaining what an operating system does, why applications need it, and how it manages resources like CPU, memory, files, and devices.
Include this with your submission.
