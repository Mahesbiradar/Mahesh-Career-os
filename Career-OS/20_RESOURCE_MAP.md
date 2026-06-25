# Mahesh Career OS — Resource Map
> **Purpose:** Every syllabus topic mapped to a specific video resource.  
> AI uses this file when generating daily lesson files.  
> Mahesh never needs to open this file — it runs in the background.

---

## Primary Instructors

| Instructor | Platform | Why |
|---|---|---|
| **Mosh Hamedani** (Code with Mosh) | Udemy Business | Slow, structured, very clear English. Covers Python, SQL, Django, Git, Docker, React |
| **Corey Schafer** | YouTube (free) | Best Python + Django tutorials online. American, extremely clear |
| **Gate Smashers** | YouTube (free) | Indian instructor. Covers OS, DBMS, CN exactly as asked in SDE interviews in India |
| **Neso Academy** | YouTube (free) | Indian instructors. CN + OS theory, very structured |
| **Traversy Media** (Brad Traversy) | YouTube (free) | HTML, CSS, JS crash courses. Clear American English |

---

## PYTHON — Resource Map

**Course: "Python Programming with Mosh" (Udemy Business)**  
Search on Udemy Business: `Python Programming with Mosh`

| Syllabus Topic | Section in Course | Notes |
|---|---|---|
| Variables & Data Types | Section 2 — Primitive Types | First core section |
| Operators & Expressions | Section 2 — Primitive Types | Covered alongside variables |
| Control Flow (if/elif/else) | Section 3 — Control Flow | |
| Loops (for, while) | Section 3 — Control Flow | |
| Functions (definition, arguments, return) | Section 4 — Functions | |
| Built-in Functions & Methods | Section 4 — Functions | |
| Input / Output | Section 2 — Primitive Types | |
| Strings (methods, formatting, f-strings) | Section 5 — Data Structures | |
| Lists (operations, comprehensions) | Section 5 — Data Structures | |
| Tuples | Section 5 — Data Structures | |
| Sets | Section 5 — Data Structures | |
| Dictionaries | Section 5 — Data Structures | |
| Type Conversion & Casting | Section 2 — Primitive Types | |
| Functions (args, kwargs, lambda) | Section 4 — Functions | |
| Scope (local, global) | Section 4 — Functions | |
| Recursion | Section 4 — Functions | |
| Modules & Packages | Section 6 — Modules | |
| File Handling | Section 7 — Working with Files | |
| Exception Handling | Section 8 — Exceptions | |
| Iterators & Generators | Section 9 — Python Stdlib | |
| Classes & Objects | Section 10 — Classes | |
| Constructor (__init__) | Section 10 — Classes | |
| Inheritance | Section 10 — Classes | |
| Encapsulation & Access Modifiers | Section 10 — Classes | |
| Polymorphism & Duck Typing | Section 10 — Classes | |
| Dunder / Magic Methods | Section 10 — Classes | |
| Decorators | Section 11 — Advanced Python | |
| Context Managers | Section 11 — Advanced Python | |
| Type Hints & Annotations | Section 11 — Advanced Python | |

**Backup for Python (YouTube — Free):**  
Corey Schafer Python Tutorials playlist  
Search YouTube: `Corey Schafer Python Tutorials`  
Videos are 10–20 min each, one per topic. Use when Mosh's section feels rushed.

---

## BACKEND ENGINEERING — Resource Map

### Internet & Web Fundamentals
**YouTube: Mosh Hamedani — "How the Web Works" (free)**
Search YouTube: `Mosh how the web works`

| Syllabus Topic | Resource | Where |
|---|---|---|
| How the Internet Works | Mosh — "How the Web Works" video | YouTube |
| Client-Server Architecture | Mosh — "How the Web Works" video | YouTube |
| HTTP Protocol | Mosh — "HTTP Crash Course" | YouTube, search `Mosh HTTP` |
| HTTPS & TLS/SSL | Included in HTTP video above | |
| URLs, URIs, Query Parameters | Included in HTTP video above | |
| Headers & Body | Included in HTTP video above | |
| Cookies & Sessions | Django course covers this in context | Udemy Business |

### Django
**Course: "The Ultimate Django Series" by Mosh Hamedani (Udemy Business)**  
Search on Udemy Business: `Ultimate Django Series Mosh`

| Syllabus Topic | Section in Course | Notes |
|---|---|---|
| Django Project Structure | Part 1 — Getting Started | |
| Settings & Configuration | Part 1 — Getting Started | |
| URL Routing | Part 1 — Django Fundamentals | |
| Views (Function-Based, Class-Based) | Part 1 — Django Fundamentals | |
| Models & ORM | Part 1 — Building a Data Model | |
| Migrations | Part 1 — Building a Data Model | |
| Django Admin | Part 1 — Django Admin | |
| Forms & Validation | Part 2 — Advanced API Concepts | |
| Middleware | Part 2 — Advanced API Concepts | |

