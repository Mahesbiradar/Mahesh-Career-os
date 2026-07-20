# DBMS Syllabus — DBMS-OS

> **Goal:** Master Database Management Systems theory for software engineering interviews.
> **Focus:** Interview preparation + conceptual depth for production system design.
> **Scope:** ER modeling, normalization, indexing, transactions, concurrency, NoSQL awareness.

---

## Why DBMS Theory Matters for Interviews

Every software engineering interview at product companies (and most service companies) includes DBMS questions. These are not just SQL questions — they test *why* databases work the way they do. Interviewers use DBMS knowledge to assess:
- Whether you understand data modeling
- Whether you can design schemas that don't corrupt data
- Whether you understand transaction safety
- Whether you can reason about concurrent systems

---

## Level Structure

| Level | Topic | Interview Weight |
|-------|-------|----------------|
| Level 1 | Foundations & Architecture | Medium |
| Level 2 | ER Modeling | High |
| Level 3 | Relational Model & Keys | Critical |
| Level 4 | Normalization | Critical |
| Level 5 | Indexing (Deep Dive) | Critical |
| Level 6 | Transactions & ACID | Critical |
| Level 7 | Concurrency Control | High |
| Level 8 | Database Recovery | Medium |
| Level 9 | NoSQL & Modern Databases | High |

---

## Level 1 — Foundations & Database Architecture

---

### 1.1 What is a DBMS

- **Why It Matters:** Interviewers test whether you understand what problem DBMSes solve. "Why not just use files?" is a real interview question.
- **Prerequisites:** None
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Definition: software that manages databases (storage, retrieval, administration)
- Why DBMS over flat files:
  - Data redundancy and inconsistency problems in files
  - Difficulty accessing data in files
  - Data isolation
  - Integrity problems
  - Concurrency problems
  - Security problems
- DBMS advantages: data abstraction, independence, sharing, concurrency, security, recovery
- Database types: Relational, Hierarchical, Network, Object-Oriented, NoSQL

---

### 1.2 DBMS Architecture

- **Why It Matters:** Understanding layers helps you understand why queries execute the way they do.
- **Prerequisites:** 1.1
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:

**Three-Level Architecture (ANSI/SPARC):**
- External Level (View Level) — user-specific views
- Conceptual Level (Logical Level) — overall logical structure
- Internal Level (Physical Level) — physical storage

**Data Independence:**
- Logical data independence — changing conceptual schema doesn't affect external schema
- Physical data independence — changing internal schema doesn't affect conceptual schema

**DBMS Components:**
- Query Processor (Parser, Query Optimizer, Execution Engine)
- Storage Manager (Buffer Manager, File Manager, Authorization Manager)
- Transaction Manager
- Data Dictionary / System Catalog

---

### 1.3 Data Models

- **Why It Matters:** Understanding different models helps you choose the right database for the problem.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- Relational model (tables, tuples, attributes)
- Hierarchical model (tree structure — IBM IMS)
- Network model (graph structure)
- Object-relational model
- Document model (MongoDB)
- Key-value model (Redis)
- Column-family model (Cassandra)
- Graph model (Neo4j)

---

## Level 2 — Entity-Relationship (ER) Modeling

---

### 2.1 ER Model Basics

- **Why It Matters:** ER diagrams are the language of database design. Every schema design interview starts with an ER model.
- **Prerequisites:** Level 1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- **Entity:** real-world object that exists independently (Student, Order, Product)
- **Attribute:** property of an entity
  - Simple vs Composite attributes
  - Single-valued vs Multi-valued attributes
  - Stored vs Derived attributes
  - Key attribute (uniquely identifies entity)
- **Entity Set:** collection of similar entities
- **Relationship:** association between entities
- **Relationship Set:** collection of similar relationships

---

### 2.2 ER Diagram Notation

- **Why It Matters:** ER diagrams are used in design reviews, documentation, and interviews. You need to read and draw them.
- **Prerequisites:** 2.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Chen notation vs Crow's Foot notation
- Rectangle = Entity
- Ellipse = Attribute
- Diamond = Relationship
- Double rectangle = Weak Entity
- Double ellipse = Multi-valued attribute
- Dashed ellipse = Derived attribute
- Lines and connectivity notation

---

### 2.3 Relationships & Cardinality

