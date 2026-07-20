# SQL-OS

> **Goal:** Achieve professional-level SQL proficiency for backend development, interviews, and data work.
> **Database Focus:** PostgreSQL (with standard SQL compatibility noted).
> **Scope:** From foundational queries through advanced window functions and optimization.

---

## Level Structure Overview

| Level | Name | Capability |
|-------|------|-----------|
| Level 1 | Foundation | Understand relational databases, write basic queries |
| Level 2 | Core Queries | Read and manipulate data confidently |
| Level 3 | Filtering & Conditions | Write complex WHERE clauses |
| Level 4 | Aggregations & Grouping | Summarize and analyze data |
| Level 5 | Joins | Combine data from multiple tables |
| Level 6 | Subqueries & CTEs | Write modular, nested queries |
| Level 7 | Window Functions | Write analytics-level SQL |
| Level 8 | Schema Design & DDL | Design and manage database structures |
| Level 9 | Indexes | Optimize query performance |
| Level 10 | Transactions | Write safe, concurrent-safe queries |
| Level 11 | PostgreSQL Specifics | Use PostgreSQL's advanced features |

---

## Level 1 — Foundation

---

### 1.1 Relational Database Concepts

- **Why It Matters:** Without understanding the relational model, SQL is just memorizing syntax. The model explains *why* SQL works the way it does.
- **Prerequisites:** None
- **Interview Importance:** High — "explain what a relational database is"
- **Job Importance:** Critical

Topics:
- What is a relational database
- Tables (relations), rows (tuples), columns (attributes)
- Schema — the structure/definition
- Instances — the actual data
- Primary Key — uniquely identifies each row
- Foreign Key — references a primary key in another table
- Referential integrity
- Relational algebra conceptual basis (SELECT, PROJECT, JOIN)

---

### 1.2 Data Types in SQL

- **Why It Matters:** Choosing wrong data types causes storage waste, slow queries, and subtle bugs.
- **Prerequisites:** 1.1
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- **Numeric:** `INTEGER`, `BIGINT`, `SMALLINT`, `DECIMAL(p,s)`, `NUMERIC`, `REAL`, `DOUBLE PRECISION`, `SERIAL`, `BIGSERIAL`
- **Text:** `CHAR(n)`, `VARCHAR(n)`, `TEXT`
- **Boolean:** `BOOLEAN` (TRUE, FALSE, NULL)
- **Date/Time:** `DATE`, `TIME`, `TIMESTAMP`, `TIMESTAMPTZ`, `INTERVAL`
- **Binary:** `BYTEA`
- **PostgreSQL-specific:** `UUID`, `JSON`, `JSONB`, `ARRAY`, `INET`, `CIDR`
- NULL — the absence of a value (not zero, not empty string)
- Type casting: `CAST(x AS type)` and `x::type`
- Choosing the right type for money (DECIMAL, not FLOAT)

---

### 1.3 NULL Handling

- **Why It Matters:** NULL causes counterintuitive behavior. Bugs from misunderstanding NULL are extremely common.
- **Prerequisites:** 1.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- NULL vs 0 vs empty string
- Three-valued logic (TRUE, FALSE, NULL)
- `IS NULL` and `IS NOT NULL` (never use `= NULL`)
- NULL in arithmetic (`5 + NULL = NULL`)
- NULL in comparisons (`NULL = NULL` is NULL, not TRUE)
- NULL in aggregate functions (most ignore NULLs)
- `COALESCE(x, default)` — return first non-NULL
- `NULLIF(x, y)` — return NULL if x equals y
- NULL in sorting (`NULLS FIRST` / `NULLS LAST`)

---

## Level 2 — Core Queries (DML)

---

### 2.1 SELECT Statement

- **Why It Matters:** SELECT is 90% of SQL. Every analysis, every API data fetch, every report uses SELECT.
- **Prerequisites:** Level 1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `SELECT column1, column2 FROM table`
- `SELECT *` — when to use (and when not to)
- Column aliases (`AS`)
- Table aliases (e.g., `users AS u`)
- `DISTINCT` — remove duplicate rows
- Arithmetic in SELECT
- String concatenation in SELECT
- `SELECT` without `FROM` (expressions, functions)
- Query execution order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

---

### 2.2 INSERT

- **Why It Matters:** Creating data is fundamental. Understanding the full INSERT syntax prevents errors.
- **Prerequisites:** 2.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- Single row insert
- Multi-row insert
- `INSERT INTO ... SELECT ...` (copy data from another query)
- Default values
- `RETURNING` clause (PostgreSQL — get inserted row back)
- `INSERT ON CONFLICT DO NOTHING` (UPSERT)
- `INSERT ON CONFLICT DO UPDATE` (UPSERT)

