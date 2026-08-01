# Phase 2 — Interview-Focused Syllabus

---

# 1. HTML

## Level 1: HTML Fundamentals

### Module: Semantic Markup

#### Topic: HTML5 Structure & Semantics

- **Priority:** Category A
- **Prerequisites:** None
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** React Official Docs (Beta) — Free
- **Completion Criteria:** Can build a semantic HTML page with proper document structure, heading hierarchy, and form elements; can explain why semantic tags matter for accessibility and SEO

**Subtopics:**
- Semantic elements (`header`, `nav`, `main`, `section`, `article`, `aside`, `footer`)
- Document structure (`DOCTYPE`, `html`, `head`, `body`, meta tags)
- Forms (`input` types, `label`, `fieldset`, validation attributes)
- Tables (`table`, `thead`, `tbody`, `tr`, `td`, `th`)
- Multimedia (`img`, `video`, `audio`, `figure`, `figcaption`)
- Accessibility basics (`alt` text, `aria` labels, semantic structure)

---

# 2. CSS

## Level 2: CSS Layout & Styling

### Module: Modern CSS

#### Topic: CSS Fundamentals

- **Priority:** Category A
- **Prerequisites:** HTML Level 1
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Completion Criteria:** Can style a React component using Flexbox and Grid; can explain box model, specificity, and responsive breakpoints; can debug layout issues in browser dev tools

**Subtopics:**
- Box model (content, padding, border, margin, `box-sizing`)
- Flexbox (container properties, item properties, alignment, justification)
- CSS Grid (template areas, auto-fill, minmax, gap)
- Positioning (`static`, `relative`, `absolute`, `fixed`, `sticky`)
- Responsive design (media queries, mobile-first approach)
- CSS variables and basic animations
- Common selectors and specificity rules

---

# 3. JavaScript

## Level 3: JavaScript Core

### Module: ES6+ Fundamentals

#### Topic: Variables, Types & Control Flow

- **Priority:** Category A
- **Prerequisites:** HTML Level 1, CSS Level 2
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** None
- **Completion Criteria:** Can declare variables with `let`, `const`, and `var` and explain scoping differences; can use all primitive and reference types correctly

**Subtopics:**
- `let`, `const`, `var` and block scoping
- Primitive types (`string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`)
- Reference types (`object`, `array`, `function`)
- Type coercion and strict equality (`===` vs `==`)
- Template literals and string methods
- Control flow (`if/else`, `switch`, `for`, `while`, `for...of`, `for...in`)

#### Topic: Functions & Scope

- **Priority:** Category A
- **Prerequisites:** Variables, Types & Control Flow
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** JavaScript.info — Free
- **Completion Criteria:** Can write arrow functions, use default parameters, rest/spread syntax, and explain lexical scope and the scope chain

**Subtopics:**
- Function declarations vs expressions vs arrow functions
- Default parameters, rest parameters (`...args`)
- Spread operator (`...`) for arrays and objects
- Destructuring (arrays and objects)
- Lexical scope and the scope chain
- Higher-order functions and callbacks

#### Topic: Arrays & Objects

- **Priority:** Category A
- **Prerequisites:** Functions & Scope
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** None
- **Completion Criteria:** Can manipulate arrays and objects using modern ES6+ methods; can choose the right data structure for a given problem

**Subtopics:**
- Array methods (`map`, `filter`, `reduce`, `find`, `some`, `every`, `flat`, `sort`)
- Object methods (`Object.keys`, `Object.values`, `Object.entries`)
- Array and object immutability patterns
- Sets and Maps basics
- JSON serialization and parsing

## Level 4: DOM & Events

### Module: Browser Interaction

#### Topic: DOM Manipulation

- **Priority:** Category A
- **Prerequisites:** JavaScript Core Level 3
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** React Official Docs (Beta) — Free
- **Completion Criteria:** Can select, create, modify, and delete DOM elements; can explain the difference between DOM manipulation and React's declarative approach

**Subtopics:**
- Selecting elements (`querySelector`, `getElementById`, `querySelectorAll`)
- Creating and removing elements (`createElement`, `append`, `remove`)
- Modifying attributes, classes, and styles
- Traversing the DOM (parent, child, sibling)
- Event delegation and bubbling

#### Topic: Event Handling

- **Priority:** Category A
- **Prerequisites:** DOM Manipulation
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** None
- **Completion Criteria:** Can attach and remove event listeners; can explain event propagation and use event delegation for dynamic lists