- **Why It Matters:** Cardinality defines how many instances of one entity relate to another. Getting this wrong leads to wrong schema design.
- **Prerequisites:** 2.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- **One-to-One (1:1):** one entity relates to exactly one other (Person ↔ Passport)
- **One-to-Many (1:N):** one entity relates to many others (Department → Employees)
- **Many-to-Many (M:N):** many entities relate to many others (Students ↔ Courses)
- Participation constraints:
  - **Total participation:** every entity must participate (double line)
  - **Partial participation:** entity may or may not participate (single line)
- Degree of relationship (unary, binary, ternary)

---

### 2.4 Weak Entities

- **Why It Matters:** Weak entities appear frequently in schema design (OrderItem depends on Order, RoomBooking depends on Room).
- **Prerequisites:** 2.3
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Weak entity definition (no independent existence, no key of its own)
- Identifying relationship (owner ↔ weak entity)
- Discriminator / Partial Key
- Examples: OrderItem, LoanPayment, RoomAllocation
- Representation in relational schema (composite PK = parent PK + discriminator)

---

### 2.5 Specialization & Generalization

- **Why It Matters:** Inheritance in databases — mapping Person to Employee/Customer is a common schema design question.
- **Prerequisites:** 2.4
- **Interview Importance:** Medium
- **Job Importance:** Medium-High

Topics:
- **Generalization:** combining multiple lower-level entity sets into a higher-level one (bottom-up)
- **Specialization:** creating sub-entities from a higher-level entity (top-down)
- ISA hierarchy
- Attribute inheritance
- Disjoint vs Overlapping specialization
- Mapping to relational schema (3 strategies)

---

### 2.6 ER to Relational Mapping

- **Why It Matters:** Every ER model must be converted to a relational schema. This process is tested directly.
- **Prerequisites:** 2.5
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Mapping strong entity sets → tables
- Mapping weak entity sets → table with composite PK
- Mapping 1:1 relationships
- Mapping 1:N relationships (FK on the "many" side)
- Mapping M:N relationships (junction table)
- Mapping multi-valued attributes (separate table)
- Mapping ternary relationships
- Mapping specialization (three strategies: single table, joined table, concrete table)

---

## Level 3 — Relational Model & Keys

---

### 3.1 Relational Model Concepts

- **Why It Matters:** The relational model is the theoretical foundation. Interviewers ask about domains, tuples, relations.
- **Prerequisites:** Level 2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Relation (table) as a set of tuples
- Tuple (row) as an ordered list of attribute values
- Attribute domain — allowed values
- Degree — number of attributes
- Cardinality — number of tuples
- Relation schema vs relation instance
- Null values in relational model

---

### 3.2 Keys

- **Why It Matters:** Keys are the identity mechanism of relational databases. Every interview includes key questions.
- **Prerequisites:** 3.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- **Super Key:** any set of attributes that uniquely identifies a tuple
- **Candidate Key:** minimal super key (no proper subset is a super key)
- **Primary Key:** chosen candidate key; no NULLs
- **Alternate Key:** candidate keys not chosen as primary
- **Foreign Key:** attribute(s) in one relation referencing PK/CK in another
- **Composite Key:** primary key consisting of multiple attributes
- **Surrogate Key:** system-generated key (auto-increment, UUID)
- **Natural Key:** key from the domain (SSN, email)
- Surrogate vs Natural key tradeoffs

---

### 3.3 Integrity Constraints

- **Why It Matters:** Constraints enforce data correctness at the database level. Missing them leads to corrupt data.
- **Prerequisites:** 3.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- **Domain Constraint:** values must be from the attribute's domain
- **Entity Integrity:** primary key cannot be NULL
- **Referential Integrity:** foreign key value must exist in referenced table or be NULL
- **Key Constraint:** primary key must be unique
- **User-Defined Integrity:** CHECK constraints, TRIGGER-based
- Enforcement mechanisms (database vs application layer)
- Deferrable constraints

---

## Level 4 — Normalization

> *Normalization is the most commonly tested DBMS topic in software engineering interviews.*

---

### 4.1 Why Normalization

