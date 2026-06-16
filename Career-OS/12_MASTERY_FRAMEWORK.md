# Mahesh Career OS — Mastery Framework

> **File:** `12_MASTERY_FRAMEWORK.md`
> **Version:** 1.0
> **Purpose:** Governing framework for all learning, evaluation, planning, progress tracking, and adaptation across the Career OS.
> **Authority:** This file overrides all other definitions of progress, completion, and readiness. When any other file conflicts with this framework, this file takes precedence.
> **Scope:** All 10 domains in Career OS. DSA is explicitly excluded.

---

## IMPORTANT: How AI Agents Must Use This File

When this file is provided to an AI agent alongside any Career OS syllabus file, the agent must:

1. Use the **Universal Mastery Levels** (Section 2) to assess every topic.
2. Use the **Evaluation Dimensions** (Section 3) as the rubric for every evaluation.
3. Use the **AI Dependency Scoring System** (Section 4) to score every session.
4. Apply the **Topic Completion Rules** (Section 5) before marking any topic done.
5. Apply the **Promotion Rules** (Section 10) before advancing to any next level/tier.
6. Compute the **Career Readiness Score** (Section 12) when a full-system assessment is requested.
7. Never accept self-reported mastery as evidence. Always require demonstrated performance.

---

## Section 1 — Mastery Philosophy

### 1.1 Core Principles

**Principle 1: Real Mastery Is Independent Performance**
A topic is not mastered because it was read, watched, or discussed. A topic is mastered when the learner can perform it independently — without AI assistance, without copying, without prompting. Everything else is exposure, not mastery.

**Principle 2: AI Is a Learning Accelerator, Not a Crutch**
AI tools are permitted for learning. They are permitted for initial understanding. They are permitted for checking work. They are NOT a substitute for independent thinking. The goal of every learning session is to transfer capability from AI to brain. If AI dependency is not decreasing over time on a topic, the topic is not being learned — it is being outsourced.

**Principle 3: False Progress Is Worse Than No Progress**
Marking a topic "done" when it is not done creates debt. False progress leads to gaps that collapse during interviews. The framework is deliberately strict. A topic marked incomplete is honest feedback. A topic marked complete incorrectly is a lie that costs you the job.

**Principle 4: Understanding Before Implementation, Implementation Before Interview**
The sequence is: conceptual understanding → implementation with reference → implementation without reference → explanation under pressure. Skipping stages creates fragile knowledge that fails in interviews. No topic advances until the current stage is genuinely solid.

**Principle 5: Production Thinking Always**
Every topic is evaluated with the question: "Could Mahesh use this in a real production codebase?" Not "has he seen it?", not "can he copy an example?", but "can he apply it under uncertainty, with real constraints, on unfamiliar code?" This standard sets the bar.

**Principle 6: Interview Readiness Is Non-Negotiable**
The final purpose of this system is employment. Every topic must be evaluated against interview standards, not just job performance standards. These are different. An engineer may know SQL deeply but be unable to explain it under interview pressure. Both dimensions must be tracked separately.

### 1.2 What This Framework Is Not

- It is NOT a study plan. Study plans are generated separately using this framework.
- It is NOT a roadmap. Roadmaps are generated separately.
- It is NOT a timeline. No dates are embedded here.
- It is NOT a motivational tool. It is a precise measurement system.

---

## Section 2 — Universal Mastery Levels (ML-0 through ML-6)

> These levels apply to every individual topic across all 10 domains. The same scale is used for Python decorators, SQL window functions, OS scheduling, and interview communication.

---

### ML-0 — Unaware

**Definition:** The learner has not encountered this topic. It does not exist in their mental model.

**Characteristics:**
- Cannot name the topic
- Cannot describe what problem it solves
- No awareness that the concept exists

**Evidence Required to Assign:** (none — this is the default state for untouched topics)

**Promotion to ML-1:** First encounter with the topic (reading, watching, hearing) is sufficient.

---

### ML-1 — Exposed

**Definition:** The learner has encountered the topic but cannot explain it or use it independently.

**Characteristics:**
- Has read about it or seen it mentioned
- Can name the topic
- Cannot explain what it does in own words
- Cannot write any code or query related to it from scratch
- Would require AI to do anything practical with it

**Evidence Required to Assign:** Learner has completed at least one pass of study materials (reading, video, notes).

**Promotion to ML-2:** Must pass a verbal explanation test: explain the topic in plain English in 3-5 sentences without referencing notes.

---

### ML-2 — Understood

**Definition:** The learner can explain the topic clearly but cannot implement it without assistance.

**Characteristics:**
- Can explain what the topic is and why it exists
- Can explain it to both technical and non-technical audiences
- Cannot implement it from scratch without AI or reference
- If asked to code it, would need to look up syntax or structure
- Can answer "what is X?" but not "write X" or "debug X"

**Evidence Required to Assign:**
- Explain the topic verbally in ≥ 3 sentences: what it is, why it exists, when to use it
- Correctly answer 2 conceptual questions about it

**Promotion to ML-3:** Successfully implement a minimal working example using AI assistance or reference materials.

---

### ML-3 — Guided Implementation

**Definition:** The learner can implement the topic but requires assistance (AI, documentation, or worked examples) during implementation.

**Characteristics:**
- Can implement with AI scaffolding
- Understands what the AI-suggested code does after reading it
- Cannot implement from a blank file without help
- Makes multiple implementation errors that require AI to diagnose
- Cannot debug novel errors related to this topic independently
- AI Dependency Score ≥ 3 on most sessions involving this topic

**Evidence Required to Assign:**
- Implement a working example with AI/reference assistance
- Be able to explain every line of the resulting code

**Promotion to ML-4:** Implement the same or equivalent task from scratch without AI assistance. Only documentation (official docs, not StackOverflow answers or AI) is permitted.

---

### ML-4 — Independent Implementation

**Definition:** The learner can implement the topic from scratch without AI assistance. Documentation may be referenced for syntax specifics.

**Characteristics:**
- Can open a blank file and implement from memory
- Knows the structure, the logic, the gotchas
- May reference official documentation for exact parameter names or edge cases
- Can debug common errors independently
- Does NOT use AI to figure out what to write
- AI Dependency Score ≤ 1 on sessions involving this topic
- Can answer most interview questions on the topic

