# NOTES SYSTEM ARCHITECTURE
Version: 1.0

---

# PURPOSE

This document is the single source of truth for the Career OS Knowledge Management System.

It defines

• Folder Structure

• Read Locations

• Write Locations

• Engine Dependencies

• Subject Skill Mapping

• Prompt Execution Flow

• Chapter Organization Rules

• Naming Conventions

• Knowledge Evolution Rules

Every Core Engine, Subject Skill and Prompt must follow this architecture.

If any instruction conflicts with this document, this document takes precedence.

---

# SYSTEM PHILOSOPHY

The Notes System is NOT a note generator.

It is a Knowledge Management System.

Its purpose is to continuously build and maintain a professional Software Engineering Knowledge Base.

Knowledge should evolve.

Knowledge should never duplicate.

Knowledge should never be organized by learning dates.

---

# DIRECTORY STRUCTURE

Career-OS/

├── STATUS.md
│
├── lessons/
├── submissions/
│
├── Python/
├── Operating Systems/
├── DBMS/
├── SQL/
├── Computer Networks/
├── backend/
├── Frontend/
├── Cloud/
├── communication/
│
└── noteskills/
    ├── core/
    ├── subjects/
    └── prompts/

---

# DIRECTORY RESPONSIBILITIES

STATUS.md

Tracks roadmap progress.

Read Only.

Never modify.

---

lessons/

Contains AI-generated daily learning plans.

Temporary.

Read Only.

Never write notes here.

---

submissions/

Contains completed assignments.

Temporary.

Read Only.

Never write notes here.

---

Python/

Permanent Knowledge Base.

Read + Write.

---

Operating Systems/

Permanent Knowledge Base.

Read + Write.

---

DBMS/

Permanent Knowledge Base.

Read + Write.

---

SQL/

Permanent Knowledge Base.

Read + Write.

---

Computer Networks/

Permanent Knowledge Base.

Read + Write.

---

backend/

Permanent Knowledge Base.

Read + Write.

---

Frontend/

Permanent Knowledge Base.

Read + Write.

---

Cloud/

Permanent Knowledge Base.

Read + Write.

---

communication/

Ignore completely.

Never generate notes.

Never read for technical knowledge.

Never update.

---

noteskills/

Contains the Notes System.

Never generate notes here.

Only read these files as instructions.

---

# READ LOCATIONS

The Notes System may read only from

STATUS.md

lessons/

submissions/

Existing Knowledge Base

noteskills/

---

# WRITE LOCATIONS

The Notes System may write only to

Python/

Operating Systems/

DBMS/

SQL/

Computer Networks/

backend/

Frontend/

Cloud/

No other folders may be modified.

---

# FORBIDDEN WRITE LOCATIONS

Never create notes inside

lessons/

submissions/

communication/

noteskills/

STATUS.md

These locations are read-only.

---

# SUBJECT ROUTING

If subject is

Python

↓

Career-OS/Python/

↓

PYTHON_KNOWLEDGE_SKILL.md

---

Operating Systems

↓

Career-OS/Operating Systems/

↓

OPERATING_SYSTEMS_KNOWLEDGE_SKILL.md

---

DBMS

↓

Career-OS/DBMS/

↓

DBMS_KNOWLEDGE_SKILL.md

---

SQL

↓

Career-OS/SQL/

↓

SQL_KNOWLEDGE_SKILL.md

---

Computer Networks

↓

Career-OS/Computer Networks/

↓

COMPUTER_NETWORKS_KNOWLEDGE_SKILL.md

---

Backend Engineering

↓

Career-OS/backend/

↓

BACKEND_ENGINEERING_KNOWLEDGE_SKILL.md

---

Frontend

↓

Career-OS/Frontend/

↓

FRONTEND_KNOWLEDGE_SKILL.md

---

Cloud & Deployment

↓

Career-OS/Cloud/

↓

CLOUD_DEPLOYMENT_KNOWLEDGE_SKILL.md

---

Communication

↓

Ignore completely.

---