- **Why It Matters:** Unnormalized databases have anomalies. Interviewers use normalization to assess schema design skill.
- **Prerequisites:** Level 3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- **Update Anomaly:** updating one row requires updating multiple rows (inconsistency risk)
- **Insertion Anomaly:** cannot insert data without unrelated data
- **Deletion Anomaly:** deleting a row causes loss of unrelated data
- Redundancy problems
- Goal of normalization: eliminate anomalies by removing redundancy

---

### 4.2 Functional Dependencies

- **Why It Matters:** Functional dependencies are the mathematical basis of normalization. You cannot explain 2NF or 3NF without them.
- **Prerequisites:** 4.1
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- **Functional Dependency (FD):** X → Y (X determines Y; for every value of X there is one value of Y)
- Trivial vs Non-trivial FDs
- Armstrong's Axioms:
  - Reflexivity
  - Augmentation
  - Transitivity
- Derived rules: Union, Decomposition, Pseudotransitivity
- Closure of a set of FDs (F+)
- Closure of an attribute set (X+)
- Finding candidate keys using FD closure
- Minimal cover (canonical cover)
- Equivalence of FD sets

---

### 4.3 First Normal Form (1NF)

- **Why It Matters:** 1NF is the baseline. Violating it means arrays and repeating groups in columns — a schema that can't be queried properly.
- **Prerequisites:** 4.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- 1NF requirements:
  - All attributes are atomic (no multi-valued attributes)
  - No repeating groups
  - Each row is unique (has a key)
- Identifying 1NF violations
- Converting to 1NF (separate tables for multi-valued attributes)
- Example: storing multiple phone numbers in one column

---

### 4.4 Second Normal Form (2NF)

- **Why It Matters:** 2NF eliminates partial dependencies. Violations cause update anomalies in tables with composite keys.
- **Prerequisites:** 4.3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- 2NF requirement: in 1NF AND no non-prime attribute is partially dependent on any candidate key
- **Partial dependency:** non-key attribute depends on part of a composite key
- Only relevant when candidate key is composite
- Identifying partial dependencies
- Decomposing to 2NF (move partially dependent attributes to a new table)
- Example: (StudentID, CourseID) → StudentName — StudentName depends only on StudentID

---

### 4.5 Third Normal Form (3NF)

- **Why It Matters:** 3NF is the industry standard normalization target. Most production schemas aim for 3NF.
- **Prerequisites:** 4.4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- 3NF requirement: in 2NF AND no non-prime attribute transitively depends on any candidate key
- **Transitive dependency:** A → B → C where A is the key
- Identifying transitive dependencies
- Decomposing to 3NF (separate transitively dependent attributes)
- Example: StudentID → ZipCode → City — City transitively depends on StudentID
- 3NF decomposition algorithm (using minimal cover)
- Lossless join decomposition
- Dependency preservation in decomposition

---

### 4.6 Boyce-Codd Normal Form (BCNF)

- **Why It Matters:** BCNF is stricter than 3NF. Understanding why BCNF and 3NF differ is a senior-level interview question.
- **Prerequisites:** 4.5
- **Interview Importance:** High
- **Job Importance:** Medium-High

Topics:
- BCNF requirement: for every non-trivial FD X → Y, X must be a super key
- 3NF vs BCNF difference (3NF allows non-key dependency if the right side is prime)
- Example where 3NF ≠ BCNF
- BCNF decomposition
- BCNF may not preserve all FDs (tradeoff with dependency preservation)
- Choosing between 3NF and BCNF

---

### 4.7 Higher Normal Forms (4NF, 5NF)

- **Why It Matters:** 4NF addresses multi-valued dependencies. Awareness expected at senior level.
- **Prerequisites:** 4.6
- **Interview Importance:** Medium
- **Job Importance:** Low

Topics:
- Multi-valued dependencies (MVDs)
- Fourth Normal Form (4NF): no non-trivial MVDs unless determinant is a super key
- Fifth Normal Form (5NF) / PJNF: join dependency decomposition
- Practical relevance

---

### 4.8 Denormalization

- **Why It Matters:** Production systems often denormalize for performance. Knowing when and how to denormalize is a real skill.
- **Prerequisites:** 4.6
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Why denormalize (performance, fewer JOINs, caching convenience)
- Denormalization techniques:
  - Storing derived/computed values
  - Pre-joining tables
  - Duplicating columns across tables
  - Storing aggregates
- Tradeoffs: faster reads, slower writes, data inconsistency risk
- Materialized views as managed denormalization
- When denormalization is the right choice (reporting, analytics)

