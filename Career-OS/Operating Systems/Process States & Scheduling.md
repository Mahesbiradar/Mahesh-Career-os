# Process States & Scheduling + OS Basics (Operating Systems)

## Introduction to Operating System & its Functions (from Day 12)

### Why It Matters
- ⭐ **Why interviewers ask it**: OS is the “platform” that lets applications access hardware safely.
- **Production relevance**: CPU scheduling, memory management, filesystem, and I/O directly affect performance.
- **Backend relevance**: servers depend on OS for process/thread scheduling and device I/O.

### Core Concepts
#### What is an OS?
An **Operating System (OS)** is system software that acts as a **bridge between**:
- **applications** (your programs)
- **hardware** (CPU, memory, storage, devices)

Apps can’t safely control hardware directly, so the OS provides services for reliable execution.

#### Main OS functions (high level)
- **Process management**: create/schedule/terminate processes/threads
- **Memory management**: allocate RAM/virtual memory, isolate memory
- **File management**: organize files/directories, read/write data
- **CPU scheduling**: decide who runs next
- **I/O / device management**: handle disk/network/device operations
- **Security & resource control**: isolation and permissions

#### Why apps need the OS
- Safe access to hardware
- Enables multi-program and multi-user execution
- Prevents conflicts and crashes via isolation

### Interview Questions
**Basic**
1. What is an OS in one line?
2. Why can’t applications directly control hardware?

⭐ **Frequently Asked**
3. List 3 OS functions.

**Scenario-based**
4. If a server becomes slow, which OS responsibilities might be involved? (CPU scheduling, memory, disk I/O)

### Real Backend Usage
- **Linux/Windows**: networking stack, filesystem, process scheduling
- **Databases**: DB performance depends on OS disk/network I/O
- **Production systems**: OS manages contention and I/O waits

## Process States & Scheduling (from Day 13 theory)

### Why It Matters
- ⭐ **Why interviewers ask it**: It explains process lifecycle and CPU scheduling decisions.
- **Debugging**: “Why is my process slow/hung?” often maps to waiting vs running.

### Core Concepts
#### Process states (high level)
- **New**: created
- **Ready**: waiting in the queue for CPU
- **Running**: executing on CPU
- **Waiting / Blocked**: waiting for event/resource (I/O, lock, network)
- **Terminated**: done; resources released

#### Why the scheduler moves processes
The OS scheduler picks which **ready** process gets CPU time.
It moves processes due to events like:
- time slice end (preemption)
- I/O request (goes to waiting/blocked)
- I/O completion (back to ready)
- process exit (to terminated)

#### Ready vs Running vs Waiting
- **Ready**: eligible to run, waiting for CPU
- **Running**: currently using CPU
- **Waiting/Blocked**: paused for external work, not consuming CPU

### Important Rules
- Scheduling depends on **state + policies** (priority, fairness, time quantum).
- Waiting is not running.

### Diagram
```
          +--------+
          |  New   |
          +--------+
              |
              v
          +--------+      CPU slice ends / preempt
          | Ready  | <-----------------------------+
          +--------+                               |
              |                                     |
              v                                     |
          +---------+     I/O/lock/network wait   |
          | Running | ---------------------------->+
          +---------+                              
              |
              v
     +-------------------+
     | Waiting / Blocked |
     +-------------------+
              |
              v
          +--------+
          | Ready  |
          +--------+
```

### Revision Box
- [ ] New → Ready → Running
- [ ] Running can go to Waiting/Blocked due to I/O/resource needs
- [ ] Waiting/Blocked returns to Ready when event completes
- [ ] Terminated ends process lifecycle

### Submission Review (from Day 13 theory block)
- ✅ Good: you listed states and the idea of scheduler-driven transitions.
- ⚠ Needs improvement:
  - Keep “waiting/blocked” separate from “terminated”.
  - Describe scheduling as state transitions driven by events and policies.

### 30-Second Interview Revision
- Ready = waiting for CPU
- Running = executing on CPU
- Waiting/Blocked = paused for I/O/resource/event
- Terminated = done; resources freed
- Scheduler moves processes based on events + scheduling policy