**Subtopics:**
- `addEventListener` and `removeEventListener`
- Event object and common properties (`target`, `currentTarget`, `preventDefault`, `stopPropagation`)
- Event bubbling and capturing phases
- Event delegation pattern

## Level 5: JavaScript Advanced

### Module: Asynchronous Programming

#### Topic: Promises & Async/Await

- **Priority:** Category A
- **Prerequisites:** JavaScript Core Level 3, DOM & Events Level 4
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** None
- **Completion Criteria:** Can chain promises, handle errors with `try/catch`, and rewrite callback-based code into async/await; can explain the event loop at a high level

**Subtopics:**
- Promises (`then`, `catch`, `finally`, `Promise.all`, `Promise.race`)
- Async/await syntax and error handling
- Fetch API for HTTP requests
- Event loop basics (call stack, task queue, microtasks)
- Callbacks vs Promises vs Async-Await

#### Topic: Advanced Concepts

- **Priority:** Category A
- **Prerequisites:** Promises & Async/Await
- **Recommended Resource:** The Complete JavaScript Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** JavaScript.info — Free
- **Completion Criteria:** Can explain `this` in all four binding rules, write a closure, and describe how prototypal inheritance differs from class-based inheritance

**Subtopics:**
- `this` keyword (implicit, explicit, `new`, default binding; `call`, `apply`, `bind`)
- Closures and practical use cases
- Prototypes and prototypal inheritance
- ES6 Classes (`class`, `constructor`, `extends`, `super`, `get`, `set`)
- Modules (`import`, `export`, default vs named exports)

---

# 4. React

## Level 7: React Fundamentals

### Module: React Core

#### Topic: Components & JSX

- **Priority:** Category A
- **Prerequisites:** JavaScript Advanced Level 5
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** React Official Docs (Beta) — Free
- **Completion Criteria:** Can create functional components with JSX; can explain why React uses a virtual DOM and the benefits of component-based architecture

**Subtopics:**
- JSX syntax and rules
- Functional components vs class components
- Component composition and children
- Conditional rendering and lists (`&&`, ternary, `map`)
- Keys in lists and reconciliation basics
- Virtual DOM and re-rendering

#### Topic: Props & State

- **Priority:** Category A
- **Prerequisites:** Components & JSX
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** Scrimba Learn React — Bob Ziroll — Free
- **Completion Criteria:** Can pass data via props, lift state up, and manage local component state; can explain one-way data flow and why props are read-only

**Subtopics:**
- Props (passing data, prop drilling, destructuring)
- State with `useState` (initialization, updates, batching)
- One-way data flow
- Lifting state up pattern
- Derived state and computed values

## Level 8: React Hooks

### Module: Core Hooks

#### Topic: useState, useEffect & useRef

- **Priority:** Category A
- **Prerequisites:** Props & State
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** React Official Docs (Beta) — Free
- **Completion Criteria:** Can manage side effects with `useEffect` (data fetching, subscriptions, manual DOM manipulation); can use `useRef` for persistent values and DOM access; can explain the dependency array and cleanup functions

**Subtopics:**
- `useEffect` (mount, update, unmount phases)
- Dependency array rules and ESLint warnings
- Cleanup functions (subscriptions, timers, event listeners)
- `useRef` (DOM references, storing previous values)
- Rules of Hooks

#### Topic: Advanced Hooks

- **Priority:** Category A
- **Prerequisites:** useState, useEffect & useRef
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** Scrimba Learn React — Bob Ziroll — Free
- **Completion Criteria:** Can share state across components without prop drilling using `useContext`; can manage complex state logic with `useReducer`; can write custom hooks for reusable logic

**Subtopics:**
- `useContext` (Provider, Consumer, avoiding prop drilling)
- `useReducer` (actions, reducers, dispatch, initial state)
- `useMemo` and `useCallback` (basic awareness)
- Custom hooks (naming convention, extraction patterns)
- Hook composition and reusability

## Level 9: React Router

### Module: Client-Side Navigation

#### Topic: Routing & Navigation

- **Priority:** Category A
- **Prerequisites:** React Hooks Level 8
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** React Official Docs (Beta) — Free
- **Completion Criteria:** Can implement multi-page navigation in a React SPA; can handle dynamic routes, nested routes, and programmatic navigation

**Subtopics:**
- `BrowserRouter`, `Routes`, `Route`
- `Link` and `NavLink`
- Dynamic routes and URL parameters (`useParams`)
- Nested routes and layout routes
- Programmatic navigation (`useNavigate`)
- 404 handling and redirects