---

## Level 5 — Indexing (Deep Dive)

---

### 5.1 Index Types & Structures

- **Why It Matters:** Index internals explain query performance behavior. Interviewers ask about B-Tree specifically.
- **Prerequisites:** Level 3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Why indexes (avoid full table scan O(n) → O(log n))
- **Ordered Index:** entries stored in sorted order
  - Primary Index (on ordering key of ordered data file)
  - Clustering Index (on non-key ordering field)
  - Secondary Index (on non-ordering field)
- **Dense Index:** entry for every record
- **Sparse Index:** entry only for some records (anchors)
- **Multi-level Index:** index on the index

---

### 5.2 B-Tree & B+ Tree

- **Why It Matters:** B+ Tree is the data structure behind almost every database index. Interviewers ask "how does an index work?" expecting B+ Tree knowledge.
- **Prerequisites:** 5.1
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- B-Tree properties (self-balancing, sorted, each node has multiple keys)
- B+ Tree vs B-Tree:
  - B+ Tree stores all data in leaf nodes
  - B+ Tree leaf nodes are linked (range queries efficient)
  - Internal nodes in B+ Tree are only for navigation
- B+ Tree order (max keys per node)
- Insert and delete with rebalancing
- Height of B+ Tree = O(log_n(N))
- Why B+ Trees are perfect for disk-based storage
- Clustered vs Non-Clustered index using B+ Tree

---

### 5.3 Hash Indexes

- **Why It Matters:** Hash indexes are O(1) for equality but useless for range queries. Understanding this tradeoff is frequently tested.
- **Prerequisites:** 5.1
- **Interview Importance:** High
- **Job Importance:** Medium-High

Topics:
- Static hashing (fixed bucket count)
- Hash collision handling (chaining, open addressing)
- Dynamic hashing (Extendible Hashing, Linear Hashing)
- Hash index for equality queries only
- No range query support (vs B+ Tree)
- PostgreSQL hash indexes (now crash-safe since PG 10)

---

### 5.4 Bitmap Indexes

- **Why It Matters:** Bitmap indexes are used in data warehouses for low-cardinality columns.
- **Prerequisites:** 5.1
- **Interview Importance:** Low-Medium
- **Job Importance:** Low

Topics:
- Bit vector per distinct value
- Efficient for low-cardinality columns (gender, status)
- Bitwise AND/OR for complex queries
- Not suited for OLTP (high write volume)

---

## Level 6 — Transactions & ACID

---

### 6.1 Transaction Concepts

- **Why It Matters:** Transactions are a critical interview topic. Every senior engineer must explain them clearly.
- **Prerequisites:** Level 4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Transaction definition: a unit of work that must complete entirely or not at all
- Transaction operations: READ, WRITE, COMMIT, ROLLBACK
- Transaction states:
  - Active
  - Partially Committed
  - Committed
  - Failed
  - Aborted
- State transition diagram

---

### 6.2 ACID Properties

- **Why It Matters:** ACID is the most tested DBMS interview topic. Explain each property with examples.
- **Prerequisites:** 6.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**Atomicity:**
- All-or-nothing execution
- Enforced by rollback on failure
- Example: bank transfer — debit + credit must both succeed or both fail

**Consistency:**
- Transaction takes DB from one valid state to another
- Integrity constraints must be satisfied before and after
- Not automatically enforced by DBMS — application responsibility

**Isolation:**
- Concurrent transactions appear to execute sequentially
- Dirty reads, non-repeatable reads, phantom reads are isolation failures
- Enforced by concurrency control mechanisms

**Durability:**
- Committed transactions persist even after system failure
- Enforced by write-ahead logging (WAL)
- Storage must be non-volatile

---

### 6.3 Schedules & Serializability

- **Why It Matters:** Serializability is the theoretical correctness criterion for concurrent transaction execution.
- **Prerequisites:** 6.2
- **Interview Importance:** High
- **Job Importance:** Medium

