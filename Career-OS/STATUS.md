# Career OS — STATUS
Last updated: 2026-07-18 | Day 15 PASS, ready for Day 16
Current phase: Ignition (Days 1–30)
Active domain: Python — Level 2 Intermediate
Next lesson: Day 16 — next mapped Python topic after Inheritance

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
| Current Day | 15 |
| Current Phase | Ignition |
| Active Domain | Python |
| Current Topic | Inheritance |
| Last Lesson | Day 15 — Inheritance |
| Last Grade | PASS |
| Last Submission File | submissions/day-15.py |

---

## DOMAIN PROGRESS TRACKER

| Domain | Phase | Status | Last Topic | Days Spent | Notes |
| Domain | Phase | Status | Last Topic | Days Spent | Notes |
|--------|-------|--------|-----------|-----------|-------|
| Python | Ignition | In Progress | Inheritance | 15 | Day 15 inheritance submission passed: `Person`, `Employee`, `super()`, overridden `info()`, two employee objects, and two exact print lines were all demonstrated. |
| Backend Engineering | Ignition | Not Started | — | 0 | Starts ~Day 31 |
| SQL | Core Depth | Not Started | — | 0 | Starts ~Day 45 |
| DBMS (Theory) | Parallel | In Progress | ER Modeling | 2 | Day 11 ER modeling submitted: entity, attribute, and relationship concepts present; proofreading/spelling still need polish |
| OS (Theory) | Parallel | In Progress | Process States & Schedulers | 2 | Day 13 OS explanation covered new, ready, running, waiting/blocked, terminated, and scheduler roles; next time correct medium-term scheduler wording and continue proofreading. |
| CN (Theory) | Parallel | In Progress | What is a Network + OSI Model intro | 1 | Day 14 CN explanation covered networks, protocols, layered design, and the OSI model as seven stages of network communication. |
| Frontend | Build Phase | Not Started | — | 0 | Starts ~Day 76 |
| Cloud/Deployment | Build Phase | Not Started | — | 0 | Starts ~Day 100 |
| Communication | Parallel | In Progress | classmethod vs staticmethod explanation | 9 | Day 14 answer had the correct basic idea, but needs 6 polished sentences and proofreading; Day 15 communication is clearer but still needs polish. |
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
| Lists | 8 | PASS | All 5 requirements + stretch met on first attempt: append/insert/remove/enumerate all correct, sort+slice stretch correct, no errors |
| Tuples + Sets | 9 | PASS | All 5 requirements + stretch met: tuple creation/unpacking correct, set overlap/intersection/union/difference correct by inspection; Python launcher unavailable in shell |
| Dictionaries | 10 | PASS (resubmit) | Initial submission had two f-string quote syntax errors; corrected to use single quotes inside f-string expressions. All required dictionary operations + stretch met by inspection. |
| Exception Handling | 11 | PASS | All required exception-handling pieces present by inspection: exact raw score list, `ValueError` handling, `else`, `finally`, collected valid/skipped data, and average output. Optional stretch attempted but not fully polished. |

### Level 2 — Intermediate (Days ~12–20)