**Backup for Django (YouTube — Free):**  
Corey Schafer Django Tutorial Series  
Search YouTube: `Corey Schafer Django Tutorial`  
Best free Django resource available. 22-part series, very thorough.

### Django REST Framework (DRF)
**Same course: "The Ultimate Django Series" Part 2 and Part 3 (Udemy Business)**

| Syllabus Topic | Section | Notes |
|---|---|---|
| Serializers | Part 2 — Django REST Framework | |
| APIView, ViewSets, GenericViews | Part 2 — Building APIs | |
| Routers | Part 2 — Building APIs | |
| Permissions & Authentication Classes | Part 2 — Securing APIs | |
| Throttling | Part 2 — Securing APIs | |
| Pagination | Part 2 — Advanced API Concepts | |
| JWT Authentication | Part 3 — Advanced Topics | |

---

## SQL — Resource Map

**Course: "Complete SQL Mastery" by Mosh Hamedani (Udemy Business)**  
Search on Udemy Business: `Complete SQL Mastery Mosh`

| Syllabus Topic | Section in Course | Notes |
|---|---|---|
| Relational Database Concepts | Section 1 — Getting Started | |
| Tables, Rows, Columns, Schema | Section 1 — Getting Started | |
| Data Types | Section 1 — Getting Started | |
| Primary Key & Foreign Key | Section 1 — Getting Started | |
| SELECT basics | Section 2 — Retrieving Data | |
| WHERE Clause | Section 2 — Retrieving Data | |
| ORDER BY, LIMIT | Section 2 — Retrieving Data | |
| INSERT, UPDATE, DELETE | Section 3 — Inserting, Updating, Deleting | |
| IN, BETWEEN, LIKE | Section 2 — Retrieving Data | |
| IS NULL / IS NOT NULL | Section 2 — Retrieving Data | |
| INNER JOIN | Section 4 — Summarizing Data | |
| LEFT, RIGHT, FULL OUTER JOIN | Section 4 — Summarizing Data | |
| SELF JOIN | Section 4 — Summarizing Data | |
| COUNT, SUM, AVG, MIN, MAX | Section 5 — Writing Complex Queries | |
| GROUP BY, HAVING | Section 5 — Writing Complex Queries | |
| Subqueries | Section 5 — Writing Complex Queries | |
| CTEs (WITH clause) | Section 6 — Essential MySQL Functions | |
| Window Functions | Section 7 — Views | |
| CREATE TABLE, ALTER TABLE | Section 8 — Stored Procedures | |
| Indexes | Section 9 — Triggers | |
| Transactions & ACID | Section 10 — Transactions | |

**Note on PostgreSQL specifics:**  
After completing the Mosh SQL course (which uses MySQL), spend 1 session on:  
YouTube: `Amigoscode PostgreSQL Tutorial` — covers PostgreSQL-specific syntax (RETURNING, ON CONFLICT, JSONB)

---

## DBMS THEORY — Resource Map

**YouTube: Gate Smashers — DBMS Playlist**  
Search YouTube: `Gate Smashers DBMS`  
Indian instructor, interview-focused, covers exact topics asked in SDE rounds.

| Syllabus Topic | Video to Watch | Notes |
|---|---|---|
| What is a DBMS | "Introduction to DBMS" | First video in playlist |
| ER Modeling | "ER Diagram in DBMS" | |
| Entities, Attributes, Relationships | "ER Diagram in DBMS" | |
| Relational Model, Keys | "Keys in DBMS" | Super, Candidate, Primary, Foreign |
| Normalization (1NF, 2NF, 3NF, BCNF) | "Normalization in DBMS" | Multiple videos |
| Functional Dependencies | "Functional Dependency" | |
| Indexing (B-Tree, B+ Tree) | "Indexing in DBMS" | |
| Transactions & ACID | "Transaction in DBMS" | |
| Concurrency Control | "Concurrency Control" | |
| Isolation Levels | "Isolation Levels in DBMS" | |
| Deadlocks in DBMS | "Deadlock in DBMS" | |
| Recovery (Undo/Redo logs) | "Recovery in DBMS" | |

---

## OPERATING SYSTEMS — Resource Map

**YouTube: Gate Smashers — OS Playlist**  
Search YouTube: `Gate Smashers Operating System`

