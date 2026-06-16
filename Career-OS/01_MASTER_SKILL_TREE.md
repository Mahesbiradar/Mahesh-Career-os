# Mahesh Career OS — Master Skill Tree

> **Purpose:** Complete knowledge architecture for software engineering employability.
> **Scope:** All subjects except DSA (managed in separate system).
> **Audience:** Mahesh Biradar — transitioning from Telecom to Software Engineering.

---

## Architecture Overview

```
Software Engineering (Career OS)
│
├── 01. Python
│
├── 02. Backend Engineering
│
├── 03. SQL
│
├── 04. Database Management Systems (DBMS)
│
├── 05. Operating Systems
│
├── 06. Computer Networks
│
├── 07. Frontend Engineering
│
├── 08. Cloud & Deployment
│
├── 09. Communication Skills
│
└── 10. Job Preparation
```

---

## 01. Python

```
Python
│
├── Level 1 — Core Fundamentals
│   ├── Variables & Data Types
│   ├── Operators & Expressions
│   ├── Control Flow (if/elif/else)
│   ├── Loops (for, while, break, continue)
│   ├── Functions (definition, arguments, return)
│   ├── Built-in Functions & Methods
│   └── Input / Output
│
├── Level 2 — Data Structures & Collections
│   ├── Strings (methods, formatting, f-strings)
│   ├── Lists (operations, comprehensions)
│   ├── Tuples
│   ├── Sets
│   ├── Dictionaries (methods, comprehensions)
│   └── Type Conversion & Casting
│
├── Level 3 — Intermediate Programming
│   ├── Functions (args, kwargs, defaults, lambda)
│   ├── Scope (local, global, enclosing, built-in)
│   ├── Recursion
│   ├── Modules & Packages
│   ├── File Handling (read, write, append, context managers)
│   ├── Exception Handling (try/except/finally, custom exceptions)
│   └── Iterators & Generators
│
├── Level 4 — Object-Oriented Programming
│   ├── Classes & Objects
│   ├── Constructor (__init__)
│   ├── Instance vs Class vs Static Methods
│   ├── Inheritance (single, multiple, MRO)
│   ├── Encapsulation & Access Modifiers
│   ├── Polymorphism & Duck Typing
│   ├── Dunder / Magic Methods
│   ├── Properties & Descriptors
│   └── Abstract Classes & Interfaces
│
├── Level 5 — Advanced Python
│   ├── Decorators (function, class-based)
│   ├── Context Managers (__enter__, __exit__)
│   ├── Closures & Higher-Order Functions
│   ├── Map, Filter, Reduce
│   ├── Comprehensions (list, dict, set, generator)
│   ├── Type Hints & Annotations
│   ├── Dataclasses
│   ├── Enum
│   ├── Functools Module
│   ├── Itertools Module
│   └── Collections Module (Counter, defaultdict, namedtuple, deque)
│
├── Level 6 — Concurrency & Performance
│   ├── Multithreading (threading module)
│   ├── Multiprocessing (multiprocessing module)
│   ├── Async Programming (async/await, asyncio)
│   ├── GIL (Global Interpreter Lock)
│   ├── Event Loop
│   └── Performance Profiling
│
├── Level 7 — Standard Library & Ecosystem
│   ├── os & sys
│   ├── pathlib
│   ├── datetime
│   ├── json
│   ├── csv
│   ├── re (Regular Expressions)
│   ├── logging
│   ├── argparse
│   ├── subprocess
│   └── hashlib
│
├── Level 8 — Testing
│   ├── Unit Testing (unittest)
│   ├── Pytest Fundamentals
│   ├── Fixtures & Conftest
│   ├── Mocking (unittest.mock)
│   ├── Test Coverage
│   ├── Test-Driven Development (TDD) concepts
│   └── Integration Testing concepts
│
└── Level 9 — Python for Backend
    ├── Virtual Environments (venv, pip)
    ├── Requirements & Dependency Management
    ├── Environment Variables & dotenv
    ├── HTTP Requests (requests, httpx)
    ├── Working with APIs
    ├── JSON Serialization/Deserialization
    ├── Database Connectivity (psycopg2, SQLAlchemy ORM basics)
    └── Packaging & Project Structure
```