**Evidence Required to Assign:**
- Complete a timed implementation task (30-45 minutes) without AI assistance
- Achieve AI Dependency Score of 0 or 1 for the session
- Pass 4 out of 5 evaluation questions (see Section 3)

**This is the MINIMUM ACCEPTABLE mastery level for any topic to be counted as "completed" in the Career OS progress tracker.**

**Promotion to ML-5:** Implement the topic in an integrated context (multiple topics working together), explain all decisions, and answer all 5 evaluation questions correctly.

---

### ML-5 — Fluent

**Definition:** The learner has internalized the topic. Implementation is fast and correct. Explanation is clear and complete. Interview performance is strong.

**Characteristics:**
- Implements without hesitation or second-guessing
- Can explain under interview pressure (time-limited, adversarial questioning)
- Catches own mistakes and corrects them before running code
- Can discuss tradeoffs, edge cases, and alternatives confidently
- AI Dependency Score = 0 on all sessions involving this topic
- Zero documentation needed for core implementation
- Can teach this topic to another person

**Evidence Required to Assign:**
- Complete a mock interview question on this topic with a passing score
- Explain tradeoffs and alternatives without prompting
- Achieve AI Dependency Score of 0 for 3 consecutive sessions involving this topic

**Promotion to ML-6:** Demonstrate ability to design a system or architecture that incorporates this topic as a component, not just as a skill in isolation.

---

### ML-6 — Expert

**Definition:** The learner's knowledge of this topic exceeds what is needed for the target job level. They can teach it, optimize it, and design around it.

**Characteristics:**
- Can teach the topic to others clearly
- Knows non-obvious edge cases and failure modes
- Knows historical context, alternatives, and evolution
- Can spot misuse of this topic in other people's code
- Can design systems that use this topic optimally
- Has encountered real failure modes through building

**Evidence Required to Assign:**
- Write a technical explanation (blog post or document) that could be published
- Identify a non-obvious bug or misuse in a provided code sample

**Note:** ML-6 is NOT required for employability. ML-4 to ML-5 is the employment target. ML-6 develops naturally with experience on the job.

---

### Mastery Level Summary Table

| Level | Name | AI Dependency | Can Explain | Can Implement | Interview Ready |
|-------|------|--------------|-------------|---------------|----------------|
| ML-0 | Unaware | N/A | No | No | No |
| ML-1 | Exposed | N/A | Partially | No | No |
| ML-2 | Understood | N/A | Yes | No | Partially |
| ML-3 | Guided Implementation | ≥ 3 | Yes | With help | Partially |
| ML-4 | Independent Implementation | ≤ 1 | Yes | Yes | Mostly |
| ML-5 | Fluent | 0 | Fully | Yes, fast | Yes |
| ML-6 | Expert | 0 | Fully + teach | Yes, optimized | Exceeds |

---

## Section 3 — Evaluation Dimensions

> Every topic evaluation uses these 6 dimensions. Each dimension is scored 0–4.

---

### Dimension 1: Conceptual Understanding (CU)

**What is measured:** Can the learner explain the topic clearly, correctly, and completely — in their own words, without referencing notes?

| Score | Description |
|-------|-------------|
| 0 | Cannot explain. No coherent response. |
| 1 | Partial explanation with significant gaps or errors. |
| 2 | Mostly correct explanation but missing key aspects. |
| 3 | Correct and complete explanation with minor gaps. |
| 4 | Complete, precise explanation including edge cases and why it matters. |

**Required score for ML-4:** ≥ 3
**Required score for ML-5:** 4

---

### Dimension 2: Implementation Ability (IA)

**What is measured:** Can the learner write correct, working code/query/configuration for this topic from scratch?

| Score | Description |
|-------|-------------|
| 0 | Cannot write anything functional. |
| 1 | Writes code that is structurally wrong or does not run. |
| 2 | Writes code that runs but has logic errors or incomplete coverage. |
| 3 | Writes correct, working code with minor issues (style, efficiency). |
| 4 | Writes clean, idiomatic, correct code on the first attempt. |

**Required score for ML-4:** ≥ 3
**Required score for ML-5:** 4

---

### Dimension 3: Debugging Ability (DA)

**What is measured:** When presented with broken code or a failing scenario related to this topic, can the learner identify and fix the issue?

| Score | Description |
|-------|-------------|
| 0 | Cannot identify the problem. |
| 1 | Identifies the general area but cannot fix it. |
| 2 | Fixes the specific issue but cannot explain why it was broken. |
| 3 | Identifies, fixes, and explains the root cause. |
| 4 | Identifies, fixes, explains, and identifies related failure modes. |

**Required score for ML-4:** ≥ 2
**Required score for ML-5:** ≥ 3

---

### Dimension 4: Integration Knowledge (IK)

**What is measured:** Does the learner understand how this topic connects to adjacent topics and the broader system?

| Score | Description |
|-------|-------------|
| 0 | Cannot connect this topic to anything else. |
| 1 | Names adjacent topics but cannot explain the relationship. |
| 2 | Explains how this topic connects to 1-2 adjacent topics. |
| 3 | Explains integration patterns with multiple adjacent topics correctly. |
| 4 | Can design a system that uses this topic in combination with others; aware of interaction effects. |

**Required score for ML-4:** ≥ 2
**Required score for ML-5:** ≥ 3

---

### Dimension 5: Interview Readiness (IR)

**What is measured:** Can the learner answer this topic's interview questions under simulated pressure — concise, clear, and correct?

| Score | Description |
|-------|-------------|
| 0 | Cannot answer basic questions on this topic. |
| 1 | Partial answers; significant hesitation or errors. |
| 2 | Answers basic questions; struggles with follow-up or edge cases. |
| 3 | Answers most questions correctly; handles follow-ups reasonably. |
| 4 | Answers all questions correctly, confidently, and concisely. |

**Required score for ML-4:** ≥ 2
**Required score for ML-5:** ≥ 3

---

### Dimension 6: AI Independence (AI-I)

**What is measured:** How little AI assistance was required during the learning session or evaluation for this topic?

