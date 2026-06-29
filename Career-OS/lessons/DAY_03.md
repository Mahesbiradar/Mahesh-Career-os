# Day 3 — Strings — Python Level 1
Phase: Ignition (Days 1–30)
Estimated time: 2.5 hours

---

## Fix from Yesterday (Day 2 — NEEDS WORK)

Before starting today's video, fix these three things mentally:

1. **f-string labels must match the operation** — `f"x + y = {x+y}"` not `f"x-y = {x+y}"` for addition
2. **Short-circuit proof means a direct expression** — `print(False and print("runs"))` shows short-circuit, not an if/else block
3. **bool() usage** — `bool(0)`, `bool("")`, `bool([])` called directly, not wrapped in if/else

These are not major — your concept understanding was solid. Watch out for these in today's code.

---

## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube (free) |
| Playlist | Python Beginner Series |
| Video | "Python Tutorial for Beginners 2: Strings - Working with Textual Data" |
| Duration | ~25 min |
| Link | Search: `Corey Schafer Python Strings` on YouTube |

**What to focus on while watching:**
- How slicing works: `s[start:stop:step]` — what happens when you omit start or stop
- The difference between a method that **returns** a new string vs modifies in place (strings are immutable — nothing modifies in place)
- Which string methods are most common in real code: `.strip()`, `.split()`, `.join()`, `.replace()`, `.find()`, `.startswith()`, `.upper()`, `.lower()`
- How f-strings handle expressions inside `{}` — you can put calculations, method calls, anything

---

## CONCEPT SUMMARY (read AFTER video, not before)

Strings in Python are **immutable sequences of characters**. Once created, you cannot change individual characters — every method returns a new string.

Slicing `s[start:stop:step]` is the most powerful string tool. `s[::-1]` reverses a string. `s[0]` is first character. `s[-1]` is last. Negative index counts from the end.

String methods do not change the original string. `name.upper()` returns an uppercase copy — `name` itself is unchanged. This is the immutability rule.

f-strings `f"Hello {name}"` evaluate whatever is inside `{}` at runtime. You can write `f"Result: {2 + 2}"` and get `Result: 4`. The label inside the string should describe what you are showing — this was yesterday's fix.

`.split()` turns a string into a list: `"a,b,c".split(",")` → `["a","b","c"]`. `.join()` does the reverse: `",".join(["a","b","c"])` → `"a,b,c"`.

The `in` keyword checks membership: `"ell" in "hello"` → `True`. Faster than `.find()` for simple checks.

---

## TODAY'S ASSIGNMENT

**Goal:** Write a string toolkit program that demonstrates slicing, immutability, and at least 6 string methods — each with a correct, specific f-string label.

**Requirements (must complete all):**

- [ ] Create a variable `sentence = "  Python is a powerful programming language  "` (with leading/trailing spaces)
- [ ] Use `.strip()` to remove the spaces, store in a new variable, print with label `"Stripped:"`
- [ ] Use slicing to extract the word `"powerful"` from the stripped sentence. Print with label `"Sliced word:"`
- [ ] Use `.upper()` and `.lower()` on the stripped sentence. Print both with correct labels
- [ ] Use `.replace()` to replace `"powerful"` with `"beautiful"`. Print with label `"Replaced:"`
- [ ] Use `.split()` to split the stripped sentence into a list of words. Print the list with label `"Words list:"` and print the word count with label `"Word count:"`
- [ ] Demonstrate immutability: print the original `sentence` variable after all the above operations and confirm it has not changed. Add a comment `# immutability proof`

**Stretch (optional — only after all above are done):**
- [ ] Ask the user to input a sentence. Use `.startswith()` to check if it starts with "I" or "i". Print result with a clear f-string label.

**Rules:**
- No AI or Google during the assignment. Watch video, then close everything and code.
- Every `print()` must use an f-string with a specific label that describes what is being printed.
- The word `"powerful"` is at a known position in the stripped sentence — find the index first using `.find()` or by counting, then slice by exact index.
- Your code must run without errors before you submit.

---

## HOW TO SUBMIT

When done:
1. Save your file as: `submissions/day-03.py`
2. Come back to chat
3. Type: **"Submitting Day 3"** and paste your entire file content

The AI will check each requirement against your actual code. Not your description of it.

---

## COMMUNICATION PRACTICE (15 min)

**Today's task:** Rewrite your Day 1 self-introduction as a **professional email** to a hiring manager.

Format:
```
Subject: Application for Backend Developer Role — [Your Name]

Dear Hiring Manager,

[3–4 sentences: who you are, your background, what you're building toward, why you're a strong candidate]

[1 sentence: what you're asking for — a referral, a call, an application review]

Regards,
Mahesh Biradar
```

Rules:
- No casual language. "I am" not "I'm" in the opening.
- Be specific: mention Python, backend engineering, your transition from telecom.
- It should sound like you are writing to a real person at a real company.

Paste the email with your code submission.

---

## REVISION CHECK (2 min — answer without looking)

Topic from yesterday: **Day 2 — Operators & Expressions**

1. What is the difference between `//` and `/` in Python? What does `7 // 2` return?
2. You write `print(False and risky_function())`. Does `risky_function()` get called? What is this behaviour called, and why does it happen?

Answer in your head. If you cannot answer: re-read Day 2's concept summary before starting today's video.

---

## DAILY SUMMARY

| Slot | Content |
|------|---------|
| Video | Corey Schafer — Python Strings (~25 min) |
| Assignment | String toolkit — slicing, immutability, 6 methods |
| Communication | Rewrite self-intro as professional email |
| Revision check | 2 questions from Day 2 |
| **Total estimated time** | **~2.5 hours** |