---

## 02. Backend Engineering

```
Backend Engineering
│
├── Tier 1 — Internet & Web Fundamentals
│   ├── How the Internet Works
│   ├── Client-Server Architecture
│   ├── HTTP Protocol (request, response, methods, status codes)
│   ├── HTTPS & TLS/SSL
│   ├── URLs, URIs, Query Parameters
│   ├── Headers & Body
│   ├── Cookies
│   ├── Sessions
│   └── Web Browsers & DNS
│
├── Tier 2 — API Design
│   ├── What is an API
│   ├── REST Architecture & Constraints
│   ├── RESTful Resource Design
│   ├── HTTP Methods (GET, POST, PUT, PATCH, DELETE)
│   ├── Status Codes (2xx, 3xx, 4xx, 5xx)
│   ├── Request & Response Formats (JSON)
│   ├── API Versioning
│   ├── Pagination, Filtering, Sorting
│   ├── Rate Limiting
│   ├── API Documentation (Swagger/OpenAPI)
│   └── GraphQL (conceptual awareness)
│
├── Tier 3 — Authentication & Authorization
│   ├── Authentication vs Authorization
│   ├── Session-Based Authentication
│   ├── Token-Based Authentication
│   ├── JWT (structure, signing, validation, expiry)
│   ├── OAuth 2.0 (conceptual flow)
│   ├── API Keys
│   ├── Role-Based Access Control (RBAC)
│   ├── Permission Systems
│   ├── Password Hashing (bcrypt, argon2)
│   └── CSRF & XSS Protection
│
├── Tier 4 — Django Framework
│   ├── Django Project Structure
│   ├── Settings & Configuration
│   ├── URL Routing
│   ├── Views (Function-Based, Class-Based)
│   ├── Models & ORM
│   ├── Migrations
│   ├── Django Admin
│   ├── Forms & Validation
│   ├── Middleware
│   ├── Static & Media Files
│   ├── Templates
│   └── Django Authentication System
│
├── Tier 5 — Django REST Framework (DRF)
│   ├── Serializers (ModelSerializer, Serializer)
│   ├── Views (APIView, ViewSets, GenericViews)
│   ├── Routers
│   ├── Permissions & Authentication Classes
│   ├── Throttling
│   ├── Filtering & Search
│   ├── Pagination (PageNumber, Cursor, Limit-Offset)
│   ├── Nested Serializers
│   ├── Custom Permissions
│   └── API Testing with DRF
│
├── Tier 6 — Database Integration
│   ├── ORMs vs Raw SQL
│   ├── Django ORM Queries
│   ├── Relationships (OneToOne, ForeignKey, ManyToMany)
│   ├── Query Optimization (select_related, prefetch_related)
│   ├── Database Transactions in Django
│   ├── Migrations Best Practices
│   └── Connection Pooling
│
├── Tier 7 — Caching
│   ├── Caching Concepts & Strategies
│   ├── Redis Basics
│   ├── Django Cache Framework
│   ├── Cache Invalidation
│   └── Content Delivery Networks (CDN)
│
├── Tier 8 — Task Queues & Background Processing
│   ├── Why Background Tasks
│   ├── Celery Fundamentals
│   ├── Task Queues & Brokers (Redis, RabbitMQ)
│   ├── Scheduled Tasks (Celery Beat)
│   └── Task Monitoring
│
├── Tier 9 — Architecture & System Design Basics
│   ├── Monolithic Architecture
│   ├── Microservices (conceptual)
│   ├── 12-Factor App Principles
│   ├── Separation of Concerns
│   ├── Service Layer Pattern
│   ├── Repository Pattern
│   └── Event-Driven Architecture (conceptual)
│
└── Tier 10 — Production Backend Concepts
    ├── Environment Management (dev, staging, production)
    ├── Logging & Monitoring
    ├── Error Tracking (Sentry concepts)
    ├── Performance Optimization
    ├── Security Hardening
    ├── API Gateway
    ├── Load Balancing (conceptual)
    ├── Horizontal vs Vertical Scaling
    └── Database Backups & Recovery
```

