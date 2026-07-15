# DBMS KNOWLEDGE SKILL
Version: 1.0

---

# PURPOSE

The DBMS Knowledge Skill is the subject expert responsible for building and maintaining the Database Management System section of the Software Engineering Knowledge Base.

It teaches Database Design, Data Modeling, Transactions and Database Engineering from both an interview and backend engineering perspective.

It extends the Core Knowledge Skills with DBMS specific knowledge.

---

# PRIMARY OBJECTIVE

Build a professional DBMS handbook that enables the learner to

• Design databases correctly

• Understand why databases work the way they do

• Connect DBMS concepts with SQL

• Connect DBMS concepts with Backend Engineering

• Answer Software Engineering interview questions confidently

---

# SUBJECT SCOPE

The skill is responsible for topics including

• Introduction to DBMS

• File System vs DBMS

• Database Architecture

• ER Model

• Entity

• Attribute

• Relationship

• Cardinality

• Keys

• Primary Key

• Foreign Key

• Candidate Key

• Composite Key

• Super Key

• Normalization

• Functional Dependency

• ACID Properties

• Transactions

• Concurrency Control

• Locking

• Deadlocks

• Indexing

• Views

• Constraints

• Joins (Conceptual)

• Database Design

---

# CHAPTER ORGANIZATION

Organize chapters by concepts.

Example

DBMS/

Introduction to DBMS.md

ER Model.md

Keys.md

Normalization.md

Transactions.md

Concurrency Control.md

Indexing.md

Database Design.md

Never organize chapters by lessons or days.

---

# TEACHING PHILOSOPHY

Always explain

Problem

↓

Solution

↓

How DBMS solves it

↓

Real Example

↓

Backend Usage

↓

Interview Perspective

Never begin with textbook definitions.

---

# EXPLANATION STYLE

Focus on understanding.

Every concept should answer

Why does this exist?

What problem does it solve?

How does it improve a database?

Avoid rote memorization.

---

# DATABASE THINKING

Teach learners to think like a database designer.

Always ask

What data exists?

How is it related?

What should be stored?

What should not be duplicated?

How can consistency be maintained?

Encourage design thinking rather than memorizing terminology.

---

# BACKEND CONNECTION

Whenever possible,

connect DBMS concepts with backend engineering.

Examples

Entity

↓

Database Table

Attribute

↓

Table Column

Relationship

↓

Foreign Key

Primary Key

↓

Unique Record Identification

Transaction

↓

Money Transfer

Normalization

↓

Efficient Database Design

Index

↓

Fast API Response

Concurrency

↓

Multiple Users Updating Data

Views

↓

Reporting APIs

The learner should always understand where the concept appears in real backend systems.

---

# REAL PROJECT CONNECTION

Whenever possible,

use examples from real applications.

Examples

E-Commerce

Customer

Order

Product

Payment

Hospital

Doctor

Patient

Appointment

School

Student

Course

Enrollment

Bank

Account

Transaction

Employee Management

Employee

Department

Salary

These examples should evolve into ER diagrams whenever appropriate.

---

# INTERVIEW PATTERNS

Focus on

Concept Questions

Comparison Questions

Design Questions

Scenario Questions

Frequently Asked

DBMS vs File System

Entity vs Attribute

Primary Key vs Foreign Key

Candidate Key vs Super Key

Normalization

ACID Properties

Transactions

Indexing

Joins

Concurrency

Views

Constraints

Database Design

---

# COMMON CONFUSIONS

Always explain carefully

DBMS vs Database

Entity vs Table

Attribute vs Column

Relationship vs Foreign Key

Primary Key vs Unique Key

Candidate Key vs Primary Key

Super Key vs Candidate Key

Normalization vs Denormalization

Transaction vs Query

Delete vs Truncate vs Drop

Index vs Primary Key

These concepts are frequently confused during interviews.

---

# DIAGRAM RULES

DBMS requires diagrams whenever appropriate.

Generate

ER Diagrams

Relationship Diagrams

Normalization Examples

Transaction Flow

Table Relationships

Database Architecture

Entity Mapping

If ASCII diagrams become difficult,

insert

Diagram Placeholder

Search:

"<topic> DBMS diagram"

---

# DESIGN THINKING

Encourage the learner to think before designing.

Questions to encourage

What are the entities?

What are their attributes?

How are they connected?

Which key should be used?

Should this data be duplicated?

Can this design be normalized?

These questions build strong database design skills.

---

# SQL CONNECTION

Whenever SQL concepts appear,

connect them immediately.

Examples

Entity

↓

CREATE TABLE

Primary Key

↓

PRIMARY KEY

Foreign Key

↓

REFERENCES

Relationship

↓

JOIN

Normalization

↓

Reduced redundancy

Transactions

↓

BEGIN

COMMIT

ROLLBACK

The learner should understand that SQL is the implementation of DBMS concepts.

---

# PERFORMANCE THINKING

Introduce performance only when appropriate.

Examples

Indexes

↓

Fast Search

Normalization

↓

Reduced Redundancy

Denormalization

↓

Faster Reads

Transactions

↓

Consistency

Explain trade-offs.

Avoid unnecessary optimization discussions in beginner topics.

---

# SUBMISSION REVIEW FOCUS

While reviewing DBMS submissions,

observe

Conceptual understanding

Correct terminology

Correct ER diagrams

Correct key selection

Database thinking

Relationship understanding

Ability to explain design decisions

Avoid rewarding memorized definitions.

---

# CHAPTER EVOLUTION

Future lessons should expand existing chapters.

Example

ER Model

↓

Cardinality

↓

Weak Entity

↓

Relationship Types

↓

Update ER Model.md

Example

Transactions

↓

ACID

↓

Isolation Levels

↓

Concurrency

↓

Update Transactions.md

Avoid unnecessary chapter duplication.

---

# INTERVIEW ENGINEERING

Whenever possible,

convert theory into engineering discussions.

Examples

Why is normalization important?

Why are transactions necessary?

Why should primary keys be stable?

Why are indexes not created on every column?

Why do foreign keys improve integrity?

Teach learners to justify design decisions.

---

# FAILURE CONDITIONS

The skill has failed if

• DBMS is taught as definitions only.

• Real applications are missing.

• Database design thinking is absent.

• Backend relevance is ignored.

• Diagrams are missing where appropriate.

• SQL connection is missing.

---

# SUCCESS CONDITIONS

The skill succeeds when

The learner understands

How databases are designed.

Why DBMS exists.

How SQL implements DBMS concepts.

How backend applications use databases.

How interviewers evaluate database knowledge.

How to design scalable and maintainable databases.

---

# FINAL PRINCIPLE

DBMS is not about remembering definitions.

It is about learning how to design reliable, scalable and maintainable data systems.

Every chapter should make the learner think like a Software Engineer designing real-world databases, not a student memorizing textbook concepts.