## Level 10: State Management

### Module: Global & Server State

#### Topic: State Management Libraries

- **Priority:** Category B
- **Prerequisites:** React Router Level 9
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** Full Stack Open — University of Helsinki — Free
- **Completion Criteria:** Can set up Redux Toolkit or Zustand for global state; can explain when global state is necessary vs overkill; aware of React Query (TanStack Query) for server state

**Subtopics:**
- Redux Toolkit (store, slices, reducers, `useSelector`, `useDispatch`)
- Zustand basics (create store, subscribe, actions)
- React Query / TanStack Query awareness (caching, synchronization)
- Global vs local vs server state decision framework

## Level 11: API Integration

### Module: Backend Communication

#### Topic: Data Fetching & API Consumption

- **Priority:** Category A
- **Prerequisites:** React Router Level 9
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** Scrimba Learn React — Bob Ziroll — Free
- **Completion Criteria:** Can fetch data from a Django REST API and display it in React; can handle loading, error, and empty states; can explain CORS from the frontend perspective

**Subtopics:**
- Fetch API and Axios for HTTP requests
- `useEffect` data fetching patterns
- Loading states and error boundaries (basic)
- POST/PUT/DELETE requests and optimistic updates
- CORS errors and frontend-backend integration debugging
- Environment variables for API URLs

## Level 12: React Advanced

### Module: Performance & Patterns

#### Topic: Performance Optimization

- **Priority:** Category B
- **Prerequisites:** State Management Level 10, API Integration Level 11
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** Full Stack Open — University of Helsinki — Free
- **Completion Criteria:** Can identify unnecessary re-renders; can use `useMemo` and `useCallback` appropriately; aware of code splitting and lazy loading

**Subtopics:**
- React DevTools Profiler basics
- Memoization with `React.memo`, `useMemo`, `useCallback`
- Code splitting and `React.lazy` with `Suspense`
- Render props and higher-order components (awareness)

## Level 13: Build Tools

### Module: Tooling

#### Topic: Modern React Tooling

- **Priority:** Category B
- **Prerequisites:** React Advanced Level 12
- **Recommended Resource:** The Ultimate React Course 2025/2026 — Jonas Schmedtmann — Udemy
- **Gap Resource:** Full Stack Open — University of Helsinki — Free
- **Completion Criteria:** Can create a production build with Vite; can explain what transpilation and bundling do; aware of TypeScript benefits

**Subtopics:**
- Vite (development server, production build, HMR)
- Babel and transpilation basics
- ESLint and Prettier configuration
- TypeScript awareness (basic types, interfaces, props typing)

## Level 14: Testing

### Module: React Testing

#### Topic: Component Testing

- **Priority:** Category B
- **Prerequisites:** API Integration Level 11
- **Recommended Resource:** React Testing Library with Jest/Vitest — Bonnie Schulkin — Udemy
- **Gap Resource:** React Official Docs (Beta) — Free
- **Completion Criteria:** Can write unit tests for React components; can test user interactions, async data fetching, and form submissions; can explain the difference between unit and integration tests

**Subtopics:**
- React Testing Library (`render`, `screen`, `fireEvent`, `userEvent`)
- Jest / Vitest matchers and assertions
- Testing async components (`waitFor`, `findBy`)
- Mocking API calls (`msw` or manual mocks)
- Testing custom hooks

---

# 5. DBMS

## Level 1: Foundations & Architecture

### Module: DBMS Basics

#### Topic: Introduction & Architecture

- **Priority:** Category A
- **Prerequisites:** None
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** None
- **Completion Criteria:** Can explain the three-schema architecture, data independence, and the role of DBA; can differentiate between DBMS and file systems

**Subtopics:**
- DBMS vs file system
- Three-schema architecture (external, conceptual, internal)
- Data independence (logical and physical)
- Data models (hierarchical, network, relational, object-oriented)
- Database languages (DDL, DML, DCL, TCL)
- ACID overview (detailed in Level 6)

## Level 2: ER Modeling

### Module: Conceptual Design

#### Topic: Entity-Relationship Model

- **Priority:** Category A
- **Prerequisites:** DBMS Foundations Level 1
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** Database Management Systems (RDBMS) & Microsoft Fabric SQL — Atchyut Kumar — Udemy
- **Completion Criteria:** Can draw an ER diagram for a given requirement; can identify entities, attributes, relationships, and cardinalities (1:1, 1:N, M:N)

