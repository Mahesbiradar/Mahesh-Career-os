# Mahesh Career OS — Course Engine
> **Version:** 2.0  
> **Replaces:** Files 13, 16, 18 for daily use  
> **Purpose:** The only file you need to read to operate the system every day.

---

## What This System Is

A personal online course built specifically for you.

- AI acts as your instructor — prepares your lesson, gives you the assignment, evaluates your work
- You act as the student — watch, build, submit
- No hunting for resources. No self-scoring. No complex prompts.

---

## Your Daily Flow (3 Steps)

```
MORNING
  AI generates your lesson file → lessons/DAY_XX.md
  You open it. Read it top to bottom. Takes 2 minutes.
        ↓
DURING THE DAY
  Step 1: Watch the video linked in the lesson (15–30 min)
  Step 2: Read the concept summary in the file (5 min)
  Step 3: Do the assignment at the bottom of the file (45–90 min)
        ↓
END OF DAY
  Paste your work into chat (code / written explanation)
  AI reviews what you actually built and gives feedback
  AI generates tomorrow's lesson file
```

That is the entire system. Nothing else.

---

## The Lesson File

Every morning you get one file: `lessons/DAY_XX.md`

It contains exactly:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DAY [N] — [TOPIC NAME]
Domain: [Python / Backend / SQL / etc.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON VIDEO
  Course: [Course name]
  Section: [Section name]
  Video: [Video title]
  Duration: [X min]
  Watch at: [Udemy / YouTube link]

WHAT TO FOCUS ON WHILE WATCHING
  [3–4 specific things to notice in the video]

CONCEPT SUMMARY
  [AI-written plain-English explanation of the topic]
  [Key points, syntax, common mistakes]

TODAY'S ASSIGNMENT
  Task: [Specific thing to build or write]
  Time estimate: [X min]
  Difficulty: [Beginner / Intermediate]

  Requirements:
  [ ] Requirement 1
  [ ] Requirement 2
  [ ] Requirement 3

  DO NOT use AI while doing the assignment.
  Official docs are allowed.

HOW TO SUBMIT
  For code: Paste your code in chat + say "Submitting Day [N]"
  For theory: Paste your written explanation in chat

WHAT AI WILL CHECK
  [Specific things AI will look for when reviewing your submission]

REVISION FROM PREVIOUS LESSON
  Topic: [topic from 3 days ago]
  Quick check: [One question — answer it before starting today's video]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## How to Submit Your Work

### For Code Topics (Python, Django, SQL, React)

Paste your code directly in chat like this:

```
Submitting Day 3

[paste your code here]
```

AI will read your actual code and tell you:
- What is correct
- What is wrong and why
- What to fix before moving on
- Your grade: PASS / NEEDS WORK / REDO

### For Theory Topics (OS, CN, DBMS)

Write a 100–150 word explanation in your own words. Then paste it:

```
Submitting Day 12

[your written explanation here]
```

AI will check:
- Is it accurate?
- Did you miss any key points?
- Can you explain it in an interview?

### For SQL Topics

Paste your query:

```
Submitting Day 8

[your SQL query here]
```

---

## Grades

Every submission gets one of three results:

| Grade | Meaning | What Happens Next |
|---|---|---|
| **PASS** | Correct and complete | Move to next topic tomorrow |
| **NEEDS WORK** | Mostly right, small fixes needed | Fix and resubmit tonight or early tomorrow |
| **REDO** | Significant gaps | Redo the assignment. Same lesson tomorrow. |

---

## AI Is OFF During Assignments

When you are doing the assignment:
- No asking AI "how do I do this"
- No asking AI to write any code for you
- No asking AI to explain a concept mid-assignment

**Allowed:**
- Official documentation (docs.djangoproject.com, docs.python.org, MDN)
- Re-reading the concept summary in the lesson file
- Re-watching a specific part of the video

**Why:** Every interview will test you without AI. The assignment is your practice for that.

If you get stuck for more than 20 minutes on one specific thing — note it down. Paste your stuck code when submitting. AI will diagnose exactly where it broke.

---

## DSA Block

DSA runs separately. It is not tracked here.
DSA time: 60–75 minutes, done first thing in the morning before the Career OS lesson.

---

## Communication Practice (15 Minutes Daily)

Built into every lesson file at the bottom.
It is always one of these three:
- Explain today's topic out loud as if to an interviewer (record on phone or just say it)
- Practice your self-introduction (2 minutes)
- Answer one behavioural question using the STAR format

This is non-negotiable. 15 minutes every day.

---

## Weekly Check-In (Sunday, 20 Minutes)

At the end of every week, paste this in chat:

```
Weekly check-in — Week [N]

Days studied this week: [N]
Lessons submitted: [N]
Grades received: [list e.g. PASS, PASS, NEEDS WORK, PASS]
One thing I understood well this week: [topic]
One thing I'm still unsure about: [topic or question]
```

AI will:
- Tell you your overall progress
- Flag anything that needs revision
- Confirm next week's lesson sequence
- Tell you your current job readiness level

---

## What Happens If You Miss a Day

**Missed 1 day:**
Paste this in chat the next morning:
```
Missed yesterday. Resuming today.
```
AI continues from where you left off. No penalty.

**Missed 3+ days:**
Paste this in chat:
```
Missed [N] days. Last lesson was Day [N]. Resuming today.
```
AI will give you a quick 10-minute recall check on the last lesson before continuing.

---

## How to Ask for Your Next Lesson

Every morning, paste in chat:

```
Generate Day [N] lesson.
Last submission grade: [PASS / NEEDS WORK / REDO]
```

AI will create the lesson file at `lessons/DAY_[N].md` and tell you it's ready.

If you got REDO — AI generates the same lesson again with a different assignment.
If you got NEEDS WORK — AI includes a quick fix check at the top of the next lesson.

---

## Folder Structure

```
Career-OS/
├── lessons/              ← AI generates lesson files here
│   ├── DAY_01.md
│   ├── DAY_02.md
│   └── ...
├── submissions/          ← You save your work files here (optional)
│   ├── day01_variables.py
│   ├── day03_loops.py
│   └── ...
└── [existing syllabus and framework files]
```

You do not need to open any other Career OS file during daily study.
This guide + the daily lesson file is everything.

---

## Quick Reference

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVERY MORNING:
  "Generate Day [N] lesson. Last grade: [grade]"

EVERY EVENING:
  "Submitting Day [N]" + paste your work

EVERY SUNDAY:
  "Weekly check-in — Week [N]" + paste the check-in block

STUCK DURING ASSIGNMENT (20+ min):
  Finish as much as you can. Paste stuck code when submitting.
  AI diagnoses it.

MISSED DAYS:
  "Missed [N] days. Resuming today."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RULES:
  AI OFF during assignments
  Official docs allowed anytime
  Paste actual work — not descriptions of work
  15 min communication practice daily
  DSA block separate, first thing in the morning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