# CHAPTER ORGANIZATION

Organize by

Subject

↓

Chapter

↓

Subtopic

Never organize by

Day

Week

Sprint

Lesson

---

# FILE NAMING RULES

Correct

Variables & Data Types.md

Functions.md

ER Model.md

Processes.md

HTTP.md

JWT.md

Authentication.md

Incorrect

Day01.md

Lesson05.md

Functions Part 2.md

Variables Final.md

Revision.md

Week03.md

---

# CHAPTER UPDATE RULE

Before creating a chapter

Search the existing subject folder.

If chapter exists

↓

Update

If chapter does not exist

↓

Create

Never skip this step.

---

# KNOWLEDGE TYPES

Every detected topic belongs to one of

NEW

CONTINUATION

REVISION

ADVANCED

REDO

NEW

↓

Create chapter

CONTINUATION

↓

Update chapter

REVISION

↓

Improve chapter

ADVANCED

↓

Expand chapter

REDO

↓

Improve existing chapter only

---

# ENGINE DEPENDENCY GRAPH

Prompt

↓

Knowledge Base Engine

↓

Topic Classification Engine

↓

Chapter Management Engine

↓

Subject Knowledge Skill

↓

Submission Review Engine

↓

Interview Engine

↓

Knowledge Writing Standard

↓

Knowledge Quality Assurance Engine

↓

Knowledge Base

Every execution must follow this order.

---

# CORE ENGINE LOCATIONS

Career-OS/noteskills/core/

01_KNOWLEDGE_BASE_ENGINE.md

02_CHAPTER_MANAGEMENT_ENGINE.md

03_SUBMISSION_REVIEW_ENGINE.md

04_KNOWLEDGE_WRITING_STANDARD.md

05_INTERVIEW_ENGINE.md

06_TOPIC_CLASSIFICATION_ENGINE.md

07_KNOWLEDGE_QUALITY_ASSURANCE_ENGINE.md

---

# SUBJECT SKILL LOCATIONS

Career-OS/noteskills/subjects/

PYTHON_KNOWLEDGE_SKILL.md

OPERATING_SYSTEMS_KNOWLEDGE_SKILL.md

DBMS_KNOWLEDGE_SKILL.md

SQL_KNOWLEDGE_SKILL.md

COMPUTER_NETWORKS_KNOWLEDGE_SKILL.md

BACKEND_ENGINEERING_KNOWLEDGE_SKILL.md

FRONTEND_KNOWLEDGE_SKILL.md

CLOUD_DEPLOYMENT_KNOWLEDGE_SKILL.md

---

# PROMPT LOCATIONS

Career-OS/noteskills/prompts/

01_INITIAL_KNOWLEDGE_BASE_BUILD.md

02_DAILY_KNOWLEDGE_UPDATER.md

Prompts never contain business logic.

They only orchestrate execution.

---

# KNOWLEDGE BASE PHILOSOPHY

Lessons are temporary.

Submissions are temporary.

The Knowledge Base is permanent.

Improve the Knowledge Base.

Do not copy lessons.

Do not archive daily work.

Extract knowledge.

---

# IDEMPOTENCY

The Notes System must be safe to execute multiple times.

Running the same prompt twice must

Improve

Merge

Validate

Refine

Never duplicate knowledge.

---

# COMMUNICATION POLICY

Communication is outside the scope of the Knowledge Base.

Ignore

Communication lessons

Communication submissions

Communication folders

Communication topics

Never generate Communication notes.

---

# SUCCESS CRITERIA

The Notes System succeeds when

Every lesson improves the handbook.

Every topic has one authoritative chapter.

No duplicate chapters exist.

Knowledge remains organized.

Interview preparation improves.

Backend relevance is maintained.

The handbook becomes more valuable after every execution.

---

# FINAL PRINCIPLE

The Notes System is a Software Engineering Knowledge Management System.

Every engine, every subject skill and every prompt exists to maintain one continuously evolving, interview-ready Software Engineering Handbook.

The handbook is the product.

Everything else exists to improve it.