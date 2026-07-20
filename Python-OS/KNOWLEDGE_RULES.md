# Python-OS — Knowledge Rules

> This file is read by the Notes Update agent (Prompt 3).
> It defines how Python concepts should be organized, explained, and written in the notes/ folder.
> You never need to open this file manually.

---

## PURPOSE

The notes/ folder is your Python knowledge base.
It grows as you study.
Every note file is a living document — it gets better each time you revisit a topic.

---

## CHAPTER ORGANIZATION

Organize Python notes by concept. Never by lesson number or day.

One file per topic. Examples:

```
notes/
  Variables & Data Types.md
  Operators & Expressions.md
  Strings.md
  Control Flow & Loops.md
  Functions.md
  Lists & List Methods.md
  Tuples & Sets.md
  Dictionaries.md
  Exception Handling.md
  OOP Basics.md
  Class Variables.md
  Inheritance.md
  Decorators.md
  Context Managers.md
```

Do not create unnecessary files.
If a new concept extends an existing topic, update that file. Do not create a new one.

---

## NOTE FILE STRUCTURE

Every note file should follow this structure:

```
# [Topic Name] (Python)

## Why It Matters
- Why interviewers ask about it
- How it appears in backend / Django / APIs

## Core Concepts
- The key idea in plain English
- Small code example demonstrating one concept

## Important Syntax
[2–4 lines of the exact syntax pattern — no full programs]

## Memory Tricks
[Simple mental model or analogy if helpful]

## Interview Questions
Basic / Intermediate / Scenario-based
Star (⭐) the most frequently asked ones

## Common Mistakes
[What goes wrong most often]

## Common Confusions ⚠
[Pairs of things that get mixed up — e.g. == vs is, append vs extend]

## Real Backend Usage
[Where this appears in Django, DRF, FastAPI, or REST APIs]

## 30-Second Interview Revision
[5 bullet points — the fastest possible recall of the essential facts]
```

---

## EXPLANATION STYLE

Always explain in this order:
1. What it is
2. Why it exists
3. How to use it
4. Where it appears in backend code
5. How interviewers ask about it

Never start with syntax.
Use simple English.
Use small, minimal code examples — not full assignment programs.
Avoid documentation style.

---

## CODE EXAMPLES

Every code example should:
- Compile without error
- Be minimal (3–8 lines maximum)
- Demonstrate exactly one concept
- Avoid unnecessary complexity
- Never copy the full submission code

---

## BACKEND CONNECTION

Always connect Python concepts to backend engineering:

| Python Concept | Backend Usage |
|---|---|
| Variables | API input fields |
| Functions | Business logic |
| Dictionaries | JSON responses |
| Lists | Database query results |
| Exception Handling | API validation (HTTP 400) |
| Classes | Django Models |
| Generators | Streaming data |
| Decorators | Authentication, logging |
| Context Managers | Database connections |

Answer the implicit question: "Where will I use this in backend development?"

---

## INTERVIEW PATTERN FOCUS

For every topic, generate questions around:
- The concept itself (what is X)
- Differences (X vs Y)
- Use cases (when would you use X)
- Trade-offs (why X over Y)

Frequently tested Python pairs:
- `print` vs `return`
- `list` vs `tuple`
- `set` vs `dict`
- `is` vs `==`
- `class` vs `object`
- instance vs class variable
- `classmethod` vs `staticmethod`
- inheritance vs composition
- iterators vs generators
- mutable vs immutable

Highlight common interview traps whenever they appear.

---

## COMMON PYTHON CONFUSIONS (always watch for these)

- `input()` returns a string — always
- Mutable vs immutable defaults
- `==` (equality) vs `is` (identity)
- `append` adds one item; `extend` adds all items from iterable
- `remove` takes a value; `pop` takes an index
- `list` is mutable; `tuple` is immutable
- `print` shows output; `return` gives a value back to the caller
- `class` is the blueprint; `object` is the instance
- instance variable belongs to one object; class variable belongs to all
- `classmethod` uses `cls`; `staticmethod` uses neither `self` nor `cls`
- `try/except` catches errors; `try/finally` always runs cleanup
- `raise` throws an error; `return` gives back a value

---

## CHAPTER EVOLUTION RULES

As new Python lessons arrive, update existing chapters:

- Functions lesson → update `Functions.md`
- Lambda covered in functions lesson → update `Functions.md` (do NOT create `Lambda.md`)
- OOP Basics lesson → update `OOP Basics.md`
- Inheritance lesson → update `Inheritance.md` (or create if new topic)

Do not create unnecessary files.
Do not duplicate content that already exists.
Only add what is genuinely new or improved.

---

## QUALITY CHECKS

The notes have failed if:
- Python is explained like documentation (no practical context)
- Backend relevance is missing
- Interview traps are ignored
- Chapters duplicate the same concept
- Code examples are longer than 10 lines
- Concepts lack practical backend examples

The notes succeed when:
- The learner understands what the concept is, why it exists, where it is used
- The 30-Second Revision section gives complete recall in under 30 seconds
- Interview questions cover what interviewers actually ask
- Backend connections make the concept professionally relevant