| Score | Description |
|-------|-------------|
| 0 | AI wrote all code / AI explained every step. Learner was a passive observer. |
| 1 | AI debugged issues and suggested structure. Learner wrote some code. |
| 2 | AI answered specific questions. Learner wrote most code independently. |
| 3 | AI used only to verify finished work. Learner wrote all code. |
| 4 | No AI used. Fully independent. Documentation (official only) permitted. |

**Required score for ML-4:** ≥ 3
**Required score for ML-5:** 4

> Note: AI-I score of 4 means exactly that — zero AI interaction during implementation. Official documentation is not AI.

---

### Topic Score Computation

For any topic, the **Topic Mastery Score (TMS)** is computed as:

```
TMS = (CU + IA + DA + IK + IR + AI-I) / 24 × 100

Where 24 = maximum possible score (6 dimensions × 4 max each)
```

| TMS Range | Corresponding Mastery Level |
|-----------|---------------------------|
| 0–16% | ML-0 or ML-1 |
| 17–33% | ML-2 |
| 34–54% | ML-3 |
| 55–74% | ML-4 |
| 75–91% | ML-5 |
| 92–100% | ML-6 |

**Minimum TMS to count a topic as Complete: 55% (ML-4 threshold)**

---

## Section 4 — AI Dependency Scoring System

> This system tracks and enforces the reduction of AI dependency over time. It is separate from the Evaluation Dimensions because it must also be tracked longitudinally, not just per evaluation.

---

### 4.1 AI Dependency Score (ADS) — Per Session

Every study or practice session receives an **AI Dependency Score** on a 0–4 scale:

| ADS | Label | Description |
|-----|-------|-------------|
| 4 | Fully Dependent | AI wrote code, explained logic, and structured the solution. Learner followed along. |
| 3 | Heavily Assisted | AI wrote key parts. Learner could not continue without AI prompting. Used AI to understand errors. |
| 2 | Moderately Assisted | AI helped debug and answered specific questions. Learner wrote structure independently. |
| 1 | Minimally Assisted | AI used to verify or check finished work only. No implementation help. |
| 0 | Fully Independent | Zero AI interaction. May have used official documentation. |

---

### 4.2 Acceptable ADS by Mastery Stage

| Learner is working at... | Maximum Acceptable ADS |
|--------------------------|----------------------|
| First pass of a topic (ML-0 → ML-1) | 4 (full AI use to understand) |
| Learning to implement (ML-1 → ML-3) | 3 (AI scaffolding is expected) |
| Building independent skill (ML-3 → ML-4) | 2 (transitioning away from AI) |
| Proving independence (ML-4 evaluation) | 1 (verify only; no implementation help) |
| Fluency practice (ML-5 target) | 0 (no AI, no exceptions) |

---

### 4.3 AI Dependency Trend Rule

The ADS must trend downward on any topic over consecutive sessions. Specifically:

**Rule ADS-1:** If a topic has been studied for ≥ 3 sessions and the ADS has not decreased by at least 1 point from session 1 to session 3, the topic's mastery level must be downgraded by 1 level.

**Rule ADS-2:** If a topic's last 2 evaluations both have ADS ≥ 3, the topic cannot be promoted to ML-4 regardless of other scores.

**Rule ADS-3:** If a topic was previously evaluated at ML-4 and a subsequent session shows ADS ≥ 2, the topic is flagged for re-evaluation. It retains ML-4 until re-evaluated, but cannot be counted toward domain readiness until the re-evaluation confirms ML-4.

**Rule ADS-4:** Any topic used in a project or real implementation context automatically has its ADS ceiling reduced by 1 for future evaluations. (If you built it in a real project, you should be less dependent on AI for it.)

---

### 4.4 Cumulative AI Dependency Index (CADI)

The CADI is a domain-level metric computed weekly:

```
CADI = Average ADS across all sessions in the domain during the past week

Scale:
CADI 3.0–4.0 → AI Crutch Zone (serious concern)
CADI 2.0–2.9 → Learning Zone (acceptable for early stages)
CADI 1.0–1.9 → Independence Zone (target for productive study)
CADI 0.0–0.9 → Mastery Zone (ML-5 territory)
```

**Weekly Target:** CADI ≤ 2.0 for any domain where the learner is beyond their first 2 levels.

---

### 4.5 AI Usage That Is Always Permitted (Never Penalized)

The following AI uses do NOT count toward AI Dependency and do not increase ADS:

1. Using AI to generate **evaluation questions** to test yourself
2. Using AI to **check completed work** after finishing (not during)
3. Using AI to **plan what to study** (not how to do it)
4. Using AI to **explain a concept** during first-pass learning (ML-0 → ML-1 only)
5. Using AI to **review code for style or best practices** after independently writing it
6. Using AI to **simulate an interviewer** asking questions

---

### 4.6 AI Usage That Always Increases ADS to ≥ 3

The following uses immediately cap ADS at 3 or 4 for that session:

1. Asking AI "write this code for me" or equivalent
2. Asking AI "what should I write here?" during implementation
3. Asking AI to debug code before attempting to debug independently
4. Copy-pasting AI output into a project without understanding each line
5. Using AI-generated code as the starting template for a task

---

## Section 5 — Topic Completion Rules

> A topic is counted as **Complete** in the Career OS system ONLY when ALL of the following rules are satisfied simultaneously.

---

### Rule TC-1: Minimum Mastery Level

The topic must be evaluated at **ML-4 (Independent Implementation)** or higher.

No exceptions. ML-3 is not complete. A topic studied but not independently implementable is not complete.

---

### Rule TC-2: Minimum Evaluation Dimension Scores

All 6 evaluation dimensions must meet their ML-4 thresholds:

| Dimension | Minimum Score for Completion |
|-----------|------------------------------|
| Conceptual Understanding (CU) | ≥ 3 |
| Implementation Ability (IA) | ≥ 3 |
| Debugging Ability (DA) | ≥ 2 |
| Integration Knowledge (IK) | ≥ 2 |
| Interview Readiness (IR) | ≥ 2 |
| AI Independence (AI-I) | ≥ 3 |

If any single dimension is below threshold, the topic is **not complete** regardless of overall TMS.

---

### Rule TC-3: Mini-Task Requirement

Every topic must have a corresponding **Mini-Task** completed:

