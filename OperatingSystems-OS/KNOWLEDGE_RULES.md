# OperatingSystems-OS — Knowledge Rules

> Read by the Notes Update agent. Defines how OS concepts are organized in notes/.

## CHAPTER ORGANIZATION
One file per OS concept. Never by lesson or day.

Example:
```
notes/
  Introduction to OS.md
  Processes.md
  Threads.md
  CPU Scheduling.md
  Synchronization.md
  Deadlock.md
  Memory Management.md
  Virtual Memory.md
  File Systems.md
```

## NOTE FILE STRUCTURE
```
# [Topic] (Operating Systems)

## Why It Matters
- What problem this OS mechanism solves
- Backend relevance

## Core Concept
- Plain English explanation
- What the OS is doing under the hood

## State Diagram / Flow (if applicable)
[ASCII diagram]

## Real-World Example
[Concrete example: opening Chrome, downloading a file, etc.]

## Backend Engineering Connection
[How this OS concept affects backend applications]

## Interview Questions
⭐ most frequently asked

## Common Confusions ⚠
- Process vs Thread
- Ready vs Waiting vs Blocked
- Semaphore vs Mutex
- Paging vs Segmentation
- Deadlock vs Starvation

## 30-Second Interview Revision
[5 bullet points]
```

## TEACHING STYLE
- What → Why → How → Real system example → Backend relevance → Interview perspective
- Never start with definitions alone
- OS should feel like the invisible software making backend possible
- Use diagrams whenever it improves understanding (process states, scheduling queues)

## QUALITY CHECK
Failed if: topics are just definitions, no real examples, no backend connection, diagrams missing.
Succeeds when: learner understands why each OS mechanism exists, not just what it is.
