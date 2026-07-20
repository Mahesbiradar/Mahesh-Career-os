# SQL-OS — Knowledge Rules

> Read by the Notes Update agent. Defines how SQL concepts are organized and explained in notes/.

---

## CHAPTER ORGANIZATION

One file per SQL concept. Never by lesson or day.

Example structure:
```
notes/
  Introduction to SQL.md
  SELECT.md
  Filtering.md
  Joins.md
  Aggregate Functions.md
  Subqueries.md
  Window Functions.md
  Transactions.md
  Indexes.md
  Query Optimization.md
```

---

## NOTE FILE STRUCTURE

```
# [Topic Name] (SQL)

## Why It Matters
- What business problem this SQL feature solves
- Backend usage (what API endpoint or report uses it)

## Core Concept
- What the query/clause does in plain English
- SQL execution order if relevant

## Syntax Pattern
```sql
-- minimal example, realistic table names
SELECT column FROM table WHERE condition;
```

## Query Analysis
| Step | What SQL Does |
|---|---|
| FROM | ... |
| WHERE | ... |
| SELECT | ... |

## Interview Questions
Basic / Intermediate / Scenario
⭐ mark the most frequently asked

## Common Confusions ⚠
- WHERE vs HAVING
- DELETE vs TRUNCATE vs DROP
- INNER vs LEFT JOIN
- COUNT(*) vs COUNT(column)

## 30-Second Interview Revision
[5 bullet points]
```

---

## SQL TEACHING STYLE

- Always explain WHY the query is written, not just HOW
- Use execution order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
- Use realistic datasets (employees, orders, customers — not table_a, col_b)
- Always show expected output
- Connect every SQL feature to a backend use case

---

## COMMON SQL CONFUSIONS
- WHERE vs HAVING — WHERE filters rows before grouping; HAVING filters after
- DELETE vs TRUNCATE vs DROP — different scope and reversibility
- INNER JOIN vs LEFT JOIN — what happens to non-matching rows
- COUNT(*) vs COUNT(col) — NULL handling
- GROUP BY vs DISTINCT — different purposes
- NULL vs Empty String — different in SQL
- Subquery vs JOIN — different use cases

---

## QUALITY CHECK
Failed if: SQL taught as syntax only, no execution order, no backend context, no realistic data.
Succeeds when: learner understands why the query works, not just that it works.
