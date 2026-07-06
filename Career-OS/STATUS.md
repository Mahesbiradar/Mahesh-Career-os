# Career OS — STATUS
Last updated: 2026-07-06 | Day 7 evaluated — advancing to Day 8
Current phase: Ignition (Days 1–30)
Active domain: Python — Level 1 Fundamentals
Next lesson: Day 8 — Lists

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
| Current Day | 8 |
| Current Phase | Ignition |
| Active Domain | Python |
| Current Topic | Lists |
| Last Lesson | Day 7 — Functions |
| Last Grade | PASS (resubmit) |
| Last Submission File | submissions/day-07.py |

---

## DOMAIN PROGRESS TRACKER

| Domain | Phase | Status | Last Topic | Days Spent | Notes |
|--------|-------|--------|-----------|-----------|-------|
| Python | Ignition | In Progress | Functions | 7 | Day 7 PASS on resubmit — advancing to Lists (Day 8) |
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
| Loops (repeat) | 6 | PASS (resubmit) | Fixed `Odd` casing and stretch spacing after first evaluation; all 5 required items met cleanly |
| Functions | 7 | NEEDS WORK → PASS | First pass: `add`/`square` returned pre-formatted label strings instead of the raw value the spec required. Resubmitted twice: 1st fix corrected return values but introduced a stray `+2` and a double-space bug from `print("Sum: ", value)`; 2nd fix used `print("Sum:", value)` relying on print's own separator — exact output confirmed by running the file. All requirements + stretch met. |
| Lists | 8 | — | Pending |
| Tuples + Sets | 9 | — | Pending |
| Dictionaries | 10 | — | Pending |
| Exception Handling | 11 | — | Pending |

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
| 6 | submissions/day-06.py | Loops (repeat) | NEEDS WORK → PASS | 2026-07-04 | First pass: `odd` lowercase instead of `Odd`. Resubmitted same day with fix + stretch spacing corrected — all requirements met |
| 7 | submissions/day-07.py | Functions | NEEDS WORK → PASS | 2026-07-06 | Initial: `add`/`square` returned label-baked strings instead of raw values. Resubmit 1 fixed return values but added a stray `+2` and a double-space bug. Resubmit 2 fixed both — verified by running the file, all output exact. `greet`, `power` (defaults), `introduce` (function calling function), and stretch `total` all correct. Revision check both correct. Communication: spelling errors persist (preform, multple, unneccesary, wrtting) and casual lowercase "i". |

---

## WEEKLY SCORES

| Week | Days Active | Lessons Done | PASS | NEEDS WORK | REDO | Domains Touched |
|------|------------|-------------|------|-----------|------|----------------|
| 1 (Jun 22–28) | 3 | 3 | 2 | 1 | 0 | Python |
| 2 (Jun 29–Jul 5) | 2 | 3 | 1 | 1 | 1 | Python |
| 3 (Jul 6–12) | 1 | 1 | 1 | 0 | 0 | Python |

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
| 5 | Loops | `continue` never used (if-condition substituted); break print had literal `<>` around item; non-empty list case never created/tested | Resolved in Day 6 — all three gaps fixed |

---

## NOTES FOR NEXT LESSON GENERATOR

- Day 7 (Functions) evaluated PASS on resubmit (2026-07-06, 2 resubmits). Day 8 (Lists) is next, Level 1 Fundamentals.
- Next path: Day 8 Lists → Day 9 Tuples+Sets → Day 10 Dictionaries (DBMS theory block begins, 20 min/day) → Day 11 Exception Handling (closes out Level 1) → Day 12 OOP basics (Level 2 begins; OS theory block begins) → Day 13 OOP continued.
- RESOLVED from Day 7: return-vs-print distinction (returning raw values vs. baking a label into the return string) — fixed correctly on 2nd resubmit, output verified by actually running the file. Keep a light watch only; no need to re-test directly.
- RESOLVED from Day 5/6: `continue`, non-empty list case, exact-output casing all now consistently correct.
- Standing carry-forward watch: exact-output string discipline (labels/spacing/casing) is now solid — Day 7's `greet`, `power`, `introduce` all hit exact formats on the first attempt with no resubmit needed. This concern can be considered resolved; keep a light watch only.
- Communication: STAR/'"I"-voice structure is fine, but spelling errors persist and got worse this round: "preform" (perform), "multple" (multiple), "unneccesary" (unnecessary), "wrtting" (writing), "diffrence" (difference), "curremt" (current), "immedeatly" (immediately), "taks" (task), "warapped" (wrapped), plus casual lowercase "i'd" instead of "I'd". Day 8 communication task should explicitly ask for a proofread pass before submitting, and keep prompts short enough that spelling errors are easy to self-catch.
- Theory block starts Day 10 (DBMS), Day 12 (OS), Day 14 (CN) — not yet active.
