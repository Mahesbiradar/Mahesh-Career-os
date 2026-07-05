# Day 6 — Loops (repeat) — Python Level 1
Phase: Ignition
Estimated time: ~1.5 hours (20 min video + 45 min assignment + 15 min communication + 2 min revision check)

---

## FIX FROM YESTERDAY

Day 5 was a REDO. Three things were missed:
1. `continue` was never actually used — an `if num % 2 != 0:` condition was substituted for it.
2. `Found: <item>` was printed with literal angle brackets (`Found: <6>`) instead of the exact value (`Found: 6`).
3. Only the empty-list case was created and tested — the non-empty list was missing entirely.

Today re-covers the same topic. All three gaps are specifically re-tested below.

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

What to focus on while watching (rewatch, don't skip — these are exactly what you missed):
- The part where `continue` skips the rest of the current iteration but the loop keeps going — notice it's a jump, not a condition wrapped around your print statement
- Pause right after any `print(f"...")` example and check character-by-character whether your own planned output would match exactly, including any punctuation
- How truthiness checks (`if some_list:`) behave differently for an empty list vs. a list with items — watch both cases run, not just one

---

## CONCEPT SUMMARY (read AFTER video, not before)

`continue` is not the same as wrapping your print in an `if` that only fires for the cases you want. `continue` jumps back to the top of the loop and skips everything below it for that iteration — so the correct pattern is: check the condition you want to SKIP, call `continue` inside it, and put the "normal" work (like your print) as a plain, unconditional line afterward with no `if` around it.

Exact output means exact — no extra characters. If a spec says the output should show a value like `6`, and you write `f"Found: <{item}>"`, Python will literally print the angle brackets. Read format instructions as "here is the literal string, character for character" unless told otherwise.

Truthiness on lists works exactly like strings: `[]` is falsy, `[1, 2, 3]` is truthy. To actually demonstrate both cases, you need two different list variables, each with its own `if list_name:` check — one where the condition is empty and one where it's not. Only creating one list "checks" only half the concept.

---

## TODAY'S ASSIGNMENT

Goal: Demonstrate correct use of `for` loops, `while` loops, `range()`, `break`, `continue`, and truthiness checks on lists — with exact output formatting, and specifically fix the three gaps from Day 5.

Requirements (must complete all):
- [ ] Use a `for` loop with `range()` to print numbers 1 to 15. Each line must be exactly: `Count: 1`, `Count: 2`, ... `Count: 15` (no extra spaces, no trailing space before the number)
- [ ] Use a `while` loop to count UP from 1 to 5 (one number per line), then print `Done!` after the loop ends. Must use a loop — no repeated print statements
- [ ] Create a list of at least 6 items. Use a `for` loop with `break` to stop as soon as you find a specific target item. Print exactly `Found: 6` style output — i.e. `Found: ` followed immediately by the item's actual value and nothing else. No angle brackets, no extra punctuation. (If your target is `7`, the printed line must be exactly `Found: 7`.)
- [ ] Loop through numbers 1 to 25 using `range(1, 26)`. You must use the `continue` keyword: if a number is even, `continue` immediately. The `print(f"Odd: {num}")` line must be a separate, unconditional statement that runs after the `continue` check — not wrapped in its own `if`.
- [ ] Create two separate lists: one empty, one with at least 3 items. For EACH list, use `if <list_name>:` directly (no `not`, no `!= []`, no `len() == 0`) to print exactly `List is empty` or `List has items`. Both checks must run in your code and both outputs must appear when the file is executed.

Stretch (optional — do only after main requirements done):
- [ ] Use a nested loop to print multiplication tables (1 through 5) for TWO different numbers of your choice, formatted exactly as: `4 x 3 = 12`

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---

## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-06.py
2. Come back to the AI chat
3. Type: "Submitting Day 6" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---

## COMMUNICATION PRACTICE (15 min)

Third attempt at STAR. Day 5's attempt did not use the labeled format at all (plain numbered paragraphs instead), still slipped into "we" instead of "I", and still had spelling errors (intrviewed, alinged, im).

Task: Answer this behavioral question using explicit STAR labels:
*"Tell me about a time you had to solve a problem under pressure or with limited information."*

Write your answer with each part clearly labeled, using this exact structure — do not paraphrase the labels away into paragraphs:
```
Situation: ...
Task: ...
Action: ...
Result: ...
```
Use "I" throughout (not "we") — this is about your individual contribution. Proofread before submitting; check spelling carefully, especially words you've misspelled before (interviewed, aligned, I'm).

Save output as: communication/day-6_comm.md (optional)
Paste it with your code submission for evaluation.

---

## REVISION CHECK (answer these without looking — 2 min)

1. If the assignment requires you to use `continue`, why doesn't writing `if num % 2 != 0: print(...)` satisfy that requirement, even though the output looks the same?
2. If a target item's value is `6` and the spec says print exactly `Found: 6`, what's wrong with writing `print(f"Found: <{item}>")`? What would it actually print?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---

*Next lesson: Day 7 — Functions — Basics (only after Day 6 passes)*
