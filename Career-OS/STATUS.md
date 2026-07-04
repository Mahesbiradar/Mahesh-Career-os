# Career OS — STATUS
Last updated: 2026-07-04 | Day 5 REDO — repeat Loops before advancing
Current phase: Ignition (Days 1–30)
Active domain: Python — Level 1 Fundamentals
Next lesson: Day 6 (repeat) — Loops

---

## SYSTEM RULES (agent must read before generating any lesson or evaluation)

Daily flow:
  Morning  → Paste PROMPT 1 → agent generates DAY_N.md lesson file
  After work → Paste PROMPT 2 → paste your submission → agent evaluates and updates STATUS.md
  Sunday   → Paste PROMPT 3 → weekly review + next week plan

Grade system per submission:
  PASS      → concept understood, assignment correct, move to next day
  NEEDS WORK → concept understood but execution has specific gaps — listed by agent
  REDO      → fundamental misunderstanding — same topic next day before advancing

Advancement rule:
  PASS or NEEDS WORK (with understanding confirmed) → advance to next day
  REDO → repeat the same topic next day. New lesson generated for the same concept.

Theory blocks (OS, CN, DBMS):
  Start at Day 10. Built into every lesson file as a 20-min block.
  Not evaluated as code — evaluated as written explanation in submission.

Communication practice:
  Built into every lesson. 15 min. Written output expected with each submission.

---

## CURRENT POSITION

| Field | Value |
|-------|-------|
| Current Day | 6 (repeat of Loops — Day 5 REDO) |
| Current Phase | Ignition |
| Active Domain | Python |
| Current Topic | Loops (for / while) — repeat |
| Last Lesson | Day 5 — Loops |
| Last Grade | REDO |
| Last Submission File | submissions/day-05.py |

---

## DOMAIN PROGRESS TRACKER

| Domain | Phase | Status | Last Topic | Days Spent | Notes |
|--------|-------|--------|-----------|-----------|-------|
| Python | Ignition | In Progress | Loops | 5 | Day 5 REDO — Day 6 repeats Loops |
| Backend Engineering | Ignition | Not Started | — | 0 | Starts ~Day 31 |
| SQL | Core Depth | Not Started | — | 0 | Starts ~Day 45 |
| DBMS (Theory) | Parallel | Not Started | — | 0 | Starts Day 10, 20 min/day |
| OS (Theory) | Parallel | Not Started | — | 0 | Starts Day 12, 20 min/day |
| CN (Theory) | Parallel | Not Started | — | 0 | Starts Day 14, 20 min/day |
| Frontend | Build Phase | Not Started | — | 0 | Starts ~Day 76 |
| Cloud/Deployment | Build Phase | Not Started | — | 0 | Starts ~Day 100 |
| Communication | Parallel | In Progress | Professional email intro | 3 | 15 min/day built into every lesson |
| Job Preparation | Offer Mode | Not Started | — | 0 | Starts ~Day 121 |

---

## PYTHON PROGRESS — Level Tracker

Python has 5 levels. Track each topic's completion status here.

### Level 1 — Fundamentals

| Topic | Day | Grade | Notes |
|-------|-----|-------|-------|
| Variables & Data Types | 1 | PASS | f-string output, type(), input(), ValueError stretch |
| Operators & Expressions | 2 | NEEDS WORK | f-string labels inconsistent, short-circuit not proved directly, bool() not used in stretch |
| Strings | 3 | PASS | All methods correct, slicing precise, stretch completed; minor label typos (stripped/World vs Stripped/Words) |
| Control Flow | 4 | NEEDS WORK | Falsy check: used double-negation instead of `if name:`, label had extra space |
| Loops | 5 | REDO | `continue` not used at all (if-condition used instead); break print had literal `<>` around item instead of exact value; non-empty list case never created/demonstrated |
| Functions | 6 | — | Pending |
| Lists | 7 | — | Pending |
| Tuples + Sets | 8 | — | Pending |
| Dictionaries | 9 | — | Pending |
| Exception Handling | 10 | — | Pending |

