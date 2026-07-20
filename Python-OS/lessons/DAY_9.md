# Day 9 — Tuples + Sets — Python Level 1
Phase: Ignition
Estimated time: 1.5 hours

---
## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python Tutorial for Beginners (series) |
| Section/Video | Python Tutorial for Beginners 4: Lists, Tuples, and Sets |
| Duration | ~24 min (watch the Tuples and Sets portions; Lists already covered Day 8) |
| Link | https://youtu.be/W8KRzm-HUcc |

What to focus on while watching:
- How tuples are written with parentheses and are immutable — once created, you can't add, remove, or change items
- Why you'd choose a tuple over a list (fixed data that shouldn't change, e.g. coordinates)
- How sets store only unique, unordered items — duplicates are automatically dropped
- Set operations: union (`|`), intersection (`&`), difference (`-`)

---
## CONCEPT SUMMARY (read AFTER video, not before)

A tuple is an ordered, immutable collection written with parentheses: `(1, 2, 3)`. "Immutable" means once it's created, you cannot append, insert, or remove items — if you need to change the data, you'd use a list instead. Tuples are ideal for fixed groups of values, like coordinates or a function returning multiple values at once.

Tuple unpacking lets you assign each item to its own variable in one line: `x, y, z = coordinates`. This only works if the number of variables matches the number of items in the tuple.

A set is an unordered collection of unique items written with curly braces: `{"a", "b", "c"}`. Sets automatically remove duplicates — if you add the same value twice, it only appears once. Sets have no index, so `my_set[0]` doesn't work.

Set math is where sets get useful: `&` gives items in both sets (intersection), `|` gives all items from either set with no duplicates (union), and `-` gives items in the first set but not the second (difference).

Two things that trip people up: an empty set must be written `set()`, not `{}` — `{}` creates an empty dictionary. And a one-item tuple needs a trailing comma: `(5,)` not `(5)` — without the comma, Python just treats it as the number in parentheses.

---
## TODAY'S ASSIGNMENT

Goal: Show you can create and unpack a tuple, and use sets with intersection/union operations to compare two collections.

Requirements (must complete all):
- [ ] Create a tuple called `coordinates` with exactly 3 numbers (x, y, z), then print it with the label `Coordinates:`
- [ ] Unpack `coordinates` into three variables `x`, `y`, `z`, then print them with the label `Unpacked:` in the exact format `x=1, y=2, z=3` (using your actual values)
- [ ] Create two sets, `python_skills` and `java_skills`, each with at least 4 string items, with at least 2 items overlapping between them
- [ ] Use `&` to find the skills common to both sets, then print the result with the label `Common skills:`
- [ ] Use `|` to combine both sets into all unique skills, then print the result with the label `All skills:`

Stretch (optional — do only after main requirements done):
- [ ] Use `-` to find skills that are in `python_skills` but not in `java_skills`, then print the result with the label `Python only:`

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---
## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-09.py
2. Come back to the AI chat
3. Type: "Submitting Day 9" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---
## COMMUNICATION PRACTICE (15 min)

Today's task: In 3-4 sentences, explain the difference between a list and a tuple, as if answering it in an interview. Before submitting, proofread it once: check that every sentence is a complete sentence (not a fragment ending in a period where it should be joined with a comma), and that no sentence starts with "And". Also double-check spelling on any word you're unsure of.
Save output as: communication/day-9_comm.md (optional)
Paste it with your code submission for evaluation.

---
## REVISION CHECK (answer these without looking — 2 min)

1. What's the difference between `append()` and `insert()` on a list?
2. What does `enumerate()` give you when looping over a list, and why is it more useful than a plain `for item in list` loop when you also need the position?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)