---

### 2.3 UPDATE

- **Why It Matters:** Updating data safely (with proper WHERE) is critical. Updating without WHERE is a career incident.
- **Prerequisites:** 2.2
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- Basic `UPDATE table SET column = value WHERE condition`
- Updating multiple columns
- `UPDATE ... RETURNING` (PostgreSQL)
- `UPDATE ... FROM` (joining another table in update)
- Atomic increment (`SET count = count + 1`)
- Always use WHERE in production UPDATE

---

### 2.4 DELETE

- **Why It Matters:** Deletion is irreversible without backups. Understanding DELETE properly prevents disasters.
- **Prerequisites:** 2.3
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `DELETE FROM table WHERE condition`
- `DELETE ... RETURNING` (PostgreSQL)
- Soft delete pattern (logical delete with `is_deleted` flag)
- Cascade deletes (via foreign key constraints)
- `TRUNCATE` vs `DELETE` (truncate is faster, no WHERE, no RETURNING)
- Protecting against accidental full deletes

---

### 2.5 ORDER BY & LIMIT

- **Why It Matters:** Pagination, top-N queries, and sorted results all require ORDER BY and LIMIT.
- **Prerequisites:** 2.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `ORDER BY column ASC/DESC`
- Ordering by multiple columns
- Ordering by expression
- `LIMIT n` — first n rows
- `OFFSET n` — skip n rows
- `LIMIT` + `OFFSET` for pagination
- Performance of OFFSET at large values (degrades)
- `FETCH FIRST n ROWS ONLY` (SQL standard syntax)

---

## Level 3 — Filtering & Conditions

---

### 3.1 WHERE Clause Operators

- **Why It Matters:** Precise filtering is the difference between returning the right data and the wrong data.
- **Prerequisites:** Level 2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Comparison: `=`, `<>` / `!=`, `<`, `>`, `<=`, `>=`
- `BETWEEN x AND y` (inclusive on both ends)
- `IN (value1, value2, ...)`
- `NOT IN` — careful with NULLs (`NOT IN (NULL)` returns nothing)
- `LIKE` — pattern matching with `%` and `_`
- `ILIKE` — case-insensitive LIKE (PostgreSQL)
- `SIMILAR TO` — regex-like (PostgreSQL)
- `~` operator for regex (PostgreSQL)
- Combining: `AND`, `OR`, `NOT`
- Parentheses for logical grouping

---

### 3.2 CASE Expression

- **Why It Matters:** CASE is SQL's if-else. Used in SELECT, WHERE, ORDER BY, and aggregate functions.
- **Prerequisites:** 3.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Simple CASE: `CASE column WHEN value THEN result`
- Searched CASE: `CASE WHEN condition THEN result`
- `ELSE` clause
- Nested CASE
- CASE in SELECT (conditional columns)
- CASE in ORDER BY (conditional sorting)
- CASE in aggregates (`SUM(CASE WHEN ... THEN 1 ELSE 0 END)`)
- CASE vs `FILTER` clause (PostgreSQL)

---

## Level 4 — Aggregations & Grouping

---

### 4.1 Aggregate Functions

- **Why It Matters:** Almost every business report and API analytics endpoint uses aggregates.
- **Prerequisites:** Level 2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `COUNT(*)` — count all rows
- `COUNT(column)` — count non-NULL values
- `COUNT(DISTINCT column)` — unique non-NULL values
- `SUM(column)` — total
- `AVG(column)` — mean
- `MIN(column)` — minimum
- `MAX(column)` — maximum
- `STDDEV()`, `VARIANCE()` (statistics)
- Aggregate with NULL behavior
- `STRING_AGG(column, separator)` (PostgreSQL) — concatenate strings

---

### 4.2 GROUP BY

- **Why It Matters:** GROUP BY is how you calculate statistics per category. Required for any reporting query.
- **Prerequisites:** 4.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `GROUP BY column`
- Grouping by multiple columns
- All non-aggregate SELECT columns must be in GROUP BY
- `GROUP BY` with expressions
- `ROLLUP` — subtotals
- `CUBE` — all combinations
- `GROUPING SETS` — custom rollup
- `GROUPING()` function

---

### 4.3 HAVING

