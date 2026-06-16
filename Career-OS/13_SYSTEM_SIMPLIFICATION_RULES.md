# Mahesh Career OS — System Simplification Rules

> **File:** `13_SYSTEM_SIMPLIFICATION_RULES.md`
> **Version:** 1.0
> **Depends On:** `12_MASTERY_FRAMEWORK.md` (all standards remain fully enforced)
> **Purpose:** Define how the Mastery Framework operates in daily practice with minimum administrative overhead.
> **Guarantee:** This file reduces friction. It does not reduce standards. Every mastery rule, evaluation threshold, and completion requirement in `12_MASTERY_FRAMEWORK.md` remains 100% in effect.

---

## The Operating Principle

The Mastery Framework defines what mastery means.
This file defines who does what to achieve it.

**The division is simple:**

| Responsibility | Owner |
|----------------|-------|
| Learning new topics | Mahesh |
| Writing and implementing | Mahesh |
| Attempting evaluations | Mahesh |
| Pushing evidence to GitHub | Mahesh |
| Filling the daily log (5 lines) | Mahesh |
| Generating plans | AI |
| Scoring evaluations | AI |
| Tracking mastery levels | AI |
| Computing DRS and CRS | AI |
| Scheduling revisions | AI |
| Detecting bottlenecks | AI |
| Flagging regressions | AI |
| Running the weekly review | AI |
| Generating next week's plan | AI |

**Mahesh's daily admin ceiling: 10 minutes.**
**Mahesh's weekly review ceiling: 30 minutes.**
Everything beyond that ceiling is AI's job.

---

## Section 1 — Role Division

### 1.1 What Mahesh Does (and Only Mahesh)

1. **Studies** — reads syllabus topics, watches explanations, takes mental notes.
2. **Implements** — writes code, queries, configurations from scratch.
3. **Answers evaluation questions** — responds to AI-generated questions honestly.
4. **Pushes evidence** — commits to GitHub or writes a one-paragraph note.
5. **Fills the 5-line daily log** — takes ≤ 2 minutes.
6. **Sends standard prompts to AI** — copy-paste prompts from Section 4.

Mahesh does NOT:
- Compute TMS scores
- Track revision schedules
- Calculate CADI or CRS
- Generate study plans
- Identify which topic comes next
- Maintain spreadsheets or progress trackers
- Write the Framework-format full session log (AI generates this from the 5-line input)

---

### 1.2 What AI Does (Every Session)

When Mahesh sends a session log prompt, the AI must:

1. Parse the 5-line log.
2. Expand it into the full Framework session log format (Section 6.1 of the Mastery Framework).
3. Score all 6 evaluation dimensions based on the session context and any evaluation responses.
4. Apply Topic Completion Rules (TC-1 through TC-6).
5. Update the mastery level.
6. Check ADS trend (Rules ADS-1 through ADS-4).
7. Flag any interventions triggered (Section 7.3 of the Mastery Framework).
8. Identify the next topic in the syllabus sequence.
9. Check the revision schedule and surface any topics due for revision.
10. Output the next-day plan in the standard format (Section 3.3 of this file).

The AI does this automatically from the 5-line input. Mahesh does not need to request each of these steps individually.

---

## Section 2 — Daily Workflow

> Total daily admin: ≤ 10 minutes. Study and implementation: ~5 hours 50 minutes.

---