**Subtopics:**
- Entities, attributes (simple, composite, multi-valued, derived)
- Relationships and relationship sets
- Cardinality ratios and participation constraints
- Weak entities and identifying relationships
- ER to relational mapping rules
- Enhanced ER (generalization, specialization, aggregation)

## Level 3: Relational Model & Keys

### Module: Relational Algebra

#### Topic: Relational Model & Keys

- **Priority:** Category A
- **Prerequisites:** ER Modeling Level 2
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** Database Management Systems (RDBMS) & Microsoft Fabric SQL — Atchyut Kumar — Udemy
- **Completion Criteria:** Can define all key types; can perform relational algebra operations; can map an ER diagram to relational tables

**Subtopics:**
- Relational model concepts (relation, tuple, attribute, domain)
- Keys (super key, candidate key, primary key, foreign key, alternate key)
- Relational algebra (select, project, union, set difference, Cartesian product, join types)
- Integrity constraints (entity, referential, domain)
- ER-to-relational mapping

## Level 4: Normalization

### Module: Database Design

#### Topic: Normal Forms & Functional Dependencies

- **Priority:** Category A
- **Prerequisites:** Relational Model & Keys Level 3
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** Database System Concepts — Silberschatz, Korth, Sudarshan — Textbook
- **Completion Criteria:** Can normalize a schema up to BCNF; can identify functional dependencies and candidate keys; can explain when and why to denormalize

**Subtopics:**
- Functional dependencies (full, partial, transitive, multivalued)
- Closure of attributes and canonical cover
- 1NF, 2NF, 3NF definitions and decomposition
- BCNF definition and decomposition algorithm
- Lossless join and dependency preservation
- Denormalization use cases and tradeoffs

## Level 5: Indexing

### Module: Physical Design

#### Topic: Index Structures

- **Priority:** Category A
- **Prerequisites:** Relational Model & Keys Level 3
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** Database System Concepts — Silberschatz, Korth, Sudarshan — Textbook
- **Completion Criteria:** Can explain B-Tree and B+ Tree structures; can differentiate clustered vs non-clustered indexes; can explain when indexing improves or hurts performance

**Subtopics:**
- Indexing concepts and dense vs sparse indexes
- B-Tree and B+ Tree structure, search, insertion, deletion
- Clustered vs non-clustered indexes
- Primary vs secondary indexes
- Composite indexes and covering indexes
- When NOT to index (write-heavy tables, low cardinality)

## Level 6: Transactions & ACID

### Module: Transaction Management

#### Topic: ACID Properties & Schedules

- **Priority:** Category A
- **Prerequisites:** Normalization Level 4
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** Database Management Systems (RDBMS) & Microsoft Fabric SQL — Atchyut Kumar — Udemy
- **Completion Criteria:** Can explain all four ACID properties with examples; can classify schedules as serial, serializable, or non-serializable; can explain how PostgreSQL ensures durability

**Subtopics:**
- Transaction concepts (BEGIN, COMMIT, ROLLBACK, SAVEPOINT)
- ACID properties (Atomicity, Consistency, Isolation, Durability)
- Transaction states (active, partially committed, committed, failed, aborted)
- Serial and non-serial schedules
- Conflict serializability (precedence graph)
- View serializability (awareness)

## Level 7: Concurrency Control

### Module: Concurrent Execution

#### Topic: Locking & Isolation

- **Priority:** Category A
- **Prerequisites:** Transactions & ACID Level 6
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** GeeksforGeeks DBMS — Free
- **Completion Criteria:** Can explain dirty read, non-repeatable read, and phantom read; can describe Two-Phase Locking and isolation levels; can solve concurrency problems

**Subtopics:**
- Concurrency problems (dirty read, non-repeatable read, phantom read, lost update)
- Lock-based protocols (shared/exclusive locks, lock compatibility matrix)
- Two-Phase Locking (2PL) — growing and shrinking phases
- Strict 2PL and rigorous 2PL
- Deadlock handling in databases (wait-die, wound-wait)
- Isolation levels (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE)
- Timestamp-based protocols (basic awareness)

## Level 8: Database Recovery

### Module: Recovery Mechanisms

#### Topic: Recovery Systems

- **Priority:** Category B
- **Prerequisites:** Transactions & ACID Level 6
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** GeeksforGeeks DBMS — Free
- **Completion Criteria:** Can explain write-ahead logging (WAL) and checkpointing; aware of ARIES algorithm basics; can explain how PostgreSQL handles crash recovery