---

## 03. SQL

```
SQL
│
├── Foundation
│   ├── Relational Database Concepts
│   ├── Tables, Rows, Columns, Schema
│   ├── Data Types
│   ├── NULL vs Empty
│   ├── Primary Key & Foreign Key
│   └── SQL Syntax Rules
│
├── Core Queries (DML)
│   ├── SELECT (basic to advanced)
│   ├── INSERT
│   ├── UPDATE
│   ├── DELETE
│   ├── WHERE Clause
│   ├── ORDER BY
│   ├── LIMIT & OFFSET
│   └── DISTINCT
│
├── Filtering & Conditions
│   ├── Comparison Operators
│   ├── Logical Operators (AND, OR, NOT)
│   ├── IN, NOT IN
│   ├── BETWEEN
│   ├── LIKE & Pattern Matching
│   ├── IS NULL / IS NOT NULL
│   └── CASE WHEN
│
├── Aggregations & Grouping
│   ├── COUNT, SUM, AVG, MIN, MAX
│   ├── GROUP BY
│   ├── HAVING
│   └── Aggregate with NULL handling
│
├── Joins
│   ├── INNER JOIN
│   ├── LEFT JOIN
│   ├── RIGHT JOIN
│   ├── FULL OUTER JOIN
│   ├── CROSS JOIN
│   ├── SELF JOIN
│   └── Multiple Table Joins
│
├── Subqueries
│   ├── Scalar Subqueries
│   ├── Row Subqueries
│   ├── Table Subqueries
│   ├── Correlated Subqueries
│   ├── EXISTS & NOT EXISTS
│   └── Subquery vs JOIN performance
│
├── CTEs & Advanced Queries
│   ├── Common Table Expressions (WITH clause)
│   ├── Recursive CTEs
│   └── Query Readability & Modularity
│
├── Window Functions
│   ├── ROW_NUMBER
│   ├── RANK & DENSE_RANK
│   ├── NTILE
│   ├── LAG & LEAD
│   ├── FIRST_VALUE & LAST_VALUE
│   ├── SUM/AVG OVER (running totals)
│   └── PARTITION BY & FRAME clauses
│
├── DDL & Schema Management
│   ├── CREATE TABLE
│   ├── ALTER TABLE
│   ├── DROP TABLE
│   ├── Constraints (NOT NULL, UNIQUE, CHECK, DEFAULT)
│   ├── Foreign Key Constraints
│   └── Schema Design from Requirements
│
├── Indexes
│   ├── Why Indexes Exist
│   ├── B-Tree Index
│   ├── Composite Index
│   ├── Covering Index
│   ├── When NOT to Index
│   └── EXPLAIN / Query Plan Analysis
│
├── Transactions
│   ├── BEGIN / COMMIT / ROLLBACK
│   ├── ACID Properties
│   ├── Isolation Levels
│   ├── Savepoints
│   └── Transaction in Application Code
│
└── PostgreSQL Specifics
    ├── JSON / JSONB columns
    ├── Array Types
    ├── Full-Text Search
    ├── RETURNING clause
    ├── UPSERT (INSERT ON CONFLICT)
    ├── pg_stat tools
    └── PostgreSQL Data Types
```

---

## 04. Database Management Systems (DBMS)