- **Why It Matters:** WHERE filters rows before grouping. HAVING filters groups after aggregation. Mixing them up produces wrong results.
- **Prerequisites:** 4.2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `HAVING aggregate_condition`
- WHERE vs HAVING (execution order)
- HAVING with multiple conditions
- HAVING without GROUP BY (rare but valid)
- Performance: filter with WHERE before GROUP BY when possible

---

## Level 5 — Joins

> *Joins are the most tested SQL concept in interviews. Master all types.*

---

### 5.1 INNER JOIN

- **Why It Matters:** Returns rows with matches in both tables. Most common join type in production queries.
- **Prerequisites:** Level 1 (keys)
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Syntax: `table1 JOIN table2 ON table1.col = table2.col`
- Implicit vs explicit JOIN (always use explicit)
- Multi-column join conditions
- Chaining multiple JOINs
- Performance considerations (join column indexing)

---

### 5.2 LEFT (OUTER) JOIN

- **Why It Matters:** Returns all rows from the left table, NULLs for no match on right. Essential for "find records without related records."
- **Prerequisites:** 5.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- All left rows preserved
- NULL in right-side columns when no match
- `WHERE right.id IS NULL` pattern — find unmatched left rows
- LEFT JOIN vs INNER JOIN result difference
- Use cases: optional relationships, existence checks

---

### 5.3 RIGHT (OUTER) JOIN

- **Why It Matters:** Mirror of LEFT JOIN. Less common — most developers rewrite as LEFT JOIN with tables swapped.
- **Prerequisites:** 5.2
- **Interview Importance:** Medium
- **Job Importance:** Low-Medium

Topics:
- All right rows preserved
- Rewriting as LEFT JOIN (preferred practice)

---

### 5.4 FULL OUTER JOIN

- **Why It Matters:** Preserves all rows from both tables. Used for reconciliation queries, finding mismatches in both directions.
- **Prerequisites:** 5.2
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- All rows from both tables
- NULLs for non-matching rows on either side
- Detecting rows missing from either table
- Simulating with UNION of LEFT + RIGHT JOIN

---

### 5.5 CROSS JOIN

- **Why It Matters:** Cartesian product. Used for generating combinations. Understanding it explains accidental cartesian products (a common performance bug).
- **Prerequisites:** 5.1
- **Interview Importance:** Medium
- **Job Importance:** Low-Medium

Topics:
- Every row from table1 combined with every row from table2
- N × M rows result
- Accidental cross join when forgetting JOIN condition
- Use cases: generating test data, combinations

---

### 5.6 SELF JOIN

- **Why It Matters:** Used for hierarchical data — employees and managers, category trees, org charts.
- **Prerequisites:** 5.1
- **Interview Importance:** High — common interview question
- **Job Importance:** Medium-High

Topics:
- Joining a table to itself
- Alias required for both copies
- Hierarchical data queries (manager-employee)
- Finding pairs in same table

---

### 5.7 Multi-Table Joins & Patterns

- **Why It Matters:** Real queries join 3-10 tables. Understanding join order and optimization is critical.
- **Prerequisites:** 5.1-5.6
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Joining 3+ tables
- Join order (SQL optimizer handles, but understanding helps)
- Joining on expressions (not just equality)
- Non-equi joins
- `USING` clause (shorthand for equality on same-named column)
- `NATURAL JOIN` (avoid — fragile)
- JOIN with GROUP BY and aggregation

---

## Level 6 — Subqueries & CTEs

---

### 6.1 Subqueries

- **Why It Matters:** Subqueries allow query composition — the output of one query becomes the input of another.
- **Prerequisites:** Level 5
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Scalar subquery (returns single value) — in SELECT, WHERE, HAVING
- Row subquery (returns single row)
- Table subquery (returns multiple rows) — in FROM (derived table)
- Subquery in WHERE with `=`, `IN`, `ANY`, `ALL`
- `IN` with subquery
- `NOT IN` with subquery (careful with NULLs)
- `ANY` / `SOME` — at least one row matches
- `ALL` — all rows match

---

### 6.2 Correlated Subqueries

- **Why It Matters:** Correlated subqueries reference the outer query — powerful but often have performance implications.
- **Prerequisites:** 6.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Outer query reference in subquery
- Execution model (runs once per outer row)
- Performance implications (can be slow)
- `EXISTS` — does any row match?
- `NOT EXISTS` — does no row match?
- `EXISTS` vs `IN` (performance and NULL behavior)
- Rewriting correlated subqueries as JOINs

---

### 6.3 Common Table Expressions (CTEs)