### 2.1 The Full Day in Four Blocks

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOCK 0 — MORNING STARTUP          [ 5 min ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Read today's AI-generated plan.  [ 2 min ]
2. Open syllabus file for today's   [ 1 min ]
   topic.
3. Open a blank code file or notes  [ 1 min ]
   file. Nothing else.
4. Start the timer.                 [ 0 min ]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOCK 1 — STUDY BLOCK              [ ~3 hr ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Read. Take notes mentally.
Attempt to explain to yourself.
Begin implementation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOCK 2 — IMPLEMENTATION BLOCK    [ ~2 hr ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mini-task or integration exercise.
No AI for writing code.
Official docs only.
Commit to GitHub when done.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOCK 3 — REVISION BLOCK          [ 30 min ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI surfaces today's revision due.
Quick recall check or mini re-attempt.
≤ 2 topics per day.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOCK 4 — END-OF-DAY ADMIN        [ 5 min ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fill in 5-line daily log.           [ 2 min ]
Push evidence (commit or note).     [ 1 min ]
Send "Process Session" prompt.      [ 30 sec ]
Read AI feedback.                   [ 90 sec ]
Done.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 2.2 The Non-Negotiable Rules of the Day

**Rule D-1: Block 0 must happen before Block 1.**
Never open Reddit, YouTube, or social media before starting Block 1. Read the plan first. Then study.

**Rule D-2: Block 2 is AI-free for implementation.**
AI may be used before Block 2 for conceptual understanding. During implementation in Block 2, AI is off. Only official documentation (Django docs, MDN, Python docs) is permitted.

**Rule D-3: Evidence before the log.**
The GitHub commit or written note must exist before the 5-line log is filled in. Evidence is not optional — see Section 6.

**Rule D-4: The log is always filed, even on partial days.**
A 2-hour study day still requires a log. A day with only reading (no implementation) still requires a log. The log is never skipped.

**Rule D-5: If today's plan does not match what was actually studied, update the log to reflect reality.**
The log records what happened — not what was planned. Honesty in the log is the foundation of the entire system.

---

## Section 3 — Standard Templates

### 3.1 The 5-Line Daily Log (Mahesh fills this)

```
TOPIC:       [Exact topic name from syllabus, e.g., "Python Decorators — Level 5.1"]
BUILT:       [One sentence: what I implemented or practiced today]
ADS:         [0 / 1 / 2 / 3 / 4]
BLOCKER:     [None — OR — one sentence describing what stopped progress]
LEVEL GUESS: [ML-0 / ML-1 / ML-2 / ML-3 / ML-4 / ML-5]
```

**Examples of correctly filled logs:**

```
TOPIC:       Django ORM — Tier 4 — T4.5 — select_related
BUILT:       Rewrote a BlogPost list view, eliminating N+1 using select_related
ADS:         1
BLOCKER:     None
LEVEL GUESS: ML-4
```

```
TOPIC:       SQL Window Functions — Level 7.2 — Ranking Functions
BUILT:       Wrote ROW_NUMBER + RANK + DENSE_RANK queries on employee salary data
ADS:         2
BLOCKER:     Confused about PARTITION BY with multiple ORDER BY columns
LEVEL GUESS: ML-3
```

```
TOPIC:       OS — Deadlocks — Section 6.3 — Deadlock Handling Strategies
BUILT:       Written explanation of all four strategies with examples
ADS:         0
BLOCKER:     None
LEVEL GUESS: ML-4
```

That is the entire daily administrative input. Nothing more.

---

### 3.2 AI-Expanded Log (AI generates this from the 5-line input)

When the AI receives the 5-line log, it generates the full Framework log (Section 6.1 of `12_MASTERY_FRAMEWORK.md`) automatically:

```
DATE: [AI fills from session timestamp or asks if unclear]
DOMAIN: [AI infers from topic name]
TOPIC: [from log]
SYLLABUS_REFERENCE: [AI infers from topic name + domain]
STUDY_DURATION_MINUTES: [AI estimates from log content; can ask Mahesh]
PRIOR_MASTERY_LEVEL: [AI retrieves from previous session record]

WHAT WAS DONE:
[AI infers from BUILT field]

AI DEPENDENCY SCORE: [from log ADS field]
AI USAGE DESCRIPTION: [AI infers from ADS level + BLOCKER field]

EVALUATION RESULTS:
[AI scores based on BUILT + LEVEL GUESS + any evaluation responses if evaluation was run]

NEW MASTERY LEVEL: [AI determines based on all inputs]
TOPIC STATUS: [AI determines based on TC rules]

BLOCKERS: [from log BLOCKER field]
TOMORROW'S FOCUS: [AI generates based on syllabus sequence + revision schedule]
```

Mahesh never writes this format. The AI always writes it.

---

### 3.3 AI-Generated Daily Plan (format Mahesh receives each morning)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TODAY'S PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIMARY TOPIC (Block 1 + 2):
  Domain:    [domain name]
  Topic:     [exact topic from syllabus]
  Syllabus:  [file + section reference]
  Your Level: [current ML]
  Target Today: [ML-X → ML-Y]
  Mini-Task:  [specific task to implement]

REVISION DUE TODAY (Block 3):
  Topic 1:   [topic + quick check type]
  Topic 2:   [topic + quick check type]   ← may be empty

SECONDARY (if primary finishes early):
  Domain:    [domain name]
  Topic:     [topic name]

FLAGS:
  [Any interventions, bottlenecks, or urgent actions from yesterday's log]

CRS ESTIMATE (last computed):
  [X]% — [Employment Status]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

This plan is read in 2 minutes. Everything is decided by AI. Mahesh reads and executes.

---

### 3.4 Weekly Review Output (AI generates, Mahesh reads + confirms)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK [N] REVIEW REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOPICS COMPLETED THIS WEEK:    [N] (Target: ≥ 5)
TOPICS REGRESSED:              [N] (Target: 0)
EVALUATION PASS RATE:          [X]% (Target: ≥ 70%)
AVG ADS ACROSS ALL SESSIONS:   [X.X] (Target: ≤ 2.0)

CAREER READINESS SCORE:        [X]% → [Employment Status]
LAST WEEK CRS:                 [X]%
DELTA:                         +/- [X]%

DOMAIN HEALTH:
  Python             [DRS%]  [Green/Yellow/Red]
  Backend Eng.       [DRS%]  [Green/Yellow/Red]
  SQL                [DRS%]  [Green/Yellow/Red]
  DBMS               [DRS%]  [Green/Yellow/Red]
  Operating Systems  [DRS%]  [Green/Yellow/Red]
  Computer Networks  [DRS%]  [Green/Yellow/Red]
  Frontend           [DRS%]  [Green/Yellow/Red]
  Cloud & Deployment [DRS%]  [Green/Yellow/Red]
  Communication      [DRS%]  [Green/Yellow/Red]
  Job Preparation    [DRS%]  [Green/Yellow/Red]

HARD CONSTRAINTS:
  Python ≥ 60%?        [YES/NO]
  Backend ≥ 60%?       [YES/NO]
  SQL ≥ 55%?           [YES/NO]
  Communication ≥ 60%? [YES/NO]

INTERVENTIONS TRIGGERED:
  [List any from Section 7.3 of Mastery Framework, or NONE]

REGRESSED TOPICS:
  [List with root cause, or NONE]

STRUGGLING TOPICS:
  [List any topics stuck at ML-3 for > 14 days, or NONE]

THIS WEEK'S CONSOLIDATION TASK:
  [One 20-minute exercise to confirm this week's most important topic]
  Instructions: [specific]
  Evidence required: [GitHub commit / written explanation]

NEXT WEEK PLAN:
  Core Track:      [Python topic + Backend topic]
  Support Track:   [SQL/DBMS/OS/CN topic]
  Practical Track: [Frontend or Cloud topic]
  Career Track:    [Communication or Job Prep topic]
  Priority Revisions: [list, max 5]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Mahesh reads this report (5 minutes), completes the Consolidation Task (20 minutes), and confirms or adjusts the next week's plan (5 minutes).

Total weekly review time: 30 minutes.

---

## Section 4 — AI Prompt Library

> These are the exact prompts Mahesh sends to AI. Copy-paste. No customization needed beyond the bracketed fields.

---

### PROMPT 1 — Morning Plan Request

Used: Every morning before studying.

```
Generate today's study plan.

My last session log:
[paste yesterday's 5-line log]

My current status:
- Available hours today: 6
- Any topics I want to prioritize: [optional — leave blank if none]

Use 12_MASTERY_FRAMEWORK.md and the relevant syllabus files.
Output in the daily plan format from 13_SYSTEM_SIMPLIFICATION_RULES.md Section 3.3.
```

---

### PROMPT 2 — Session Log Submission

Used: End of every study day.

```
Process my session.

[paste 5-line log]

If I attempted any evaluation questions today, my answers were:
[paste answers, or write NONE if no evaluation was run today]

Evidence link: [GitHub commit URL, or "Written note saved locally"]

Output:
1. Full expanded session log
2. Updated mastery level with reason
3. Topic completion status
4. ADS trend flag (if any)
5. Any intervention triggered
6. Tomorrow's plan
```

---

### PROMPT 3 — Evaluation Request

Used: When Mahesh wants to test readiness for a topic's Complete status.

```
Evaluate me on: [exact topic name + syllabus reference]
My current estimate: ML-[X]
ADS on my last session for this topic: [0-4]

Run the full evaluation sequence from 12_MASTERY_FRAMEWORK.md Appendix B.
Ask me one question at a time. Wait for my answer before asking the next.
Score all 6 dimensions at the end.
Tell me if the topic is Complete or what I need to fix.
```

---

### PROMPT 4 — Weekly Review Request

Used: At the end of every week.

```
Run my weekly review.

My session logs for this week:
[paste all 5-line logs from the week, one per line block]

Evidence submitted this week:
[GitHub repo URL or "Notes file updated"]

Output the full weekly review report from 13_SYSTEM_SIMPLIFICATION_RULES.md Section 3.4.
Then give me next week's plan.
```

---

### PROMPT 5 — Stuck Escalation

Used: When the same topic has been attempted 3+ times without reaching ML-4.

```
I am stuck on: [topic name + syllabus reference]
Number of sessions attempted: [N]
ADS across those sessions: [list, e.g., 3, 3, 2]
What I can do: [one sentence]
What I cannot do: [one sentence]

Diagnose why I'm stuck using the Struggling Topic Protocol
(Rule AL-2 in 12_MASTERY_FRAMEWORK.md).
Break this topic into sub-components and give me a structured drill plan.
Do NOT give me the answer or write the code.
```

---

### PROMPT 6 — Revision Check

Used: When AI flags a topic for scheduled revision.

```
Run a revision check on: [topic name]
Time since last evaluation: [X days]
My current mastery level: ML-[X]

Use the appropriate revision type from 12_MASTERY_FRAMEWORK.md Section 9.1.
Ask the questions one at a time. Assess whether the topic holds at ML-[X] or has decayed.
```

---

### PROMPT 7 — Full System Status

Used: Any time Mahesh wants to see the complete picture.

```
Give me a full system status.

My session logs to date:
[paste all logs since last full status, or describe current state]

Compute:
1. DRS for each domain
2. CRS
3. Hard Constraint status
4. Employment Status
5. Top 3 priorities to move the CRS
6. Any domain at Yellow or Red health
```

---

### PROMPT 8 — Evaluation on Multiple Topics (Quick)

Used: For revision sessions where depth is less critical than breadth.

```
Quick revision evaluation on these 3 topics:
1. [topic]
2. [topic]
3. [topic]

For each topic, ask 2 questions only (one Definition, one Implementation or Tradeoff).
Score each as PASS / NEEDS WORK / FAIL.
Tell me which topics need full re-study.
```

---

## Section 5 — Simplified Daily Evaluation

> The Mastery Framework defines a 5-question daily evaluation (Section 6.2). This section defines when the full evaluation runs vs. the lightweight daily version.

---

### 5.1 Two Modes of Evaluation

| Mode | When | Duration | Who Triggers |
|------|------|----------|-------------|
| **Quick Self-Check** | End of every study session | 2 minutes | Always — automatic |
| **Full Evaluation** | When claiming Complete status OR when AI flags for re-evaluation | 20-30 minutes | Mahesh uses PROMPT 3 |

---

### 5.2 The Quick Self-Check (2 minutes, daily)

After every study session, Mahesh answers ONE question:

> **"Right now, without AI, without notes: can I explain this topic clearly AND implement its core from scratch?"**

| Answer | What to Log | What Happens |
|--------|-------------|-------------|
| **Yes, both** | ADS + Level Guess as-is | Topic stays on track |
| **Explain yes, implement no** | Downgrade Level Guess by 1 | Tomorrow: more implementation, less reading |
| **Neither** | Set Level Guess to ML-2 or lower | Topic flagged; AI adjusts tomorrow's plan |

This check is not scored. It is a calibration check. It keeps Mahesh honest about actual capability vs. familiarity.

**One rule applies:** If Mahesh answers "yes, both" three days in a row for the same topic, the Full Evaluation must be triggered. The self-check cannot replace evaluation forever.

---

### 5.3 When Full Evaluation Is Mandatory

Full Evaluation (PROMPT 3) is required before any of these events:

1. Marking a topic as Complete
2. Using a topic as a prerequisite for a new topic (if the topic has not been evaluated in > 14 days)
3. After any regression is detected by the AI
4. After 3 consecutive "yes, both" self-checks on the same topic
5. As part of the weekly Consolidation Task (Section 3.4)

Full Evaluation is NOT required:
- Every single day
- Before starting a new topic (only before marking the current one Complete)
- During revision sessions where Prompt 8 (Quick revision) is used

---

### 5.4 Honest Calibration Rule

The Quick Self-Check only works if it is honest. The entire system collapses if Mahesh says "yes, both" when the true answer is "no."

The safeguard: **the Full Evaluation acts as the truth teller.** If the Quick Self-Check has been "yes, both" but the Full Evaluation scores ML-3 or lower, the AI flags this as an overconfidence event (Rule AL-6 of the Mastery Framework) and adjusts the CADI ceiling for that domain for that week.

This means: inflated self-checks do not damage the system permanently. They are caught and corrected at evaluation time. But consistent inflation over time will cause the system to distrust self-reports, which slows everything down. Honesty is the faster path.

---

## Section 6 — Evidence Requirements

> Simplified from the Mastery Framework's Rule FI-4. Same standard, minimum format.

---

### 6.1 Evidence Is Mandatory for Completion

No topic can be marked Complete without an evidence artifact. This is non-negotiable.

### 6.2 Accepted Evidence Formats

| Topic Type | Required Evidence | Takes How Long |
|------------|------------------|----------------|
| Code implementation topic | GitHub commit in a public or private repo | 30 seconds to commit and push |
| Theory-only topic (OS, DBMS, CN, DBMS) | One paragraph written explanation saved in a notes file | 2–3 minutes to write |
| Communication topic | Recorded audio (any format) or written STAR answer | 5 minutes to record or write |
| Job Preparation topic | The deliverable itself (resume draft, LinkedIn update, etc.) | Varies |

### 6.3 Evidence Format Rules

**For code evidence:**
- Commit message must name the topic: `"feat: python decorators mini-task — timing decorator"`
- Code must be original (not AI-generated)
- No specific folder structure required
- Does NOT need to be a polished project — a single file is fine

**For written evidence:**
- Must be in Mahesh's own words
- One paragraph minimum (3-5 sentences)
- Saved anywhere (Notion, Google Docs, a `.md` file in the repo, a text file)
- Does NOT need to be formatted or structured

**What does NOT count as evidence:**
- A screenshot of AI-generated output
- A file with code that Mahesh copied and did not understand
- "I understand it" without any artifact
- A link to a tutorial that covers the topic

### 6.4 Evidence Submission

When submitting a session log (PROMPT 2), Mahesh includes one of:
- GitHub commit URL
- "Written note saved in [location]"

The AI does not verify the evidence exists. The system operates on trust. Rule FI-1 (No Self-Certification) applies — the evidence requirement exists to create a habit of producing artifacts, not to create a bureaucratic audit trail.

---

## Section 7 — Time Budget Rules

> Governing how 6 daily study hours are allocated. AI uses these rules when generating daily plans.

---

### 7.1 Daily Time Allocation

```
Total available: 6 hours (360 minutes)
Admin (Blocks 0 + 4): 10 minutes
Net study time: 350 minutes

ALLOCATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Activity                    | Target Time
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
New topic study (Block 1)   | 90 minutes
Implementation (Block 2)    | 120 minutes
Revision (Block 3)          | 30 minutes
Evaluation (if triggered)   | 30 minutes
Buffer / catch-up           | 80 minutes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total                       | 350 minutes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 7.2 Allocation Rules for AI Planners

When the AI generates a daily plan, it must follow these time budget rules:

**Rule TB-1:** Implementation time must always be ≥ study time. Reading without building is not learning.

**Rule TB-2:** Revision block cannot be zero unless this is the first week of study and no topics have been completed yet.

**Rule TB-3:** A single topic should not consume more than 150 minutes in one day unless it is explicitly a "deep-dive day" (triggered by a Struggling Topic Protocol).

**Rule TB-4:** No more than 2 domains per day. Switching between 3+ domains in one day creates fragmented sessions with no depth.

**Rule TB-5:** The Primary Topic receives the largest single block (Block 1 + Block 2 = 210 min combined). All other activities fit around it.

**Rule TB-6:** The buffer (80 min) is not free time — it is flexible time. AI assigns it to: extra implementation if going well, or extra study if the topic is difficult. If neither applies, it goes to the Secondary topic or a revision.

---

### 7.3 Weekly Time Allocation (Domain Tracks)

AI uses these ratios when building the weekly plan:

| Track | Domains | Weekly Hours Target |
|-------|---------|-------------------|
| Core Track | Python, Backend Engineering | 16–18 hours |
| Support Track | SQL, DBMS, OS, CN | 8–10 hours |
| Practical Track | Frontend, Cloud & Deployment | 8–10 hours |
| Career Track | Communication, Job Preparation | 4–6 hours |
| **Total** | All 10 domains | **36–42 hours** |

**Track enforcement:**
- Core Track cannot drop below 14 hours per week during Months 1–4.
- Career Track cannot drop below 3 hours per week at any point.
- Support Track subjects (OS, CN, DBMS) require steady hours — not a sprint before interviews.

---

### 7.4 Time Budget Override Conditions

The default allocation above is overridden in these conditions:

| Condition | Override |
|-----------|---------|
| A topic is Struggling (AL-2) | +60 min dedicated to that topic; cut buffer |
| An intervention is triggered | That day's new topic time shifts to remediation |
| Evaluation scheduled | 30 min of buffer allocated to evaluation |
| Weekly Consolidation Task (Sundays) | 20 min taken from buffer |
| CRS < 55% and interviews are approaching | Shift to 50% revision, 50% new topics |
| CRS ≥ 65% and actively applying | Shift Career Track to 10+ hours/week |

---

## Section 8 — Weekly Review Workflow

> Total time ceiling: 30 minutes. Strictly enforced.

---

### 8.1 The 30-Minute Weekly Review Protocol

```
MINUTE 00–05: Read the AI-generated weekly report.
              → Use PROMPT 4 the evening before.
              → Wake up, pour coffee, read. No action yet.

MINUTE 05–08: Identify the ONE most important thing this week.
              → Best: topic completed that felt genuinely solid.
              → Worst: topic stuck or regressed.
              → This becomes the Consolidation Task focus.

MINUTE 08–28: Complete the Consolidation Task.
              → AI generates the task in the weekly report (Section 3.4).
              → This is a 20-minute implementation or written explanation.
              → Done independently. No AI. Evidence pushed when done.

MINUTE 28–30: Confirm or adjust next week's plan.
              → AI already generated it in the weekly report.
              → Mahesh either confirms ("looks good") or says one thing to adjust.
              → AI adjusts and sends final plan.

DONE. Close the laptop.
```

### 8.2 What the Weekly Review Is Not For

- Not for detailed analysis of every session log
- Not for rewriting the plan from scratch
- Not for second-guessing every mastery level
- Not for reading through all 12 syllabus files
- Not for setting up new tracking systems

The AI has already done all of that. The weekly review is for: one consolidation task, one confirmation, one read-through.

### 8.3 Rescheduling the Weekly Review

The weekly review happens on the last day of the study week. If that day is missed:
- It must happen the next morning — no later.
- The weekly review cannot be skipped, only postponed by 24 hours maximum.
- If skipped entirely: the AI generates an "overdue review" notice at the start of the next session and the review happens at the start of that day before any new study begins.

---

## Section 9 — AI Usage Rules

> These rules govern how AI is used during learning — distinct from how it is used for system management.

---

### 9.1 The Two Roles of AI in This System

| AI Role | Description | Always Permitted |
|---------|-------------|-----------------|
| **System Manager** | Planning, tracking, scoring, scheduling | Yes, always |
| **Learning Assistant** | Explaining concepts, generating questions | Permitted with ADS tracking |

These roles must not be confused. Using AI to explain a concept is a learning assist (affects ADS). Using AI to generate next week's plan is system management (does not affect ADS).

---

### 9.2 AI as Learning Assistant — Usage Rules

**Permitted (no ADS penalty):**

| Use | Permitted At |
|-----|-------------|
| AI explains a concept during first study pass (ML-0 → ML-1) | Any time |
| AI generates evaluation questions to test yourself | Any time |
| AI checks completed work AFTER independent implementation | Any time |
| AI simulates an interviewer asking questions | Any time |
| AI explains an error message AFTER you have spent ≥ 15 min debugging it | After 15 min |
| AI reviews code for style / best practices after you wrote it | After writing |

**Permitted but raises ADS:**

| Use | ADS Impact |
|-----|-----------|
| AI helps you understand what to write next (before starting) | ADS → 3 minimum |
| AI debugs your code before you attempt to debug it | ADS → 3 minimum |
| AI completes a partial implementation | ADS → 4 |
| AI writes any code that goes into your implementation | ADS → 4 |

**Never permitted (integrity rules):**

| Use | Rule |
|-----|------|
| AI writes the mini-task implementation | Violates TC-3 |
| AI writes the evaluation answer | Violates FI-1 |
| AI writes the GitHub commit content | Violates FI-4 |
| AI marks a topic Complete on Mahesh's behalf without evaluation | Violates TC-1 |

---

### 9.3 The 15-Minute Rule

Before using AI for debugging, Mahesh must attempt to solve the problem independently for at least 15 minutes.

This rule is self-enforced. No AI can enforce it. But it is the single most important rule for building genuine debugging skill. Every interview will require debugging without AI. This 15 minutes per day builds that muscle.

Logging the 15-minute attempt is not required. The commitment is the rule.

---

### 9.4 Context to Always Provide AI Agents

When starting any new conversation with an AI agent for Career OS work, Mahesh must provide:

**Minimum context:**
```
I am using the Mahesh Career OS system.
Governing files:
- 12_MASTERY_FRAMEWORK.md (mastery standards)
- 13_SYSTEM_SIMPLIFICATION_RULES.md (operating rules)
- [relevant syllabus file, e.g., 02_PYTHON_SYLLABUS.md]

My last session log:
[paste most recent 5-line log]

Request: [describe what you need]
```

Without this context, the AI cannot apply framework rules correctly and will give generic responses that do not serve the system.

---

## Section 10 — Escalation Rules

> When standard prompts and daily workflows are insufficient, these escalation rules apply.

---

### 10.1 Level 1 Escalation — Topic Blockage

**Trigger:** A topic has been in IN PROGRESS for > 7 days with no mastery improvement.

**Action:** Use PROMPT 5 (Stuck Escalation). AI applies the Struggling Topic Protocol (Rule AL-2 of Mastery Framework). No new topics in that domain until this topic clears.

**Mahesh's job:** Answer the diagnostic questions AI asks. Attempt the sub-component drill. Do not skip the topic.

---

### 10.2 Level 2 Escalation — Domain Stall

**Trigger:** An entire domain has had no Complete topics for > 10 days.

**Action:**
1. AI runs a domain diagnostic (identify the root cause: too difficult? prerequisites missing? wrong resources?).
2. Mahesh answers 3 diagnostic questions about why progress stalled.
3. AI revises the domain's plan: either slows down (more depth per topic) or restructures (different topic order).
4. One "clean sweep" session is scheduled: spend one full block (3 hours) on that domain only.

---

### 10.3 Level 3 Escalation — AI Dependency Not Decreasing

**Trigger:** CADI > 3.0 in any domain for 2 consecutive weeks.

**Action:**
1. AI declares a 1-day AI-Free Day in that domain (Rule: Section 7.3 of Mastery Framework).
2. On that day: no AI prompts during study, no AI during implementation, no AI for debugging.
3. Official documentation ONLY.
4. Log what was accomplished independently. The log goes to AI that evening.
5. If even one topic reaches ML-3 on the AI-Free Day, it proves the CADI was inflated — proceed normally.
6. If nothing works on the AI-Free Day, it proves the topic is genuinely at ML-2 — reset mastery level, slow down, rebuild.

---

### 10.4 Level 4 Escalation — CRS Plateau

**Trigger:** CRS has not increased in 3 consecutive weeks despite daily study.

**Action:**
1. AI runs a "CRS Bottleneck Analysis" — identifies the 3 topics whose completion would have the highest CRS impact.
2. These 3 topics become the sole focus for the following week (no new topics in any domain).
3. Each of the 3 topics gets a Full Evaluation attempt within the week.
4. After the week, CRS is recomputed. If it has increased, return to normal plan. If not, repeat with the next 3 bottleneck topics.

---

### 10.5 Level 5 Escalation — Interview Imminent

**Trigger:** Mahesh receives a first interview invite.

**Action:** This overrides everything. Send PROMPT 7 (Full System Status) immediately. The AI generates an emergency interview preparation schedule based on:
- Company (if known) and role type
- Current CRS and domain health
- Days available before the interview
- Domains most likely to be tested (based on job description if available)

Study plan shifts immediately:
- No new topics until after the interview
- 100% focus on revision and evaluation on relevant domains
- Daily mock interview questions via PROMPT 3
- Evidence requirement is suspended (no new GitHub commits needed — all time goes to revision)

---

## Section 11 — AI Agent Responsibilities (Complete List)

> This section is an instruction set for any AI agent operating within the Career OS system. It defines everything the AI must handle automatically, without Mahesh needing to ask.

---

### 11.1 Per-Session Responsibilities (triggered by PROMPT 2)

When Mahesh submits a session log, the AI automatically does all of the following without being asked:

```
☐ 1.  Parse the 5-line log into the full Framework session log format.
☐ 2.  Infer domain and syllabus section from topic name.
☐ 3.  Retrieve prior mastery level from conversation history or state.
☐ 4.  Score AI-I dimension based on ADS value (ADS 0→AI-I 4, ADS 4→AI-I 0).
☐ 5.  Score CU, IK, IR dimensions from BUILT description and self-explanation.
☐ 6.  Determine whether IA and DA can be scored or require evaluation.
☐ 7.  Compute TMS if all 6 dimensions are scorable.
☐ 8.  Determine mastery level based on TMS and dimension thresholds.
☐ 9.  Check ADS trend rule (Rule ADS-1): has ADS improved over last 3 sessions?
☐ 10. Check ADS-2: if last 2 sessions had ADS ≥ 3, block ML-4 promotion.
☐ 11. Check all 6 Topic Completion Rules (TC-1 through TC-6).
☐ 12. Update topic status (NOT STARTED / IN PROGRESS / NEEDS EVALUATION / COMPLETE / REGRESSED).
☐ 13. Check for any triggered interventions (Section 7.3 of Mastery Framework).
☐ 14. Check if any prerequisites are now unblocked by this session's progress.
☐ 15. Update the revision schedule: add this topic to Day 3 / 7 / 14 / 30 / 60 / 90 queue.
☐ 16. Surface any topics due for revision today or tomorrow.
☐ 17. Generate tomorrow's plan in Section 3.3 format.
☐ 18. Report: mastery level, status, ADS flag, intervention, tomorrow's plan.
☐ 19. If BLOCKER was reported: diagnose and include resolution suggestion.
☐ 20. If Level Guess is inflated vs. evidence: correct it and explain why.
```

### 11.2 Per-Week Responsibilities (triggered by PROMPT 4)

When Mahesh submits the weekly log batch, the AI automatically does all of the following:

```
☐ 1.  Parse all session logs for the week.
☐ 2.  Compute W1 (topics completed), W2 (regressions), W3 (avg ADS per domain),
       W4 (evaluation pass rate), W5 (CRS delta).
☐ 3.  Compute DRS for all 10 domains.
☐ 4.  Compute CRS using the weighted formula (Section 12.1 of Mastery Framework).
☐ 5.  Determine Employment Status.
☐ 6.  Check all 4 Hard Constraints.
☐ 7.  Compute CADI per domain.
☐ 8.  Classify each domain as Green / Yellow / Red.
☐ 9.  Identify any Struggling Topics (stuck at ML-3 for > 14 days).
☐ 10. Identify any intervention triggers from Section 7.3 of Mastery Framework.
☐ 11. Generate root cause for any regressions.
☐ 12. Generate the Consolidation Task for the weekly review.
☐ 13. Build next week's plan using domain tracks and time budget rules.
☐ 14. Identify the top 5 priority revisions for next week.
☐ 15. Output the full weekly report in Section 3.4 format.
```

### 11.3 Evaluation Responsibilities (triggered by PROMPT 3)

When Mahesh requests an evaluation, the AI automatically does all of the following:

```
☐ 1.  Retrieve the topic's current mastery level.
☐ 2.  Determine the evaluation level (ML-4 target = standard; ML-5 target = add
       Type 6 and 7 questions).
☐ 3.  Generate one question at a time in this order:
       2 × Type 1 (Definition) → 1 × Type 2 (Comparison) → 1 × Type 3 (Implementation)
       → 1 × Type 4 (Debugging) → 1 × Type 5 (Integration) → [Type 6/7 if ML-5 target]
☐ 4.  Wait for each answer before proceeding.
☐ 5.  Score each dimension after all questions are answered.
☐ 6.  Apply the ML-4 dimension thresholds (Section 3 of Mastery Framework).
☐ 7.  Compute TMS.
☐ 8.  Check all 6 TC rules.
☐ 9.  Issue a verdict: COMPLETE, NOT YET (specific gaps named), or REGRESSED.
☐ 10. If NOT YET: give exactly 2-3 specific things to fix. No more.
☐ 11. Update the revision schedule based on evaluation outcome.
```

### 11.4 Context Inference Rules for AI Agents

When partial context is provided, the AI must infer rather than ask repeatedly:

| Missing Information | AI Action |
|--------------------|-----------|
| Domain not stated | Infer from topic name + syllabus filenames |
| Prior mastery level not stated | Start at ML-0 and ask once to confirm |
| Syllabus section not stated | Search for topic name across all syllabus files |
| ADS not stated | Ask once. If no response: assume ADS = 2 |
| Date not stated | Ask once. If no response: note as undated |

The AI asks clarifying questions at most ONCE per ambiguity. If the answer is not provided, the AI makes the best reasonable inference and proceeds. Excessive questions from the AI create friction that breaks the 10-minute admin ceiling.

---

## Section 12 — Compatibility Rules

> How this file interacts with `12_MASTERY_FRAMEWORK.md` and all syllabus files.

---

### 12.1 Authority Hierarchy

```
AUTHORITY ORDER (highest to lowest):
1. 12_MASTERY_FRAMEWORK.md — standards, definitions, rules
2. 13_SYSTEM_SIMPLIFICATION_RULES.md — operating procedures
3. Individual syllabus files — topic content, structure, prerequisites
```

When any rule in this file conflicts with the Mastery Framework, the Mastery Framework wins. This file may only simplify the procedure — it cannot lower the standard.

**Examples of what this file CAN do:**
- Compress a 15-question daily eval into a 1-question self-check (procedure simplification)
- Replace a 20-field session log with a 5-line input (format simplification)
- Delegate tracking and computation to AI (responsibility reassignment)

**Examples of what this file CANNOT do:**
- Lower the ML-4 threshold for topic completion
- Reduce the ADS requirement for Complete status
- Waive the Mini-Task requirement
- Exempt theory topics from evaluation
- Override the Hard Constraint rules on CRS

---

### 12.2 Syllabus File Integration

The 10 syllabus files (02 through 11) define the topic inventory. This file defines how that inventory is worked through. The relationship is:

- Syllabus files answer: "What topics exist?"
- Mastery Framework answers: "What does mastery of a topic mean?"
- This file answers: "How does Mahesh work through topics day by day?"

When an AI agent builds a daily plan, it reads:
1. The syllabus file to find the next topic in sequence
2. The Mastery Framework to determine the target mastery level
3. This file to determine the time allocation, format, and workflow

All three files must be loaded for any Career OS AI agent to function correctly.

---

### 12.3 Version Compatibility

This file is version 1.0, compatible with:
- `12_MASTERY_FRAMEWORK.md` version 1.0
- All syllabus files as created in the initial Career OS build

If the Mastery Framework is updated to a new version, this file must be reviewed for compatibility before continuing to use it. Sections 11.1, 11.2, and 11.3 in particular must be re-verified against any updated AI agent responsibilities.

---

## Appendix — Quick Reference Card

> Print this. Tape it to the wall.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAHESH CAREER OS — DAILY OPERATING RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MAHESH'S JOB:          LEARN. BUILD. LOG. PUSH.
AI'S JOB:              PLAN. TRACK. SCORE. SCHEDULE.

──────────────────────────────────────────────────
EVERY MORNING (2 min):
  Read today's plan. Open syllabus. Start studying.

EVERY EVENING (5 min):
  Fill 5-line log. Push evidence. Send PROMPT 2.
  Read AI feedback.

EVERY WEEK-END (30 min):
  Read weekly report. Do Consolidation Task.
  Confirm next week's plan.
──────────────────────────────────────────────────
THE 5-LINE LOG:
  TOPIC:        [name + syllabus ref]
  BUILT:        [one sentence]
  ADS:          [0-4]
  BLOCKER:      [None / one sentence]
  LEVEL GUESS:  [ML-0 through ML-5]
──────────────────────────────────────────────────
EVIDENCE RULE:
  Code → GitHub commit (one file is fine)
  Theory → One paragraph in a notes file
  No evidence = topic cannot be marked Complete
──────────────────────────────────────────────────
QUICK SELF-CHECK (end of every session):
  "Without AI, right now: can I explain this
   AND implement it?"
   Yes both → on track
   Explain only → need more implementation
   Neither → reset to ML-2, rebuild
──────────────────────────────────────────────────
THE 15-MINUTE RULE:
  Before calling AI for debugging help:
  15 minutes of independent struggle first.
──────────────────────────────────────────────────
STANDARDS DON'T CHANGE:
  ML-4 minimum to Complete any topic.
  ADS must trend down.
  No AI during mini-tasks.
  Hard Constraints must pass before applying.
  CRS ≥ 65% = Application Ready.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

*This file does not make the journey shorter. It makes the journey sustainable. The standards are unchanged. The process is human.*