```
DBMS
│
├── Foundations
│   ├── What is a DBMS
│   ├── DBMS vs File System
│   ├── Types of Databases (Relational, NoSQL, NewSQL)
│   ├── Database Architecture (3-tier)
│   └── Roles (DBA, Developer, Analyst)
│
├── ER Modeling
│   ├── Entities & Attributes
│   ├── Relationships & Cardinality
│   ├── ER Diagrams
│   ├── Strong vs Weak Entities
│   ├── Specialization & Generalization
│   └── ER to Relational Mapping
│
├── Relational Model
│   ├── Relations & Tuples
│   ├── Keys (Super, Candidate, Primary, Foreign, Composite)
│   ├── Integrity Constraints
│   └── Relational Algebra (conceptual)
│
├── Normalization
│   ├── Functional Dependencies
│   ├── 1NF
│   ├── 2NF
│   ├── 3NF
│   ├── BCNF
│   ├── Denormalization (when & why)
│   └── Anomalies (insertion, update, deletion)
│
├── Indexing (Deep Dive)
│   ├── Dense vs Sparse Index
│   ├── Primary vs Secondary Index
│   ├── B-Tree & B+ Tree Structure
│   ├── Hash Index
│   ├── Multi-level Indexing
│   └── Clustered vs Non-Clustered
│
├── Transactions & Concurrency
│   ├── ACID Properties
│   ├── Transaction States
│   ├── Serializability
│   ├── Conflict Serializability
│   ├── Isolation Levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable)
│   ├── Concurrency Problems (Dirty Read, Non-Repeatable Read, Phantom Read)
│   └── Two-Phase Locking (2PL)
│
├── Recovery
│   ├── Log-Based Recovery
│   ├── Undo / Redo Logs
│   ├── Checkpoints
│   └── RAID Concepts
│
└── NoSQL Awareness
    ├── Key-Value Stores (Redis)
    ├── Document Stores (MongoDB concepts)
    ├── Column-Family (Cassandra concepts)
    ├── Graph Databases (concepts)
    ├── CAP Theorem
    └── When to choose NoSQL over SQL
```

---

## 05. Operating Systems

```
Operating Systems
│
├── Foundations
│   ├── What is an OS
│   ├── OS Types (Batch, Time-Sharing, Distributed, Real-Time)
│   ├── System Calls
│   ├── OS Architecture (monolithic, microkernel)
│   └── Kernel vs User Space
│
├── Processes
│   ├── Process Concept & PCB
│   ├── Process States
│   ├── Process Creation & Termination (fork, exec)
│   ├── Inter-Process Communication (IPC)
│   ├── Pipes, Shared Memory, Message Queues
│   └── Signals
│
├── Threads
│   ├── Thread Concept vs Process
│   ├── User-Level vs Kernel-Level Threads
│   ├── Thread Models (many-to-one, one-to-one, many-to-many)
│   ├── Thread Lifecycle
│   ├── Benefits of Multithreading
│   └── Thread Safety
│
├── CPU Scheduling
│   ├── Scheduling Criteria (CPU utilization, throughput, turnaround)
│   ├── FCFS
│   ├── SJF (preemptive & non-preemptive)
│   ├── Round Robin
│   ├── Priority Scheduling
│   ├── Multilevel Queue
│   └── Context Switching
│
├── Synchronization
│   ├── Race Conditions
│   ├── Critical Section Problem
│   ├── Mutex Locks
│   ├── Semaphores (binary, counting)
│   ├── Monitors
│   ├── Condition Variables
│   └── Classic Problems (Producer-Consumer, Readers-Writers, Dining Philosophers)
│
├── Deadlocks
│   ├── Deadlock Conditions (Coffman conditions)
│   ├── Resource Allocation Graph
│   ├── Deadlock Prevention
│   ├── Deadlock Avoidance (Banker's Algorithm)
│   ├── Deadlock Detection
│   └── Deadlock Recovery
│
├── Memory Management
│   ├── Memory Hierarchy
│   ├── Contiguous Memory Allocation
│   ├── Paging
│   ├── Segmentation
│   ├── Fragmentation (internal vs external)
│   ├── Page Tables & TLB
│   └── Memory-Mapped Files
│
├── Virtual Memory
│   ├── Virtual vs Physical Address Space
│   ├── Demand Paging
│   ├── Page Faults
│   ├── Page Replacement Algorithms (FIFO, LRU, Optimal)
│   ├── Thrashing
│   └── Working Set Model
│
├── File Systems
│   ├── File Concept & Operations
│   ├── Directory Structure
│   ├── File System Implementation
│   ├── Disk Scheduling
│   └── RAID Levels
│
└── Linux Fundamentals (OS in Practice)
    ├── Linux File System Hierarchy
    ├── Essential Commands (ls, cd, pwd, mkdir, rm, cp, mv)
    ├── File Permissions (chmod, chown)
    ├── Process Management (ps, top, kill)
    ├── Shell & Scripting Basics
    ├── Environment Variables
    ├── Package Management (apt, yum)
    └── SSH & Remote Access
```