| Topic | Day | Grade | Notes |
|-------|-----|-------|-------|
| OOP Basics | 12 | NEEDS WORK → PASS | Initial submission missed the exact second role label; resubmit fixed it to `Employee 2 role still:`. All required OOP pieces met by inspection: `Employee`, `__init__`, instance attributes, `full_name`, `annual_salary`, two objects, role update, and optional raise method. |
| Class Variables | 13 | PASS | All 5 requirements met by inspection: class variables, employee counter, instance attributes, `full_name`, `apply_raise` with `self.raise_amount`, two objects, exact output labels, employee-specific override, and stretch third employee. |
| classmethods & staticmethods | 14 | NEEDS WORK | Resubmission fixed the workday-print syntax error. Core concept is still understood, but the checklist still fails because the exact required output label `Raise amount:` is not printed as written. |
| Inheritance | 15 | PASS | All required inheritance pieces met by inspection: `Person`, `Employee`, `super()`, override `info()`, two employees, and two exact print lines. |

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
| 8 | submissions/day-08.py | Lists | PASS | 2026-07-07 | First attempt clean: append/insert/remove/enumerate all correct with exact labels; stretch sort+slice correct too. Revision check both correct (concept accurate despite typos). Self-intro had no spelling errors this time (improvement), but revision-check answers still had typos (returing, interget, prameter, defualt) and casual lowercase "i"/sentence fragments recur. |
| 9 | submissions/day-09.py | Tuples + Sets | PASS | 2026-07-08 | All required tuple/set items met, plus stretch difference operation. Revision check both correct. Communication concept clear, but grammar/spelling still need polish (`an ordered`, `parentheses`, `Therefore`, spacing after commas). |
| 10 | submissions/day-10.py | Dictionaries | NEEDS WORK → PASS | 2026-07-10 | Initial: two f-strings used nested double quotes, causing syntax errors. Resubmit fixed quote usage; create/read/update/delete/get/items and stretch scores all met by inspection. Revision check correct. Communication and DBMS theory were conceptually clear, but proofreading issues persist. |
| 11 | submissions/day-11.py | Exception Handling | PASS | 2026-07-11 | All required `try`/`except ValueError`/`else`/`finally` items met by inspection; valid/skipped lists and average printed. Revision check correct. Communication and ER theory were conceptually clear, but sentence polish/spelling still need work. |
| 12 | submissions/day-12.py | OOP Basics | NEEDS WORK → PASS | 2026-07-13 | Initial: exact label missed (`Updated Employee 2 role:` instead of `Employee 2 role still:`). Resubmit fixed the label; all required OOP items met by inspection. Revision check correct. Communication and OS theory were conceptually clear, but proofreading and own-words-only theory discipline need work. |
| 13 | submissions/day-13.py | Class Variables | PASS | 2026-07-14 | All required class-variable items met by inspection, including shared employee count, object-level raise override, exact output labels, and stretch third employee. Revision check correct. Communication needs proofreading; OS theory mostly correct but medium-term scheduler wording needs correction. |
| 14 | submissions/day-14.py | classmethods & staticmethods | NEEDS WORK | 2026-07-16 | Resubmission fixed the Monday/Sunday syntax error. `set_raise_amount`, `from_string`, `is_workday`, and stretch `from_csv` are present, but the exact required label `Raise amount:` is still missing, so the checklist is not fully met. Revision and CN theory are correct; communication still needs 6 polished sentences and proofreading. |
| 15 | submissions/day-15.py | Inheritance | PASS | 2026-07-18 | All required inheritance pieces present; no code logic issues. Theory block needs factual correction and communication needs proofreading. |

---

## WEEKLY SCORES

| Week | Days Active | Lessons Done | PASS | NEEDS WORK | REDO | Domains Touched |
|------|------------|-------------|------|-----------|------|----------------|
| 1 (Jun 22–28) | 3 | 3 | 2 | 1 | 0 | Python |
| 2 (Jun 29–Jul 5) | 2 | 3 | 1 | 1 | 1 | Python |
| 3 (Jul 6–12) | 5 | 5 | 5 | 0 | 0 | Python, DBMS, Communication |
| 4 (Jul 13–19) | 5 | 5 | 3 | 2 | 0 | Python, OS, CN, Communication |

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

- Day 15 inheritance submission passed; advance to Day 16.
- Day 16 should cover the next mapped Python topic after Inheritance.
- Carry-forward watch: exact output labels remain important; keep communication/proofreading polished.
- Theory next: continue CN with the mapped resource, but correct factual names (`ISO`/`DARPA/ARPANET`) in future written explanations.
- Communication: Day 14 classmethod/staticmethod answer had the right idea, but needs 6 complete polished sentences, exact terms (`classmethod`, `staticmethod`, `cls`, `self`, `object`), and proofreading.
- REDO watch: no topic has 2+ REDO attempts; no DOMAIN PROGRESS TRACKER flag needed.