- **Mini-Task:** A small, focused implementation exercise that requires applying only the topic at hand.
- The Mini-Task must be completed **without AI assistance** (ADS ≤ 1).
- The Mini-Task result must be committed to GitHub (public repository) or documented in the session log.
- Examples:
  - Python Decorators: Write a `@retry(times=3)` decorator from scratch.
  - SQL Window Functions: Write a query that ranks employees by salary within each department.
  - Django ORM: Write a query using `select_related` that eliminates an N+1 problem.
  - OS — Deadlocks: Explain the Coffman conditions and write pseudocode for Banker's Algorithm.

---

### Rule TC-4: No Recent Regression

The topic must not have failed an evaluation in the **7 days preceding** the completion mark. If a topic was at ML-4, then failed an evaluation (scored ML-3 or lower), it must be re-evaluated and pass before the completion mark is restored.

---

### Rule TC-5: Explanation Requirement

The learner must be able to explain the topic verbally (or in writing) in response to the question: *"Explain [topic] to me as if I'm a technical interviewer who wants to assess depth, not just definition."*

This must be assessed via an AI-administered verbal evaluation or written explanation session.

---

### Rule TC-6: Theory-Only Topics

For topics that are inherently theoretical and have no direct implementation (e.g., OS Coffman Conditions, CAP Theorem, Normalization theory):

- Rule TC-3 (Mini-Task) is modified: the task is a **written explanation or worked example** rather than a code implementation.
- All other rules still apply.
- AI Independence is measured by whether the explanation was generated independently.

---

### Completion Status Definitions

| Status | Description |
|--------|-------------|
| **NOT STARTED** | ML-0. No study has occurred. |
| **IN PROGRESS** | ML-1 to ML-3. Being studied, not yet complete. |
| **NEEDS EVALUATION** | Study is done but formal evaluation not yet performed. Cannot be called Complete without evaluation. |
| **COMPLETE** | ML-4+, all TC rules satisfied. Counts toward domain progress. |
| **REGRESSED** | Was Complete, failed a subsequent evaluation. Flagged. Requires re-evaluation. |
| **EXEMPT** | Topic explicitly marked out of scope (none currently; all topics in syllabi are in scope). |

---

## Section 6 — Daily Evaluation Process

> This process must be executed at the END of every study day. It takes 15–20 minutes. Skipping it breaks the feedback loop.

---

### 6.1 Daily Session Log (Required Fields)

Every study session must produce a log entry with these fields:

```
DATE: [YYYY-MM-DD]
DOMAIN: [Python / Backend / SQL / DBMS / OS / CN / Frontend / Cloud / Communication / Job Prep]
TOPIC: [Exact topic name from the relevant syllabus file]
SYLLABUS_REFERENCE: [e.g., 02_PYTHON_SYLLABUS.md — Level 4 — 4.3 Inheritance]
STUDY_DURATION_MINUTES: [actual time spent]
PRIOR_MASTERY_LEVEL: [ML-0 through ML-6]

WHAT WAS DONE:
[ ] Read/watched material
[ ] Took notes
[ ] Attempted implementation
[ ] Completed mini-task
[ ] Ran evaluation questions
[ ] Debugged code
[ ] Built something integrating this topic

AI DEPENDENCY SCORE: [0–4] — see Section 4.1
AI USAGE DESCRIPTION: [What specifically was AI used for, if anything]

EVALUATION RESULTS:
CU score: [0–4]
IA score: [0–4]
DA score: [0–4]
IK score: [0–4]
IR score: [0–4]
AI-I score: [0–4]
TMS: [computed]

NEW MASTERY LEVEL: [ML-0 through ML-6]
TOPIC STATUS: [NOT STARTED / IN PROGRESS / NEEDS EVALUATION / COMPLETE / REGRESSED]

BLOCKERS:
[What stopped progress, if anything]

TOMORROW'S FOCUS:
[What must happen next for this topic]
```

---

### 6.2 Daily Self-Evaluation Protocol

At the end of each session, the learner must answer these questions:

**Q1 — Can I explain this topic without notes?**
(Tests CU) — Attempt a 90-second verbal or written explanation. Score it.

**Q2 — Can I implement this from a blank file?**
(Tests IA) — Close all tabs. Open a blank file. Write the core implementation. Give yourself 20 minutes.

**Q3 — Can I debug this broken code?**
(Tests DA) — If an AI agent is available: ask it to introduce a bug in the implementation. Try to find and fix it.

**Q4 — How does this connect to what I already know?**
(Tests IK) — Name 2 adjacent topics and explain how they interact with today's topic.

**Q5 — Could I answer this in an interview right now?**
(Tests IR) — Simulate 2 interview questions on this topic. Answer them aloud or in writing.

---

### 6.3 Daily Study Hour Allocation Reference

This is a reference allocation. The actual plan is managed separately. This framework defines the **minimum time per activity type** per study day:

| Activity | Minimum Daily Time |
|----------|--------------------|
| New topic study (reading + notes) | 60 minutes |
| Implementation practice | 90 minutes |
| Evaluation / self-testing | 30 minutes |
| Revision of prior topics | 30 minutes |
| **Total minimum** | **210 minutes (3.5 hours)** |

With 6 hours available daily, remaining 2.5 hours goes to deeper implementation, projects, or catch-up.

---

### 6.4 Evaluation Question Bank (AI Agent Instruction)

When an AI agent is asked to evaluate a topic, it must generate and administer questions in these categories:

**Type 1 — Definition Questions (tests ML-2)**
Format: "What is [topic]? Why does it exist?"
Example: "What is a generator in Python? Why would you use it instead of a list?"

**Type 2 — Comparison Questions (tests ML-2 to ML-3)**
Format: "What is the difference between [X] and [Y]?"
Example: "What is the difference between `select_related` and `prefetch_related`?"

**Type 3 — Implementation Questions (tests ML-4)**
Format: "Write [implementation]."
Example: "Write a Python decorator that logs execution time of any function."

**Type 4 — Debugging Questions (tests ML-4 DA)**
Format: "Here is broken code. Find and fix the error. Explain why it was broken."

**Type 5 — Integration Questions (tests ML-4 IK)**
Format: "How would you use [topic] in a real Django/React/SQL application?"
Example: "Where would you use a covering index in a Django-backed API?"