- **Why It Matters:** CTEs make complex queries readable by breaking them into named, reusable query blocks. Essential for maintainable SQL.
- **Prerequisites:** 6.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `WITH cte_name AS (SELECT ...)` syntax
- Multiple CTEs (chained)
- Referencing CTE in main query
- CTE vs subquery vs temp table (when to use each)
- `MATERIALIZED` vs `NOT MATERIALIZED` hints (PostgreSQL)

---

### 6.4 Recursive CTEs

- **Why It Matters:** Hierarchical data (org charts, categories, trees, bill of materials) requires recursive CTEs or repeated queries.
- **Prerequisites:** 6.3
- **Interview Importance:** Medium-High
- **Job Importance:** Medium

Topics:
- `WITH RECURSIVE` syntax
- Anchor member (base case)
- Recursive member
- `UNION ALL` (or `UNION`)
- Termination condition (cycle prevention)
- Traversing org charts
- Path enumeration
- Depth tracking

---

## Level 7 — Window Functions

> *Window functions are the most powerful SQL feature after joins. They're heavily tested in senior interviews and essential for analytics.*

---

### 7.1 Window Function Fundamentals

- **Why It Matters:** Window functions perform calculations across a set of rows related to the current row WITHOUT collapsing them like GROUP BY does.
- **Prerequisites:** Level 6
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `function() OVER (...)` syntax
- OVER clause components: PARTITION BY, ORDER BY, FRAME
- Window functions vs GROUP BY (both rows and aggregated values simultaneously)
- `PARTITION BY` — groups within the window
- `ORDER BY` in OVER clause
- Named windows (`WINDOW w AS (...)`)
- Which rows each window function sees

---

### 7.2 Ranking Functions

- **Why It Matters:** Top-N per group, deduplication, rank-based analysis — all use ranking functions.
- **Prerequisites:** 7.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `ROW_NUMBER()` — unique sequential number (no ties)
- `RANK()` — same rank for ties, gaps after ties
- `DENSE_RANK()` — same rank for ties, no gaps
- `NTILE(n)` — divides rows into n buckets
- Filtering with window functions (wrap in subquery/CTE)
- "Top N per group" pattern using `ROW_NUMBER()`

---

### 7.3 Offset Functions

- **Why It Matters:** Time series analysis, comparing to previous period, lead/lag calculations — ubiquitous in data work.
- **Prerequisites:** 7.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `LAG(column, offset, default)` — access previous row's value
- `LEAD(column, offset, default)` — access next row's value
- `FIRST_VALUE(column)` — first value in window
- `LAST_VALUE(column)` — last value in window (watch frame)
- `NTH_VALUE(column, n)` — nth value in window
- Period-over-period comparison
- Default values for first/last rows

---

### 7.4 Aggregate Window Functions

- **Why It Matters:** Running totals, moving averages, cumulative distributions — all done with aggregate window functions.
- **Prerequisites:** 7.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `SUM() OVER (ORDER BY ...)` — running total
- `AVG() OVER (PARTITION BY ...)` — group average alongside each row
- `COUNT() OVER (...)`
- `MIN() OVER (...)` and `MAX() OVER (...)`
- Frame clauses:
  - `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` — cumulative
  - `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` — rolling window
  - `RANGE BETWEEN INTERVAL '7 days' PRECEDING AND CURRENT ROW`
- Moving averages
- Cumulative sums

---

### 7.5 Distribution Functions

- **Why It Matters:** Used for percentile analysis, outlier detection, and statistical reporting.
- **Prerequisites:** 7.1
- **Interview Importance:** Medium
- **Job Importance:** Medium-High

Topics:
- `CUME_DIST()` — cumulative distribution (0 to 1)
- `PERCENT_RANK()` — relative rank (0 to 1)
- `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY column)` — median
- `PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY column)`

---

## Level 8 — Schema Design & DDL

---

### 8.1 CREATE TABLE & Constraints

- **Why It Matters:** Designing tables with proper constraints prevents data corruption at the database level.
- **Prerequisites:** Level 1
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `CREATE TABLE` syntax
- `NOT NULL` constraint
- `UNIQUE` constraint (single and composite)
- `PRIMARY KEY` (column and table level)
- `FOREIGN KEY` with `ON DELETE` and `ON UPDATE` actions (CASCADE, RESTRICT, SET NULL, SET DEFAULT)
- `CHECK` constraint
- `DEFAULT` value
- Constraint naming (important for error handling and migration)

---

### 8.2 ALTER TABLE