**Subtopics:**
- Failure types (transaction, system, disk, media)
- Log-based recovery (deferred vs immediate modification)
- Write-Ahead Logging (WAL)
- Checkpoints and fuzzy checkpoints
- ARIES algorithm (analysis, redo, undo phases) — awareness
- Shadow paging (awareness)

## Level 9: NoSQL & Modern Databases

### Module: Non-Relational Systems

#### Topic: NoSQL & CAP Theorem

- **Priority:** Category A
- **Prerequisites:** Concurrency Control Level 7
- **Recommended Resource:** Database Management Systems (DBMS) — Neso Academy — YouTube (Free)
- **Gap Resource:** GeeksforGeeks DBMS — Free
- **Completion Criteria:** Can explain CAP Theorem and choose between SQL and NoSQL for a given system design scenario; can describe the four types of NoSQL databases with use cases

**Subtopics:**
- CAP Theorem (Consistency, Availability, Partition Tolerance)
- SQL vs NoSQL tradeoffs
- Document databases (MongoDB) — use cases and structure
- Key-value stores (Redis, DynamoDB) — use cases
- Wide-column stores (Cassandra) — use cases
- Graph databases (Neo4j) — use cases
- BASE properties (Basically Available, Soft state, Eventual consistency)

---

# 6. Operating Systems

## Level 1: OS Foundations

### Module: OS Basics

#### Topic: Operating System Concepts

- **Priority:** Category A
- **Prerequisites:** None
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can explain OS types, structures, and services; can describe dual-mode operation and system calls; can differentiate between user space and kernel space

**Subtopics:**
- OS definition, functions, and types (batch, multiprogramming, multitasking, real-time, distributed)
- OS structure (monolithic, layered, microkernel, hybrid)
- System calls and APIs
- Dual-mode operation (user mode vs kernel mode)
- Interrupts and traps

## Level 2: Processes

### Module: Process Management

#### Topic: Process Concepts

- **Priority:** Category A
- **Prerequisites:** OS Foundations Level 1
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can explain process vs program; can describe PCB contents and process state transitions; can explain what happens during a `fork()` system call

**Subtopics:**
- Process vs program
- Process Control Block (PCB) contents
- Process states (new, ready, running, waiting, terminated)
- Process state transitions and diagrams
- Context switch and its overhead
- Process creation (`fork`, `exec`, `wait`, `exit`)
- Inter-process communication (shared memory, message passing) — basics

## Level 3: Threads

### Module: Thread Management

#### Topic: Thread Concepts

- **Priority:** Category A
- **Prerequisites:** Processes Level 2
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can explain process vs thread; can describe multithreading models and their tradeoffs; can explain thread-specific data and the benefits of threading

**Subtopics:**
- Process vs thread (address space, resource sharing, overhead)
- Thread states and Thread Control Block (TCB)
- Multithreading models (many-to-one, one-to-one, many-to-many)
- User-level vs kernel-level threads
- Thread pools and threading benefits/challenges

## Level 4: CPU Scheduling

### Module: Scheduling Algorithms

#### Topic: CPU Scheduling

- **Priority:** Category A
- **Prerequisites:** Processes Level 2
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can solve scheduling problems for FCFS, SJF, SRTF, Priority, and Round Robin; can calculate waiting time and turnaround time; can explain starvation and aging

**Subtopics:**
- Scheduling criteria (CPU utilization, throughput, turnaround time, waiting time, response time)
- First-Come First-Served (FCFS) and convoy effect
- Shortest Job First (SJF) — preemptive and non-preemptive
- Shortest Remaining Time First (SRTF)
- Priority scheduling and starvation/aging
- Round Robin (time quantum selection)
- Multilevel Queue (MLQ) and Multilevel Feedback Queue (MLFQ)

## Level 5: Process Synchronization

### Module: Synchronization

#### Topic: Critical Section & Primitives

- **Priority:** Category A
- **Prerequisites:** Threads Level 3
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can explain critical section problem and its requirements; can solve synchronization problems using mutex, semaphore, and monitor; can explain the dining philosophers problem

**Subtopics:**
- Critical section problem and requirements (mutual exclusion, progress, bounded waiting)
- Peterson's solution (software approach)
- Mutex locks and spinlocks
- Semaphores (binary and counting, `wait`/`signal` operations)
- Classical synchronization problems (producer-consumer, readers-writers, dining philosophers)
- Monitors and condition variables

## Level 6: Deadlocks

### Module: Deadlock Management

