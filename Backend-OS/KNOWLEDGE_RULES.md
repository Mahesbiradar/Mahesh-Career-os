# Backend-OS — Knowledge Rules

> This file is read by the Notes Update agent (Prompt 3).
> It defines how Backend Engineering concepts should be organized, explained, and written in the notes/ folder.
> You never need to open this file manually.

---

## PURPOSE

The notes/ folder is your Backend Engineering knowledge base.
It grows as you study.
Every note file is a living document — it gets better each time you revisit a topic.

---

## CHAPTER ORGANIZATION

Organize Backend notes by concept. Never by lesson or day.

One file per topic. Example structure:

```
notes/
  Client-Server Architecture.md
  HTTP.md
  REST APIs.md
  Authentication.md
  JWT.md
  Django Basics.md
  Django ORM.md
  DRF Serializers.md
  Caching.md
  Deployment.md
```

Do not create unnecessary files.
If a new concept extends an existing topic, update that file.

---

## NOTE FILE STRUCTURE

Every note file should follow this structure:

```
# [Topic Name] (Backend Engineering)

## Why It Matters
- Why engineers build this
- What problem it solves in production

## Core Concept
- The engineering idea in plain English
- How it fits into the request-response lifecycle

## Architecture Diagram (if applicable)
[ASCII flow diagram]

## Implementation Pattern
[Code or config snippet — minimal, 5–10 lines max]

## Interview Questions
Basic / Intermediate / Scenario-based
Star (⭐) the most frequently asked ones

## Common Confusions ⚠
[Pairs of things that get mixed up]

## 30-Second Interview Revision
[5 bullet points — fastest possible recall]
```

---

## TEACHING PHILOSOPHY

Always explain in this order:
1. Problem that exists
2. Why this solution was designed
3. How it works architecturally
4. How it appears in production code
5. How interviewers ask about it

Never begin with code or framework syntax.
Always begin with engineering thinking.

---

## COMMON BACKEND CONFUSIONS (always watch for these)

- Authentication vs Authorization
- JWT vs Session
- REST vs HTTP
- PUT vs PATCH
- GET vs POST
- Monolith vs Microservices
- Cache vs Database
- Load Balancer vs Reverse Proxy
- Validation vs Authentication
- Business Logic vs Controller
- ORM vs SQL

---

## REQUEST LIFECYCLE PATTERN

Always connect concepts using the request lifecycle:

Browser → DNS → HTTP → Load Balancer → Reverse Proxy → Application Server → Authentication → Business Logic → Database / Cache → Response

Every Backend concept belongs somewhere in this flow.
Always identify where.

---

## QUALITY CHECKS

The notes have failed if:
- Backend is taught as framework syntax only
- Architecture diagrams are missing where helpful
- Production scenarios are absent
- Interview confusions are not addressed
- The request lifecycle is never referenced

The notes succeed when:
- The learner understands the engineering reason behind each concept
- The 30-Second Revision gives complete recall in under 30 seconds
- Common confusions are clearly resolved
- The concept is placed in the request lifecycle
