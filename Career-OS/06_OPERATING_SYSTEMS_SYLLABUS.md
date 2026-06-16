# Operating Systems Syllabus — Mahesh Career OS

> **Goal:** Master OS theory for software engineering interviews + Linux practical skills for backend deployment.
> **Focus:** Interview preparation with practical Linux as a secondary layer.
> **Scope:** Processes, threads, scheduling, memory, synchronization, deadlocks, virtual memory.

---

## Why OS Theory Matters for Software Engineers

OS is not about writing device drivers. For software engineers, OS knowledge explains:
- Why concurrent code has race conditions (scheduling, preemption)
- Why you need thread locks (critical sections)
- Why programs crash with out-of-memory errors (virtual memory)
- Why some operations are expensive (context switching, page faults)
- Why databases use fsync (durability)
- How Docker containers work (processes, namespaces, cgroups)

Every product company interview includes OS questions. FAANG interviews treat OS as a core competency.

---

## Level Structure

| Level | Topic | Interview Weight |
|-------|-------|----------------|
| Level 1 | OS Foundations | Medium |
| Level 2 | Processes | Critical |
| Level 3 | Threads | Critical |
| Level 4 | CPU Scheduling | High |
| Level 5 | Process Synchronization | Critical |
| Level 6 | Deadlocks | Critical |
| Level 7 | Memory Management | Critical |
| Level 8 | Virtual Memory | High |
| Level 9 | File Systems | Medium |
| Level 10 | Linux Practical | High (for backend developers) |

---

## Level 1 — OS Foundations

---

### 1.1 What is an Operating System

- **Why It Matters:** Defines what problem OS solves and sets up the mental model for everything else.
- **Prerequisites:** None
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- OS as a resource manager (CPU, memory, I/O, storage)
- OS as an abstraction layer
- OS roles: resource allocator, control program, kernel
- Types of OS:
  - Batch OS
  - Time-sharing (Multiprogramming) OS
  - Real-Time OS (RTOS)
  - Distributed OS
  - Embedded OS
- OS examples: Linux, Windows, macOS, Android

---

### 1.2 System Calls

- **Why It Matters:** System calls are how programs interact with the OS. Every file read, network socket, and process creation is a system call.
- **Prerequisites:** 1.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- User mode vs Kernel mode (privilege separation)
- Mode switch (trap instruction)
- System call categories:
  - Process control (fork, exec, exit, wait)
  - File management (open, read, write, close)
  - Device management (ioctl)
  - Information maintenance (getpid, alarm)
  - Communication (pipe, socket, mmap)
- System call overhead (context switch to kernel mode)
- Wrapper functions (libc wraps raw system calls)

---

### 1.3 OS Architecture

- **Why It Matters:** Architecture decisions affect extensibility, performance, and security.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium
- **Job Importance:** Low-Medium

Topics:
- **Monolithic Kernel:** entire OS in kernel space (Linux, traditional Unix)
  - Pro: fast (no IPC between components)
  - Con: large, any module crash crashes OS
- **Microkernel:** minimal kernel; most services in user space (QNX, Minix)
  - Pro: modular, stable, secure
  - Con: slower (IPC overhead)
- **Hybrid Kernel:** macOS XNU, Windows NT
- **Exokernel** (conceptual)
- **Hypervisor / VMM:** Type 1 (bare metal) vs Type 2 (hosted)

---

### 1.4 Interrupts & I/O

- **Why It Matters:** Understanding how hardware communicates with software explains async I/O, event loops, and system responsiveness.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- Hardware interrupts (keyboard, disk, network)
- Software interrupts (system calls, exceptions)
- Interrupt Service Routines (ISR)
- I/O techniques:
  - Polling (CPU constantly checks) — CPU wasteful
  - Interrupt-Driven I/O (hardware notifies CPU)
  - DMA (Direct Memory Access) — hardware transfers without CPU
- I/O scheduler (disk scheduling)
- Buffering, Caching, Spooling

---

## Level 2 — Processes

---

### 2.1 Process Concept

- **Why It Matters:** A process is the fundamental unit of execution. Understanding processes is prerequisite to everything in OS.
- **Prerequisites:** Level 1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Process definition: program in execution (program is passive, process is active)
- Process vs Program
- Process components: code (text), data, stack, heap
- **Process Control Block (PCB):**
  - Process ID (PID)
  - Process state
  - CPU registers
  - Memory limits
  - I/O status
  - Scheduling info
  - Accounting info