- **Why It Matters:** Schema evolves. Knowing how to safely modify tables in production prevents downtime.
- **Prerequisites:** 8.1
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `ADD COLUMN` — safe to add nullable columns
- `DROP COLUMN`
- `ALTER COLUMN TYPE` — risky in production
- `RENAME COLUMN`
- `ADD CONSTRAINT` / `DROP CONSTRAINT`
- `RENAME TABLE`
- Adding indexes `CONCURRENTLY` (PostgreSQL — no lock)
- Zero-downtime migration strategies

---

### 8.3 Database Design from Requirements

- **Why It Matters:** Real job skill — converting a business problem into a normalized schema.
- **Prerequisites:** 8.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Identifying entities from requirements
- One-to-one, one-to-many, many-to-many patterns
- Junction/association table for many-to-many
- Choosing between embedding and relating
- Handling soft deletes (`deleted_at` timestamp)
- Audit columns (`created_at`, `updated_at`, `created_by`)
- UUID vs auto-increment primary key (tradeoffs)
- Schema versioning with migrations

---

## Level 9 — Indexes

---

### 9.1 Index Fundamentals

- **Why It Matters:** Missing indexes cause slow queries. Wrong indexes waste storage and slow writes. Knowing when and what to index is a core skill.
- **Prerequisites:** Level 8
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Why indexes exist (avoid full table scans)
- B-Tree index (default — for equality and range)
- Hash index (equality only — PostgreSQL)
- GIN index (JSONB, arrays, full-text search)
- GiST index (geographic, full-text)
- BRIN index (huge tables with sequential data)
- Index tradeoff: faster reads, slower writes, storage
- `CREATE INDEX idx_name ON table(column)`
- `CREATE INDEX CONCURRENTLY` (no table lock)
- Partial index (`CREATE INDEX ... WHERE condition`)
- Composite index (multiple columns)
- Index column order matters for composite indexes

---

### 9.2 Query Plan Analysis

- **Why It Matters:** SQL tuning requires reading the query plan. You can't optimize what you can't measure.
- **Prerequisites:** 9.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `EXPLAIN` — show query plan
- `EXPLAIN ANALYZE` — run and show actual times
- `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` — detailed output
- Sequential Scan vs Index Scan vs Bitmap Heap Scan
- Nested Loop vs Hash Join vs Merge Join
- Understanding costs (startup, total)
- Understanding rows estimate vs actual
- When PostgreSQL ignores your index
- Vacuuming and statistics (`ANALYZE` command, autovacuum)
- `pg_stat_user_indexes` — index usage

---

### 9.3 Index Optimization Patterns

- **Why It Matters:** Knowing the patterns lets you diagnose and fix performance issues systematically.
- **Prerequisites:** 9.2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Covering index (index-only scan)
- Index on foreign key columns (prevent sequential scans on JOINs)
- Composite index column order: equality first, then range
- Function index (`CREATE INDEX ON table(lower(email))`)
- Index bloat (dead tuples)
- `REINDEX` and `VACUUM`
- When NOT to index (small tables, high-write columns)
- Identifying unused indexes

---

## Level 10 — Transactions

---

### 10.1 Transaction Basics

- **Why It Matters:** Transactions ensure data integrity. Without them, concurrent writes corrupt data.
- **Prerequisites:** Level 2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `BEGIN` / `START TRANSACTION`
- `COMMIT` — make changes permanent
- `ROLLBACK` — undo all changes
- Autocommit mode
- `SAVEPOINT name` — partial rollback point
- `ROLLBACK TO SAVEPOINT name`
- `RELEASE SAVEPOINT name`
- Implicit transactions in ORMs (Django `atomic()`)

---

### 10.2 ACID Properties

- **Why It Matters:** ACID is the fundamental guarantee of relational databases. Every DBMS interview question about reliability comes back to ACID.
- **Prerequisites:** 10.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- **Atomicity** — all or nothing (no partial commits)
- **Consistency** — transaction moves DB from valid state to valid state
- **Isolation** — concurrent transactions don't interfere
- **Durability** — committed transactions survive failures
- ACID in PostgreSQL
- BASE (Basically Available, Soft state, Eventually consistent) as the NoSQL contrast

---

### 10.3 Isolation Levels

- **Why It Matters:** Isolation levels control the tradeoff between concurrency and consistency. Wrong level causes data bugs.
- **Prerequisites:** 10.2
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:

