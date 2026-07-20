# Day 7 — Functions (Basics) — Python Level 1
Phase: Ignition
Estimated time: ~1.5 hours (20 min video + 45 min assignment + 15 min communication + 2 min revision check)

---

## TODAY'S VIDEO

| Field | Detail |
|-------|--------|
| Instructor | Corey Schafer |
| Platform | YouTube |
| Course | Python Tutorial for Beginners (series) |
| Section/Video | Python Tutorial for Beginners 8: Functions |
| Duration | ~15–20 min (approx) |
| Link | https://youtu.be/9Os0o3wzS_I |

What to focus on while watching:
- The difference between a function that `print()`s something and a function that `return`s something — notice what happens if you try to use the result of a function that only prints
- How default parameter values work: `def power(base, exponent=2):` — what happens when you call it with one argument vs two
- How a function can call another function inside its own body
- The exact wording of any f-string examples shown — same character-for-character rule applies inside functions too

---

## CONCEPT SUMMARY (read AFTER video, not before)

A function is defined with `def name(parameters):` and a body. The body can `print()` something, but that is NOT the same as `return`ing something — if a function only prints and you try to do `result = my_function()`, `result` will be `None`, because nothing was returned. Use `return` when you need the value usable outside the function; use `print()` only when you want to display something on screen.

Parameters can have default values, e.g. `def power(base, exponent=2):`. If the caller writes `power(3)`, `exponent` falls back to `2`. If the caller writes `power(3, 4)`, the default is overridden. The default is only used when that argument is omitted.

Functions can call other functions — this is completely normal. A function's body is just code, so it can include a call to a function you already defined above it. This is how larger programs are built in layers instead of one giant block.

Exact-output discipline still applies here: an f-string inside a function is no different from one anywhere else — the label, spacing, and casing all matter character-for-character.

---

## TODAY'S ASSIGNMENT

Goal: Demonstrate function definitions with `return`, default parameters, and functions calling other functions — with exact output formatting.

Requirements (must complete all):
- [ ] Define a function `greet(name)` that RETURNS (does not print inside the function) the string `f"Hello, {name}!"`. Call it once with your own name and print the returned value — output must be exactly `Hello, Mahesh!` (use your own name in place of Mahesh).
- [ ] Define a function `add(a, b)` that returns the sum of the two arguments. Call it twice with two different number pairs and print each result using the exact format `Sum: 8` (label, colon, space, then the result — nothing else).
- [ ] Define a function `power(base, exponent=2)` with a default value for `exponent`. Call it once passing only `base` (relying on the default) and once passing both `base` and a different `exponent`. Print both results using the exact format `Result: 9`.
- [ ] Define a function `square(n)` that returns `n * n`. The function body itself must NOT contain a `print()` statement — only `return`. Call `square()` on a number and print the returned value using the exact format `Square: 16`.
- [ ] Define a function `introduce(name, age)` that calls your `greet(name)` function from requirement 1 inside its own body, then also prints the age using the exact format `Age: 24`. Call `introduce()` once. This must demonstrate one function calling another — do not just copy the greet logic again inline.

Stretch (optional — do only after main requirements done):
- [ ] Define a function `total(*args)` that returns the sum of any number of arguments passed to it. Call it with 4 numbers and print the result using the exact format `Total: 30`.

Rules:
- No Googling or AI during the assignment. Watch video first. Then close everything and code.
- Test your code before submitting. It must run without errors.

---

## HOW TO SUBMIT

When done:
1. Save your file as: submissions/day-07.py
2. Come back to the AI chat
3. Type: "Submitting Day 7" and paste your entire file content

The AI will evaluate your actual code/writing. Not your description of it.

---

## COMMUNICATION PRACTICE (15 min)

STAR labels and "I"-voice are working now (Day 6) — today's task is different: explain a technical concept out loud/in writing, the way you'd do it in an actual interview.

Task: Explain "functions" as if an interviewer just asked: *"Can you explain what a function is and why we use them?"*

Write a short explanation (4–6 sentences) covering:
- What a function is, in your own words
- Why you'd use one instead of repeating code
- One concrete example from today's assignment (e.g., `greet`, `add`, or `power`)

Keep it professional in tone, use "I" where relevant (e.g., "I'd use a function when..."), and proofread before submitting — check spelling carefully since that's been the recurring issue in your last few submissions.

Save output as: communication/day-7_comm.md (optional)
Paste it with your code submission for evaluation.

---

## REVISION CHECK (answer these without looking — 2 min)

1. What is the actual difference between using `continue` inside a loop and wrapping the rest of your loop body in an `if` condition to skip an item?
2. If a spec requires the exact output `Result: 9`, what's wrong with writing `Result:9` (no space) or `result: 9` (lowercase r)?

(Answer in your head. If you cannot answer: re-read yesterday's concept summary before starting today's video.)

---

*Next lesson: Day 8 — Lists (only after Day 7 passes)*