#### Topic: Deadlock Concepts

- **Priority:** Category A
- **Prerequisites:** Process Synchronization Level 5
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System Concepts — Silberschatz, Galvin, Gagne — Textbook
- **Completion Criteria:** Can explain the four Coffman conditions; can detect deadlock using resource allocation graphs; can explain Banker's algorithm for avoidance; can describe prevention and recovery strategies

**Subtopics:**
- Deadlock definition and four necessary conditions (Coffman conditions)
- Resource Allocation Graphs (RAG) — single instance and multiple instances
- Deadlock prevention (breaking each Coffman condition)
- Deadlock avoidance (Banker's algorithm — safe state, resource allocation)
- Deadlock detection and recovery
- Ostrich algorithm (awareness)

## Level 7: Memory Management

### Module: Memory Allocation

#### Topic: Memory Management Techniques

- **Priority:** Category A
- **Prerequisites:** OS Foundations Level 1
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can explain contiguous and non-contiguous allocation; can solve paging and segmentation address translation problems; can explain internal and external fragmentation

**Subtopics:**
- Memory allocation (first-fit, best-fit, worst-fit)
- Internal vs external fragmentation
- Paging (page table, address translation, TLB)
- Segmentation (segment table, address translation)
- Segmentation with paging (awareness)
- Swapping and overlay concepts

## Level 8: Virtual Memory

### Module: Virtual Memory Concepts

#### Topic: Demand Paging & Page Replacement

- **Priority:** Category A
- **Prerequisites:** Memory Management Level 7
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can explain demand paging and page fault handling; can solve page replacement problems using FIFO, LRU, and Optimal algorithms; can explain thrashing and working set model

**Subtopics:**
- Virtual memory concepts and benefits
- Demand paging and page fault handling
- Page replacement algorithms (FIFO, LRU, Optimal, Clock/Second Chance)
- Belady's anomaly
- Thrashing and working set model
- Page fault frequency and allocation strategies
- Copy-on-write (linked to process creation)

## Level 9: File Systems

### Module: File Management

#### Topic: File System Implementation

- **Priority:** Category B
- **Prerequisites:** Memory Management Level 7
- **Recommended Resource:** Operating Systems from Scratch — Parts 1-4 — Vignesh Sekar — Udemy
- **Gap Resource:** Operating System Concepts — Silberschatz, Galvin, Gagne — Textbook
- **Completion Criteria:** Can explain file allocation methods; aware of inode structure and directory implementation; can describe RAID levels

**Subtopics:**
- File concepts and attributes
- Directory structure (single-level, two-level, tree, acyclic graph, general graph)
- File allocation methods (contiguous, linked, indexed)
- Inodes and UNIX file system basics
- Free space management
- Disk scheduling algorithms (FCFS, SSTF, SCAN, C-SCAN, LOOK)
- RAID levels (0, 1, 5, 6, 10) — awareness

## Level 10: Linux Practical

### Module: Linux Commands

#### Topic: Linux Fundamentals

- **Priority:** Category A
- **Prerequisites:** Processes Level 2, File Systems Level 9
- **Recommended Resource:** The Linux Command Line Bootcamp — Colt Steele — Udemy
- **Gap Resource:** Operating System — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can navigate Linux file system, manage permissions, inspect processes, and use grep/find; can write basic shell scripts; can SSH into a remote server and manage files

**Subtopics:**
- File system hierarchy and navigation (`ls`, `cd`, `pwd`, `mkdir`, `rm`, `cp`, `mv`)
- File permissions (`chmod`, `chown`, `umask`, octal notation)
- Text processing (`cat`, `grep`, `awk`, `sed`, `sort`, `uniq`, `wc`)
- Process management (`ps`, `top`, `htop`, `kill`, `nice`)
- Networking (`ssh`, `scp`, `curl`, `ping`, `netstat`)
- Package management (`apt`, `yum` — awareness)
- Shell scripting basics (variables, loops, conditionals, functions)
- `systemd` and service management (awareness)

---

# 7. Computer Networks

## Level 1: Foundations

### Module: Networking Basics

#### Topic: Network Fundamentals

- **Priority:** Category A
- **Prerequisites:** None
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** Computer Networking Full Course 2026 — Simplilearn — YouTube (Free)
- **Completion Criteria:** Can classify network types by size and topology; can explain transmission media and switching techniques; can differentiate between circuit switching and packet switching

**Subtopics:**
- Network types (PAN, LAN, MAN, WAN)
- Network topologies (bus, star, ring, mesh, hybrid)
- Transmission media (guided and unguided)
- Circuit switching vs packet switching vs message switching
- Connection-oriented vs connectionless services
- Network performance metrics (bandwidth, throughput, latency, jitter)

## Level 2: OSI Model

### Module: OSI Reference Model

#### Topic: OSI Layers

- **Priority:** Category A
- **Prerequisites:** Network Foundations Level 1
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** None
- **Completion Criteria:** Can name all seven OSI layers in order; can explain the function, protocols, and devices at each layer; can map real-world protocols to their correct layers

**Subtopics:**
- Layer 1: Physical (bits, cables, hubs, repeaters)
- Layer 2: Data Link (frames, MAC addresses, switches, bridges, Ethernet)
- Layer 3: Network (packets, IP, routers, routing)
- Layer 4: Transport (segments, TCP/UDP, ports)
- Layer 5: Session (session management, NetBIOS)
- Layer 6: Presentation (encryption, compression, translation)
- Layer 7: Application (HTTP, FTP, SMTP, DNS)

## Level 3: TCP/IP Model

### Module: TCP/IP Protocol Suite

#### Topic: TCP/IP Architecture

- **Priority:** Category A
- **Prerequisites:** OSI Model Level 2
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** The Complete Networking Fundamentals Course — David Bombal — Udemy
- **Completion Criteria:** Can map TCP/IP layers to OSI layers; can explain the encapsulation and decapsulation process; can identify key protocols at each TCP/IP layer

**Subtopics:**
- TCP/IP 4-layer model (Network Interface, Internet, Transport, Application)
- Mapping OSI to TCP/IP
- Encapsulation and decapsulation process
- Protocols at each layer (IP, ICMP, ARP, TCP, UDP, HTTP, FTP, SMTP)
- TCP/IP protocol stack data flow

## Level 4: IP Addressing

### Module: Network Layer Addressing

#### Topic: IPv4 & IPv6

- **Priority:** Category A
- **Prerequisites:** TCP/IP Model Level 3
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** The Complete Networking Fundamentals Course — David Bombal — Udemy
- **Completion Criteria:** Can explain IPv4 address classes and CIDR notation; can perform subnetting calculations; can explain NAT and private IP ranges; aware of IPv6 basics

**Subtopics:**
- IPv4 address structure and classes (A, B, C, D, E)
- Private IP ranges and loopback
- Subnetting and CIDR notation
- Subnet mask calculations
- Variable Length Subnet Masking (VLSM) — awareness
- NAT (Network Address Translation) and PAT
- IPv6 address structure and notation — awareness
- DHCP basics

## Level 5: TCP & UDP

### Module: Transport Layer Protocols

#### Topic: TCP & UDP Deep Dive

- **Priority:** Category A
- **Prerequisites:** TCP/IP Model Level 3
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** The Complete Networking Fundamentals Course — David Bombal — Udemy
- **Completion Criteria:** Can explain TCP three-way handshake and four-way termination step-by-step; can differentiate TCP and UDP with use cases; can explain sequence numbers, ACKs, and flow control; can explain congestion control basics

**Subtopics:**
- TCP segment structure (source port, destination port, sequence number, ACK number, flags)
- TCP three-way handshake (SYN, SYN-ACK, ACK)
- TCP four-way termination (FIN, ACK, FIN, ACK)
- TCP reliable delivery (sequence numbers, acknowledgments, retransmission)
- Flow control (sliding window)
- Congestion control (slow start, congestion avoidance, fast retransmit, fast recovery) — basics
- UDP structure and characteristics (connectionless, unreliable, low overhead)
- TCP vs UDP comparison and use cases
- Port numbers (well-known, registered, dynamic/ephemeral)

## Level 6: HTTP & HTTPS

### Module: Application Layer Protocols

#### Topic: HTTP & Web Communication

- **Priority:** Category A
- **Prerequisites:** TCP & UDP Level 5
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** GeeksforGeeks Computer Networks — Free
- **Completion Criteria:** Can explain HTTP request/response structure; can list common methods and status codes; can explain HTTPS/TLS handshake at a high level; can explain HTTP/1.1 vs HTTP/2 vs HTTP/3 differences

**Subtopics:**
- HTTP request structure (method, URL, headers, body)
- HTTP response structure (status line, headers, body)
- HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)
- HTTP status codes (1xx, 2xx, 3xx, 4xx, 5xx — common codes)
- HTTP headers (Content-Type, Authorization, Cache-Control, CORS headers)
- Cookies and session management
- HTTPS and TLS/SSL basics (encryption, certificates, TLS handshake overview)
- HTTP/1.1 vs HTTP/2 (multiplexing, server push, header compression)
- HTTP/3 and QUIC (awareness)

