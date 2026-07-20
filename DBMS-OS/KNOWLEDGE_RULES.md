# DBMS-OS — Knowledge Rules

> Read by the Notes Update agent. Defines how DBMS concepts are organized in notes/.

---

## CHAPTER ORGANIZATION

One file per DBMS concept. Never by lesson or day.

Example structure:
```
notes/
  Introduction to DBMS.md
  ER Model.md
  Keys.md
  Normalization.md
  Transactions.md
  Concurrency Control.md
  Indexing.md
  Database Design.md
```

## NOTE FILE STRUCTURE

```
# [Topic Name] (DBMS)

## Why It Matters
- What problem this concept solves
- Backend relevance (where it appears in real systems)

## Core Concept
- Plain English explanation (not a textbook definition)
- The engineering insight behind it

## Real-World Example
[Concrete example: e-commerce, hospital, bank — not abstract]

## Key Terms
[Define each important term in one sentence]

## Connection to SQL
[How this DBMS concept maps to actual SQL syntax]

## Interview Questions
Basic / Intermediate / Design
⭐ most frequently asked

## Common Confusions ⚠
[Pairs of concepts that get mixed up]

## 30-Second Interview Revision
[5 bullet points — fastest recall]
```

## TEACHING STYLE
- Problem → Solution → How DBMS solves it → Real Example → Backend connection
- Never start with textbook definitions
- Always connect to SQL implementation
- Always use real-world domain examples (not abstract entity/attribute names)

## COMMON DBMS CONFUSIONS
- DBMS vs Database (the software vs the data)
- Entity vs Table (conceptual vs physical)
- Attribute vs Column (model vs implementation)
- Primary Key vs Unique Key
- Candidate Key vs Primary Key
- Normalization vs Denormalization (why each is used)
- Transaction vs Query
- Delete vs Truncate vs Drop

## QUALITY CHECK
Failed if: topics taught as definitions, no real examples, no SQL connection, no backend relevance.
Succeeds when: learner can explain what it is, why it exists, where it appears, and how interviewers ask it.
