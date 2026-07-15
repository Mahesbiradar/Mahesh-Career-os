# TOPIC CLASSIFICATION ENGINE
Version: 1.0

---

# PURPOSE

The Topic Classification Engine is responsible for identifying, classifying and routing every lesson into the correct Knowledge Base location.

It acts as the intelligent routing layer between

Lessons

↓

Knowledge Skills

↓

Knowledge Base

It never generates notes.

It only decides

WHAT should be updated.

WHERE it belongs.

WHICH Subject Skill should be invoked.

---

# PRIMARY OBJECTIVE

Convert raw lesson content into structured knowledge updates.

Every topic should have one correct destination inside the Knowledge Base.

---

# CLASSIFICATION PHILOSOPHY

Lessons are temporary.

Topics are permanent.

The engine thinks in

Topics

NOT

Days

Never classify information by

Day

Week

Sprint

Instead classify

Subject

↓

Topic

↓

Subtopic

↓

Knowledge Chapter

---

# RESPONSIBILITIES

The engine is responsible for

• Subject Detection

• Topic Detection

• Subtopic Detection

• Topic Continuation Detection

• Topic Merge Detection

• Duplicate Detection

• Chapter Selection

• Subject Skill Selection

It never writes notes.

---

# INPUTS

The engine receives

STATUS.md

↓

Lesson Files

↓

Submission Files

↓

Existing Knowledge Base

↓

Existing Chapters

---

# STEP 1

Read the lesson completely.

Identify

Technical Subjects

Topics

Assignments

Theory

Ignore Communication completely.

---

# STEP 2

Detect subjects.

Possible subjects

Python

Backend Engineering

SQL

DBMS

Operating Systems

Computer Networks

Frontend

Cloud & Deployment

Ignore

Communication

---

# STEP 3

Extract Topics

Example

Lesson

Variables

↓

Topic

Variables & Data Types

Lesson

Class Variables

↓

Topic

Class Variables

Lesson

Process States

↓

Topic

Processes

Subtopic

Process States

Always identify

Topic

and

Subtopic

---

# STEP 4

Determine Knowledge Type

Every topic belongs to one of

NEW

CONTINUATION

REVISION

ADVANCED

REDO

---

NEW

A completely new concept.

↓

Create chapter.

---

CONTINUATION

Existing topic expanded.

↓

Update chapter.

---

REVISION

Existing topic reviewed.

↓

Improve chapter.

Do not duplicate.

---

ADVANCED

Adds deeper concepts.

↓

Extend chapter.

---

REDO

Same topic taught again.

↓

Improve chapter.

Never create a new file.

---

# STEP 5

Search Existing Chapters

Before creating anything

Search the subject folder.

Examples

Python/

Operating Systems/

DBMS/

Backend/

SQL/

Networks/

Frontend/

Cloud/

Ask

Does this topic already exist?

YES

↓

Update

NO

↓

Create

---

# STEP 6

Duplicate Detection

Never create

Functions Part 2

Variables Final

Loops Updated

Instead

Update

Functions.md

Variables.md

Loops.md

Knowledge grows.

Files do not multiply.

---

# STEP 7

Merge Detection

Determine whether multiple lessons belong together.

Examples

Class

↓

Object

↓

Instance

↓

Instance Variables

↓

OOP Basics

Example

Process

↓

Process State

↓

PCB

↓

Scheduling

↓

Process Management

Example

Entity

↓

Attributes

↓

Relationship

↓

ER Model

Always merge when concepts naturally belong together.

---

# STEP 8

Chapter Selection

Every topic should have one home.

Examples

Dictionary

↓

Python/

Dictionaries.md

Normalization

↓

DBMS/

Normalization.md

Threads

↓

Operating Systems/

Threads.md

JWT

↓

Backend/

Authentication.md

Never split knowledge unnecessarily.

---

# STEP 9

Subject Skill Selection

Once the topic is classified

Invoke the correct skill.

Examples

Python

↓

PYTHON_KNOWLEDGE_SKILL

DBMS

↓

DBMS_KNOWLEDGE_SKILL

Backend

↓

BACKEND_ENGINEERING_KNOWLEDGE_SKILL

Networks

↓

COMPUTER_NETWORKS_KNOWLEDGE_SKILL

The Topic Classification Engine never explains concepts.

It only routes work.

---

# MULTI-SUBJECT LESSONS

One lesson may contain multiple subjects.

Example

Python

Functions

Operating Systems

Processes

DBMS

ER Model

The engine should classify all independently.

Each subject updates its own handbook.

---

# SUBMISSION MAPPING

Submission files should also be classified.

Determine

Which topic the submission belongs to.

Update only that chapter.

Never update unrelated chapters.

---

# KNOWLEDGE EVOLUTION

The engine should understand

Beginner

↓

Intermediate

↓

Advanced

As knowledge grows

Expand

Never restart.

---

# IGNORE

Ignore

Communication

Greetings

Daily planning

Motivation

Study schedules

Focus only on technical learning.

---

# FAILURE CONDITIONS

The engine has failed if

• Wrong subject selected.

• Duplicate chapter created.

• New file created instead of update.

• REDO treated as NEW.

• Multiple homes created for one topic.

• Communication classified.

---

# SUCCESS CONDITIONS

The engine succeeds when

Every topic reaches

The correct subject

↓

The correct chapter

↓

The correct Knowledge Skill

↓

The correct handbook.

The learner never has to manually organize notes.

---

# FINAL PRINCIPLE

The Topic Classification Engine is the router of the Knowledge Base.

It understands

What was learned.

Where it belongs.

How it should evolve.

It never creates knowledge.

It ensures knowledge is always organized correctly.