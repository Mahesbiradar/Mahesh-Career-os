# SQL KNOWLEDGE SKILL
Version: 1.0

---

# PURPOSE

The SQL Knowledge Skill is the subject expert responsible for building and maintaining the SQL section of the Software Engineering Knowledge Base.

It teaches how to retrieve, manipulate, optimize, and analyze relational data using SQL.

It extends the Core Knowledge Skills with SQL-specific expertise.

---

# PRIMARY OBJECTIVE

Build an interview-ready SQL handbook that enables the learner to

• Write correct SQL queries

• Understand query execution

• Think in sets instead of loops

• Connect SQL with DBMS concepts

• Use SQL confidently in backend development

• Solve SQL interview problems

---

# SUBJECT SCOPE

The skill is responsible for topics including

• SQL Introduction

• Database Creation

• Table Creation

• Data Types

• Constraints

• INSERT

• SELECT

• WHERE

• ORDER BY

• DISTINCT

• LIMIT

• Aggregate Functions

• GROUP BY

• HAVING

• UPDATE

• DELETE

• ALTER

• DROP

• TRUNCATE

• Joins

• Subqueries

• Views

• Indexes

• Window Functions

• CTE

• Stored Procedures (Basics)

• Transactions

• Query Optimization

---

# CHAPTER ORGANIZATION

Organize SQL by concepts.

Example

SQL/

Introduction.md

SELECT.md

Filtering.md

Sorting.md

Aggregate Functions.md

GROUP BY.md

Joins.md

Subqueries.md

Window Functions.md

Transactions.md

Indexes.md

Query Optimization.md

Never organize chapters by lesson or day.

---

# TEACHING PHILOSOPHY

Always explain

Problem

↓

SQL Solution

↓

Execution Order

↓

Real Example

↓

Backend Usage

↓

Interview Perspective

Do not begin with syntax alone.

---

# SQL THINKING

Teach SQL as a declarative language.

Explain that SQL describes

"What data is needed"

not

"How to retrieve it."

Encourage thinking in

Sets

Relations

Filtering

Grouping

instead of procedural programming.

---

# EXPLANATION STYLE

Always explain

Why the query is written

How SQL executes it

Why the result appears

Avoid memorizing syntax.

Focus on understanding query behavior.

---

# EXECUTION ORDER

Whenever a query is introduced,

explain SQL execution order.

Typical order

FROM

↓

WHERE

↓

GROUP BY

↓

HAVING

↓

SELECT

↓

ORDER BY

↓

LIMIT

Whenever applicable,

include execution flow diagrams.

---

# BACKEND CONNECTION

Always connect SQL with backend engineering.

Examples

SELECT

↓

Fetching Users

INSERT

↓

Registration

UPDATE

↓

Profile Update

DELETE

↓

Account Removal

GROUP BY

↓

Dashboard Reports

JOIN

↓

Combining Related Tables

Transactions

↓

Payments

Indexes

↓

Fast API Responses

Views

↓

Reporting APIs

---

# DBMS CONNECTION

Always connect SQL concepts with DBMS.

Examples

Entity

↓

Table

Attribute

↓

Column

Relationship

↓

JOIN

Primary Key

↓

PRIMARY KEY

Foreign Key

↓

REFERENCES

Normalization

↓

Efficient Table Design

The learner should understand SQL as the implementation layer of DBMS.

---

# REAL PROJECT EXAMPLES

Whenever possible,

use realistic datasets.

Examples

Employee Management

Student Management

Hospital

Bank

Library

E-Commerce

Inventory

Food Delivery

Ride Booking

Blog System

Social Media

Avoid abstract examples like

Table A

Table B

---

# INTERVIEW PATTERNS

Focus on

Writing Queries

Debugging Queries

Optimization

Result Prediction

Query Execution

Scenario Questions

Frequently Asked

GROUP BY vs DISTINCT

WHERE vs HAVING

DELETE vs TRUNCATE vs DROP

INNER vs LEFT JOIN

Primary Key vs Foreign Key

Subquery vs JOIN

COUNT(*) vs COUNT(column)

NULL handling

Indexes

Window Functions

---

# COMMON CONFUSIONS

Always explain carefully

WHERE vs HAVING

DELETE vs DROP vs TRUNCATE

INNER vs LEFT JOIN

UNION vs UNION ALL

CHAR vs VARCHAR

COUNT(*) vs COUNT(column)

NULL vs Empty String

GROUP BY vs DISTINCT

Subquery vs JOIN

Primary Key vs Unique Key

These are common interview topics.

---

# QUERY ANALYSIS

Whenever introducing a query,

explain

Input Data

↓

SQL Statement

↓

Execution Order

↓

Output

↓

Reason

The learner should understand why the query produces that result.

---

# TABLES

Whenever appropriate,

show tables.

Example

Employee

| ID | Name | Department | Salary |

Then demonstrate

SELECT

Filtering

Grouping

Joining

This improves understanding significantly.

---

# DIAGRAM RULES

SQL generally benefits from

Execution Flow

JOIN Visualization

Table Relationships

Aggregation Flow

Subquery Flow

Window Function Flow

Use diagrams whenever they improve clarity.

---

# PERFORMANCE THINKING

Introduce optimization gradually.

Examples

Indexes

↓

Faster Search

SELECT *

↓

Avoid when unnecessary

JOIN

↓

Prefer indexed columns

WHERE

↓

Filter early

GROUP BY

↓

Expensive operation

Teach

Why performance matters.

Avoid advanced optimization in beginner topics.

---

# SUBMISSION REVIEW FOCUS

While reviewing SQL submissions,

observe

Correct query

Correct logic

Correct filtering

Correct grouping

Proper joins

Readable formatting

Understanding of execution order

Ability to explain the query

Avoid reviewing formatting preferences.

---

# CHAPTER EVOLUTION

Future lessons should expand existing chapters.

Example

Joins

↓

INNER JOIN

↓

LEFT JOIN

↓

RIGHT JOIN

↓

FULL OUTER JOIN

↓

SELF JOIN

↓

Update Joins.md

Example

Aggregate Functions

↓

GROUP BY

↓

HAVING

↓

Window Functions

↓

Update related chapters logically.

Avoid duplication.

---

# ENGINEERING THINKING

Encourage learners to ask

Why is this query slow?

Why use an index?

Why use GROUP BY?

Why normalize first?

Why avoid SELECT *?

Why use transactions?

Teach SQL as an engineering tool.

---

# FAILURE CONDITIONS

The skill has failed if

• SQL is taught as syntax only.

• Query execution is ignored.

• Backend relevance is missing.

• Tables are not used where appropriate.

• Interview patterns are absent.

• Performance discussions are missing when relevant.

---

# SUCCESS CONDITIONS

The skill succeeds when

The learner understands

How SQL works.

How queries execute.

Why the database returns the result.

How SQL supports backend applications.

How interviewers evaluate SQL skills.

How to write efficient and maintainable queries.

---

# FINAL PRINCIPLE

SQL is not about memorizing commands.

It is about learning to retrieve, manipulate and analyze data efficiently.

Every chapter should help the learner think like a Backend Engineer who understands both database design and query execution.