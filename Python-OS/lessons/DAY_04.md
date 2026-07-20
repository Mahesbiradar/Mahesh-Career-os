# Day 4 — Control Flow — Python Level 1
Phase: Ignition (Days 1–30)
Estimated time: 2.5 hours

---

## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube (free) |
| Video title | Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements |
| Duration | ~20 min |
| Direct link | https://youtu.be/DZwmZ8Usvnk |

**What to focus on while watching:**
- The exact syntax of `if / elif / else` — indentation, colon, no parentheses needed around condition
- How Python evaluates conditions: `==` checks value, `is` checks identity — they are NOT the same
- Boolean operators `and`, `or`, `not` — and the term **short-circuit evaluation** (when Python stops evaluating early)
- What values are "falsy" in Python: `0`, `""`, `[]`, `None`, `False` — any condition check on these evaluates to `False`

---

## CONCEPT SUMMARY (read AFTER video, not before)

`if / elif / else` is Python's decision-making tool. Only one branch runs — the first condition that is `True`. If none match, `else` runs. If there is no `else`, nothing runs.

Conditions use comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`. The result is always `True` or `False`. You can combine conditions with `and` and `or`.

**Short-circuit evaluation**: with `and`, if the first condition is `False`, Python does not check the second — the result is already `False`. With `or`, if the first is `True`, Python stops — the result is already `True`. This is not an edge case, it is how Python is designed.

**Falsy values**: `0`, `""`, `[]`, `{}`, `None`, and `False` all evaluate to `False` in a condition. So `if name:` and `if name != "":` are equivalent. This is used everywhere in real Python code.

Nested `if` blocks (an `if` inside another `if`) work but are harder to read. Prefer `elif` over nesting when possible.

`not` flips a boolean: `not True` → `False`. `not False` → `True`. `not ""` → `True` (because `""` is falsy).

---

## TODAY'S ASSIGNMENT

**Goal:** Write a grade classifier program that uses `if / elif / else`, `and` / `or`, short-circuit evaluation, and falsy value checks — with a specific, correct f-string label on every print statement.

**Requirements (must complete all):**

- [ ] Ask the user to input a score (0–100) using `input()`. Convert it to `int`. Store in variable `score`.
- [ ] Use `if / elif / else` to classify the score:
  - 90–100 → `"A"`
  - 80–89 → `"B"`
  - 70–79 → `"C"`
  - 60–69 → `"D"`
  - below 60 → `"F"`
  - Print result with label exactly: `f"Grade: {grade}"`
- [ ] Add a condition using `and`: if score is between 85 and 95 (inclusive), print `f"Distinction range: True"` or `f"Distinction range: False"`
- [ ] Add a condition using `or`: if score is below 40 or above 95, print `f"Extreme score: True"` or `f"Extreme score: False"`
- [ ] Demonstrate short-circuit evaluation with `and`: write `result = score > 50 and score < 100`. Print `f"Short-circuit result: {result}"`. Add a comment on the line: `# short-circuit: if score > 50 is False, second check is skipped`
- [ ] Demonstrate falsy check: ask user for their name with `input()`. Use `if name:` (not `if name != ""`). If name is empty, print `f"Name: not provided"`. If name is given, print `f"Name: {name}"`

**Stretch (optional — only after all above are done):**
- [ ] Add input validation: if the user enters a score below 0 or above 100, print `f"Invalid score: {score}"` and do not classify it. Use a single `if` check at the top before the grade classification block.

**Rules:**
- Every `print()` must use an f-string. The label must describe exactly what is being printed — no generic labels like `"result"` or `"output"`.
- The label in requirement 2 must be exactly `f"Grade: {grade}"` — not `f"grade: {grade}"`, not `f"The grade is {grade}"`.
- Your code must run without errors before you submit.

---

## HOW TO SUBMIT

When done:
1. Save your file as: `submissions/day-04.py`
2. Come back to chat
3. Type: **"Submitting Day 4"** and paste your entire file content

The AI will check each requirement against your actual code. Not your description of it.

---

## COMMUNICATION PRACTICE (15 min)

**Today's task:** Answer this STAR behavioral question in writing.

**Question:** *"Tell me about a time you solved a problem under pressure."*

Use the STAR format:
```
Situation: [1–2 sentences — what was the context?]
Task:       [1 sentence — what was your responsibility?]
Action:     [2–3 sentences — what did YOU specifically do?]
Result:     [1–2 sentences — what was the outcome? Numbers if possible.]
```

Rules:
- Use your telecom work experience. Real situation, real outcome.
- Do not use "we did" — use "I did". Interviewers want to know what YOU did.
- Keep it under 150 words total. Brevity is a skill.

Paste your STAR answer with your code submission.

---

## REVISION CHECK (2 min — answer without looking)

Topic from yesterday: **Day 3 — Strings**

1. What does `"  hello  ".strip()` return? Does it change the original string?
2. You write `s = "backend engineer"`. What does `s[8:16]` return?

Answer in your head. If you cannot answer: re-read Day 3's concept summary before starting today's video.

---

## DAILY SUMMARY

| Slot | Content |
|------|---------|
| Video | Mosh — Python Section 3 — Control Flow (~35 min) |
| Assignment | Grade classifier — if/elif/else, and/or, short-circuit, falsy check |
| Communication | STAR answer — problem under pressure |
| Revision check | 2 questions from Day 3 |
| **Total estimated time** | **~2.5 hours** |