## Level 7: DNS

### Module: Domain Name System

#### Topic: DNS Resolution

- **Priority:** Category A
- **Prerequisites:** IP Addressing Level 4
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** The Complete Networking Fundamentals Course — David Bombal — Udemy
- **Completion Criteria:** Can explain DNS resolution step-by-step from browser cache to authoritative server; can describe DNS record types; can explain caching and TTL

**Subtopics:**
- DNS hierarchy (root, TLD, authoritative, recursive)
- DNS resolution process (recursive vs iterative queries)
- DNS record types (A, AAAA, CNAME, MX, NS, TXT, SOA)
- Caching at browser, OS, and resolver levels
- TTL and propagation
- DNS load balancing and failover basics

## Level 8: Web Communication Protocols

### Module: Modern Web Protocols

#### Topic: WebSockets & gRPC

- **Priority:** Category B
- **Prerequisites:** HTTP & HTTPS Level 6
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** ByteByteGo Free Articles — Free
- **Completion Criteria:** Can explain WebSockets vs HTTP polling vs Server-Sent Events; aware of gRPC as an alternative to REST; can describe when real-time communication is needed

**Subtopics:**
- WebSockets (full-duplex, persistent connection, handshake)
- HTTP polling, long polling, and Server-Sent Events (SSE)
- WebSocket use cases (chat, live updates, gaming)
- gRPC basics (HTTP/2, Protocol Buffers, unary, streaming) — awareness
- REST vs gRPC vs GraphQL (high-level comparison)

