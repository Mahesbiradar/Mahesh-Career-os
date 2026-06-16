# Mahesh Career OS — Execution Engine

> **File:** `16_EXECUTION_ENGINE.md`
> **Version:** 1.0
> **Depends On:** `12_MASTERY_FRAMEWORK.md`, `13_SYSTEM_SIMPLIFICATION_RULES.md`, `15_180_DAY_ROADMAP.md`
> **Purpose:** Define the precise mechanics of how Mahesh executes the system — how a session runs, how resources are consumed, how failures are recovered, how AI is used, and how every element connects to produce measurable mastery.
> **Scope:** Execution mechanics only. Not a plan. Not a schedule. Not a list of topics.

---

## The Core Distinction

`15_180_DAY_ROADMAP.md` answers: **Where are we going?**
`13_SYSTEM_SIMPLIFICATION_RULES.md` answers: **Who does what?**
`12_MASTERY_FRAMEWORK.md` answers: **What does mastery mean?**
**This file answers: How exactly does Mahesh move through the system every single day?**

If the roadmap is a map and the mastery framework is the graduation criteria, this file is the engine — the mechanism that converts daily hours into mastered topics into career readiness.

---

## Section 1 — Execution Philosophy

### 1.1 The Three Laws of Execution

**Law 1: Proof over Familiarity**

Familiarity is the feeling of knowing something. Proof is the ability to build it without help. The system does not care about familiarity. Every evaluation, every completion check, every interview is a test of proof. Study sessions that end in familiarity without implementation are incomplete.

The test: After this session, what can I build that I could not build before?

If the answer is nothing, the session produced familiarity. Familiarity is not worthless — it is necessary before implementation — but it is not sufficient. The session is not done until implementation is attempted.

**Law 2: Artifacts over Notes**

Notes describe what was read. Artifacts prove what was understood. A paragraph written in Mahesh's own words after closing all references is an artifact. A GitHub commit of independently written code is an artifact. A highlight or a copy-paste from documentation is not.

Artifacts are evidence. Notes are intentions. The system runs on evidence.

**Law 3: Independence over Speed**

An AI-assisted fast completion is worth less than a slow independent completion. A session where Mahesh understood 40% of the topic independently and struggled is more valuable than a session where AI explained 100% of it. The ADS system enforces this — faster AI-assisted progress lowers ADS scores and delays ML-4 promotion. Slower independent work raises ADS scores and accelerates actual mastery.

Counterintuitive but true: working slower and independently is the faster path to employment.

---

### 1.2 The Execution Mindset

Mahesh is not a student consuming a curriculum. He is a professional learning a craft. The distinction changes how every session is approached:

| Student Mode | Professional Mode |
|-------------|------------------|
| "I read this chapter." | "I built this feature." |
| "I watched this tutorial." | "I debugged this failure." |
| "I understand the concept." | "I can implement it without reference." |
| "I'm learning Django." | "I can explain every line I wrote in this Django view." |
| "AI helped me with this." | "This is AI-assisted; I need to rebuild it independently." |

The professional mode is the default. Every session starts by asking: "What will I be able to do independently by the end of this session that I cannot do now?"

---

### 1.3 The Session Contract

Every study session is a contract with three terms:

1. **Input term:** A specific topic from the syllabus (not "study Python" — "study Python Decorators, Level 5.1")
2. **Output term:** An artifact (code commit, written explanation, STAR answer)
3. **Proof term:** A completed Quick Self-Check (can explain + can implement without AI)

A session that produces no artifact has not satisfied its contract. The session is not over until the artifact exists and is pushed.

---

## Section 2 — Daily Operating Cycle

### 2.1 The Morning Decision Engine

Every morning runs the same decision sequence. This takes 2 minutes:

```
START
  │
  ▼
Is an intervention flagged from yesterday's AI feedback?
  ├─ YES → That intervention IS today's primary focus. Read it first.
  └─ NO → Continue ↓
  │
  ▼
Is there an active topic IN PROGRESS from yesterday?
  ├─ YES → That topic continues today unless it was explicitly completed.
  └─ NO → AI's plan determines today's topic (from PROMPT 1 output).
  │
  ▼
Is a revision overdue by > 3 days?
  ├─ YES → That revision becomes Block 3, mandatory, before Block 2 ends.
  └─ NO → Revisions proceed per AI-scheduled Block 3.
  │
  ▼
Read today's AI plan. Confirm topic, mini-task, and revision items.
  │
  ▼
Open the syllabus file for today's topic.
Open a blank code file or notes file.
Start the timer.
```

Do not open email, social media, or news before this sequence is complete.

---

### 2.2 Block Transitions

The four daily blocks (from `13_SYSTEM_SIMPLIFICATION_RULES.md`) transition as follows:

**Block 0 → Block 1 trigger:** Today's plan is read. Syllabus file is open.

**Block 1 → Block 2 trigger:** One of these occurs:
- The study phase (see Section 3) is complete and understanding is at ML-2 minimum
- 90 minutes have elapsed (enforce transition even if study feels incomplete — implementation reveals gaps better than more reading)

