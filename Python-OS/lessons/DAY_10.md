# Day 10 — Dictionaries — Python Level 1
Phase: Ignition
Estimated time: 2 hours

---
## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python Tutorial for Beginners (series) |
| Section/Video | Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs |
| Duration | ~10 min |
| Link | https://youtu.be/daefaLgNkw0 |

What to focus on while watching:
- How a dictionary stores data as `key: value` pairs instead of by position like a list
- Why dictionary keys must be unique, and what happens when you assign a new value to an existing key
- The difference between `student["name"]` and `student.get("name")`, especially when a key may not exist
- How to add, update, remove, and loop through dictionary data using `.items()`

---
## CONCEPT SUMMARY (read AFTER video, not before)

A dictionary stores related data using keys and values, like `"name": "Mahesh"` or `"course": "Python"`.
Use a dictionary when you want to access data by a clear label instead of remembering an index number.
Keys are unique: if you reuse the same key, Python replaces the old value with the new one.
Square brackets like `student["name"]` are direct, but they crash if the key is missing.
`.get()` is safer for optional data because it can return a default value instead of an error.
Looping with `.items()` gives both the key and the value, which is useful when printing or processing a full record.

---
## TODAY'S ASSIGNMENT

Goal: Show you can create, read, update, delete, safely access, and loop through dictionary data.

Requirements (must complete all):
- [ ] Create a dictionary called `student` with exactly these keys: `"name"`, `"age"`, `"course"`, and `"city"`, then print it with the label `Original profile:`
- [ ] Print the student's name using `student["name"]` with the label `Student name:`
- [ ] Add a new key `"email"` and update the `"city"` value to a different city, then print the dictionary with the label `Updated profile:`
- [ ] Use `.get()` to read a missing key called `"phone"` with the default value `"Not provided"`, then print it with the label `Phone:`
- [ ] Remove the `"age"` key, then loop through `student.items()` and print every remaining key-value pair under the label `Final profile:`

Stretch (optional — do only after main requirements done):
- [ ] Create a second dictionary called `skill_scores` with at least 3 skills and numeric scores. Loop through it and print only the skills with a score of 7 or higher.

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---
## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-10.py
2. Come back to the AI chat
3. Type: "Submitting Day 10" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---
## COMMUNICATION PRACTICE (15 min)

Today's task: In 4-5 polished sentences, explain what a Python dictionary is and when you would use one in a real project. Include one example, such as storing a user profile, product details, or API response data. Before submitting, proofread once for complete sentences, capital `I`, correct spelling, and spaces after commas.
Save output as: communication/day-10_comm.md (optional)
Paste it with your code submission for evaluation.

---
## REVISION CHECK (answer these without looking — 2 min)

1. Why can you not change an item inside a tuple after creating it?
2. What is the difference between `{}` and `set()` when creating an empty collection?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---
## THEORY BLOCK (20 min)

Subject: DBMS
Resource: Gate Smashers YouTube — "Lec-2: Introduction to DBMS (Database Management System) With Real life examples"
Link: https://youtu.be/3EJlovevfcA
Topic today: What is a DBMS

After watching, write 3 sentences in your own words explaining what a DBMS does and why applications use it instead of storing everything in plain files.
Include this with your submission.