**Type 6 — Tradeoff Questions (tests ML-5)**
Format: "When would you NOT use [topic]? What are its limitations?"
Example: "When would you choose session-based auth over JWT?"

**Type 7 — Scenario Questions (tests ML-5)**
Format: "You are debugging a production issue. The symptoms are [X]. How do you investigate?"

---

## Section 7 — Weekly Review Process

> This process must be executed at the END of every study week (Sunday or final day of study that week). It takes 60–90 minutes.

---

### 7.1 Weekly Metrics to Compute

At every weekly review, compute the following:

**Metric W1 — Topics Completed This Week**
Count of topics reaching Complete status this week.
Target: ≥ 5 topics per week across all domains.

**Metric W2 — Topics Regressed This Week**
Count of topics falling from Complete to Regressed.
Target: 0. Any regression > 0 triggers a revision audit.

**Metric W3 — Average ADS This Week (Per Domain)**
Sum of all session ADS values ÷ number of sessions.
Target: ≤ 2.0 for any active domain.

**Metric W4 — Evaluation Pass Rate**
Topics that passed their evaluation on first attempt ÷ total topics evaluated.
Target: ≥ 70%. Below 70% means the domain is being rushed.

**Metric W5 — Career Readiness Score (CRS)**
Computed as per Section 12.
Track week-over-week delta.

---

### 7.2 Weekly Review Protocol

**Step 1: Score Summary (15 minutes)**
- Fill in Metrics W1–W5.
- Compare to prior week.
- Note any domains where ADS is increasing (red flag).

**Step 2: Regression Audit (15 minutes)**
- For every regressed topic: identify the root cause.
  - Was it not studied enough initially?
  - Was AI dependency too high during initial learning?
  - Was the mini-task skipped?
- Add regressed topics to next week's revision queue with higher priority.

**Step 3: Domain Health Check (15 minutes)**
Per domain, answer:
- Is CADI ≤ 2.0? If not, why?
- Are any topics stuck at ML-3 for > 2 weeks? If yes, intervention needed.
- Are all promoted topics holding? Or are re-evaluations showing decay?

**Step 4: Forward Planning Input (15 minutes)**
Generate inputs for next week's plan:
- Which topics are next in the syllabus sequence?
- Which completed topics need revision (per the Revision Framework)?
- Are there any domain-level gaps that will block upcoming topics?

---

### 7.3 Weekly Intervention Triggers

The following conditions automatically trigger a mandatory intervention before the next week's plan can begin:

| Condition | Intervention Required |
|-----------|-----------------------|
| CADI > 3.0 in any domain | 1-day AI-free implementation day in that domain |
| Evaluation pass rate < 50% | Slow down; no new topics until existing topics are consolidated |
| ≥ 3 topics regressed in one week | Full revision week; no new topics |
| ADS has not improved in 2 consecutive weeks | Re-evaluate learning method for that domain |
| Same topic stuck at ML-3 for > 14 days | Escalate to tutoring, different resource, or structured problem-solving session |

---

## Section 8 — Adaptive Learning Rules

> These rules govern how the system adapts the pace, order, and intensity of learning based on performance data.

---

### Rule AL-1: Prerequisite Enforcement

No topic may be studied until its prerequisites (as listed in the syllabus files) are at ML-3 or higher.

If a learner attempts a topic whose prerequisites are below ML-3, the topic session is not counted and the prerequisite topics are added to the front of the queue.

---

### Rule AL-2: Struggling Topic Protocol

A topic is classified as **Struggling** if:
- It has been in IN PROGRESS status for > 14 days, OR
- Its last 3 evaluations have all failed to achieve ML-4

When a topic is Struggling:
1. Do NOT skip it or defer it. Skipping creates a gap that collapses later.
2. Break the topic into sub-components and evaluate each component separately.
3. Reduce AI use for one session to zero — force active struggle.
4. If still failing after 3 more sessions: seek external resource (documentation, worked examples from official sources only).
5. Add it to every weekly review until resolved.

---

### Rule AL-3: Accelerated Topic Protocol

A topic is classified as **Accelerated** if:
- It reaches ML-4 in fewer than 3 sessions, AND
- All TC rules are satisfied

When a topic is Accelerated:
1. Mark it Complete immediately — do not slow it down.
2. Use the saved time to either go deeper on the next topic or address a Struggling topic.
3. Log it as a strong area for that domain — it may indicate prior exposure from projects.

---

### Rule AL-4: Domain Sequencing Rule

Domains must be studied in **parallel**, not sequentially. The following rule governs the distribution of study time across domains each week:

- **Core Track (highest weekly hours):** Python + Backend Engineering
- **Support Track (moderate weekly hours):** SQL + DBMS + OS + CN
- **Practical Track (moderate weekly hours):** Frontend + Cloud & Deployment
- **Career Track (consistent weekly hours):** Communication + Job Preparation

At no point should fewer than 3 domains be actively studied in a given week. Studying only one domain creates tunnel vision and delays employability in adjacent areas.

---

### Rule AL-5: Bottleneck Detection

A **bottleneck** exists when one domain's incomplete topics are blocking progress in another domain.

Common bottleneck patterns:
- Python OOP incomplete → blocks Django Models
- SQL JOINs incomplete → blocks Django ORM optimization
- HTTP fundamentals incomplete → blocks REST API design
- Linux commands incomplete → blocks Docker and deployment

When a bottleneck is detected, the blocking domain must be elevated to Core Track priority until the prerequisite topics are unblocked.

---

### Rule AL-6: Overconfidence Correction

If a learner self-reports ML-4 or higher but an AI-administered evaluation returns ML-3 or lower, the following applies:

1. The AI evaluation result overrides the self-report.
2. The topic is set to its AI-evaluated level.
3. A note is added: "Self-report was inflated. AI evaluation corrected."
4. If this happens ≥ 2 times in the same domain in one week, that domain's CADI floor is raised by 0.5 for that week (treat sessions as if more AI-dependent than reported).

---

## Section 9 — Revision Framework

> Retention requires revisiting. This framework defines when and how topics are revised to prevent decay from Complete to Regressed.

---

### 9.1 Revision Intervals (Spaced Repetition Schedule)

Every topic that reaches Complete status enters the revision schedule:

| Time Since Completion | Revision Type | Duration |
|-----------------------|--------------|----------|
| Day 3 | Quick recall check | 10 minutes |
| Day 7 | Mini-task re-attempt | 20 minutes |
| Day 14 | Full evaluation (3 questions) | 30 minutes |
| Day 30 | Full evaluation (5 questions) | 30 minutes |
| Day 60 | Integration challenge | 45 minutes |
| Day 90 | Interview simulation question | 20 minutes |

**Quick Recall Check:** Can you define it and give one use case? If yes, pass. If no, schedule full revision.

**Mini-Task Re-attempt:** Same or equivalent mini-task, fully independent. If pass: revision complete. If fail: demote to IN PROGRESS, add to this week's study queue.

**Full Evaluation:** AI administers 3–5 evaluation questions from Section 6.4. Must pass 4/5. If 3/5 or below: demote, add to study queue.

---

### 9.2 Revision Priority Queue

The revision queue is ordered as follows (highest priority first):

1. Topics that failed their last evaluation (Regressed)
2. Topics due for Day 7 revision
3. Topics due for Day 14 revision
4. Topics due for Day 30+ revision
5. Topics identified as prerequisites for upcoming new topics

Revision must be scheduled into every week's plan. A week with zero revisions is a week of guaranteed future decay.

---

### 9.3 Bulk Revision Sessions

When ≥ 5 topics from the same domain are due for revision in the same week, instead of individual topic revisions, run a **Domain Bulk Revision Session**:

- Duration: 60–90 minutes
- Method: Write a mini-integration exercise that requires using all 5+ topics together
- Scoring: If the integration exercise is completed independently (ADS ≤ 1), all 5 topics pass their revision
- Benefit: Tests integration knowledge, not just isolated recall

---

### 9.4 Revision During Interview Preparation Phase

In the final 4–6 weeks before active job applications, the revision strategy shifts:

- All topics due for revision get elevated to **interview simulation** format
- No mini-tasks; all revision is via spoken/written interview Q&A
- New study is reduced to 30%; revision and interview simulation is 70%
- CADI target drops to ≤ 1.0 across all domains

---

## Section 10 — Promotion Rules

> These rules govern advancement from one level to the next within a domain's structure (e.g., Python Level 1 → Level 2, Backend Tier 1 → Tier 2).

---

### Rule P-1: Level Completion Prerequisite

A learner may not begin studying Level N+1 of any domain until Level N satisfies:

- **≥ 80% of topics are Complete** (ML-4+, all TC rules satisfied)
- **Average TMS ≥ 60%** across all completed topics in the level
- **Average AI-I score ≥ 3** across all completed topics in the level

The remaining 20% of topics may be in IN PROGRESS or NEEDS EVALUATION. They do not need to be Complete, but they must not be in NOT STARTED.

---

### Rule P-2: The Capstone Gate

Before promoting to the next level, the learner must complete a **Level Capstone Task**:

A Level Capstone is a single implementation or explanation exercise that requires integrating ≥ 3 topics from the current level.

| Domain | Capstone Format |
|--------|----------------|
| Python | Code challenge — implement a class-based program using the level's topics |
| Backend Engineering | Build a mini-feature (endpoint, auth, query) using the tier's concepts |
| SQL | Write a multi-part query that uses all major constructs from the level |
| DBMS | Written exam — answer 5 mixed theory questions without notes |
| OS | Written exam — answer 5 mixed theory questions without notes |
| Computer Networks | Trace a request end-to-end, naming protocols at each layer |
| Frontend | Build a small UI component using the level's concepts |
| Cloud & Deployment | Deploy or configure a component using the level's tools |
| Communication | Recorded mock answer to a behavioral question — reviewed against rubric |
| Job Preparation | Produce a module deliverable (resume draft, LinkedIn update, etc.) |

Capstone must be completed with **ADS ≤ 1**. AI may be used to evaluate the result, not to produce it.

---

### Rule P-3: No Skipping

No level may be skipped. If a learner already knows a topic (from prior projects), they must still demonstrate ML-4 via evaluation. Prior knowledge earns faster completion — it does not earn exemption from evaluation.

---

### Rule P-4: Regression Blocks Promotion

If any topic in the current level is in Regressed status, promotion is blocked until that topic is restored to Complete status.

---

### Rule P-5: Domain Interaction Promotion Rule

If completing Domain A's next level requires knowledge from Domain B that is not yet at ML-4, the learner cannot advance in Domain A's sequence. The prerequisite in Domain B must be completed first.

Example: Advancing to Backend Engineering Tier 5 (DRF) requires Python Level 4 (OOP) to be at ≥ 80% Complete. If Python OOP is at 60%, DRF study must wait.

---

## Section 11 — Domain Readiness Levels

> Each domain has its own readiness score that feeds into the Career Readiness Score (Section 12).

---

### 11.1 Domain Readiness Score (DRS) Computation

```
DRS = (Topics at ML-4 or higher) / (Total topics in domain) × 100

where Total topics = all topics listed in the domain's syllabus file
```

| DRS Range | Label | Meaning |
|-----------|-------|---------|
| 0–19% | Unstarted | Domain not yet meaningfully begun |
| 20–39% | Foundation | Core concepts only; not employable in this domain |
| 40–59% | Developing | Substantial progress; significant gaps remain |
| 60–74% | Functional | Can perform basic job tasks; interviews will expose gaps |
| 75–84% | Proficient | Strong in this domain; can handle most job tasks |
| 85–94% | Interview Ready | Can pass interviews on this domain; gaps are minor |
| 95–100% | Expert Ready | Exceeds job requirements; minor gaps only |

**Minimum DRS for Employment Target:**
Not all domains need to reach the same threshold. The employment target thresholds are:

| Domain | Minimum DRS for Employment |
|--------|--------------------------|
| Python | 75% (Proficient) |
| Backend Engineering | 75% (Proficient) |
| SQL | 70% (upper Functional) |
| DBMS | 60% (Functional) |
| Operating Systems | 60% (Functional) |
| Computer Networks | 60% (Functional) |
| Frontend Engineering | 65% (upper Functional) |
| Cloud & Deployment | 65% (upper Functional) |
| Communication | 75% (Proficient) |
| Job Preparation | 80% (Interview Ready) |

---