**Block 2 → Block 3 trigger:** One of these occurs:
- The mini-task implementation is committed to GitHub
- 120 minutes have elapsed without completion (log the partial state; note where it stopped; continue in tomorrow's session)

**Block 3 → Block 4 trigger:** Revision items complete OR 30 minutes elapsed.

**Block 4:** 5-line log filled, evidence pushed, PROMPT 2 sent, AI feedback read.

---

### 2.3 When Plans Break Down Mid-Day

Real study days rarely follow plans. These are the four common mid-day scenarios and how to handle each:

**Scenario A: Topic is harder than expected and implementation fails**
Do not abandon the topic. Do not switch domains mid-session. Break the implementation into a smaller first step (the minimum viable implementation — one function, one endpoint, one CSS rule). Commit that. Continue tomorrow with the next step. A partial commit with a clear note of where it stopped is better evidence than no commit.

**Scenario B: Topic is easier than expected and finishes early**
Invoke the Secondary Topic from the AI plan. Do not declare the day complete at 3 hours because the primary topic was easy. Use the remaining time on the secondary topic or on revision.

**Scenario C: Energy collapses mid-day**
Log the work done so far. File a partial 5-line log. Rest. Resume if possible. A partial day is not a failed day. The log records reality — partial progress is honest progress.

**Scenario D: Interruption destroys session continuity**
Note exactly where the session stopped in the BLOCKER field. Do not try to remember context the next morning — write it down while it is fresh. The next session starts from that note, not from the beginning.

---

## Section 3 — Standard Study Session Workflow

> The atomic unit of execution. Every topic follows this workflow, every time.

---

### 3.1 The Seven-Step Session Protocol

```
┌─────────────────────────────────────────────────────┐
│  STEP 1: CALIBRATE                      [ 5 min ]   │
│  Before reading anything:               [ max ]    │
│  "What do I already know about this?"              │
│  Say it out loud or write it.                      │
│  Note the gaps in what you could not say.          │
└─────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────┐
│  STEP 2: STUDY                         [ 20–40 min ]│
│  Read the syllabus topic entry.                    │
│  Open ONE primary resource (official docs).        │
│  Read with a goal: "I need to understand X         │
│  well enough to build Y."                          │
│  Maximum 40 min. If still confused → implement     │
│  anyway. Confusion resolves through doing.         │
└─────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────┐
│  STEP 3: CLOSE REFERENCES              [ 30 sec ]   │
│  Close all tabs. Close the docs.                   │
│  Open only: the code editor or a blank text file.  │
│  AI is OFF.                                        │
└─────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────┐
│  STEP 4: IMPLEMENT                     [ 60–90 min ]│
│  Build the mini-task from the AI plan.             │
│  Write every line yourself.                        │
│  When stuck: think for 5 min → check specific      │
│  docs (not tutorials) → try again.                 │
│  After 15 min stuck on ONE thing: use AI           │
│  (ADS impact applies — see Section 7).             │
└─────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────┐
│  STEP 5: DEBUG AND FIX                 [ until done]│
│  When something breaks: read the error message     │
│  fully. Attempt to understand it before searching. │
│  15-minute rule: try independently first.          │
│  The debugging process IS the learning.            │
│  Do not skip it.                                   │
└─────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────┐
│  STEP 6: VERIFY                        [ 10 min ]   │
│  Implementation works (or is stopped at a logical  │
│  boundary).                                        │
│  Quick Self-Check: "Can I explain this AND         │
│  implement the core without AI right now?"         │
│  YES both → proceed. NO → note what is missing.   │
└─────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────┐
│  STEP 7: EVIDENCE AND LOG              [ 5 min ]    │
│  Commit to GitHub (code) or save note (theory).   │
│  Fill 5-line log.                                  │
│  Send PROMPT 2.                                    │
└─────────────────────────────────────────────────────┘
```

---

### 3.2 Theory-Only Session Variant

For OS, CN, DBMS, and Communication topics where no code is produced, Step 4 is replaced:

**Step 4T: Write-to-Understand**
After closing all references, write a 150–250 word explanation of the topic in a notes file. Not a summary. Not a copy of the textbook. An explanation written as if speaking to another engineer who has never seen this topic.

Rules:
- Write from memory only. Do not look at notes while writing.
- If you cannot write 150 words from memory, re-read the source (Step 2) and try again.
- The written explanation IS the implementation for theory topics.
- Commit the file to GitHub or save in a designated notes folder.

**Step 4T for Communication topics:**
Record a 60-second voice explanation (phone memo app) or write a STAR answer for a scenario related to the topic. No reading from notes during recording.

---

### 3.3 Evaluation Session Variant

When a Full Evaluation is triggered (PROMPT 3), the session structure changes entirely:

```
STEP 1: Read the topic's current state from AI plan (prior ML + dimension scores).
STEP 2: Do NOT review the topic before the evaluation. The evaluation tests actual retention.
STEP 3: Send PROMPT 3. Answer questions one at a time.
STEP 4: After all questions: receive score. Read AI verdict.
STEP 5: If COMPLETE → revision scheduled; log submitted; done.
STEP 6: If NOT YET → AI gives exactly 2-3 specific gaps. Fill those gaps in the remaining session time. Re-evaluate in the next session.
STEP 7: Log submitted with evaluation outcome as BUILT field.
```

The evaluation session has no implementation block. The evaluation IS the session. Do not study before the evaluation — pre-study before an evaluation is teaching to the test and produces inflated scores.

---

### 3.4 The Integration Session

Once per week (Day 5 of each week), Block 2 is replaced with an Integration Session:

**Goal:** Use this week's new topic inside a system larger than itself.

**Mechanics:**
- Identify which milestone project this topic belongs to.
- Find the component in the project where this topic applies.
- Implement or improve that component using this week's new knowledge.
- If the topic does not map to the milestone project: simulate its use in a simple system from scratch.

**Why this matters:** The IK (Integration Knowledge) dimension of TMS requires demonstrating that a topic can function within a larger system, not just in isolation. Topics learned in isolation often fail integration dimension evaluations. The weekly integration session closes this gap systematically.

**Log format for Integration Sessions:**
```
TOPIC:       [This week's topic + the system it was integrated into]
BUILT:       [Description of the integration: "Added Redis caching to the BlogPost list view using Django cache_page decorator"]
ADS:         [0-4]
BLOCKER:     [None / description]
LEVEL GUESS: [ML-X]
```

---

## Section 4 — Time Allocation Engine by Phase

> These allocations are inputs for AI plan generation. AI must use the active phase's allocation when distributing the 6 daily hours.

---

### 4.1 Phase Time Profiles

**Time allocation in minutes per 6-hour (360 min) day:**

| Block | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|-------|---------|---------|---------|---------|---------|
| DSA external track | 75 min | 75 min | 75 min | 45 min | 60 min |
| Admin (Blocks 0+4) | 10 min | 10 min | 10 min | 10 min | 10 min |
| **Net Career OS time** | **275 min** | **275 min** | **275 min** | **305 min** | **290 min** |
| Study (Block 1) | 110 min | 80 min | 55 min | 45 min | 30 min |
| Implementation (Block 2) | 80 min | 100 min | 130 min | 75 min | 50 min |
| Revision (Block 3) | 15 min | 30 min | 40 min | 55 min | 50 min |
| Evaluation | — | 15 min | 25 min | 75 min | 60 min |
| Job Prep / Applications | — | — | 15 min | 35 min | 80 min |
| Interview Practice | — | — | 10 min | 20 min | 20 min |
| Buffer | 70 min | 50 min | — | — | — |

**How to read this table:**
- Phase 1 is study-heavy because foundations must be built before they can be implemented.
- Phase 2 begins shifting to implementation-dominant.
- Phase 3 is implementation-dominant — the milestone project is being built.
- Phase 4 shifts to revision and evaluation — converting knowledge to interview currency.
- Phase 5 is application-heavy — knowledge exists; the remaining work is getting hired.
- Buffer minutes are flexible; AI assigns them based on daily state.

---

### 4.2 Domain Time Shares Within Career OS Time

These percentages apply to the net Career OS time in each phase. AI uses these when deciding how to split time across domain tracks.

| Domain Track | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|-------------|---------|---------|---------|---------|---------|
| Python | 20% | 25% | 15% | 10% | 5% |
| Backend Engineering | 20% | 25% | 20% | 15% | 5% |
| SQL | 15% | 12% | 10% | 8% | 5% |
| Frontend | 12% | 10% | 12% | 8% | 3% |
| Cloud & Deployment | 10% | 8% | 15% | 8% | 5% |
| DBMS + OS + CN (combined) | 15% | 10% | 10% | 15% | 8% |
| Communication | 5% | 5% | 8% | 10% | 10% |
| Job Preparation | 3% | 5% | 10% | 26% | 59% |

**Interpretation:** Job Preparation is nearly absent in early phases — that is by design. Applying before CRS ≥ 60% wastes opportunity. By Phase 5, the majority of Career OS time (outside of revision) is Job Preparation — applying, networking, interview feedback, negotiation.

---

### 4.3 How AI Applies the Phase Time Profile

When the AI generates a daily plan, it:
1. Identifies the current phase from session logs and CRS trajectory.
2. Applies that phase's domain time shares to allocate the day.
3. Applies the block structure from Section 2.
4. Adjusts for any interventions, revision debts, or escalations.
5. Selects the specific topic within the target domain based on syllabus sequence and mastery levels.

If a domain is at Red health (DRS far below target), AI increases its share by up to 8 percentage points, pulling equally from the two lowest-priority domains in that phase.

---

## Section 5 — Resource Consumption Rules

### 5.1 The Resource Hierarchy

When studying any topic, resources are consumed in this order. Moving to the next tier is permitted only if the current tier is insufficient.

```
TIER 1: Official Documentation
    Django docs, MDN Web Docs, Python docs, PostgreSQL docs,
    AWS docs, React docs, Docker docs.
    Always try here first. Always.

TIER 2: Syllabus Topic Entry
    The relevant syllabus file (02–11). Contains the "Why it matters"
    and "Interview importance" context. Use to orient study.

TIER 3: One Targeted Reference Video
    ≤ 20 minutes per concept. One video per concept, not a series.
    No watching without simultaneously pausing and attempting.
    After the video: close it. Never re-watch during the same topic.

TIER 4: AI Explanation (ADS impact)
    Only after 15 min of independent struggle.
    Never as the first resource.
    ADS increases by minimum 1 step when this tier is used.

TIER 5: Tutorials and Guided Projects
    Absolute last resort. High rabbit-hole risk.
    If a tutorial is used: study the concept from the tutorial,
    then close it and rebuild from scratch independently.
    Copying tutorial code without rebuilding is ADS = 4.

FORBIDDEN: Stack Overflow for learning
    Stack Overflow is for debugging specific errors, not for
    learning how a concept works. Its answers are decontextualized
    and often outdated. Do not study from it.
```

---

### 5.2 Resource Time Caps

| Resource Type | Maximum Time Per Session | Enforcement |
|--------------|--------------------------|-------------|
| Official docs (reading) | 40 min per session | After 40 min, close and implement |
| Reference video | 20 min total | One video, not a playlist |
| AI explanation session | 15 min per concept | Explain-back rule applies after |
| Tutorial consumption | 30 min total | Must rebuild independently after |
| Stack Overflow | 10 min per error | If unsolved in 10 min, move to AI (ADS 2) |

**The 40-minute reading cap is the most important.** Extended reading without attempting implementation is the primary cause of familiarity without proof. When 40 minutes of reading have passed and the concept is not fully clear: stop reading and start implementing. The implementation will reveal exactly which parts are unclear — much more precisely than continued reading.

---

### 5.3 Resource Selection by Topic Type

| Topic Type | Primary Resource | Secondary | Tertiary |
|-----------|-----------------|-----------|---------|
| Python concepts | Python official docs | One focused video | AI evaluation only |
| Django / DRF | Django docs + DRF docs | Django source code (GitHub) | AI explanation if stuck |
| SQL | PostgreSQL docs | db-fiddle.com to run queries | AI for query review |
| DBMS theory | DBMS textbook concepts | CMU/Stanford lecture notes (official) | AI evaluation only |
| OS theory | OSTEP (free online textbook) | Linux man pages | AI evaluation only |
| CN theory | Beej's Guides (free) | RFC documents for specific protocols | AI evaluation only |
| React / Frontend | React official docs + MDN | One targeted video | AI evaluation only |
| Docker / Cloud | Official Docker docs / AWS docs | AWS skill builder | AI explanation if stuck |
| Linux commands | man pages + tldr.sh | None needed | — |
| Communication | Syllabus topics + STAR template | Record and listen back | AI for question generation |

---

### 5.4 The "Rebuild After Tutorial" Rule

If a tutorial, guided project, or YouTube walkthrough is used:

1. Complete the tutorial while following along.
2. Delete all tutorial code.
3. Rebuild the same thing from scratch with no reference to the tutorial.
4. The rebuild is the evidence, not the followed-along code.
5. If the rebuild cannot be completed: the tutorial did not produce understanding — it produced copying. Reduce the scope (one function instead of the full app) and rebuild that.

This rule exists because tutorials create the illusion of progress. The feeling of "I can do this" while following a tutorial is familiarity, not proof. The rebuild is the test.

---

## Section 6 — Evidence Creation Rules

### 6.1 The Minimum Viable Evidence Standard

Evidence must satisfy one question: **"If a future interviewer saw only this artifact, could they verify that Mahesh understood this topic?"**

Minimum Viable Evidence (MVE) by topic type:

| Topic Type | MVE Definition | Examples |
|-----------|---------------|---------|
| Code implementation | One file or function that demonstrates the core concept, written independently, committed to GitHub | `decorators.py` with 3 decorator examples; `views.py` with a DRF ViewSet |
| Theory (CS fundamentals) | 150–250 word written explanation in Mahesh's own words | Paragraph explaining MVCC in PostgreSQL; explanation of how the TLS handshake works |
| SQL | Runnable SQL query or set of queries demonstrating the concept, with a comment explaining what it does | Window function query on a sample dataset with ROW_NUMBER + PARTITION BY |
| Communication | Recorded 60-second explanation OR written STAR answer | Voice memo explaining event-driven architecture; STAR answer for "Tell me about a complex system you built" |
| Job Preparation | The deliverable itself | Resume PDF; LinkedIn section update; cover letter draft |

---

### 6.2 Evidence Quality Rules

**Rule E-1: Original content only.**
Evidence written or coded by AI is not Mahesh's evidence. Evidence must come from Mahesh's own understanding expressed in Mahesh's own words or code.

**Rule E-2: References must be closed when creating evidence.**
Code written with the tutorial open on one screen is copying. Code written with the official docs open for reference to syntax is acceptable. AI open while writing is ADS = 4.

**Rule E-3: Commit messages must name the topic.**
`git commit -m "decorators"` is not acceptable.
`git commit -m "feat: python decorators — timing decorator and retry decorator from scratch"` is acceptable.

The commit message is part of the evidence. It tells the story of what was built and why. In 90 days, Mahesh should be able to read any commit message and immediately know what topic was studied and what was built.

**Rule E-4: Partial evidence is still evidence.**
A partial implementation that is explicitly noted as partial ("implements the base case; edge cases not yet handled") is better than no evidence. Partial commits are honest records of progress. No commits are gaps in the record.

**Rule E-5: Theory evidence stays findable.**
Written theory notes must be saved in a consistent location (a `notes/` folder in the main repo, or a dedicated Notion/Google Doc). If they cannot be found in 10 seconds, they do not count as evidence.

---

### 6.3 Evidence Anti-Patterns

The following do NOT satisfy the evidence requirement:

| What Was Submitted | Why It Fails |
|-------------------|-------------|
| Screenshot of code running in AI chat | Not original code; not reproducible |
| Copy-pasted code from a tutorial with no modification | No original implementation |
| "I understand this" as a commit message | No content |
| A long notes file of copy-pasted definitions | Not Mahesh's words |
| A GitHub repo with only generated boilerplate | No demonstration of understanding |
| An AI-generated explanation saved as a text file | AI's words, not Mahesh's understanding |
| A topic marked Complete with no artifact | Violates TC-6 of Mastery Framework |

---

### 6.4 The GitHub Repo Architecture

All Career OS code evidence lives in one or two GitHub repositories:

**Repo 1: `career-os-practice`** (private)
- Purpose: Daily practice, mini-tasks, topic exploration code
- Structure: One folder per domain (`python/`, `backend/`, `sql/`, `frontend/`, etc.)
- Commits: Daily, named by topic
- Privacy: Private is fine. The practice repo is for evidence, not showcase.

**Repo 2: `[project-name]`** (public)
- Purpose: Milestone Project 3 (the portfolio centrepiece)
- Structure: Monorepo or separate backend/frontend repos
- Commits: Meaningful, clean history
- Privacy: Public. This is what employers see.

Theory notes (OS, CN, DBMS, Communication STAR answers) live in either:
- A `notes/` folder inside `career-os-practice`, or
- A linked Notion/Google Doc referenced from the repo README

---

## Section 7 — AI Interaction Protocols

### 7.1 The Three AI Modes

At any moment during a session, AI is in exactly one of three modes:

| Mode | Name | AI Can Do | AI Cannot Do |
|------|------|-----------|-------------|
| **Mode 0** | OFF | Nothing | Everything |
| **Mode 1** | EVALUATOR | Ask evaluation questions, score answers, assess mastery | Explain concepts, write code, hint at answers |
| **Mode 2** | EXPLAINER | Explain a concept, debug an error message, clarify a single point | Write implementation code, complete partial code, do the mini-task |

**Mode 0 (OFF)** is active during:
- All of Block 2 (implementation) — no exceptions
- Any evaluation session after questions begin
- Any mini-task attempt
- The rebuild phase after a tutorial

**Mode 1 (EVALUATOR)** is active during:
- Evaluation sessions (PROMPT 3)
- Quick revision checks (PROMPT 6, PROMPT 8)
- Weekly consolidation tasks

**Mode 2 (EXPLAINER)** is active during:
- Block 1 (study phase), after the 40-minute reading cap is hit and understanding is incomplete
- Debugging, after 15 minutes of independent struggle
- Conceptual questions that arise after implementation (why did this work?)

---

### 7.2 The Explain-Back Rule

Whenever Mode 2 is used and AI explains a concept:

1. Read the explanation once.
2. Close the AI conversation.
3. Immediately write or say the explanation back in Mahesh's own words.
4. Do not re-read the AI explanation during the write-back.

If the write-back cannot be completed in Mahesh's own words: the AI explanation did not produce understanding — it produced passive reception. Request a different angle from AI, or use a different resource. The test of an explanation is whether it can be reproduced, not whether it felt clear.

This rule applies to every AI explanation in Mode 2. Without it, AI creates the illusion of understanding — the same illusion that collapses in interviews.

---

### 7.3 Prompt Construction Rules

When sending prompts to AI, these rules produce better outputs:

**Rule AI-1: Always provide context before the request.**
Bad: "Explain Django signals."
Good: "I just finished writing a Django post_save signal to send a welcome email. The signal fires but the email is not being sent. I've confirmed the email backend is configured. Here's my signal code: [code]. What am I missing?"

Context-first prompts produce targeted, relevant responses. Context-free prompts produce generic textbook answers.

**Rule AI-2: Ask for one thing at a time.**
Bad: "Explain decorators, show an example, and tell me when to use them."
Good: "Explain what a Python decorator is." (Then in the next message: "Show me the minimal code example for a timing decorator.")

One concept per prompt produces depth. Multiple concepts per prompt produces superficiality.

**Rule AI-3: When asking AI to evaluate, provide the full context.**
Use the standard prompts from `13_SYSTEM_SIMPLIFICATION_RULES.md` Section 4. Do not paraphrase them. The prompts are engineered to produce Framework-compatible evaluations.

**Rule AI-4: When asking AI to debug, describe what you expected vs. what happened.**
Bad: "My code doesn't work, help."
Good: "My Django serializer is returning an empty list. I expected it to return all BlogPost objects. The queryset is `BlogPost.objects.all()`. Here's the serializer: [code]. Here's the view: [code]. What's wrong?"

The act of writing "I expected X, I got Y" forces a diagnostic thought process that often reveals the bug before AI responds.

**Rule AI-5: Do not ask AI to write code during implementation.**
Asking AI to write any implementation code — even one function — resets the session's ADS to 4 for that topic. The only exception is AI writing a test for code Mahesh has already written (testing the implementation, not replacing it).

---

### 7.4 AI Session Handoff Protocol

When starting a new AI conversation for Career OS work, always send the handoff context block:

```
CONTEXT:
I am using the Mahesh Career OS system.
Active framework files:
  - 12_MASTERY_FRAMEWORK.md (mastery standards)
  - 13_SYSTEM_SIMPLIFICATION_RULES.md (operating procedures)
  - 16_EXECUTION_ENGINE.md (execution mechanics)
  - [relevant syllabus file]
  - [15_180_DAY_ROADMAP.md if phase-level planning is needed]

Current state:
  - Active phase: [1/2/3/4/5]
  - Most recent session log: [paste 5-line log]
  - Current CRS estimate: [X]% (if known)

Request: [specific request]
```

Without this block, the AI has no framework context and will give generic responses. This block takes 30 seconds to fill in and dramatically improves response quality.

---

## Section 8 — Escalation Protocol

### 8.1 Escalation Decision Tree

Run this decision tree at the end of every study week (during the weekly review):

```
START
  │
  ▼
Has any single topic been IN PROGRESS for > 7 days without level improvement?
  ├─ YES → Level 1 Escalation: Stuck Topic
  └─ NO → Continue ↓
  │
  ▼
Has any entire domain had 0 new Complete topics in > 10 days?
  ├─ YES → Level 2 Escalation: Domain Stall
  └─ NO → Continue ↓
  │
  ▼
Is CADI > 3.0 in any domain for 2+ consecutive weeks?
  ├─ YES → Level 3 Escalation: AI Dependency Crisis
  └─ NO → Continue ↓
  │
  ▼
Is CRS unchanged or decreasing for 3+ consecutive weeks?
  ├─ YES → Level 4 Escalation: CRS Plateau
  └─ NO → Continue ↓
  │
  ▼
Has an interview invite been received?
  ├─ YES → Level 5 Escalation: Interview Emergency
  └─ NO → System is healthy. Proceed normally.
```

---

### 8.2 Escalation Execution Protocol

**Level 1: Stuck Topic**

Detection: Same topic, > 7 days, no ML improvement in session logs.

Execution:
1. Send PROMPT 5 (Stuck Escalation) with the topic name, session count, ADS history, and a description of what Mahesh can and cannot do.
2. AI performs root cause diagnosis (3 likely causes: missing prerequisite, wrong resource, insufficient implementation attempts).
3. AI generates a sub-component drill plan (breaks the stuck topic into 3–5 smaller pieces).
4. Work through the sub-components one at a time over the next 3 sessions.
5. Do not attempt the full topic evaluation until all sub-components are at ML-3.

Resolution signal: Can complete the mini-task independently (ADS ≤ 1) on at least 2 consecutive sessions.

---

**Level 2: Domain Stall**

Detection: Entire domain, > 10 days, 0 new Complete topics.

Execution:
1. AI runs domain diagnostic (answer 3 questions: What is the last topic attempted? What specific part is not working? Has anything been implemented successfully in this domain this week?).
2. Based on diagnosis, AI takes one of three actions:
   - **Prerequisite gap:** Redirects to an earlier topic in the dependency chain.
   - **Resource mismatch:** Replaces the current resource with an alternative.
   - **Volume problem:** Schedules 3 consecutive full days (Block 1 + Block 2) dedicated solely to that domain.
3. The domain's time share is temporarily increased by 8 percentage points until 3 new topics Complete.

Resolution signal: 3 new Complete topics in the stalled domain within 10 days.

---

**Level 3: AI Dependency Crisis**

Detection: CADI > 3.0 in any domain for 2+ consecutive weeks.

Execution:
1. Declare one AI-Free Day in the affected domain. On that day: no AI for any purpose in that domain. Official docs and previously saved notes only.
2. Attempt to complete a mini-task from that domain using only official documentation.
3. Log the result. If the mini-task was completed: CADI was inflated; return to normal operations.
4. If the mini-task could not be completed: the topic is genuinely at ML-2 or below. Reset mastery level. Rebuild from sub-components.
5. After the AI-Free Day, AI usage is restricted to Mode 1 (Evaluator only) in that domain for 1 week.

Resolution signal: CADI drops below 2.5 in the domain for the following week.

---

**Level 4: CRS Plateau**

Detection: CRS unchanged (±1%) across 3 consecutive weekly reviews.

Execution:
1. Send PROMPT 7 (Full System Status).
2. AI identifies the 3 topics whose completion would have the highest CRS impact (highest weight domain + most topics near ML-4 threshold).
3. The next 7 days are a "Completion Sprint" — only those 3 topics, plus mandatory revision. No new topics.
4. Each of the 3 topics receives a Full Evaluation (PROMPT 3) within the sprint week.
5. After the sprint: recompute CRS.

If CRS still does not move after the sprint: escalate to AI agent for a deeper system audit — there may be a systematic scoring issue or a Hard Constraint failure suppressing CRS.

Resolution signal: CRS increases by ≥ 3% within 10 days.

---

**Level 5: Interview Emergency**

Detection: Interview invite received.

Execution (immediately upon receiving invite):
1. Send PROMPT 7. Get full current status.
2. Identify company name and role (if known). Send to AI with the job description.
3. AI generates a compressed interview preparation plan based on:
   - Days until interview
   - Known domains tested by that company type
   - Mahesh's current weak spots in those domains
4. New topic learning stops. Revision and evaluation only.
5. DSA time increases to 90 min/day.
6. Daily mock interview questions via PROMPT 3 on the most likely-to-be-tested topics.
7. Evidence requirement suspended (no new GitHub commits needed — all time goes to interview prep).
8. One STAR story rehearsed per day for every milestone project feature likely to be asked about.

Resolution: The interview happens. Post-interview analysis feeds into the system regardless of outcome.

---

## Section 9 — Revision Execution Rules

### 9.1 Revision Types by Schedule Position

Spaced repetition schedule: Day 3 → Day 7 → Day 14 → Day 30 → Day 60 → Day 90.
Each checkpoint has a different depth requirement.

| Revision Day | Name | Format | Duration | Pass Criteria |
|-------------|------|--------|----------|---------------|
| Day 3 | Quick Recall | Answer: "Explain this in 2 minutes" without notes | 5 min | Can explain core concept without reference |
| Day 7 | Implementation Check | Rebuild the mini-task from scratch, no reference | 20 min | Working implementation; ADS ≤ 1 |
| Day 14 | Integration Check | Use this topic inside a broader system (or simulate it) | 30 min | Can integrate; explains integration decisions |
| Day 30 | Interview Simulation | Answer 3 interview-style questions via PROMPT 8 | 20 min | AI scores as PASS on 2 of 3 questions |
| Day 60 | Full Re-Evaluation | Complete PROMPT 3 evaluation if any doubt | 30 min | ML still at prior level or higher |
| Day 90 | Final Confirmation | One question: "Explain + implement core in 5 min" | 10 min | Passes; topic enters long-term retention |

---

### 9.2 Revision Failure Handling

When a revision check reveals decay (topic cannot be recalled or reimplemented):

| Decay Level | Definition | Recovery Action |
|-------------|------------|----------------|
| **Mild** | Can explain but cannot implement | Rebuild mini-task (1 session). Reschedule Day-3 revision from today. |
| **Moderate** | Cannot explain core; confused on details | Re-study the topic (30 min). Rebuild (60 min). Reschedule Day-7 revision from today. |
| **Severe** | Cannot recall what the topic even is | Topic status reverts to IN PROGRESS. Full re-study required. Run Level 1 Escalation. |

More than 2 severe decays in the same week signals: either too many topics in the revision queue (reduce new topic intake), or insufficient implementation during original study (increase implementation depth in current sessions).

---

### 9.3 Revision Load Management

If the AI surfaces more than 4 revision topics in a single day:

1. Prioritize by weight: topics in higher-CRS-weight domains first.
2. Prioritize by time since last evaluation: topics closest to the revision due date first.
3. Carry forward remaining revisions to the next day — but never carry forward more than 2 consecutive days.
4. If 3+ days of revision backlog accumulates: stop new topics. Spend 2 days clearing the backlog exclusively.

Revision backlog is a silent system failure. It means topics are being "learned" without being retained. AI must flag revision backlogs in the weekly report.

---

### 9.4 Revision During Phase Transitions

At the end of each phase, before transitioning to the next phase, a structured revision sweep is required:

**Phase Transition Revision Sweep:**
1. AI identifies all topics completed in the outgoing phase.
2. All topics with a pending Day-7 or Day-14 revision are moved to the transition sweep.
3. Mahesh runs PROMPT 8 (Quick revision, 3 topics per session) across all transition topics over 3 days.
4. Topics that fail the PROMPT 8 check are flagged. If > 20% of the phase's topics fail: the phase is not complete. Continue Phase before transitioning.
5. Topics that pass proceed to their next scheduled revision on the normal spaced repetition schedule.

This sweep takes 3 days maximum and prevents the common failure mode of building new knowledge on top of forgotten foundations.

---

## Section 10 — Weekly Sprint Execution

### 10.1 The Week as a Unit

A study week is not 7 individual days. It is a cohesive sprint with internal structure. The structure ensures that by the end of the week, knowledge gained on Day 1 is integrated, revised, and ready for the following week's work.

**Structural rhythm of a standard study week:**

| Day in Week | Primary Focus | Secondary Focus | Block 3 (Revision) |
|-------------|-------------|-----------------|-------------------|
| Day 1 | New topic — Study phase | Domain track continuation | AI-scheduled revision |
| Day 2 | New topic — Implementation phase | Same topic mini-task | AI-scheduled revision |
| Day 3 | New topic — Complete or continue | 3-day revision of last week's most important topic | AI-scheduled revision |
| Day 4 | New topic or next topic in sequence | Integration work begins | AI-scheduled revision |
| Day 5 | **Integration Session** (see Section 3.4) | Second domain topic | AI-scheduled revision |
| Day 6 | Revision sweep | Fill remaining gaps from the week | All pending Day-7 revisions |
| Day 7 | Weekly review (30 min) + Consolidation Task | Buffer time or secondary domain | 30-day revisions |

---

### 10.2 Weekly Sprint Initiation

Every week begins with a single read-through of the AI-generated weekly plan (from the previous week's PROMPT 4 output). This read-through sets the mental context for the week.

The read takes 3 minutes. It covers:
- The week's primary domain focus and topic sequence
- Any priority interventions or escalations carried from last week
- The 2–3 revision topics most important to address this week
- The week's CRS target and domain health status

After reading: close the weekly plan. Do not refer to it again during the week. The daily plans (PROMPT 1 outputs) handle execution. The weekly plan is context, not a checklist.

---

### 10.3 The Consolidation Task in Context

The weekly Consolidation Task (from `13_SYSTEM_SIMPLIFICATION_RULES.md` Section 3.4) runs on Day 7. Its purpose within the weekly sprint execution is:

1. To confirm that the week's most significant new topic is retained at the level claimed.
2. To produce one high-quality artifact per week that demonstrates integration, not just isolated understanding.
3. To close the week with a success experience — a completed task, independently done, with evidence pushed.

The Consolidation Task is never optional. On shortened weeks (illness, emergency) where days were missed: the Consolidation Task still happens, even if it is the only thing accomplished on Day 7. It is the minimum viable week.

---

### 10.4 Sprint Velocity Tracking

Sprint velocity = topics reaching ML-4+ in a given week.

Target velocities by phase:

| Phase | Target Velocity | Note |
|-------|----------------|------|
| Phase 1 | 3–5 topics/week | Low velocity is expected — foundations take longer to build |
| Phase 2 | 5–8 topics/week | Python + Backend sprint; velocity should rise |
| Phase 3 | 6–10 topics/week | Implementation-heavy; topics in multiple domains complete |
| Phase 4 | 4–6 topics/week | Lower new topic velocity; more revision and evaluation |
| Phase 5 | 2–4 topics/week | Mostly maintenance; main work is applications |

If velocity is consistently below target for 2+ weeks: Level 4 Escalation (CRS Plateau) is likely approaching. AI should flag this proactively.

If velocity is consistently above target: check for quality drift (are topics truly at ML-4, or is the self-check being inflated?). Run 3 random Full Evaluations across domains to calibrate.

---

## Section 11 — AI Responsibilities (Complete Execution Specification)

> This section is the instruction set for any AI agent operating in the Career OS system. Everything here is automatic — Mahesh does not need to request these individually.

---

### 11.1 Pre-Session Responsibilities

Before generating a daily plan (triggered by PROMPT 1), the AI must:

```
☐ Retrieve and parse the previous session's 5-line log.
☐ Confirm the active phase based on CRS trajectory and day count (if known).
☐ Check the revision schedule. Surface any topics overdue by > 1 day.
☐ Check for any active interventions or escalations from previous sessions.
☐ Check domain health for all 10 domains. Flag any at Red health.
☐ Identify the next topic in the active domain's syllabus sequence.
☐ Confirm prerequisites for that topic are at ML-3+.
☐ If prerequisites are not met: reroute to the prerequisite topic instead.
☐ Apply today's phase time profile to determine block durations.
☐ Generate today's mini-task (specific, achievable in Block 2's time allocation).
☐ Output the daily plan in Section 3.3 format of 13_SYSTEM_SIMPLIFICATION_RULES.md.
```

---

### 11.2 Post-Session Responsibilities

After receiving a session log (triggered by PROMPT 2), the AI must:

```
☐ Parse the 5-line log.
☐ Expand to full Framework session log format (Section 6.1 of Mastery Framework).
☐ Score the AI-I dimension: ADS 0 → AI-I 4; ADS 1 → AI-I 3; ADS 2 → AI-I 2;
   ADS 3 → AI-I 1; ADS 4 → AI-I 0.
☐ Score CU (Conceptual Understanding) from the BUILT description.
☐ Score IK (Integration Knowledge) if the session was an Integration Session.
☐ Flag which dimensions require a Full Evaluation to score (IA, DA, IR usually).
☐ Infer mastery level from scored dimensions + Level Guess.
☐ Check ADS trend across last 3 sessions for this topic:
    If ADS is not decreasing → flag ADS stagnation.
    If ADS = 3+ for 2 consecutive sessions → block ML-4 promotion.
☐ Check all 6 Topic Completion Rules (TC-1 through TC-6 of Mastery Framework).
☐ Assign topic status: NOT STARTED / IN PROGRESS / NEEDS EVALUATION / COMPLETE / REGRESSED.
☐ Update the revision schedule. Add this topic to Day 3 revision queue.
☐ Check if any revisions are now past due.
☐ Run the escalation decision tree (Section 8.1 of this file). Flag any triggered level.
☐ Generate tomorrow's plan.
☐ If BLOCKER was reported: provide one targeted diagnostic, not a lecture.
☐ If Level Guess is inconsistent with BUILT description: correct it with explanation.
☐ Output: updated mastery level, status, ADS trend flag, any escalation, tomorrow's plan.
```

---

### 11.3 Weekly Review Responsibilities

After receiving the weekly log batch (triggered by PROMPT 4), the AI must:

```
☐ Parse all session logs from the week.
☐ Compute W1: topics completed this week (target ≥ 5 in Phases 2–3).
☐ Compute W2: topic regressions detected this week (target = 0).
☐ Compute W3: average ADS per domain for the week.
☐ Compute W4: evaluation pass rate (PASS / total evaluations attempted).
☐ Compute W5: CRS delta from last week to this week.
☐ Compute DRS for all 10 domains.
☐ Compute CRS using the weighted formula.
☐ Determine Employment Status.
☐ Check all 4 Hard Constraints.
☐ Compute CADI (weekly average ADS) per domain.
☐ Classify each domain as Green (on track), Yellow (1–2 weeks behind), or Red (>2 weeks behind or failing Hard Constraint).
☐ Identify all Struggling Topics (stuck at ML-3 for > 14 days with no improvement).
☐ Identify the most impactful escalation to address next week (if any).
☐ Generate a Consolidation Task: a 20-minute independent task targeting the week's most important topic.
☐ Build next week's domain track plan using the phase time profile.
☐ Identify the top 5 revision priorities for next week.
☐ Output the full weekly report in Section 3.4 format of 13_SYSTEM_SIMPLIFICATION_RULES.md.
```

---

### 11.4 Proactive Flagging Responsibilities

The AI must proactively flag any of these conditions without waiting to be asked:

| Condition | Flag Type | When to Surface |
|-----------|-----------|-----------------|
| Prerequisite for next topic not yet at ML-3 | Blocking warning | In tomorrow's plan |
| A topic has had ADS ≥ 3 for 3+ consecutive sessions | Dependency warning | In next session feedback |
| CRS trajectory suggests Gate G-X will be missed | Timeline warning | In weekly report |
| A domain is on track to hit Hard Constraint failure | Constraint warning | In weekly report |
| Revision backlog is > 2 days | Backlog warning | In next session feedback |
| Sprint velocity has been below target for 2 weeks | Velocity warning | In weekly report |
| A topic marked Complete has not been revised in > 90 days | Retention alert | In weekly report |

---

## Section 12 — Mahesh Responsibilities

### 12.1 The Non-Negotiable Daily List

These are the only things Mahesh must do every day. Everything else is handled by AI or the system.

```
☐ 1.  Read today's AI-generated plan before starting study (2 min, non-negotiable).
☐ 2.  Study and implement for ≥ 5 hours (any reduced day is logged honestly).
☐ 3.  Keep AI in Mode 0 during all implementation blocks.
☐ 4.  Debug independently for 15 min before escalating to AI.
☐ 5.  Push evidence (GitHub commit or written note) before filing the log.
☐ 6.  Fill the 5-line log honestly. Especially: honest ADS, honest Level Guess.
☐ 7.  Send PROMPT 2 with the day's log attached.
☐ 8.  Read AI feedback (2 min, non-negotiable — the feedback shapes tomorrow's plan).
```

---

### 12.2 The Non-Negotiable Weekly List

```
☐ 1.  Send PROMPT 4 with all week's logs on the last day of the study week.
☐ 2.  Read the weekly report (5 min).
☐ 3.  Complete the Consolidation Task (20 min, independently, with evidence pushed).
☐ 4.  Confirm or adjust next week's plan (3 min).
```

Total weekly admin: 30 minutes.

---

### 12.3 What Mahesh Must NOT Do

These actions break the system. They are listed explicitly because they are common failure modes for motivated learners who try to shortcut the process.

| Prohibited Action | Why It Breaks the System |
|------------------|--------------------------|
| Filing ADS = 0 when AI was used | Corrupts the AI dependency trend. All ADS-based evaluations become invalid. |
| Marking a topic Complete without requesting evaluation | Violates TC-1. False Complete topics inflate DRS and CRS. System gives incorrect plans. |
| Skipping the Quick Self-Check | Removes the daily calibration mechanism. Overconfidence accumulates silently. |
| Studying new topics while revision is overdue by > 3 days | Builds new knowledge on decaying foundations. Leads to confusion and regressions. |
| Filing no log on study days (even short days) | AI has no data. Next day's plan is based on outdated state. System degrades rapidly without daily logs. |
| Looking up answers during an evaluation | Makes the evaluation score meaningless. The score then drives wrong plan generation. |
| Switching domains mid-session when a topic gets hard | The difficulty IS the learning moment. Switching avoids it and creates permanent weak spots. |
| Watching tutorial content passively without pausing to implement | Produces familiarity without proof. All tutorial time must include implementation pauses. |

---

### 12.4 The Telecom Professional Advantage — How to Leverage It Daily

Mahesh's 8+ years in telecom is an asset in every single study domain. Here is how to activate it consciously:

| Domain | Telecom Connection | How to Use It |
|--------|--------------------|--------------|
| Computer Networks | Telecom IS networking — routing, switching, protocols, uptime | CN theory is not abstract; cross-reference with operational experience |
| Operating Systems | Telecom systems run on Linux at scale; systemd, process management is familiar | OS practical sections will feel comfortable; move through them faster |
| Backend Architecture | Network reliability, redundancy, failover thinking directly transfers | When studying 12-Factor App, SLAs, monitoring — connect to telecom practices |
| System Design | Experience with large-scale systems, capacity planning, vendor management | Use in Backend Tier 8-10 topics and in interview architectural discussions |
| Communication | 8 years of professional stakeholder communication, reports, escalation handling | The professional communication module is largely already mastered; focus on technical register |
| Debugging | Telecom fault management, RCA processes, ticket escalation | Debugging mindset already developed; apply it to code systematically |

In any interview: the telecom background is introduced as context, not as a career gap. "I spent 8 years operating large-scale network infrastructure — I understand reliability, monitoring, and system behaviour at scale. I'm now building software to solve the problems I saw in that world." This positions the career change as a progression, not a restart.

---

## Section 13 — Failure Recovery System

### 13.1 Failure Taxonomy

Not all disruptions are equal. Different failures require different responses. Attempting to recover from a motivation collapse the same way as a missed day will make both worse.

| Code | Failure Type | Detection Signal |
|------|-------------|-----------------|
| F-1 | Missed Study Day | No log filed; study hours = 0 |
| F-2 | Partial Day (< 3 hours) | Log filed; study hours < 3 |
| F-3 | Topic Stuck — Early (3–5 sessions) | No ML improvement across sessions |
| F-4 | Topic Stuck — Chronic (> 5 sessions) | ADS not decreasing; ML unchanged |
| F-5 | Domain Stall | 0 Complete topics in 10+ days |
| F-6 | AI Dependency Not Decreasing | CADI > 3.0 for 2+ weeks |
| F-7 | Motivation / Energy Collapse | Consistently < 3 hours for 3+ consecutive days |
| F-8 | External Disruption (illness, emergency) | Interruption with uncertain duration |
| F-9 | Failed Live Interview | Interview completed; rejection or no-pass on technical round |
| F-10 | CRS Plateau | CRS unchanged for 3+ weeks |

---

### 13.2 Recovery Protocols

**F-1: Missed Study Day**

Root causes: scheduling conflict, illness, social obligation, avoidance.

Recovery:
- Do not attempt to "make up" the missed day by studying 12 hours the next day. This leads to F-7.
- File a retroactive log entry: `TOPIC: None / ADS: N/A / BLOCKER: Day missed — [one reason] / LEVEL GUESS: N/A`
- Resume the normal schedule the next day. The missed day is recorded and forgotten.
- If the same day of the week is missed 3 weeks in a row: that time slot has a structural conflict. Adjust the schedule permanently.

Recovery time: 0 days. Resume immediately.

---

**F-2: Partial Day (< 3 hours)**

Root causes: fatigue, poor focus, external interruption.

Recovery:
- File an honest log with actual study time in the BUILT field.
- Do not extend tomorrow's session to compensate (leads to fatigue compounding).
- Identify whether this is a pattern (3+ partial days in a week) or isolated.
- Isolated: proceed normally. Pattern: investigate root cause (sleep, nutrition, study environment, topic difficulty).

Recovery time: 0 days. Resume normally.

---

**F-3: Topic Stuck — Early (3–5 sessions)**

Root causes: missing prerequisite, insufficient implementation attempts, wrong resource.

Recovery:
1. Write down specifically: "I can do X. I cannot do Y." (takes 2 minutes).
2. Check the dependency chain. Is there a prerequisite topic at ML-2 that should be ML-3?
3. If prerequisite gap: pause the stuck topic. Study the prerequisite. Return to stuck topic.
4. If no prerequisite gap: the resource is the problem. Switch resource (different doc section, or targeted video).
5. If resource is fine: do a minimum viable implementation — smallest possible working piece. Not the whole topic. One function.

Recovery time: 1–3 sessions.

---

**F-4: Topic Stuck — Chronic (> 5 sessions)**

Root causes: all F-3 causes plus deep conceptual gap, wrong mental model, insufficient practice volume.

Recovery:
1. Send PROMPT 5. Provide honest answers to all AI diagnostic questions.
2. AI breaks the topic into 3–5 sub-components.
3. Work sub-components in order. Each sub-component is treated as a separate topic with its own mini-task and evidence.
4. Do not attempt the parent topic evaluation until all sub-components are at ML-3.
5. This process takes 5–10 sessions. Do not rush it.

The chronic stuck topic is often a sign that the topic should not have been started — a prerequisite is at ML-1 or ML-2. The sub-component breakdown usually reveals this within the first session.

Recovery time: 5–10 sessions.

---

**F-5: Domain Stall**

Root causes: chronic stuck topic blocking the domain; time allocation too low; topic sequence incorrect; resource consistently inappropriate.

Recovery: Level 2 Escalation protocol (Section 8.2). Three consecutive deep-focus days on that domain.

Recovery time: 5–10 days.

---

**F-6: AI Dependency Not Decreasing**

Root causes: habit of going to AI before attempting independently; quick-fix pattern; missing the 15-minute rule.

Recovery: Level 3 Escalation — AI-Free Day in the affected domain. Forces a calibration reset.

Recovery time: 1 AI-Free Day plus 1 week of Mode 1-only AI usage in that domain.

**Root prevention:** The 15-minute rule. Every single time. No exceptions. Not "I'm busy today so I'll just ask AI." The habit of attempting first must be inviolable, or AI dependency compounds indefinitely.

---

**F-7: Motivation / Energy Collapse**

Detection: Consistently < 3 hours/day for 3+ consecutive days despite no external disruption.

Root causes: burnout, isolation, unclear progress, outcome anxiety, unrealistic expectations.

Recovery — in order:
1. Take one full rest day (no study, no logs). A real rest day.
2. After the rest day: send PROMPT 7. Get the full system status with CRS and domain health.
3. Seeing concrete progress numbers often resolves motivation collapses that were rooted in "I feel like I'm not making progress."
4. If the CRS shows real progress: identify the specific fear or doubt causing the collapse. Name it. Write it down.
5. If the CRS shows genuine slow progress: diagnose root cause (F-3, F-5, F-10) and address it structurally.
6. Return to 4-hour sessions (not 6) for 3 days. Rebuild momentum before returning to 6 hours.

**What does NOT help:** Watching motivational videos. Re-reading the roadmap. Reorganizing files and folders. These create the feeling of progress without actual study. They are avoidance.

Recovery time: 3–5 days.

---

**F-8: External Disruption**

Examples: illness for 5+ days, family emergency, job change, relocation.

Recovery:
- Do not try to maintain full study during an active emergency. Log honestly.
- On return: do not attempt to resume at full intensity immediately. 3-day ramp back (4 hours → 5 hours → 6 hours).
- Run a quick system audit via PROMPT 7 to see what the disruption cost in CRS terms.
- AI recalibrates the roadmap based on current state. Gate dates shift accordingly.
- The 180-day timeline is a planning horizon, not a deadline. If 195 days produces the employment offer, that is not failure.

Recovery time: Ramp period of 3 days plus whatever time was lost.

---

**F-9: Failed Live Interview**

Definition: Technical round rejection. Not a "no-offer" after offer stage.

Recovery — this is not failure, it is data:
1. Immediately after the interview (same day): write a post-interview analysis.
   - What questions were asked?
   - Which questions could not be answered?
   - Which answers were weak?
   - What was the interviewer's reaction to the project walkthrough?
2. Send the post-interview analysis to AI with PROMPT 5 context. AI maps each gap to a specific topic in the syllabus.
3. Those topics become the next week's primary focus (Level 5 Escalation protocol if another interview is scheduled soon).
4. Do not stop applying during recovery. Continue sending applications while addressing the gaps.

**The failure-learning loop is the fastest path to passing:**
Failed interview → specific gap identified → gap addressed → next interview → faster pass rate.

Recovery time: 1 week of targeted gap-filling per failed interview.

---

**F-10: CRS Plateau**

Recovery: Level 4 Escalation — 7-day Completion Sprint on the 3 highest-impact bottleneck topics.

Recovery time: 7–14 days.

---

### 13.3 The No-Shame Principle

The failure recovery system exists because failures are expected. 180 days of daily study without any missed days, stuck topics, or motivation collapses is not a realistic plan — it is a fantasy. The system is designed to absorb disruptions and continue.

Every failure code has a defined recovery path. Every recovery path is finite. No failure is permanent. The only genuine failure is stopping without completing the recovery protocol.

The logs record everything — both progress and failures. The record is not a judgement. It is a tool. An honest record of a difficult week is more valuable than an optimistic record of an easy one.

---

## Appendix A — Daily Execution Quick Reference

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DAILY EXECUTION — DECISION-FREE SEQUENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MORNING (2 min):
1. Run morning decision engine (Section 2.1)
2. Read today's AI plan
3. Open syllabus file and blank code file
4. Start timer

DSA BLOCK (60–75 min):
5. DSA session — external system governs this

BLOCK 1 — STUDY (per phase time profile):
6. Calibrate: what do I already know?
7. Read official docs (≤ 40 min)
8. Close all references

BLOCK 2 — IMPLEMENT (per phase time profile):
9. AI is OFF
10. Build the mini-task from scratch
11. Debug independently for 15 min first
12. Commit to GitHub when done

BLOCK 3 — REVISION (per phase time profile):
13. AI-scheduled revision topics
14. Use PROMPT 6 or PROMPT 8

BLOCK 4 — ADMIN (5 min):
15. Fill 5-line log (2 min)
16. Push evidence if not already pushed (1 min)
17. Send PROMPT 2 (30 sec)
18. Read AI feedback (90 sec)
19. Done

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THE THREE THINGS THAT CANNOT BE SKIPPED:
  1. AI plan read (morning)
  2. Evidence push (before log)
  3. 5-line log (honest)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Appendix B — Session Quality Checklist

> Run this once a week, not daily. It is a calibration tool, not a ritual.

```
☐ Are my ADS scores trending downward month-over-month?
☐ Is my implementation block genuinely AI-free?
☐ Can I explain the last 5 topics I completed without looking them up?
☐ Are my GitHub commits named specifically (topic + what was built)?
☐ Am I attempting implementation before asking AI for help?
☐ Is the 15-minute debugging rule being honored?
☐ Are evaluation sessions run before marking topics Complete?
☐ Is my weekly log honest about partial days and stuck topics?
☐ Is revision happening or is the backlog growing?
☐ Am I doing theory topics in write-to-understand mode, not just reading?
```

If more than 3 boxes are unchecked: the system is drifting. Address the unchecked items before adding new topics.

---

*This engine runs every day. Not when motivation is high. Not when it feels productive. Every day. The gap between knowing what to do and doing it is exactly what this engine is designed to close.*