### Level 2 — Intermediate (Days ~11–20)
Not started. Covers: OOP, File Handling, Modules, Comprehensions, Generators

### Level 3 — Applied Python (Days ~21–30)
Not started. Covers: Decorators, Context Managers, Standard Library, Type Hints

---

## SUBMISSION LOG

| Day | File | Topic | Grade | Date | Key Feedback |
|-----|------|-------|-------|------|-------------|
| 1 | submissions/day-01.py | Variables & Data Types | PASS | 2026-06-27 | Clean f-string output, type() correct, input() + int() conversion good |
| 2 | submissions/day-02.py | Operators & Expressions | NEEDS WORK | 2026-06-28 | f-string labels said "x-y" for all ops; short-circuit via if/else not direct proof; stretch used if/else not bool() |
| 3 | submissions/day-03.py | Strings | PASS | 2026-06-29 | All 7 requirements met, stretch completed; minor label typos; doesn't know name "short-circuit evaluation" yet |
| 4 | submissions/day-04.py | Control Flow | NEEDS WORK | 2026-06-30 | Falsy check used double-negation (`if not name != ""`) instead of `if name:`; label had extra space `"Name : "` |
| 5 | submissions/day-05.py | Loops | REDO | 2026-07-04 | `continue` requirement skipped entirely (used `if num % 2 != 0:` instead); `Found: <item>` printed literal angle brackets; only empty-list case demonstrated, non-empty list never created |

---

## WEEKLY SCORES

| Week | Days Active | Lessons Done | PASS | NEEDS WORK | REDO | Domains Touched |
|------|------------|-------------|------|-----------|------|----------------|
| 1 (Jun 22–28) | 3 | 3 | 2 | 1 | 0 | Python |
| 2 (Jun 29–Jul 5) | 2 | 2 | 0 | 1 | 1 | Python |

---

## PHASE TRACKER

| Phase | Days | Status | Focus | Target End |
|-------|------|--------|-------|-----------|
| Ignition | 1–30 | In Progress | Python fundamentals + first backend concepts | Jul 22 |
| Core Depth | 31–75 | Not Started | Django, DRF, SQL, PostgreSQL | Sep 5 |
| Build | 76–120 | Not Started | First full project (API) | Oct 20 |
| Interview Prep | 121–150 | Not Started | System design, CS theory deep-dive | Nov 19 |
| Offer Mode | 151–180 | Not Started | Mock interviews, job applications | Dec 19 |

---

## REDO QUEUE

Problems/topics that need to be redone before advancing.
(Empty = clear path forward)

| Day | Topic | Reason | Status |
|-----|-------|--------|--------|
| 5 | Loops | `continue` never used (if-condition substituted); break print had literal `<>` around item; non-empty list case never created/tested | Pending — repeat in Day 6 |

---

## NOTES FOR NEXT LESSON GENERATOR

- Day 5 was REDO — Day 6 must repeat the Loops topic, not advance to Functions. Re-teach `continue` and the empty/non-empty list truthiness check specifically.
- Carry-forward watch: `continue` was not used at all — student solved "skip evens" with `if num % 2 != 0: print(...)` instead of `if num % 2 == 0: continue` + unconditional print. Day 6 must force a scenario where `continue` is the only viable approach (e.g., skip logic placed before other required work in the loop body) so an if-only workaround doesn't satisfy it.
- Carry-forward watch: exact-output discipline — printed `Found: <6>` (literal angle brackets) instead of `Found: 6`. This is the same "extra characters in output" pattern as prior label issues (Days 2–4). Day 6 should keep hammering exact-string-match requirements.
- Carry-forward watch: student only created ONE list (empty) and skipped the non-empty case entirely, despite the requirement explicitly asking for both. Day 6 should require both branches to literally both execute and print, not just one.
- Communication: Day 5 STAR (2nd attempt) — still no STAR labels used (plain numbered paragraphs instead), still used "we" instead of "I" in the Situation line, spelling errors persist (intrviewed, alinged, im). Day 6 needs a third STAR attempt with explicit labels enforced.
- No theory block yet (starts Day 10)