**Read Phenomena:**
- **Dirty Read** — reading uncommitted data from another transaction
- **Non-Repeatable Read** — same row returns different values in same transaction
- **Phantom Read** — new rows appear in re-executed query in same transaction
- **Serialization Anomaly** — transactions produce result not achievable sequentially

**Isolation Levels (SQL standard):**
- `READ UNCOMMITTED` — allows dirty reads (not supported in PostgreSQL)
- `READ COMMITTED` — default in PostgreSQL; prevents dirty reads
- `REPEATABLE READ` — prevents dirty + non-repeatable reads
- `SERIALIZABLE` — full isolation; prevents all anomalies

**PostgreSQL Specifics:**
- Default: READ COMMITTED
- MVCC (Multi-Version Concurrency Control) implementation
- `SELECT ... FOR UPDATE` — pessimistic lock
- `SELECT ... FOR SHARE`
- `NOWAIT` and `SKIP LOCKED` options

---

### 10.4 Transactions in Application Code

- **Why It Matters:** ORMs handle transactions but developers must know when to use explicit transactions.
- **Prerequisites:** 10.3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Django `transaction.atomic()` as decorator and context manager
- Nested `atomic()` blocks (savepoints)
- `on_commit()` — run code after transaction commits (for Celery tasks)
- When to avoid transactions (long-running, read-only)
- Deadlock avoidance patterns
- Retry logic for serialization failures

---

## Level 11 — PostgreSQL Specifics

---

### 11.1 JSONB & JSON

- **Why It Matters:** Modern applications store semi-structured data. JSONB is PostgreSQL's most powerful feature for flexible schemas.
- **Prerequisites:** Level 2
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- `JSON` vs `JSONB` (JSONB is binary, indexed, faster for query)
- Accessing JSON keys: `data->>'key'` (text), `data->'key'` (JSON)
- Nested access: `data->'address'->>'city'`
- `jsonb_set()` — update a key
- `jsonb_insert()` — add key
- `@>` contains operator
- `?` key exists operator
- GIN index on JSONB columns
- `jsonb_agg()`, `jsonb_build_object()`, `json_build_array()`
- Querying JSONB arrays

---

### 11.2 Arrays

- **Why It Matters:** PostgreSQL arrays allow storing lists within a column — useful for tags, categories, permissions.
- **Prerequisites:** Level 2
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- `INTEGER[]`, `TEXT[]`, etc.
- Array literals: `ARRAY[1,2,3]`, `'{1,2,3}'`
- Array access: `arr[1]` (1-indexed!)
- `array_length()`, `cardinality()`
- `unnest()` — expand array to rows
- `array_agg()` — aggregate rows to array
- `@>`, `<@`, `&&` operators
- GIN index for array search

---

### 11.3 Full-Text Search

- **Why It Matters:** Built-in full-text search avoids Elasticsearch for simpler use cases.
- **Prerequisites:** Level 9
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- `to_tsvector()` — document to text search vector
- `to_tsquery()` — query parsing
- `@@` match operator
- GIN index on `tsvector` column
- Ranking results with `ts_rank()`
- Highlighting matches with `ts_headline()`

---

### 11.4 Performance & Utility Functions

- **Why It Matters:** PostgreSQL ships with powerful built-in functions that reduce need for application code.
- **Prerequisites:** Level 4-7
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `generate_series(start, stop, step)` — generate sequences
- `pg_sleep(seconds)` — testing delays
- `RETURNING` clause on INSERT/UPDATE/DELETE
- `UPSERT` (`INSERT ... ON CONFLICT DO UPDATE`)
- `COPY` command (bulk data loading)
- `NOW()`, `CURRENT_TIMESTAMP`, `CURRENT_DATE`
- Date arithmetic with `INTERVAL`
- `date_trunc()` — truncate to week/month/year
- `extract()` / `date_part()` — year, month, day, hour
- `age()` — compute interval between dates
- String functions: `regexp_replace()`, `regexp_match()`, `split_part()`

---

### 11.5 PostgreSQL Monitoring

- **Why It Matters:** Production databases require monitoring to catch slow queries, locks, and bloat before they become outages.
- **Prerequisites:** Level 9
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `pg_stat_activity` — active queries and locks
- `pg_stat_user_tables` — table statistics
- `pg_stat_user_indexes` — index usage statistics
- `pg_locks` — current locks
- `pg_stat_statements` — aggregate query statistics (extension)
- Long-running query detection
- Lock contention detection
- Table and index bloat queries

---

*This is the knowledge inventory for SQL. Roadmap and scheduling are managed separately.*
