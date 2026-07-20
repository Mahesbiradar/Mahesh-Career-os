# Day 11 — Exception Handling — Python Level 1
Phase: Ignition
Estimated time: 2 hours

---
## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python Tutorial |
| Section/Video | Python Tutorial: Using Try/Except Blocks for Error Handling |
| Duration | ~20 min |
| Link | https://youtu.be/NIWwJbo-9_8 |

What to focus on while watching:
- How Python stops normal execution when an exception happens
- Why the risky line should go inside `try`, not the entire program
- How `except`, `else`, and `finally` run in different situations
- Why catching a specific error like `ValueError` is safer than hiding every possible error

---
## CONCEPT SUMMARY (read AFTER video, not before)

An exception is a problem that happens while the program is running, like converting `"abc"` to an integer.
`try` lets you run code that might fail, and `except` lets you handle the expected failure without crashing the whole program.
Catch specific exceptions when possible, because a bare `except` can hide real bugs.
`else` runs only when no exception happened, so it is useful for success-only logic.
`finally` runs whether the code succeeded or failed, so it is useful for cleanup or final messages.
Keep the `try` block small: put only the risky operation inside it.
Exception handling is not for ignoring problems; it is for responding clearly when something goes wrong.

---
## TODAY'S ASSIGNMENT

Goal: Build a small score-cleaning program that handles invalid numeric data without crashing.

Requirements (must complete all):
- [ ] Create a list called `raw_scores` with exactly these values: `"85"`, `"90"`, `"absent"`, `"76"`, `"100"`, and `"error"`. Also create empty lists called `valid_scores` and `skipped_values`.
- [ ] Loop through `raw_scores`. Inside the loop, use a `try` block to convert each value to an integer.
- [ ] Use `except ValueError` to handle invalid values. In this block, add the original value to `skipped_values` and print `Skipped invalid score: <value>`.
- [ ] Use an `else` block for successful conversions. In this block, add the integer score to `valid_scores` and print `Accepted score: <score>`.
- [ ] Use a `finally` block to print `Finished checking: <value>` for every item. After the loop, print `Valid scores:`, `Skipped values:`, and `Average score:` using the data you collected.

Stretch (optional — do only after main requirements done):
- [ ] Add `"105"` to `raw_scores`, and after converting a score, manually `raise ValueError` if the score is greater than 100 or less than 0. Skip it the same way as the text errors.

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---
## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-11.py
2. Come back to the AI chat
3. Type: "Submitting Day 11" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---
## COMMUNICATION PRACTICE (15 min)

Today's task: In 5 polished sentences, answer this interview-style question: "How do you handle invalid user input in Python?" Mention `try`, `except`, a specific exception type, and what message or fallback you would give the user. Before submitting, proofread once for complete sentences, capital `I`, correct spelling of "exception" and "specific", and spaces after commas.
Save output as: communication/day-11_comm.md (optional)
Paste it with your code submission for evaluation.

---
## REVISION CHECK (answer these without looking — 2 min)

1. Why is `student.get("phone", "Not provided")` safer than `student["phone"]` when the key might be missing?
2. What syntax problem can happen when you put double quotes inside a double-quoted f-string, and how can you avoid it?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---
## THEORY BLOCK (20 min)

Subject: DBMS
Resource: Gate Smashers YouTube — "Lec-16: Introduction to ER model"
Link: https://youtu.be/gbVev8RuZLg
Topic today: ER Modeling

After watching, write 3 sentences in your own words explaining what an entity, an attribute, and a relationship mean in DBMS design.
Include this with your submission.
