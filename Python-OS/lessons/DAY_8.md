# Day 8 — Lists — Python Level 1
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
| Duration | ~24 min (watch the Lists portion fully; Tuples/Sets come Day 9) |
| Link | https://youtu.be/W8KRzm-HUcc |

What to focus on while watching:
- How `append()` adds to the end vs. `insert()` adds at a specific index
- The difference between `remove()` (deletes by value) and `pop()` (deletes by index)
- How list slicing (`list[start:stop]`) pulls out a sub-list without changing the original
- That lists are mutable — the same list object changes in place when you call these methods (no need to reassign it)

---
## CONCEPT SUMMARY (read AFTER video, not before)

A list is an ordered, changeable collection written with square brackets: `["a", "b", "c"]`. Unlike the variables you've used so far, a list is mutable — you can add, remove, or change items after creating it, and the original list itself changes (no new variable needed).

The methods that trip people up: `append(x)` always adds to the end. `insert(i, x)` adds at position `i`, shifting everything after it right. `remove(x)` deletes the *first* item that matches the *value* `x` — if the value isn't in the list, it errors. `pop(i)` deletes by *index* and also returns the removed item.

Indexing works like strings: `movies[0]` is the first item, `movies[-1]` is the last. Slicing (`movies[0:3]`) returns a new list containing items from index 0 up to (not including) index 3.

`enumerate(list)` is the clean way to loop with both the index and the value at once — you'll use it constantly instead of manually tracking a counter.

---
## TODAY'S ASSIGNMENT

Goal: Show you can create a list and modify it correctly using the core list methods, then read it back with a loop and slicing.

Requirements (must complete all):
- [ ] Create a list called `movies` containing at least 5 string items (any movies you like)
- [ ] Use `append()` to add one new movie to the end of `movies`, then print the full list with the label `After append:`
- [ ] Use `insert()` to add a movie at index `0`, then print the full list with the label `After insert:`
- [ ] Use `remove()` to delete one specific movie by name (pick one already in the list), then print the full list with the label `After remove:`
- [ ] Use a `for` loop with `enumerate()` to print every remaining movie in the format `1. Inception` (number starts at 1, not 0), with the label `Final list:` printed on the line before the loop starts

Stretch (optional — do only after main requirements done):
- [ ] Use `.sort()` to sort `movies` alphabetically, print the sorted list with the label `Sorted:`, then use slicing to print only the first 3 items of the sorted list with the label `Top 3:`

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---
## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-08.py
2. Come back to the AI chat
3. Type: "Submitting Day 8" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---
## COMMUNICATION PRACTICE (15 min)

Today's task: Write a 3-4 sentence self-introduction for an SDE interview, mentioning your move from telecom into software development. Before submitting, proofread it once yourself and fix any spelling mistakes (watch out for words like "perform", "multiple", "unnecessary", "immediately" — these have tripped you up before).
Save output as: communication/day-8_comm.md (optional)
Paste it with your code submission for evaluation.

---
## REVISION CHECK (answer these without looking — 2 min)

1. In a function, what's the difference between returning a value and printing it?
2. If a function has a parameter with a default value, what happens when you call the function without passing that argument?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)
