# Career OS — STATUS
Last updated: 2026-07-04 | Day 6 PASS (resubmit) — advancing to Day 7
Current phase: Ignition (Days 1–30)
Active domain: Python — Level 1 Fundamentals
Next lesson: Day 7 — Functions

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
| Current Day | 7 |
| Current Phase | Ignition |
| Active Domain | Python |
| Current Topic | Functions |
| Last Lesson | Day 6 — Loops (repeat) |
| Last Grade | PASS (resubmit) |
| Last Submission File | submissions/day-06.py |

---

## DOMAIN PROGRESS TRACKER

| Domain | Phase | Status | Last Topic | Days Spent | Notes |
|--------|-------|--------|-----------|-----------|-------|
| Python | Ignition | In Progress | Loops | 6 | Day 6 PASS on resubmit — advancing to Functions (Day 7) |
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
| Functions | 7 | — | Pending |
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
| 6 | submissions/day-06.py | Loops (repeat) | NEEDS WORK → PASS | 2026-07-04 | First pass: `odd` lowercase instead of `Odd`. Resubmitted same day with fix + stretch spacing corrected — all requirements met |

---

## WEEKLY SCORES

| Week | Days Active | Lessons Done | PASS | NEEDS WORK | REDO | Domains Touched |
|------|------------|-------------|------|-----------|------|----------------|
| 1 (Jun 22–28) | 3 | 3 | 2 | 1 | 0 | Python |
| 2 (Jun 29–Jul 5) | 3 | 3 | 1 | 0 | 1 | Python |

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

- Day 6 (repeat of Loops) is PASS on resubmit — advance to Day 7 (Functions), do not repeat Loops again.
- RESOLVED from Day 5: `continue` now used correctly (skip-check + unconditional print, no if-wrapper substitute); both empty and non-empty list truthiness cases created and printed.
- Carry-forward watch: exact-output discipline took two tries this time — first submission printed `odd: {num}` in lowercase when the spec explicitly wrote `print(f"Odd: {num}")` with capital O; fixed within the same day on resubmit. Days 2–6 have now all had some form of "printed text doesn't literally match the required string" (labels, angle brackets, casing). Day 7 should still test an exact-string requirement to confirm this is now caught on the FIRST attempt, not just on correction.
- Stretch (Day 6): multiplication table's spacing was fixed on resubmit (`4 x 3 = 12`); still uses an `if i % 2 == 0` filter to pick two numbers rather than directly choosing two variables — worked but convoluted, not worth flagging further since stretch is optional and output was correct.
- Communication: Day 6 STAR (3rd attempt) — RESOLVED: explicit Situation/Task/Action/Result labels used for the first time, and "I" used consistently instead of "we". Spelling errors persist though: "taks" (task), "thorough" instead of "through", "actuall" (actual), "which which" (duplicate word), "issue's" (should be "issues"). Day 7 communication practice should keep the labeled format (now working) and add a proofread-before-submit step to target spelling specifically.
- No theory block yet (starts Day 10)