---

## 06. Computer Networks

```
Computer Networks
│
├── Foundations
│   ├── What is a Network
│   ├── Network Types (LAN, WAN, MAN)
│   ├── Network Topologies
│   └── Transmission Modes
│
├── OSI Model
│   ├── Why OSI Model Exists
│   ├── Layer 1 — Physical
│   ├── Layer 2 — Data Link (MAC, ARP)
│   ├── Layer 3 — Network (IP, ICMP)
│   ├── Layer 4 — Transport (TCP, UDP)
│   ├── Layer 5 — Session
│   ├── Layer 6 — Presentation
│   ├── Layer 7 — Application
│   └── Data Encapsulation
│
├── TCP/IP Model
│   ├── TCP/IP vs OSI
│   ├── Network Access Layer
│   ├── Internet Layer (IP)
│   ├── Transport Layer (TCP, UDP)
│   ├── Application Layer
│   └── IP Addressing (IPv4, IPv6, CIDR)
│
├── TCP & UDP
│   ├── TCP — Connection-Oriented
│   ├── Three-Way Handshake
│   ├── TCP — Reliability & Flow Control
│   ├── TCP — Congestion Control
│   ├── UDP — Connectionless
│   ├── TCP vs UDP Comparison
│   └── Ports & Sockets
│
├── HTTP & HTTPS
│   ├── HTTP/1.1 vs HTTP/2 vs HTTP/3
│   ├── Request Methods
│   ├── Status Codes
│   ├── Headers (common, custom)
│   ├── HTTP Request/Response Lifecycle
│   ├── HTTPS & TLS Handshake
│   ├── SSL Certificates
│   └── HSTS
│
├── DNS
│   ├── Domain Name System Architecture
│   ├── DNS Resolution Process
│   ├── DNS Record Types (A, AAAA, CNAME, MX, TXT, NS)
│   ├── TTL
│   ├── DNS Caching
│   └── DNS Security (DNSSEC basics)
│
├── Web Communication Protocols
│   ├── WebSockets
│   ├── Long Polling
│   ├── Server-Sent Events
│   ├── REST vs WebSocket
│   └── gRPC (conceptual)
│
├── Routing & Switching
│   ├── IP Routing
│   ├── Routing Algorithms (Distance Vector, Link State)
│   ├── Subnetting
│   ├── NAT & PAT
│   └── Firewalls & Proxies
│
├── Security in Networks
│   ├── Common Attacks (MITM, DDoS, Phishing)
│   ├── Encryption (symmetric, asymmetric)
│   ├── Public Key Infrastructure (PKI)
│   ├── VPN concepts
│   └── CORS (web security)
│
└── Practical Networking
    ├── curl & wget commands
    ├── ping, traceroute, netstat
    ├── Wireshark concepts
    ├── Postman for API testing
    ├── Understanding server logs
    └── CDN & Edge Networks
```

---

## 07. Frontend Engineering