### 11.2 Domain Health Indicators

Each domain also has qualitative health indicators reviewed weekly:

**Green (Healthy):**
- DRS advancing week-over-week
- CADI ≤ 2.0
- No Regressed topics
- All topics in revision schedule are passing

**Yellow (Caution):**
- DRS stagnant for 1 week
- CADI 2.0–3.0
- 1–2 Regressed topics
- ≥ 1 topic stuck at ML-3 for > 7 days

**Red (Intervention Required):**
- DRS declining (topics regressing faster than completing)
- CADI > 3.0
- ≥ 3 Regressed topics
- Topic stuck at ML-3 for > 14 days
- ≥ 2 topics in Struggling status simultaneously

---

### 11.3 Domain Priority Tiers

These tiers drive weekly hour allocation. They are fixed for Mahesh's target roles.

**Tier 1 — Core (highest hours):**
Python, Backend Engineering

**Tier 2 — Enabling (significant hours):**
SQL, Frontend Engineering, Cloud & Deployment

**Tier 3 — Supporting (steady hours):**
DBMS, Operating Systems, Computer Networks

**Tier 4 — Career (non-negotiable, every week):**
Communication, Job Preparation

---

## Section 12 — Career Readiness Score (CRS)

> The Career Readiness Score is the single number that answers: "Is Mahesh ready to apply for software engineering jobs today?"

---

### 12.1 CRS Formula

```
CRS = Σ (DRS_domain × Weight_domain)

where weights are defined below
```

| Domain | Weight | Rationale |
|--------|--------|-----------|
| Python | 18% | Primary language; tested in every role |
| Backend Engineering | 20% | Core target skill; highest hiring weight |
| SQL | 10% | Tested in all backend and data roles |
| DBMS | 5% | Theory tested in interviews; lower job weight |
| Operating Systems | 5% | Theory tested in interviews; lower job weight |
| Computer Networks | 5% | Theory tested in interviews; lower job weight |
| Frontend Engineering | 10% | Required for Full Stack; supporting for Backend |
| Cloud & Deployment | 10% | Increasingly required at all levels |
| Communication | 10% | Differentiator in final hiring decision |
| Job Preparation | 7% | Direct multiplier on interview conversion |
| **Total** | **100%** | |

**CRS = (Python × 0.18) + (Backend × 0.20) + (SQL × 0.10) + (DBMS × 0.05) + (OS × 0.05) + (CN × 0.05) + (Frontend × 0.10) + (Cloud × 0.10) + (Communication × 0.10) + (JobPrep × 0.07)**

---

### 12.2 CRS Thresholds and Employment Status

| CRS | Employment Status | Recommended Action |
|-----|------------------|--------------------|
| 0–24% | Not Ready | Study. Do not apply. |
| 25–39% | Early Stage | Study. Build projects. Do not apply yet. |
| 40–54% | Building | Practice interviews internally. Prioritize Tier 1 domains. |
| 55–64% | Nearly Ready | Begin selective applications to practice companies (Tier 3). |
| 65–74% | **Application Ready** | **Begin active applications. Target 6-8 LPA roles.** |
| 75–84% | Strongly Ready | Apply aggressively. Target top companies. Negotiate confidently. |
| 85–100% | Fully Ready | Apply to any target company. Negotiate from strength. |

**Employment Target for Mahesh:** CRS ≥ 65% (Application Ready)
**Stretch Target:** CRS ≥ 75% (Strongly Ready)

---

### 12.3 CRS Minimum Domain Constraints

CRS alone is not sufficient. Even if CRS ≥ 65%, applications should not begin if:

**Hard Constraint 1:** Python DRS < 60%
Reason: Python is tested in every single role. A gap here is visible immediately.

**Hard Constraint 2:** Backend Engineering DRS < 60%
Reason: The primary target domain cannot be below functional.

**Hard Constraint 3:** SQL DRS < 55%
Reason: SQL is tested as a live exercise in most backend interviews.

**Hard Constraint 4:** Communication DRS < 60%
Reason: A technically strong candidate who cannot communicate will not be hired.

If any Hard Constraint is violated, CRS ≥ 65% still does not qualify for active applications. The hard constraint must be resolved first.

---

### 12.4 CRS Weekly Tracking Format

At the end of every weekly review, the CRS entry must be logged:

```
WEEK: [Week number / date range]
─────────────────────────────────────────────────────
Domain               | DRS  | Weight | Weighted Score
Python               | ___% | 0.18   | ___
Backend Engineering  | ___% | 0.20   | ___
SQL                  | ___% | 0.10   | ___
DBMS                 | ___% | 0.05   | ___
Operating Systems    | ___% | 0.05   | ___
Computer Networks    | ___% | 0.05   | ___
Frontend Engineering | ___% | 0.10   | ___
Cloud & Deployment   | ___% | 0.10   | ___
Communication        | ___% | 0.10   | ___
Job Preparation      | ___% | 0.07   | ___
─────────────────────────────────────────────────────
CAREER READINESS SCORE (CRS):         ____%
─────────────────────────────────────────────────────
PRIOR WEEK CRS:                        ____%
WEEK-OVER-WEEK DELTA:                 +/- ____%
─────────────────────────────────────────────────────
HARD CONSTRAINTS STATUS:
  Python DRS ≥ 60%?           YES / NO
  Backend DRS ≥ 60%?          YES / NO
  SQL DRS ≥ 55%?              YES / NO
  Communication DRS ≥ 60%?   YES / NO
─────────────────────────────────────────────────────
EMPLOYMENT STATUS:            [Not Ready / Building / Application Ready / etc.]
─────────────────────────────────────────────────────
FLAGGED DOMAINS:              [Any domain at Yellow or Red health]
ACTION ITEMS FOR NEXT WEEK:   [Specific adjustments]
```

---

### 12.5 CRS Interpretation Rules for AI Agents

When an AI agent is asked to compute or report the CRS, it must:

1. Request the current DRS for each domain (or compute it from the session log data if provided).
2. Apply the formula in Section 12.1 exactly.
3. Check all Hard Constraints in Section 12.3.
4. Report the Employment Status using the thresholds in Section 12.2.
5. Flag any domain at Yellow or Red health (Section 11.2).
6. Provide a 3-line recommendation: what to prioritize, what to protect, and what the biggest gap is.

