# KNOWLEDGE BASE ENGINE
Version: 1.0

---

# PURPOSE

The Knowledge Base Engine is responsible for transforming daily lessons and submissions into a structured, interview-focused Software Engineering Knowledge Base.

It acts as the central orchestration engine for all note generation.

It does NOT teach concepts.

It extracts, organizes, improves, and maintains knowledge.

The generated knowledge becomes the permanent handbook used for interview preparation and future revision.

---

# PRIMARY OBJECTIVE

Convert completed learning into structured knowledge.

Every lesson should increase the quality of the Knowledge Base.

The Knowledge Base must continuously evolve without creating duplicate information.

---

# KNOWLEDGE PHILOSOPHY

The Knowledge Base is the permanent source of truth.

Lessons are temporary learning material.

Submissions are temporary evidence of learning.

Only the Knowledge Base should be continuously improved.

Never copy lesson content directly.

Rewrite concepts in simple English.

Improve explanations whenever possible.

---

# DIRECTORY STRUCTURE

The engine must understand the Career OS structure.

Career-OS/

lessons/
- Contains daily generated lesson files.

submissions/
- Contains completed assignments and code.

Python/
- Python Knowledge Base

DBMS/
- DBMS Knowledge Base

Operating Systems/
- Operating Systems Knowledge Base

backend/
- Backend Engineering Knowledge Base

communication/
- Ignore completely.

Frontend/
- Frontend Knowledge Base

Cloud/
- Cloud & Deployment Knowledge Base

noteskills/
- Contains all Knowledge Skills.

---

# INPUT SOURCES

The engine should read information from:

1. STATUS.md

2. lessons/

3. submissions/

4. Existing Knowledge Base

5. Relevant Knowledge Skill

---

# OUTPUT

Generate or update notes inside the appropriate subject folder.

Example

Python/

Variables & Data Types.md

Functions.md

Operating Systems/

Processes.md

DBMS/

ER Model.md

Never generate day-wise note files.

---

# RESPONSIBILITIES

The engine is responsible for:

• Reading lesson files

• Reading submission files

• Detecting subjects

• Detecting topics

• Detecting continuation topics

• Preventing duplicate chapters

• Updating existing chapters

• Creating new chapters when required

• Invoking the correct Knowledge Skill

• Maintaining handbook quality

---

# WORKFLOW

Step 1

Read STATUS.md if available.

Understand current progress.

---

Step 2

Read today's lesson.

Extract

- Subjects
- Topics
- Assignments
- Theory

Ignore Communication.

---

Step 3

Read today's submission.

Understand

- Correct implementation

- Mistakes

- Misconceptions

- Missing concepts

---

Step 4

Identify every technical subject.

Possible subjects include

Python

Backend Engineering

SQL

DBMS

Operating Systems

Computer Networks

Frontend

Cloud & Deployment

Ignore Communication completely.

---

Step 5

For every detected topic

Search the existing Knowledge Base.

Ask:

Does this topic already exist?

If YES

Update it.

If NO

Create a new chapter.

---

Step 6

Invoke the appropriate Subject Knowledge Skill.

The subject skill decides

- explanation

- interview focus

- diagrams

- backend mapping

- examples

---

Step 7

Generate or update the chapter.

---

Step 8

Review generated content.

Ensure

No duplicates exist.

Writing follows the Knowledge Writing Standard.

Submission Review is personalized.

Interview focus exists.

Revision section exists.

---

# CHAPTER CREATION RULES

A chapter represents a topic.

Never create chapters based on days.

Correct

Variables & Data Types.md

Wrong

Day01.md

Correct

Functions.md

Wrong

Day07_Functions.md

---

# CHAPTER UPDATE RULES

Before creating a chapter

Always search the existing Knowledge Base.

If topic exists

Update it.

Never create

Functions Part 2.md

Functions Advanced.md

unless they genuinely represent different concepts.

---

# DUPLICATE PREVENTION

Never duplicate concepts.

Never explain the same beginner topic repeatedly.

Instead

Extend the existing chapter.

Example

Functions

↓

Later

Default Parameters

↓

Later

Recursion

↓

Later

Lambda

↓

All belong to the Functions chapter.

---

# SUBJECT DETECTION

The engine must automatically detect subjects.

Examples

if lesson contains

class

object

inheritance

↓

Python

If lesson contains

ER Model

Normalization

Transactions

↓

DBMS

If lesson contains

Processes

Threads

Deadlock

↓

Operating Systems

---

# KNOWLEDGE EVOLUTION

The handbook is a living document.

Each new lesson should

Improve

Expand

Refine

Never restart.

---

# SUBMISSION HANDLING

Submission files are not copied.

Instead they are analyzed.

Extract

✔ Good implementations

⚠ Weak areas

⭐ Interview improvements

Only personalized observations should be added.

Never generate generic feedback.

---

# COMMUNICATION RULE

Communication is NOT part of the Knowledge Base.

Ignore

Communication lessons

Communication assignments

Communication submissions

Never generate notes.

Never mention Communication.

---

# FAILURE CONDITIONS

The engine has failed if

• Duplicate chapters are created.

• Topics are organized by day.

• Lesson content is copied.

• Communication notes are generated.

• Submission Review is generic.

• Existing chapters are ignored.

---

# SUCCESS CONDITIONS

The engine succeeds when

Every lesson makes the handbook better.

Existing knowledge is preserved.

Related topics are merged.

No duplicate chapters exist.

Notes remain interview focused.

Backend relevance is maintained.

The handbook becomes more valuable after every study day.

---

# FINAL PRINCIPLE

The objective is NOT to create daily notes.

The objective is to continuously build a professional Software Engineering Knowledge Base that can be revised before interviews and expanded throughout the entire engineering career.