## Level 9: Routing & Infrastructure

### Module: Network Infrastructure

#### Topic: Routing & Load Balancing

- **Priority:** Category B
- **Prerequisites:** IP Addressing Level 4, TCP & UDP Level 5
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** GeeksforGeeks Computer Networks — Free
- **Completion Criteria:** Can explain distance-vector vs link-state routing at a high level; can describe common load balancer algorithms; aware of CDN purpose

**Subtopics:**
- Routing basics (static vs dynamic routing)
- Distance-vector routing (RIP) — basics
- Link-state routing (OSPF) — basics
- BGP (Border Gateway Protocol) — awareness
- Load balancer algorithms (round robin, least connections, IP hash, weighted)
- Reverse proxy vs load balancer
- CDN (Content Delivery Network) purpose and caching
- Reverse proxy (Nginx) role in backend deployment

## Level 10: Network Security

### Module: Security Fundamentals

#### Topic: Network Security Concepts

- **Priority:** Category A
- **Prerequisites:** HTTP & HTTPS Level 6
- **Recommended Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Gap Resource:** GeeksforGeeks Computer Networks — Free
- **Completion Criteria:** Can explain firewalls, SSL/TLS, and common network attacks; can explain CORS purpose and configuration from a networking perspective; can describe basic authentication vs bearer token transmission

**Subtopics:**
- Firewalls (packet-filtering, stateful, application layer)
- SSL/TLS certificate chain and trust model
- Common network attacks (DDoS, MITM, packet sniffing, IP spoofing)
- CORS (Cross-Origin Resource Sharing) — why it exists, preflight requests
- Authentication over HTTP (Basic Auth, Bearer tokens, cookies)
- VPN basics (tunneling, encryption) — awareness
- Network segmentation and DMZ — awareness

## Level 11: Practical Networking Tools

### Module: Network Diagnostics

#### Topic: Networking Tools

- **Priority:** Category A
- **Prerequisites:** Network Security Level 10
- **Recommended Resource:** The Complete Networking Fundamentals Course — David Bombal — Udemy
- **Gap Resource:** Computer Networks — Neso Academy — YouTube (Free)
- **Completion Criteria:** Can use `ping`, `traceroute`, `curl`, and browser dev tools to diagnose network issues; can inspect HTTP headers and status codes; aware of Wireshark for packet capture

**Subtopics:**
- `ping` and ICMP echo requests
- `traceroute` / `tracert` for path discovery
- `curl` for HTTP request testing
- `netstat` / `ss` for connection inspection
- Browser DevTools Network tab (headers, timing, waterfall)
- `nslookup` / `dig` for DNS queries
- Wireshark basics (packet capture, filtering) — awareness
- `tcpdump` basics — awareness