---

## Section 13 — Framework Integrity Rules

> These rules govern the integrity of the entire system. They exist to prevent gaming, wishful thinking, and false progress.

---

### Rule FI-1: No Self-Certification

Mastery levels cannot be self-assigned without evaluation evidence. "I feel like I know this" is not evidence. Evaluation questions, mini-tasks, and implementation attempts are evidence.

---

### Rule FI-2: The 72-Hour Rule

If a topic has not been touched (studied, practiced, or revised) in 72 hours, it is flagged as Stale. Stale topics require a 10-minute quick check before they can be used as prerequisites for new topics.

---

### Rule FI-3: Project Usage as Evidence

Completing a real project feature that uses a topic is accepted as equivalent to a Mini-Task (Rule TC-3). However, it must:
- Be documented (GitHub commit or session log)
- Have been completed with ADS ≤ 1
- Be reviewable (code exists somewhere)

Project usage does NOT replace the evaluation requirement. The topic still requires evaluation questions to be answered before being marked Complete.

---

### Rule FI-4: Version Control for Progress

Every Complete topic must have an associated artifact:
- Code committed to GitHub (for implementation topics), OR
- Written explanation saved in a notes file (for theory topics)

A topic "completed" with no artifact does not exist. Artifacts are the evidence that the work happened.

---

### Rule FI-5: Framework Version Lock

When this framework file is used to generate evaluations, plans, or assessments, the version of the framework (Version 1.0) must be referenced. If the framework is updated, the version number increments and all future computations use the new version. Prior progress records retain their original version for historical accuracy.

---

### Rule FI-6: Honest Failure Documentation

Failed evaluations must be logged — they cannot be deleted or ignored. A failed evaluation that is not logged is a violation of framework integrity. The purpose is not punishment — it is information. Failed evaluations reveal the actual state of knowledge. They are data, not judgments.

---

## Appendix A — Framework Reference Card

> One-page summary for daily use.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MASTERY LEVELS (ML-0 to ML-6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ML-0  Unaware          → Never encountered
ML-1  Exposed          → Seen it; can't explain
ML-2  Understood       → Can explain; can't implement
ML-3  Guided Impl.     → Implements WITH AI help
ML-4  Independent      → Implements WITHOUT AI ✓ MINIMUM
ML-5  Fluent           → Fast + interview-ready
ML-6  Expert           → Can teach; exceeds job needs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI DEPENDENCY SCORE (ADS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4 = AI wrote everything (fully dependent)
3 = AI debugged + suggested structure
2 = AI answered specific questions
1 = AI verified finished work only
0 = No AI used (fully independent) ✓ TARGET

MUST TREND DOWNWARD over consecutive sessions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOPIC IS COMPLETE WHEN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☐ ML-4 or higher
☐ CU ≥ 3, IA ≥ 3, DA ≥ 2, IK ≥ 2, IR ≥ 2, AI-I ≥ 3
☐ Mini-Task completed independently
☐ No failed evaluation in past 7 days
☐ Can explain under interview pressure
☐ Artifact exists (GitHub / notes file)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAREER READINESS SCORE (CRS) — Employment Thresholds
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
< 55%  Do not apply
55–64% Practice applications only
65–74% APPLICATION READY ← Target
75%+   Strongly Ready

Hard Constraints (must all pass):
  Python DRS ≥ 60%
  Backend DRS ≥ 60%
  SQL DRS ≥ 55%
  Communication DRS ≥ 60%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Appendix B — Evaluation Quick Reference for AI Agents

When an AI agent receives this file and is asked to run an evaluation session, it must follow this exact sequence:

```
EVALUATION SEQUENCE FOR AI AGENT
──────────────────────────────────
1. IDENTIFY topic + domain + syllabus reference
2. CONFIRM learner's current mastery level (ask if unknown)
3. GENERATE questions by type:
   - 2 × Type 1 (Definition)
   - 1 × Type 2 (Comparison)
   - 1 × Type 3 (Implementation — only if prior ML ≥ 3)
   - 1 × Type 4 (Debugging — present broken code)
   - 1 × Type 5 (Integration)
   - 1 × Type 6 (Tradeoff — only if targeting ML-5)
4. ADMINISTER one question at a time; wait for response
5. SCORE each dimension (CU, IA, DA, IK, IR, AI-I) as answers are given
6. COMPUTE TMS
7. DETERMINE new mastery level
8. CHECK all TC rules
9. REPORT:
   - New mastery level
   - TMS
   - Per-dimension scores
   - Topic completion status
   - What to work on next
   - Specific gaps to address
──────────────────────────────────
```

---

## Appendix C — Domain Topic Count Reference

> Used for computing DRS. These counts are approximate based on the syllabi files. AI agents should count actual topics from the syllabus files for precise computation.

| Domain | Approx. Topic Count | Syllabus File |
|--------|--------------------|----|
| Python | ~55 topics | 02_PYTHON_SYLLABUS.md |
| Backend Engineering | ~60 topics | 03_BACKEND_ENGINEERING_SYLLABUS.md |
| SQL | ~50 topics | 04_SQL_SYLLABUS.md |
| DBMS | ~45 topics | 05_DBMS_SYLLABUS.md |
| Operating Systems | ~50 topics | 06_OPERATING_SYSTEMS_SYLLABUS.md |
| Computer Networks | ~55 topics | 07_COMPUTER_NETWORKS_SYLLABUS.md |
| Frontend Engineering | ~65 topics | 08_FRONTEND_SYLLABUS.md |
| Cloud & Deployment | ~50 topics | 09_CLOUD_AND_DEPLOYMENT_SYLLABUS.md |
| Communication | ~35 topics | 10_COMMUNICATION_SYLLABUS.md |
| Job Preparation | ~40 topics | 11_JOB_PREPARATION_SKILL_TREE.md |
| **Total** | **~505 topics** | |

At 6 LPA target: Need ~65% completion = ~328 topics at ML-4+.
At 8 LPA target: Need ~75% completion = ~379 topics at ML-4+.

---

*This framework is the governing document for Mahesh Career OS. It is strict by design. The strictness is not punitive — it is protective. Every rule exists to ensure that on the day of the interview, there are no surprises.*
