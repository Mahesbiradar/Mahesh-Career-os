# Day 13 — Class Variables — Python Level 2
Phase: Ignition
Estimated time: 2 hours

---
## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python OOP Tutorial |
| Section/Video | Python OOP Tutorial 2: Class Variables |
| Duration | ~16 min |
| Link | https://youtu.be/BJ-VvGyQxho |

What to focus on while watching:
- Why `raise_amount` is stored on the class instead of copied separately into every employee at first
- How Python searches for an attribute on the object first, then on the class
- Why a shared counter like `num_of_employees` should be updated through `Employee.num_of_employees`
- What changes when you override a class variable for one object only

---
## CONCEPT SUMMARY (read AFTER video, not before)

A class variable is data stored on the class itself, so every object can use the same default value.
An instance variable is data stored on one object, like one employee's name, role, or salary.
When code uses `self.raise_amount`, Python first checks that specific object; if it does not find the value there, it uses the class value.
This means you can set a default raise for all employees, but still override the raise for one employee when needed.
Shared counters, like total number of employees, usually belong on the class because they describe the group, not one object.
The common beginner mistake is writing to `self.num_of_employees` when the value should be shared across the whole class.
In Django later, you will see this idea in model fields, settings, managers, and class-level configuration.

---
## TODAY'S ASSIGNMENT

Goal: Build a small employee tracker that proves you understand the difference between class variables and instance variables.

Requirements (must complete all):
- [ ] Create a class called `Employee` with two class variables: `raise_amount = 1.04` and `num_of_employees = 0`.
- [ ] Add an `__init__` method that accepts `first_name`, `last_name`, `role`, and `monthly_salary`, stores them as instance attributes, and increases `Employee.num_of_employees` by 1.
- [ ] Add a method called `full_name` that returns the employee's first and last name together, and a method called `apply_raise` that updates `monthly_salary` using `self.raise_amount`.
- [ ] Create two different `Employee` objects. Print both employees using the labels `Employee 1:` and `Employee 2:`, and print the shared count using the exact label `Total employees:`.
- [ ] Set only employee 1's `raise_amount` to `1.10`, call `apply_raise()` on both employees, then print the exact labels `Employee 1 raise amount:`, `Employee 2 raise amount:`, `Employee 1 salary after raise:`, and `Employee 2 salary after raise:`.

Stretch (optional — do only after main requirements done):
- [ ] Change `Employee.raise_amount` to `1.06`, create a third employee after the change, and print all three employees' raise amounts to show which values come from the class and which value was overridden on one object.

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.
- Output labels must match the checklist exactly.

---
## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-13.py
2. Come back to the AI chat
3. Type: "Submitting Day 13" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---
## COMMUNICATION PRACTICE (15 min)

Today's task: In 6 polished sentences, answer this interview-style question: "What is a class variable, and how is it different from an instance variable?" Include the words `class variable`, `instance variable`, `shared`, `object`, and `override`. Before submitting, proofread once for complete sentences, capital `I`, correct spelling of "variable" and "instance", and spaces after commas.
Save output as: communication/day-13_comm.md (optional)
Paste it with your code submission for evaluation.

---
## REVISION CHECK (answer these without looking — 2 min)

1. What does `self` refer to inside an instance method?
2. If two `Employee` objects have different roles, why does changing one object's role not automatically change the other object's role?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---
## THEORY BLOCK (20 min)

Subject: OS
Resource: Gate Smashers YouTube — "L-1.5: Process States in Operating System | Schedulers"
Link: https://youtu.be/2dJdHMpCLIg
Topic today: Process States & Schedulers

After watching, write 3 sentences in your own words explaining the main process states, why the scheduler moves a process between states, and the difference between ready, running, and waiting.
Include this with your submission.