```
Frontend Engineering
│
├── HTML
│   ├── Document Structure
│   ├── Semantic Elements
│   ├── Forms & Inputs
│   ├── Tables
│   ├── Media Elements
│   ├── Accessibility (ARIA roles)
│   └── HTML5 APIs (localStorage, sessionStorage, Canvas concepts)
│
├── CSS
│   ├── Box Model
│   ├── Selectors & Specificity
│   ├── Positioning & Display
│   ├── Flexbox
│   ├── CSS Grid
│   ├── Responsive Design & Media Queries
│   ├── CSS Variables
│   ├── Animations & Transitions
│   ├── Pseudo-classes & Pseudo-elements
│   └── CSS Preprocessors (Sass basics)
│
├── JavaScript Core
│   ├── Variables (var, let, const)
│   ├── Data Types & Type Coercion
│   ├── Functions (declarations, expressions, arrow functions)
│   ├── Scope & Closures
│   ├── Prototypes & Inheritance
│   ├── this Keyword & Context
│   ├── ES6+ Features (destructuring, spread, rest, template literals)
│   ├── Array Methods (map, filter, reduce, forEach, find)
│   ├── Object Methods
│   └── Modules (import/export)
│
├── DOM Manipulation
│   ├── DOM Tree Structure
│   ├── Selecting Elements
│   ├── Creating & Modifying Elements
│   ├── Event Handling
│   ├── Event Bubbling & Delegation
│   └── Virtual DOM (concept)
│
├── JavaScript — Advanced
│   ├── Promises
│   ├── async/await
│   ├── Fetch API
│   ├── Error Handling (try/catch)
│   ├── Event Loop & Call Stack
│   ├── Microtask Queue vs Macrotask Queue
│   ├── Debounce & Throttle
│   ├── Memory Management & Garbage Collection
│   └── Design Patterns (Module, Observer, Singleton)
│
├── Browser & Web APIs
│   ├── localStorage & sessionStorage
│   ├── Cookies (JS access)
│   ├── Geolocation API
│   ├── History API
│   ├── Web Workers (concept)
│   └── Service Workers & PWA (concept)
│
├── React
│   ├── React Fundamentals
│   │   ├── JSX
│   │   ├── Components (functional vs class)
│   │   ├── Props
│   │   ├── State (useState)
│   │   ├── Rendering & Re-rendering
│   │   └── Lists & Keys
│   │
│   ├── React Hooks
│   │   ├── useState
│   │   ├── useEffect (lifecycle equivalents)
│   │   ├── useRef
│   │   ├── useContext
│   │   ├── useReducer
│   │   ├── useCallback & useMemo
│   │   └── Custom Hooks
│   │
│   ├── React Router
│   │   ├── Route Configuration
│   │   ├── Dynamic Routes
│   │   ├── Protected Routes
│   │   ├── Navigation Hooks
│   │   └── Nested Routes
│   │
│   ├── State Management
│   │   ├── Context API
│   │   ├── Redux Toolkit (core concepts)
│   │   ├── Zustand (lightweight alternative)
│   │   └── When to use what
│   │
│   ├── API Integration
│   │   ├── Fetch + useEffect pattern
│   │   ├── Axios
│   │   ├── React Query / TanStack Query
│   │   ├── Loading & Error States
│   │   └── Optimistic Updates
│   │
│   └── React Advanced
│       ├── Code Splitting & Lazy Loading
│       ├── Error Boundaries
│       ├── Performance Optimization
│       ├── React.memo
│       └── Portals & Refs
│
├── Build Tools & Ecosystem
│   ├── npm / yarn / pnpm
│   ├── Vite / Webpack (conceptual)
│   ├── ESLint & Prettier
│   ├── Babel (conceptual)
│   └── Environment Variables in Frontend
│
└── Frontend Testing
    ├── Jest Basics
    ├── React Testing Library
    ├── Unit vs Integration vs E2E
    └── Cypress (conceptual)
```

---

## 08. Cloud & Deployment