Topics:
- Schedule: sequence of operations from multiple transactions
- Serial schedule: transactions execute one at a time (no interleaving) — always correct
- Concurrent schedule: operations interleaved
- Serializable schedule: equivalent to some serial schedule
- **Conflict:** two operations on same data item, at least one is WRITE
- Conflict-equivalent schedules
- **Conflict Serializability:** schedule is conflict serializable if it can be transformed to serial by swapping non-conflicting operations
- Precedence Graph (Serialization Graph):
  - Nodes = transactions
  - Edge Ti → Tj if Ti's operation conflicts with and precedes Tj's operation
  - Schedule is conflict serializable iff precedence graph has no cycles

---

## Level 7 — Concurrency Control

---

### 7.1 Concurrency Problems

- **Why It Matters:** These are the exact problems isolation levels are designed to prevent. Interviews test all three.
- **Prerequisites:** 6.3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- **Dirty Read:** T1 reads data written by T2 (uncommitted); T2 rolls back — T1 read invalid data
- **Non-Repeatable Read:** T1 reads data; T2 updates and commits; T1 re-reads and gets different value
- **Phantom Read:** T1 queries with a condition; T2 inserts rows matching condition and commits; T1 re-queries and sees new rows
- **Lost Update:** T1 and T2 both read value, both modify it, T2 overwrites T1's change

---

### 7.2 Lock-Based Protocols

- **Why It Matters:** Locking is the primary concurrency control mechanism in most databases.
- **Prerequisites:** 7.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- **Shared Lock (S):** allows reads by multiple transactions; blocks writes
- **Exclusive Lock (X):** allows read and write by one transaction; blocks all others
- Lock compatibility matrix (SS compatible, SX not, XS not, XX not)
- Lock granularity: row, page, table, database
- **Two-Phase Locking (2PL):**
  - Growing phase: acquire locks, don't release
  - Shrinking phase: release locks, don't acquire
  - Guarantees conflict serializability
- **Strict 2PL:** release all exclusive locks only at commit/abort (prevents dirty reads)
- **Rigorous 2PL:** release all locks only at commit/abort
- 2PL can lead to deadlocks

---

### 7.3 Deadlocks

- **Why It Matters:** Deadlocks are real production problems. Understanding detection and prevention is both a theory and practical skill.
- **Prerequisites:** 7.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Deadlock definition: circular wait for locks
- Necessary conditions (Coffman conditions):
  1. Mutual Exclusion
  2. Hold and Wait
  3. No Preemption
  4. Circular Wait
- Wait-for graph: Ti → Tj if Ti waits for a lock held by Tj
- Deadlock detection: cycle in wait-for graph
- Deadlock victim selection and rollback
- Deadlock prevention strategies:
  - Wait-Die (older waits, younger dies)
  - Wound-Wait (older wounds, younger waits)
  - Timeout-based
  - Ordering resources (prevent circular wait)
