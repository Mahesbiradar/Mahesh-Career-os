# Day 15 — Inheritance & super() — Python Level 2

Phase: Ignition

Estimated time: 2 hours

---

## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python OOP Tutorial |
| Section/Video | Python OOP Tutorial 4: Inheritance - Creating Subclasses |
| Duration | ~20 min |
| Link | https://youtu.be/RSl87lqOXDE |

What to focus on while watching:

- How one class can inherit from another
- Why inheritance reduces duplicate code
- How child classes override parent methods
- Why `super()` is used inside constructors
- The relationship between parent and child classes

---

## CONCEPT SUMMARY (read AFTER video, not before)

Inheritance allows one class to reuse the attributes and methods of another class.

The original class is called the parent (or base) class, while the new class is called the child (or subclass).

A child class automatically inherits behaviour from its parent but can also define new attributes or override existing methods.

The `super()` function is used to call the parent implementation instead of rewriting it.

Inheritance helps organize related objects and reduces repeated code.

You will later use inheritance throughout Django, including class-based views, forms, exceptions, and models.

---

## TODAY'S ASSIGNMENT

Goal:

Build a small inheritance hierarchy and prove that subclasses inherit and override behaviour correctly.

Requirements (must complete all):

- [ ] Create a `Person` parent class with an `__init__(self, name)` storing `self.name`.
- [ ] Create an `Employee(Person)` subclass that adds `employee_id`.
- [ ] Override the `info()` method inside `Employee`.
- [ ] Use `super().__init__(name)` inside the child constructor.
- [ ] Create two employee objects.
- [ ] Print exactly two output lines using `info()`.

Stretch (optional):

- [ ] Create another subclass called `Manager(Employee)`.
- [ ] Add a `team_size` attribute.
- [ ] Override `info()` while reusing the parent implementation with `super().info()`.

Rules:

- Watch the video first.
- Do not copy from Google or AI.
- Test your program before submitting.
- Output labels should match the assignment.

---

## HOW TO SUBMIT

When done:

1. Save your file as:

```
submissions/day-15.py
```

2. Return to the AI chat.

3. Type:

```
Submitting Day 15
```

and paste your complete code.

---

## COMMUNICATION PRACTICE (15 min)

Today's task:

Write **6 polished sentences** explaining:

**"What is inheritance in Python and why is `super()` important?"**

Include the following words naturally:

- inheritance
- parent class
- child class
- override
- super()
- object

Proofread before submitting.

Save as (optional):

```
communication/day-15_comm.md
```

---

## REVISION CHECK (answer without looking — 2 min)

1. What is the purpose of `super()` inside a child class constructor?

2. Why should a subclass override a method instead of copying the parent implementation?

---

## THEORY BLOCK (20 min)

Subject: CN

Resource:

Gate Smashers YouTube — TCP/IP Model vs OSI Model

Topic today:

TCP/IP Model vs OSI Model

After watching, write **3 sentences** in your own words explaining:

- the difference between the OSI and TCP/IP models,
- why TCP/IP is used on the Internet,
- and why engineers still study the OSI model.