```
Cloud & Deployment
│
├── Linux Fundamentals
│   ├── File System & Hierarchy
│   ├── Core Commands
│   ├── File Permissions
│   ├── Process Management
│   ├── Networking Commands
│   ├── Cron Jobs
│   ├── Shell Scripting Basics
│   └── Package Managers
│
├── Git & Version Control
│   ├── Git Fundamentals
│   ├── Branching Strategies
│   ├── Merging & Rebasing
│   ├── Conflict Resolution
│   ├── Git Workflows (GitFlow, Trunk-Based)
│   └── Git Hooks
│
├── GitHub
│   ├── Repositories & README
│   ├── Pull Requests & Code Review
│   ├── Issues & Project Boards
│   ├── GitHub Actions (CI/CD)
│   └── GitHub Pages
│
├── Docker
│   ├── Containers vs VMs
│   ├── Docker Architecture
│   ├── Dockerfile
│   ├── Docker Images & Layers
│   ├── Docker Containers
│   ├── Docker Volumes
│   ├── Docker Networking
│   ├── Docker Compose
│   └── Docker Registry (DockerHub)
│
├── CI/CD
│   ├── Continuous Integration Concepts
│   ├── Continuous Delivery vs Deployment
│   ├── Pipeline Design
│   ├── GitHub Actions (YAML workflows)
│   ├── Automated Testing in CI
│   ├── Environment Secrets Management
│   └── Deployment Strategies (Rolling, Blue-Green, Canary)
│
├── Cloud Fundamentals (AWS Focus)
│   ├── Cloud Computing Models (IaaS, PaaS, SaaS)
│   ├── AWS Global Infrastructure
│   ├── IAM (Users, Roles, Policies)
│   ├── EC2 (instances, AMIs, security groups)
│   ├── S3 (storage, buckets, policies)
│   ├── RDS (managed databases)
│   ├── VPC Basics
│   ├── Load Balancers (ELB)
│   ├── Route 53 (DNS)
│   └── CloudWatch (monitoring)
│
├── Application Deployment
│   ├── Deploying Django to Production
│   ├── Gunicorn & WSGI
│   ├── Nginx as Reverse Proxy
│   ├── SSL/TLS Setup (Let's Encrypt)
│   ├── Domain Configuration
│   ├── Environment Variables in Production
│   └── Static File Serving
│
├── Infrastructure as Code (IaC)
│   ├── What is IaC
│   ├── Terraform Basics (conceptual)
│   └── AWS CloudFormation (conceptual)
│
└── Monitoring & Observability
    ├── Application Logs
    ├── Structured Logging
    ├── Error Tracking (Sentry)
    ├── Metrics & Dashboards (CloudWatch, Grafana concepts)
    ├── Alerts & Uptime Monitoring
    └── Performance Monitoring
```

---

## 09. Communication Skills

```
Communication Skills
│
├── Spoken English Foundation
│   ├── Pronunciation & Clarity
│   ├── Grammar in Speech
│   ├── Vocabulary Building
│   ├── Fluency Development
│   └── Accent Reduction
│
├── Technical Communication
│   ├── Explaining Code to Non-Technical Audiences
│   ├── Explaining Code to Technical Audiences
│   ├── Technical Writing Fundamentals
│   ├── Documentation Writing
│   └── Email & Async Communication
│
├── Project Storytelling
│   ├── STAR Method (Situation, Task, Action, Result)
│   ├── Project Impact Articulation
│   ├── Quantifying Achievements
│   ├── Portfolio Narrative
│   └── Handling "Tell Me About Yourself"
│
├── Interview Communication
│   ├── Active Listening
│   ├── Clarifying Questions
│   ├── Thinking Out Loud
│   ├── Handling Unknown Questions
│   ├── Body Language (for video interviews)
│   └── Follow-Up Questions
│
├── Professional Communication
│   ├── Code Review Communication
│   ├── Stakeholder Updates
│   ├── Technical Documentation
│   ├── Slack / Email Etiquette
│   └── Presenting Technical Decisions
│
└── Vocabulary
    ├── Software Engineering Vocabulary
    ├── System Design Vocabulary
    ├── Interview-Specific Phrases
    └── Industry Jargon
```

---

## 10. Job Preparation

```
Job Preparation
│
├── Resume
│   ├── Resume Structure
│   ├── Technical Resume Formatting
│   ├── ATS Optimization
│   ├── Projects Section
│   ├── Skills Section
│   └── One-Page Rule
│
├── LinkedIn
│   ├── Profile Optimization
│   ├── Headline & About
│   ├── Skills Endorsements
│   ├── Project Showcasing
│   └── Networking & Outreach
│
├── GitHub Portfolio
│   ├── Repository Organization
│   ├── README Quality
│   ├── Contribution Graph
│   ├── Pinned Repositories
│   └── Open Source Contributions
│
├── Interview Preparation
│   ├── Technical Interview Structure
│   ├── Behavioral Interview (STAR)
│   ├── System Design Interview Basics
│   ├── HR Round Preparation
│   └── Offer Negotiation
│
└── Job Application Process
    ├── Job Search Strategy
    ├── Company Research
    ├── Application Tracking
    ├── Follow-Up Strategy
    └── Networking for Referrals
```

---

*This master tree is the canonical reference. Each branch is expanded in detail in its corresponding syllabus file.*