- Deadlock avoidance (Banker's algorithm — theoretical)
- PostgreSQL deadlock detection and behavior

---

### 7.4 MVCC (Multi-Version Concurrency Control)

- **Why It Matters:** PostgreSQL uses MVCC. Understanding it explains why reads don't block writes in PostgreSQL.
- **Prerequisites:** 7.2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- MVCC concept: maintain multiple versions of data
- Readers read consistent snapshots, don't block writers
- Writers create new versions, don't block readers
- Transaction timestamps / snapshot isolation
- MVCC in PostgreSQL:
  - xmin and xmax system columns
  - Visibility rules
  - Dead tuples and VACUUM
  - VACUUM and autovacuum
- MVCC in Oracle, MySQL, SQL Server (variations)

---

### 7.5 Isolation Levels in Practice

- **Why It Matters:** Choosing the wrong isolation level causes data bugs. Choosing too-strict a level causes performance issues.
- **Prerequisites:** 7.1, 7.4
- **Interview Importance:** Critical
- **Job Importance:** Critical

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|----------------|-----------|--------------------|--------------| 
| READ UNCOMMITTED | Possible | Possible | Possible |
| READ COMMITTED | Prevented | Possible | Possible |
| REPEATABLE READ | Prevented | Prevented | Possible |
| SERIALIZABLE | Prevented | Prevented | Prevented |

Topics:
- PostgreSQL default: READ COMMITTED
- When to use SERIALIZABLE (financial transactions)
- Performance implications of each level
- Application-level compensation for weaker isolation

---

## Level 8 — Database Recovery

---

### 8.1 Failure Types

- **Why It Matters:** Understanding what can fail helps you understand why recovery mechanisms exist.
- **Prerequisites:** Level 6
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- Transaction failure (logical error, deadlock)
- System crash (power failure, OS crash)
- Media failure (disk failure)
- Communication failure
- Recovery goals: restore to consistent state, preserve committed transactions

---

### 8.2 Log-Based Recovery

- **Why It Matters:** Write-Ahead Logging (WAL) is the universal recovery mechanism. PostgreSQL uses WAL.
- **Prerequisites:** 8.1
- **Interview Importance:** High
- **Job Importance:** Medium-High

Topics:
- Write-Ahead Log (WAL) protocol: write log before writing data
- Log record format: [Transaction ID, Action, Old Value, New Value]
- Undo Log: record old values (used to rollback uncommitted transactions)
- Redo Log: record new values (used to redo committed transactions)
- UNDO/REDO Recovery Algorithm
- ARIES Algorithm (industry standard):
  - Analysis Phase
  - Redo Phase
  - Undo Phase
- Checkpoints (reduce recovery time)

---

## Level 9 — NoSQL & Modern Databases

---

### 9.1 NoSQL Motivation & CAP Theorem

- **Why It Matters:** Every system design interview involves choosing between SQL and NoSQL. CAP theorem explains the tradeoffs.
- **Prerequisites:** Level 7
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- Why NoSQL (scale, schema flexibility, specific data models)
- **CAP Theorem:** a distributed system can only guarantee 2 of 3:
  - **Consistency:** every read gets the most recent write
  - **Availability:** every request gets a response (may not be latest data)
  - **Partition Tolerance:** system continues despite network partitions
- CA systems: traditional RDBMS (no partition tolerance)
- CP systems: HBase, MongoDB (strong consistency, may be unavailable during partition)
- AP systems: Cassandra, DynamoDB (always available, eventually consistent)
- CAP theorem limitations and nuances (PACELC theorem)

---

### 9.2 NoSQL Data Models

- **Why It Matters:** Interviewers ask "would you use MongoDB or PostgreSQL for this?" — you need to know each model.
- **Prerequisites:** 9.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:

**Key-Value Stores (Redis, DynamoDB):**
- Simple get/put by key
- Very fast, horizontally scalable
- Use cases: caching, session storage, leaderboards, pub/sub

**Document Stores (MongoDB, CouchDB):**
- Documents (JSON-like) as the unit
- Nested data, flexible schema
- Use cases: catalogs, user profiles, content management
- Query by any field (unlike key-value)

**Column-Family Stores (Cassandra, HBase):**
- Data stored by column families, not rows
- Excellent for time-series, write-heavy workloads
- Use cases: IoT data, event logs, analytics

**Graph Databases (Neo4j, Amazon Neptune):**
- Nodes and edges as first-class citizens
- Efficient for relationship traversals
- Use cases: social networks, recommendation engines, fraud detection

---

### 9.3 SQL vs NoSQL Decision Framework

- **Why It Matters:** System design interviews require you to justify your choice. This is a high-frequency question.
- **Prerequisites:** 9.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

| Factor | Choose SQL | Choose NoSQL |
|--------|-----------|-------------|
| Schema | Fixed, well-defined | Dynamic, evolving |
| Relationships | Complex, many JOINs | Few relationships |
| Consistency | ACID required | Eventually consistent OK |
| Scale | Moderate | Massive horizontal scale |
| Transactions | Multi-row ACID | Single document transactions |
| Queries | Complex ad-hoc queries | Simple, predictable queries |

Topics:
- ACID vs BASE tradeoff
- Eventual consistency — when it's acceptable
- Sharding in NoSQL
- Replication in NoSQL
- NewSQL databases (CockroachDB, Spanner — ACID + horizontal scale)

---

### 9.4 BASE Properties

- **Why It Matters:** BASE is the theoretical framework for NoSQL databases — contrasted with ACID in interviews.
- **Prerequisites:** 9.1
- **Interview Importance:** High
- **Job Importance:** Medium-High

Topics:
- **Basically Available:** system appears to work most of the time
- **Soft State:** state may change over time even without input (due to replication)
- **Eventually Consistent:** system will become consistent given enough time
- Examples of eventual consistency in practice
- Conflict resolution strategies (last-write-wins, vector clocks, CRDTs)

---

*This is the knowledge inventory for DBMS. Roadmap and scheduling are managed separately.*