| Syllabus Topic | Video | Notes |
|---|---|---|
| What is an OS | "Introduction to OS" | |
| System Calls | "System Calls in OS" | |
| Process Concept & PCB | "Process in OS" | |
| Process States | "Process States in OS" | |
| Threads vs Processes | "Threads in OS" | |
| CPU Scheduling — FCFS, SJF, RR | "CPU Scheduling" | Multiple videos |
| Race Conditions, Critical Section | "Process Synchronization" | |
| Mutex, Semaphores | "Semaphores in OS" | |
| Deadlocks — Coffman Conditions | "Deadlock in OS" | |
| Banker's Algorithm | "Banker's Algorithm" | |
| Memory Management, Paging | "Memory Management" | |
| Virtual Memory, Page Replacement | "Virtual Memory in OS" | |
| File Systems | "File System in OS" | |

**For Linux Practical:**  
YouTube: `NetworkChuck Linux for Beginners` — hands-on, fast-paced, clear English  
OR  
YouTube: `Corey Schafer Linux Command Line Tutorial`

---

## COMPUTER NETWORKS — Resource Map

**YouTube: Gate Smashers — Computer Networks Playlist**  
Search YouTube: `Gate Smashers Computer Networks`

| Syllabus Topic | Video | Notes |
|---|---|---|
| What is a Network | "Introduction to Computer Networks" | |
| OSI Model (all 7 layers) | "OSI Model in Computer Networks" | Multiple videos, one per layer |
| TCP/IP Model | "TCP/IP Model" | |
| IP Addressing, IPv4, CIDR | "IP Addressing" | |
| TCP vs UDP | "TCP vs UDP" | |
| Three-Way Handshake | "TCP Connection" | |
| HTTP/HTTPS | "HTTP vs HTTPS" | |
| DNS | "DNS in Computer Networks" | |
| Routing | "Routing in Computer Networks" | |
| Subnetting | "Subnetting" | |

**For HTTP/HTTPS practical understanding (backend-focused):**  
YouTube: `Traversy Media — HTTP Crash Course` — practical, developer-focused

---

## FRONTEND — Resource Map

### HTML & CSS
**YouTube: Traversy Media — "HTML Crash Course" and "CSS Crash Course"**  
Search YouTube: `Traversy Media HTML Crash Course`  
Search YouTube: `Traversy Media CSS Crash Course`  
Each is a single 1-hour video. Very clear.

### JavaScript
**Course: "JavaScript Basics for Beginners" by Mosh Hamedani (Udemy Business)**  
Search Udemy Business: `JavaScript Basics Mosh`

| Syllabus Topic | Section | Notes |
|---|---|---|
| Variables, Data Types | Section 2 — JavaScript Basics | |
| Functions | Section 3 — Functions | |
| Objects | Section 4 — Objects | |
| Arrays | Section 5 — Arrays | |
| DOM Manipulation | Section 7 — The DOM | |
| Events | Section 8 — Events | |
| Promises, async/await | Section 11 — Asynchronous JS | |
| Fetch API | Section 11 — Asynchronous JS | |

### React
**Course: "React 18 for Beginners" by Mosh Hamedani (Udemy Business)**  
Search Udemy Business: `React 18 Mosh`

| Syllabus Topic | Section | Notes |
|---|---|---|
| JSX, Components | Section 2 — Getting Started | |
| Props, State | Section 3 — Building Components | |
| useState, useEffect | Section 4 — React Hooks | |
| React Router | Section 7 — Routing | |
| API calls with React | Section 8 — Connecting to Backend | |

---

## CLOUD & DEPLOYMENT — Resource Map

### Git
**Course: "The Ultimate Git Course" by Mosh Hamedani (Udemy Business)**  
Search Udemy Business: `Ultimate Git Course Mosh`

### Docker
**Course: "The Ultimate Docker Course" by Mosh Hamedani (Udemy Business)**  
Search Udemy Business: `Ultimate Docker Course Mosh`

### AWS Basics
**YouTube: "AWS Tutorial for Beginners" by TechWorld with Nana**  
Search YouTube: `TechWorld Nana AWS Tutorial`  
Clear English, developer-focused, not certification-focused.

### Django Deployment
**YouTube: Corey Schafer — "Deploying Django Application" series**  
Search YouTube: `Corey Schafer Django deployment`

---

## COMMUNICATION — Resource Map

No video course needed. Built into daily lesson files directly.

Every lesson file includes one 15-minute communication task:
- Explain today's topic as if in an interview
- Practice self-introduction
- Answer a STAR behavioural question

AI writes the communication prompt in the lesson file based on what was learned that day.

---

## How AI Uses This File

When generating a daily lesson file, AI:
1. Identifies today's topic from the 180-day sequence
2. Looks up the exact course + section in this file
3. Puts the specific video link + section name in the lesson file
4. Writes the concept summary based on that topic
5. Designs the assignment around what the video teaches

Mahesh never needs to find a resource. The lesson file tells him exactly what to open.

---

## Resource Update Log

| Date | Update |
|---|---|
| 2026-06-26 | Initial resource map created. All Phase 1–2 topics mapped. |