- Process lifecycle

---

### 2.2 Process States

- **Why It Matters:** State transitions explain why processes are blocked, runnable, or running at any given time.
- **Prerequisites:** 2.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- **New:** process being created
- **Ready:** waiting for CPU assignment
- **Running:** instructions being executed
- **Blocked/Waiting:** waiting for I/O or event
- **Terminated:** finished execution
- State transition diagram (key transitions: new→ready, ready→running, running→ready, running→blocked, blocked→ready, running→terminated)
- Suspend states (ready-suspended, blocked-suspended)

---

### 2.3 Process Creation

- **Why It Matters:** Understanding fork/exec explains how shells work, how Docker containers start, and how web servers spawn workers.
- **Prerequisites:** 2.2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- **fork():** creates exact copy of parent process
  - Parent and child execute independently
  - Returns PID of child to parent, 0 to child
  - Copy-on-Write (COW) optimization
- **exec():** replaces process image with new program
  - Does not create new process
  - Combines with fork: fork + exec = new process running new program
- **wait():** parent waits for child to terminate
- **exit():** process terminates
- Process tree (init/systemd as root)
- Orphan processes (parent died before child)
- Zombie processes (child died but parent hasn't called wait)

---

### 2.4 Inter-Process Communication (IPC)

- **Why It Matters:** Microservices communicate. Background workers receive jobs. All IPC mechanisms.
- **Prerequisites:** 2.3
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- **Shared Memory:** fastest IPC; processes share memory region
  - Requires synchronization (semaphores)
  - `shmget`, `shmat` (POSIX)
- **Message Passing:** processes exchange messages without shared memory
  - Send and Receive primitives
  - Direct vs Indirect communication
  - Synchronous vs Asynchronous
- **Pipes:** unidirectional byte stream
  - Anonymous pipes (parent-child only)
  - Named pipes (FIFOs) — any two processes
- **Signals:** asynchronous notifications (SIGTERM, SIGKILL, SIGUSR1)
- **Sockets:** network or local IPC
- **Memory-Mapped Files:** file mapped into address space

---

## Level 3 — Threads

---

### 3.1 Thread Concept

- **Why It Matters:** Modern applications are multi-threaded. Web servers, databases, GUI applications all use threads.
- **Prerequisites:** Level 2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Thread definition: lightweight unit of execution within a process
- Process vs Thread:
  - Threads share: code, data, heap, open files, signals
  - Threads have own: stack, registers, program counter, thread ID
- Benefits of multithreading:
  - Responsiveness (UI thread stays responsive)
  - Resource sharing (cheaper than IPC)
  - Economy (thread creation cheaper than process)
  - Scalability (utilize multiple CPUs)
- Context switching cost: thread << process

---

### 3.2 Thread Models

- **Why It Matters:** Understanding thread models explains why Python's GIL exists and why Node.js uses a different approach.
- **Prerequisites:** 3.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- **User-Level Threads (ULT):** managed by runtime, OS unaware
  - Fast context switch (no kernel involvement)
  - Con: blocking system call blocks all threads
  - Example: green threads, goroutines (partially)
- **Kernel-Level Threads (KLT):** managed by OS
  - OS sees and schedules individual threads
  - Con: slower context switch
  - Example: Java threads, Python threads (via pthreads)
- **Threading Models:**
  - Many-to-One: many ULTs → one KLT (old)
  - One-to-One: one ULT → one KLT (Linux pthreads, Windows)
  - Many-to-Many: many ULTs → many KLTs
  - Two-Level (combines M:M and 1:1)

---

### 3.3 POSIX Threads (pthreads)

- **Why It Matters:** Linux threads use pthreads. Python's threading module wraps pthreads.
- **Prerequisites:** 3.2
- **Interview Importance:** Medium
- **Job Importance:** Medium-High

Topics:
- Thread creation: `pthread_create()`
- Thread join: `pthread_join()` (wait for thread)
- Thread detachment: `pthread_detach()`
- Thread termination: `pthread_exit()`
- Thread attributes (stack size, scheduling)
- Thread-local storage (TLS)

---

### 3.4 Thread Safety

- **Why It Matters:** Concurrent bugs (race conditions, data corruption) are caused by not writing thread-safe code.
- **Prerequisites:** 3.3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Thread-safe code: safe to call from multiple threads simultaneously
- Reentrant functions (safe even with concurrent calls)
- Non-reentrant pitfalls: global state, static variables
- Thread-safe data structures
- Immutable data (inherently thread-safe)
- Atomic operations

---

## Level 4 — CPU Scheduling

---

### 4.1 Scheduling Concepts

- **Why It Matters:** Scheduling determines system responsiveness, throughput, and fairness.
- **Prerequisites:** Level 2
- **Interview Importance:** High
- **Job Importance:** Medium

Topics:
- **CPU Burst:** phase where process uses CPU
- **I/O Burst:** phase where process waits for I/O
- CPU-bound vs I/O-bound processes
- Scheduling queues: Job queue, Ready queue, Device queue
- Schedulers:
  - Long-term (job scheduler): decides which processes enter ready queue
  - Short-term (CPU scheduler): decides which ready process gets CPU next
  - Medium-term (swapper): swaps processes in/out of memory
- Scheduling criteria:
  - CPU utilization (maximize)
  - Throughput (maximize)
  - Turnaround time (minimize)
  - Waiting time (minimize)
  - Response time (minimize)
- Preemptive vs Non-preemptive scheduling

---

### 4.2 Scheduling Algorithms

- **Why It Matters:** Classic interview question — compare algorithms with metrics. Know time calculations.
- **Prerequisites:** 4.1
- **Interview Importance:** Critical
- **Job Importance:** Medium

Topics:

**First-Come, First-Served (FCFS):**
- Non-preemptive
- Simple, but convoy effect (short processes wait behind long ones)
- Gantt chart calculation

**Shortest Job First (SJF):**
- Non-preemptive version (SSNF)
- Preemptive version = Shortest Remaining Time First (SRTF)
- Optimal for minimizing average waiting time
- Problem: requires knowing burst time in advance (predict from history)

**Priority Scheduling:**
- Each process has priority; highest priority first
- Preemptive and non-preemptive versions
- Problem: starvation of low-priority processes
- Solution: Aging (gradually increase priority)

**Round Robin (RR):**
- Time quantum (time slice): each process gets fixed time slice
- After quantum expires, process goes to back of ready queue
- Balance: small quantum = responsive, large quantum = approaches FCFS
- Default for time-sharing systems

**Multilevel Queue:**
- Multiple queues, each with different algorithm
- Foreground (interactive) vs Background (batch)
- Fixed priority or time slice between queues

**Multilevel Feedback Queue:**
- Processes can move between queues based on behavior
- Most general; used in most modern OSes
- I/O bound processes rise to high-priority queues

---

### 4.3 Context Switching

- **Why It Matters:** Context switches have real overhead. They explain why too many threads hurts performance.
- **Prerequisites:** 4.2
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Saving/restoring process state (PCB)
- Context switch cost (time during which no useful work is done)
- Factors affecting context switch cost
- Thread context switch vs Process context switch (thread is cheaper)
- Voluntary vs involuntary context switch
- `vmstat` and `perf` for measuring context switches

---

## Level 5 — Process Synchronization

> *This is the most tested OS topic for software engineers. Race conditions, locks, semaphores — all come from here.*

---

### 5.1 Race Conditions

- **Why It Matters:** Race conditions cause intermittent, hard-to-reproduce bugs. They're the main reason concurrent programming is hard.
- **Prerequisites:** Level 3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Race condition definition: outcome depends on interleaving of concurrent operations
- Example: `count++` is not atomic (read-modify-write)
- Shared resource
- Non-deterministic execution
- How to detect: stress testing, tools (ThreadSanitizer)

---

### 5.2 Critical Section Problem

- **Why It Matters:** The critical section problem is the formal statement of the race condition problem and its solution requirements.
- **Prerequisites:** 5.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Critical section: code segment that accesses shared data
- Requirements for a correct solution:
  1. **Mutual Exclusion:** only one process in critical section at a time
  2. **Progress:** if no process is in critical section, one should be able to enter
  3. **Bounded Waiting:** a process must be able to enter within bounded time (no starvation)
- Peterson's Solution (software solution for 2 processes)
- Hardware support:
  - `test_and_set` instruction (atomic)
  - `compare_and_swap` (CAS) instruction (atomic)
  - Memory barriers/fences

---

### 5.3 Mutex Locks

- **Why It Matters:** Mutex is the basic building block for thread synchronization. Every language's threading library has mutexes.
- **Prerequisites:** 5.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Mutex definition: binary lock (locked/unlocked)
- `acquire()` (lock) and `release()` (unlock) operations
- Spinlock vs sleep lock (busy waiting vs block)
- Busy waiting (spinlock) — wastes CPU but no context switch
- Sleep lock — yields CPU but has overhead
- When to use spinlock (short waits, SMP systems) vs sleep lock
- Recursive mutex
- `pthread_mutex_t`
- Python's `threading.Lock`

---

### 5.4 Semaphores

- **Why It Matters:** Semaphores generalize mutexes. They're used for resource counting, signaling between threads.
- **Prerequisites:** 5.3
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- Semaphore definition: integer variable with two atomic operations
  - `wait()` / `P()` / `down()`: decrement, block if < 0
  - `signal()` / `V()` / `up()`: increment, wake blocked process
- **Binary Semaphore:** value 0 or 1 (same as mutex)
- **Counting Semaphore:** value can be any non-negative integer (resource counting)
- Semaphore implementation (with wait queue to avoid busy waiting)
- Semaphore vs Mutex (mutex has ownership; semaphore doesn't)
- Python's `threading.Semaphore`

---

### 5.5 Classic Synchronization Problems

- **Why It Matters:** These problems are the canonical tests for synchronization correctness. Interviewers use them to test deep understanding.
- **Prerequisites:** 5.4
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:

**Bounded Buffer / Producer-Consumer:**
- Producer adds to buffer, Consumer removes from buffer
- Buffer has limited capacity
- Solution: two semaphores (empty count, full count) + one mutex
- Python: `queue.Queue` is thread-safe implementation

**Readers-Writers Problem:**
- Multiple readers can read simultaneously
- Writers need exclusive access
- First solution: readers priority (writers may starve)
- Second solution: writers priority (readers may starve)
- Fair solution using monitors or timestamps
- Read-write locks: `threading.RWLock`

**Dining Philosophers Problem:**
- 5 philosophers, 5 forks; each needs 2 forks to eat
- Demonstrates deadlock (all pick up left fork, none can pick up right)
- Solutions: resource ordering, arbitrator (waiter), limit concurrency
- Chandy/Misra solution

---

### 5.6 Monitors

- **Why It Matters:** Monitors are the high-level synchronization construct. Java's `synchronized`, Python's `with lock:` implement monitor concepts.
- **Prerequisites:** 5.4
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Monitor definition: ADT with mutex and condition variables
- Condition variables: `wait()` and `signal()`
- `wait()`: release monitor lock, block until notified
- `signal()`: wake one waiting thread (signal-and-continue vs signal-and-wait)
- Java `synchronized` keyword and `wait()`/`notify()`
- Python `threading.Condition`
- Mesa vs Hoare semantics (spurious wakeups)
- Why `while` (not `if`) when waiting on condition

---

## Level 6 — Deadlocks

---

### 6.1 Deadlock Conditions

- **Why It Matters:** Deadlocks bring systems to a halt. This is the most tested topic after race conditions.
- **Prerequisites:** Level 5
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Deadlock definition: set of processes each waiting for a resource held by another in the set — circular wait
- **Four Necessary Conditions (Coffman Conditions) — all must hold for deadlock:**
  1. **Mutual Exclusion:** resources cannot be shared
  2. **Hold and Wait:** process holds at least one resource while waiting for others
  3. **No Preemption:** resources cannot be forcibly taken; only voluntarily released
  4. **Circular Wait:** circular chain of processes each waiting for the next
- All four conditions are necessary and jointly sufficient

---

### 6.2 Resource Allocation Graph (RAG)

- **Why It Matters:** RAG is how deadlocks are visualized and detected. Interviewers draw RAGs to test understanding.
- **Prerequisites:** 6.1
- **Interview Importance:** High
- **Job Importance:** Medium

Topics:
- RAG components:
  - Processes: circles
  - Resources: rectangles (dots inside = instances)
  - Request edge: process → resource
  - Assignment edge: resource → process
- Cycle detection in RAG:
  - Single instance per resource: cycle = deadlock
  - Multiple instances: cycle = possible deadlock (need further analysis)
- Reduction algorithm for multi-instance resources

---

### 6.3 Deadlock Handling Strategies

- **Why It Matters:** OS courses teach all four strategies. Interviewers test whether you know when each is used.
- **Prerequisites:** 6.2
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:

**1. Deadlock Prevention (break one Coffman condition):**
- Break Mutual Exclusion: make resources sharable (not always possible)
- Break Hold and Wait: request all resources at once (low utilization) or release before requesting more
- Break No Preemption: allow preemption (rollback; practical for CPU, memory; not for printers)
- Break Circular Wait: impose ordering on resources; always request in order

**2. Deadlock Avoidance (dynamically check if safe):**
- Safe state: there exists a sequence in which all processes can complete
- Unsafe state: may or may not lead to deadlock
- **Banker's Algorithm:**
  - Each process declares maximum resource needs
  - OS grants request only if system remains in safe state
  - Safety algorithm: check if safe state exists
  - Resource-request algorithm: check if specific request can be granted
  - Limitation: processes must declare max in advance (impractical)

**3. Deadlock Detection & Recovery:**
- Allow deadlocks to occur; periodically run detection algorithm
- Detection: cycle detection in wait-for graph
- Recovery options:
  - Process termination (abort one or all deadlocked processes)
  - Resource preemption (take resource from process, rollback)
  - Victim selection (minimize cost)

**4. Deadlock Ignorance:**
- Ostrich algorithm: pretend deadlocks don't happen
- Most OS (Linux, Windows) use this — rare deadlocks not worth the overhead
- Application is responsible for recovering

---

## Level 7 — Memory Management

---

### 7.1 Memory Hierarchy

- **Why It Matters:** Memory hierarchy explains caching, speed-cost tradeoffs, and why memory management is needed.
- **Prerequisites:** Level 1
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Registers → L1 cache → L2 cache → L3 cache → Main Memory → SSD → HDD
- Speed, size, cost tradeoffs at each level
- Cache lines and spatial locality
- Temporal locality
- Cache hit vs cache miss
- Cache coherence in multiprocessors

---

### 7.2 Contiguous Memory Allocation

- **Why It Matters:** Foundation for understanding fragmentation and why paging was invented.
- **Prerequisites:** 7.1
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- Single-partition allocation
- Fixed-partition multiprogramming
- Variable-partition multiprogramming
- Allocation strategies:
  - **First Fit:** first hole large enough
  - **Best Fit:** smallest hole that fits
  - **Worst Fit:** largest hole
- **External Fragmentation:** total free memory enough but not contiguous
- **Internal Fragmentation:** allocated memory larger than needed
- Compaction to reduce fragmentation (expensive)

---

### 7.3 Paging

- **Why It Matters:** Paging is the dominant memory management technique. Page faults, TLB, and page tables are interview staples.
- **Prerequisites:** 7.2
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- Paging concept: divide physical memory into fixed frames, logical memory into pages
- Page size (typically 4KB)
- Page table: maps logical page number → physical frame number
- Logical address = page number (p) + offset (d)
- Physical address = frame number (f) + offset (d)
- Page table entry contents (frame number, valid bit, dirty bit, reference bit)
- **Internal fragmentation** (last page may not be full)
- No external fragmentation
- **Translation Lookaside Buffer (TLB):**
  - Hardware cache for page table entries
  - TLB hit vs TLB miss
  - TLB reach and coverage
  - Effective Access Time (EAT) calculation
- Multi-level page tables (reduce memory for page table itself)
- Inverted page table (one entry per physical frame)

---

### 7.4 Segmentation

- **Why It Matters:** Segmentation provides logical view of memory (code, stack, heap as separate segments).
- **Prerequisites:** 7.3
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- Segment: logically related unit (code, stack, heap, data)
- Segment table: segment number → (base, limit) pair
- Logical address = segment number + offset
- Hardware: Segment Table Base Register (STBR)
- External fragmentation (segments vary in size)
- Segmentation with paging (modern approach)
- x86 segmentation (legacy CS/DS/SS segments)

---

## Level 8 — Virtual Memory

---

### 8.1 Virtual Memory Concept

- **Why It Matters:** Virtual memory allows programs larger than physical memory. It's the foundation of modern OS memory management.
- **Prerequisites:** Level 7
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- Virtual memory concept: each process has illusion of its own large address space
- Virtual address space vs physical address space
- Separation of virtual and physical addresses
- Benefits:
  - Programs can be larger than physical memory
  - Process isolation (can't access other process's memory)
  - Memory-mapped files
  - Sharing libraries (same physical frames mapped to multiple virtual spaces)
- Demand paging: load pages only when needed
- **Page Fault:** accessed page not in physical memory
- Page fault handling: OS loads page from disk

---

### 8.2 Demand Paging

- **Why It Matters:** Demand paging explains lazy loading and why applications start fast even when large.
- **Prerequisites:** 8.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Lazy loading: bring page to memory only when accessed
- Valid-Invalid bit in page table
- Page fault procedure:
  1. Access page → check valid bit
  2. Invalid → page fault trap
  3. OS checks if access is legitimate
  4. Find free frame (or evict a page)
  5. Load page from backing store (disk)
  6. Update page table
  7. Restart instruction
- Pure demand paging: start with no pages in memory
- Locality of reference: reason demand paging works well
- Effective Access Time with demand paging

---

### 8.3 Page Replacement Algorithms

- **Why It Matters:** When all frames are full, a page must be evicted. The algorithm determines which one.
- **Prerequisites:** 8.2
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:

**Optimal (OPT / Bélády's):**
- Evict page not used for longest time in future
- Not implementable (requires future knowledge)
- Used as benchmark for comparison

**First-In-First-Out (FIFO):**
- Evict oldest page (in memory longest)
- Simple to implement (queue of frames)
- **Bélády's Anomaly:** more frames can cause more page faults (counter-intuitive)

**Least Recently Used (LRU):**
- Evict page not used for longest time in past
- Good approximation of optimal
- Implementation: counter/timestamp per page, or stack
- No Bélády's anomaly
- Expensive exact implementation; approximations used

**LRU Approximations:**
- **Second-Chance (Clock Algorithm):** FIFO + reference bit; if reference bit set, clear and give second chance
- **Enhanced Clock Algorithm:** uses (reference, dirty) bits

**Most Recently Used (MRU):** evict most recently used (useful for some access patterns)

**Comparison metrics:**
- Page fault rate for given reference string and frame count
- Calculation of page faults for each algorithm (Gantt chart style)

---

### 8.4 Frame Allocation

- **Why It Matters:** Allocating too few frames causes thrashing; too many wastes memory.
- **Prerequisites:** 8.3
- **Interview Importance:** Medium-High
- **Job Importance:** Medium

Topics:
- Minimum frames: based on instruction set requirements
- Fixed allocation: equal or proportional to process size
- Priority allocation: more frames to higher-priority processes
- Global vs Local replacement:
  - Global: can take frames from any process
  - Local: can only use own allocated frames
- Working set model

---

### 8.5 Thrashing

- **Why It Matters:** Thrashing is a production emergency symptom. Understanding it helps diagnose and prevent it.
- **Prerequisites:** 8.4
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Thrashing: process spends more time paging than executing
- Cause: too many processes, not enough frames for working sets
- Symptoms: CPU utilization drops, page fault rate spikes
- Detection: high page fault rate + low CPU utilization
- **Working Set Model:**
  - Working set: set of pages actively used in recent Δ time window
  - If total working sets > total frames → thrashing
- Prevention: reduce degree of multiprogramming, add more memory
- Linux OOM (Out-of-Memory) killer

---

## Level 9 — File Systems

---

### 9.1 File System Concepts

- **Why It Matters:** File systems are how all persistent data is stored. Understanding them helps debug I/O issues.
- **Prerequisites:** Level 7
- **Interview Importance:** Medium
- **Job Importance:** Medium-High

Topics:
- File: named collection of related data (OS perspective)
- File attributes: name, type, size, location, permissions, timestamps
- File operations: create, open, read, write, seek, close, delete
- File types: regular, directory, symbolic link, device file
- Access methods: sequential, direct (random), indexed
- Directory structure: flat, two-level, tree, acyclic graph, general graph
- Path: absolute vs relative
- File system mounting

---

### 9.2 File System Implementation

- **Why It Matters:** i-nodes explain how Linux represents files. Understanding this helps with permissions, hard links, and symbolic links.
- **Prerequisites:** 9.1
- **Interview Importance:** Medium-High
- **Job Importance:** Medium

Topics:
- Disk structure: blocks, boot block, superblock, data blocks
- **inode (index node):**
  - Stores file metadata (size, permissions, timestamps, ownership)
  - Contains pointers to data blocks
  - Direct, indirect, double-indirect, triple-indirect pointers
- File vs inode (multiple hard links → multiple names for same inode)
- **Hard link vs Symbolic link:**
  - Hard link: another name for same inode
  - Symbolic link: file containing path to another file (like a shortcut)
- Directory entry: maps filename to inode number
- Free space management: bitmaps, linked list

---

## Level 10 — Linux Practical

---

### 10.1 Linux File System Hierarchy

- **Why It Matters:** Backend developers constantly work on Linux servers. Knowing where things live is a prerequisite.
- **Prerequisites:** 9.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `/` — root
- `/bin` — essential binaries
- `/etc` — configuration files
- `/home` — user home directories
- `/var` — variable data (logs, databases)
- `/tmp` — temporary files
- `/usr` — user programs and libraries
- `/opt` — optional/third-party software
- `/proc` — virtual filesystem (process info)
- `/sys` — virtual filesystem (kernel/hardware info)
- `/dev` — device files

---

### 10.2 Essential Commands

- **Why It Matters:** Daily Linux usage. Backend developers use these constantly.
- **Prerequisites:** 10.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Categories:
- **Navigation:** `ls`, `cd`, `pwd`, `find`
- **File Operations:** `cp`, `mv`, `rm`, `mkdir`, `rmdir`, `touch`
- **File Content:** `cat`, `less`, `more`, `head`, `tail`, `wc`
- **Search:** `grep`, `grep -r`, `grep -E`, `awk`, `sed`
- **Permissions:** `chmod`, `chown`, `chgrp`, `umask`
- **Processes:** `ps`, `top`, `htop`, `kill`, `killall`, `nice`, `renice`
- **Disk:** `df`, `du`, `lsblk`
- **Network:** `ping`, `curl`, `wget`, `netstat`, `ss`, `nslookup`, `dig`
- **Archives:** `tar`, `gzip`, `zip`
- **Other:** `echo`, `env`, `export`, `which`, `man`, `history`, `alias`

---

### 10.3 File Permissions

- **Why It Matters:** Permission errors are among the most common Linux issues backend developers encounter.
- **Prerequisites:** 10.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Permission model: Owner, Group, Others
- Permission types: Read (r=4), Write (w=2), Execute (x=1)
- Octal notation: `chmod 755 file` (rwxr-xr-x)
- Symbolic notation: `chmod u+x file`
- `chown user:group file`
- `setuid`, `setgid`, `sticky bit`
- Directory permissions (execute = enter directory)
- `umask` — default permission subtraction

---

### 10.4 Process Management in Linux

- **Why It Matters:** Monitoring and managing processes on production servers.
- **Prerequisites:** Level 2, 10.2
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `ps aux` — all processes with details
- `top` / `htop` — interactive process viewer
- PID, PPID, PGID, SID
- Signals: `SIGTERM` (15, graceful), `SIGKILL` (9, force), `SIGHUP` (1, reload)
- `kill -15 PID`, `kill -9 PID`
- `nohup command &` — run in background, immune to hangup
- `jobs`, `fg`, `bg` — job control
- `nice` / `renice` — process priority
- `systemd` — service management (`systemctl start/stop/status/enable`)
- `journalctl` — systemd logs
- `/proc/PID/` — process information files

---

### 10.5 Shell Scripting Basics

- **Why It Matters:** Automation, deployment scripts, cron jobs — all require shell scripting.
- **Prerequisites:** 10.2
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Shebang: `#!/bin/bash`
- Variables: `VAR="value"`, `$VAR`
- Command substitution: `$(command)`
- Arithmetic: `$((expr))`
- Conditional: `if [ condition ]; then ... fi`
- Loops: `for item in list; do ... done`, `while [ condition ]; do ... done`
- Functions
- Exit codes: `$?`, `exit 0`, `exit 1`
- Redirection: `>`, `>>`, `<`, `2>`, `2>&1`
- Pipes: `command1 | command2`
- Common patterns in deployment scripts

---

*This is the knowledge inventory for Operating Systems. Roadmap and scheduling are managed separately.*
