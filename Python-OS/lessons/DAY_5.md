# Day 5 — Loops — Python Level 1
Phase: Ignition
Estimated time: ~1.5 hours (20 min video + 45 min assignment + 15 min communication + 2 min revision check)

---

## FIX FROM YESTERDAY

Yesterday's falsy check used double-negation (`if not name != ""`) instead of the direct form. Today's assignment requires `if <list_name>:` used directly — no negation, no `!= []`, no `len() == 0`.

---

## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python Tutorial for Beginners (series) |
| Section/Video | Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops |
| Duration | ~15–20 min (approx) |
| Link | https://youtu.be/6iF8Xb7Z3wQ |

What to focus on while watching:
- The difference between `for` and `while` loops — when you'd reach for each one
- How `range()` actually works (start, stop, step) and why `range(5)` gives you 0–4, not 1–5
- What `break` and `continue` do to the loop's flow — break exits entirely, continue just skips the current iteration
- Iterating directly over a list/string (`for item in my_list`) vs. using `range(len(my_list))`

---

## CONCEPT SUMMARY (read AFTER video, not before)

A `for` loop is for when you know what you're iterating over — a list, a string, a range of numbers. A `while` loop is for when you're repeating until some condition becomes false, and you don't necessarily know in advance how many times that'll take.

`range(start, stop, step)` generates numbers up to but *not including* stop — this is the single most common source of off-by-one bugs for beginners. `range(1, 11)` gives you 1 through 10.

`break` stops the loop immediately, no matter where you are in it. `continue` skips the rest of the current iteration and jumps to the next one — the loop keeps running, it just skips work for that one pass.

Checking if a list is empty follows the same "truthiness" logic as strings from Day 4: an empty list `[]` is falsy, a non-empty list is truthy. So `if my_list:` is the correct, direct way to check — same pattern as `if name:`, just applied to a different type.

---

## TODAY'S ASSIGNMENT

Goal: Demonstrate correct use of `for` loops, `while` loops, `range()`, `break`, `continue`, and a direct truthiness check on a list — with exact output formatting.

Requirements (must complete all):
- [ ] Use a `for` loop with `range()` to print numbers 1 to 10. Each line must be exactly: `Number: 1`, `Number: 2`, ... `Number: 10` (no extra spaces, no trailing space before the number)
- [ ] Use a `while` loop to count down from 5 to 1 (one number per line), then print `Liftoff!` after the loop ends. Must use a loop — no repeated print statements
- [ ] Create a list of at least 5 items. Use a `for` loop with `break` to stop as soon as you find a specific target item, printing exactly: `Found: <item>`
- [ ] Loop through numbers 1 to 20. Use `continue` to skip even numbers, and print odd numbers exactly as: `Odd: 1`, `Odd: 3`, etc.
- [ ] Create one empty list and one non-empty list. For each, use `if <list_name>:` directly (no `not`, no `!= []`, no `len() == 0`) to print exactly `List is empty` or `List has items`. Your code must demonstrate both cases running.

Stretch (optional — do only after main requirements done):
- [ ] Use a nested loop to print a multiplication table (1 through 5) for a number of your choice, formatted exactly as: `3 x 4 = 12`

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---

## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-05.py
2. Come back to the AI chat
3. Type: "Submitting Day 5" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---

## COMMUNICATION PRACTICE (15 min)

Second attempt at STAR — Day 2's attempt had spelling issues (cutomer, immedetly, thougt) and needs "I" not "we".

Task: Answer this behavioral question using explicit STAR labels:
*"Tell me about a time you had to learn something new quickly."*

Write your answer with each part clearly labeled:
```
Situation: ...
Task: ...
Action: ...
Result: ...
```
Use "I" throughout (not "we") — this is about your individual contribution. Proofread before submitting; check spelling carefully.

Save output as: communication/day-5_comm.md (optional)
Paste it with your code submission for evaluation.

---

## REVISION CHECK (answer these without looking — 2 min)

1. What was wrong with `if not name != "":` from Day 4, and what's the correct, direct way to write it?
2. If `age = 0`, does `if age:` evaluate to True or False? Why does this matter when checking truthiness?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---

*Next lesson: Day 6 — Functions — Basics*
