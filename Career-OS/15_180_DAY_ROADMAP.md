# Mahesh Career OS — 180-Day Strategic Roadmap

> **File:** `15_180_DAY_ROADMAP.md`
> **Version:** 1.0
> **Depends On:** `12_MASTERY_FRAMEWORK.md`, `13_SYSTEM_SIMPLIFICATION_RULES.md`, all syllabus files (02–11)
> **Purpose:** Define the strategic arc from current state (strong telecom professional, weak engineering fundamentals) to employment-ready software engineer at 6–8 LPA.
> **Authority:** This file governs phase sequencing and milestone priorities. Daily/weekly execution is governed by `13_SYSTEM_SIMPLIFICATION_RULES.md`. Mastery standards are governed by `12_MASTERY_FRAMEWORK.md`.

---

## Starting Position

| Dimension | Current State |
|-----------|--------------|
| Domain experience | 8+ years telecom (network ops, systems thinking, project delivery) |
| Software projects built | Multiple AI-assisted: Library, ILAS, AgriSakhi, Blinkit Logistics, Hari Tours, Digital Retail |
| Business understanding | Strong — can reason about systems, trade-offs, user needs |
| Engineering fundamentals | Weak — conceptual gaps in CS theory, implementation depth thin |
| AI dependency | High — projects built with AI assistance; independent implementation not yet proven |
| DSA | Managed in separate DSA-System; treated as external parallel track |
| All 10 Career OS domains | Start at ML-0 to ML-1 (AI-assisted familiarity does not count as mastery) |

**What this means for the roadmap:**
- No slow ramp-up phase. Start all domains in Month 1.
- Projects already built are context, not credentials — they become interview stories after evaluation confirms understanding.
- AI dependency must trend downward each month. The roadmap enforces this structurally.
- The telecom background is a genuine differentiator for backend systems, networking, and system reliability topics. Leverage it.

---

## The 180-Day Arc

```
DAY 1                DAY 30              DAY 75              DAY 120
  │                    │                   │                    │
  ▼                    ▼                   ▼                    ▼
[PHASE 1]         [PHASE 2]           [PHASE 3]           [PHASE 4]
IGNITION          CORE DEPTH          INTEGRATION         INTERVIEW PREP
                                                               │
                                                          DAY 150
                                                               │
                                                               ▼
                                                          [PHASE 5]
                                                         OFFER MODE
                                                               │
                                                          DAY 180
                                                               │
                                                               ▼
                                                        EMPLOYMENT OFFER
```

```
CRS TRAJECTORY:
Day 1    →   Day 30   →   Day 75   →   Day 120  →   Day 150  →   Day 180
 ~0%          ~15%         ~35%          ~55%          ~62%          ≥65%
[Starting]  [Seeded]   [Building]    [Near Gate]  [Applying]   [Offer Ready]
```

---

## Section 1 — Phase Architecture

### Phase 1: Ignition (Days 1–30)

**Theme:** Touch every domain. Build the study habit. Prove the first Django app works.

**Strategic Intent:**
Most learners spend Month 1 on one domain. Mahesh cannot afford that. Every domain must be seeded in Phase 1 because later phases require all 10 domains running in parallel. The goal here is breadth over depth — reach ML-2 or ML-3 across everything before drilling deep into anything.

**Phase 1 Objectives:**

| Domain | Target by End of Phase 1 | Key Topics to Cover |
|--------|--------------------------|---------------------|
| Python | ML-3 on Levels 1–3 | Syntax, data types, data structures, functions, modules |
| Backend Engineering | ML-2 on Tiers 1–3 | Internet basics, HTTP, API concepts, Django project setup |
| SQL | ML-3 on Levels 1–5 | SELECT, WHERE, GROUP BY, all JOIN types, basic aggregations |
| DBMS | ML-2 on Foundations + ER Modeling | Database concepts, ER diagrams, basic relational model |
| Operating Systems | ML-2 on Foundations + Processes | OS role, process vs. thread concept, basic scheduling |
| Computer Networks | ML-2 on Foundations + OSI Model | OSI layers, TCP/IP stack, basic IP addressing |
| Frontend | ML-3 on HTML + CSS + JS Core | Semantic HTML, CSS layout (Flexbox, Grid), JS variables/functions/arrays |
| Cloud & Deployment | ML-3 on Linux + Git | Basic Linux commands, Git workflow, GitHub repo management |
| Communication | ML-2 on Spoken English baseline | Daily 15-minute speaking practice, technical term pronunciation |
| Job Preparation | ML-1 (awareness only) | Understand the job market, browse 20 job descriptions |

**Phase 1 Completion Criteria:**
- [ ] Working Django + PostgreSQL application running locally (any simple CRUD app)
- [ ] Git workflow established: all code committed to a GitHub repo from Day 1
- [ ] SQL: can write any JOIN without looking up syntax
- [ ] Communication: can introduce yourself and describe one project in 90 seconds without hesitation
- [ ] Study routine established: 6 hours daily with daily log filed

**Phase 1 Warning Signs (if these occur, escalate immediately):**
- Django not set up and running by Day 10 → Block all other backend work until resolved
- No GitHub commits by Day 7 → Rebuild Git habit before continuing
- Study hours averaging < 4/day → Diagnose root cause before Phase 2 begins

---

### Phase 2: Core Depth (Days 31–75)

**Theme:** Python and Backend reach professional competence. First ML-4 topics confirmed.

**Strategic Intent:**
Python and Backend Engineering carry 38% of the CRS together. If these two domains do not reach solid ML-4 on their core topics by Day 75, the CRS target at Day 180 becomes mathematically very difficult. This phase is the most important single phase in the roadmap. Everything else is support.

**Phase 2 Objectives:**

| Domain | Target by End of Phase 2 | Key Topics to Cover |
|--------|--------------------------|---------------------|
| Python | ML-4 on Levels 1–6 (~33 topics at ML-4+) | OOP (full), Decorators, Context Managers, Comprehensions, Error Handling, Generators, Type Hints |
| Backend Engineering | ML-4 on Tiers 1–5 (~30 topics at ML-4+) | Django MVT deep dive, Models + ORM, Views + URLs, DRF serializers, ViewSets, Routers, JWT Auth |
| SQL | ML-4 on Levels 1–9 (~40 topics at ML-4+) | Window functions, CTEs, Subqueries, Indexes (B-tree), DDL, Transactions + ACID |
| DBMS | ML-3 on 60% of topics | Normalization (1NF–BCNF), B+ Tree, ACID deep dive, Concurrency basics |
| Operating Systems | ML-3 on Levels 1–5 | Processes + PCB, Threads + POSIX, CPU scheduling algorithms, Synchronization primitives |
| Computer Networks | ML-3 on Levels 1–5 | TCP vs UDP deep dive, HTTP/HTTPS full, TLS handshake, DNS |
| Frontend | ML-4 on Levels 1–7 (~30 topics at ML-4+) | JS DOM, Events, Closures, Promises/async-await, React fundamentals, React hooks (useState, useEffect, useRef) |
| Cloud & Deployment | ML-4 on Linux + Git + GitHub; ML-3 on Docker | Docker images + containers, Dockerfile writing, docker-compose for Django stack |
| Communication | ML-3 on Technical Vocabulary + Technical Communication | Can explain any technology in plain language; STAR method understood |
| Job Preparation | ML-2 on Resume module | Resume first draft complete; understand ATS optimization |

**Phase 2 Completion Criteria:**
- [ ] DRF API with JWT authentication running in Docker (docker-compose up works)
- [ ] Python: OOP code written independently — classes, inheritance, decorators, context managers — no AI during implementation
- [ ] SQL: Window functions and CTEs written without reference
- [ ] React: Counter, Todo list, or similar built independently with hooks
- [ ] ADS trending downward in Python and Backend domains across Phase 2

**Phase 2 Critical Dependency:**
Backend Engineering Tiers 4–5 (Django + DRF) require Python Levels 1–4 at ML-3+. Do not start Django ORM deep work until Python OOP is at ML-3. This is the single hardest dependency in the entire system.

**Phase 2 Warning Signs:**
- Python OOP still at ML-2 by Day 45 → Pause all other domains; resolve Python first
- DRF not started by Day 55 → Phase 3 milestone project is at risk
- ADS still ≥ 3 in Backend by Day 65 → Trigger Stuck Escalation protocol

---

### Phase 3: Integration (Days 76–120)

**Theme:** Connect all domains into working systems. First production deployment. CRS ≥ 50%.

**Strategic Intent:**
Phase 3 is where Mahesh transitions from learning individual topics to building integrated systems. The milestone project here is the portfolio centrepiece — a production-deployed full-stack application. This is what employers will see. Every domain studied in Phases 1–2 must now be demonstrated in working code.

**Phase 3 Objectives:**

| Domain | Target by End of Phase 3 | Key Topics to Cover |
|--------|--------------------------|---------------------|
| Python | ML-4 on Levels 1–8 (~45 topics at ML-4+) | Concurrency (asyncio, threading), Standard Library (os, pathlib, datetime, logging), Testing (pytest, mocking) |
| Backend Engineering | ML-4/5 on Tiers 1–7 (~45 topics at ML-4+) | Caching (Redis), Celery + task queues, DB query optimization, 12-Factor App, API versioning |
| SQL | ML-4 on Levels 1–11 (full SQL competency ~50 topics at ML-4+) | PostgreSQL specifics, EXPLAIN ANALYZE, JSONB, pg_trgm, full-text search |
| DBMS | ML-4 on 80%+ of topics | Concurrency control (2PL, MVCC), Recovery, CAP Theorem, NoSQL fundamentals |
| Operating Systems | ML-4 on 70%+ of topics | Memory management, Virtual memory, File systems, Linux practical (systemd, cgroups) |
| Computer Networks | ML-4 on 70%+ of topics | CORS deep dive, WebSockets, REST vs GraphQL vs gRPC, Security (HTTPS enforcing, rate limiting) |
| Frontend | ML-4 on Levels 1–12 (~55 topics at ML-4+) | React Router, Redux Toolkit or Zustand, React Query, Error boundaries, Code splitting |
| Cloud & Deployment | ML-4 on Docker + CI/CD + AWS core (~35 topics at ML-4+) | GitHub Actions pipeline, EC2 deployment, RDS + PostgreSQL on AWS, S3, IAM, Nginx + Gunicorn |
| Communication | ML-4 on Project Storytelling + Interview Communication | Can deliver STAR answers for all milestone projects; mock interview performance ≥ 70% |
| Job Preparation | ML-3 on Resume + LinkedIn + GitHub Portfolio | Resume finalized; LinkedIn complete; GitHub portfolio has ≥ 2 quality repos |

**Phase 3 Completion Criteria:**
- [ ] **Milestone Project 3 deployed** (see Section 5)
- [ ] CRS ≥ 50% (computed by AI using session logs)
- [ ] Python DRS ≥ 55%, Backend DRS ≥ 55%, SQL DRS ≥ 60%
- [ ] Can walk through the full architecture of Milestone Project 3 in a live interview without notes
- [ ] Communication: STAR answers prepared for ≥ 3 technical decisions from the project

---

### Phase 4: Interview Preparation (Days 121–150)

**Theme:** Convert competence into interview performance. CRS ≥ 60%. First applications submitted.

**Strategic Intent:**
No new domains. No new frameworks. This phase is about converting existing knowledge into interview currency. The bottleneck here is not knowledge — it is the ability to articulate, demonstrate under pressure, and perform in real interviews. Mahesh's telecom background gives him the professionalism; Phase 4 adds the technical interview fluency.

**Phase 4 Objectives:**

| Focus Area | Target | How |
|------------|--------|-----|
| Python mastery depth | ML-5 on 40%+ of completed topics | Full evaluations; no AI during explanation |
| Backend mastery depth | ML-5 on 50%+ of completed topics | System design questions; architecture trade-offs |
| SQL interview fluency | Can solve medium-complexity SQL problems live | Daily 20-minute SQL practice without reference |
| DBMS/OS/CN interview readiness | Can answer top 20 interview questions per domain | Flashcard-style drill via AI evaluation |
| Communication | ML-4/5 on Interview Communication module | Weekly mock interviews with AI; record and review |
| Job Preparation | ML-4 on Resume + LinkedIn + GitHub + Interview Prep | Resume v2 with metrics; portfolio website; 10+ applications submitted |
| Revision sweep | Every Phase 1–3 topic checked for regression | AI-run systematic revision (≤ 2 topics/day) |

**Phase 4 Completion Criteria:**
- [ ] CRS ≥ 60% (hard minimum to proceed to Phase 5 at full intensity)
- [ ] All 4 Hard Constraints met: Python DRS ≥ 60%, Backend DRS ≥ 60%, SQL DRS ≥ 55%, Communication DRS ≥ 60%
- [ ] ≥ 10 job applications submitted with tailored resumes
- [ ] ≥ 3 mock interviews completed (AI-simulated or peer); post-interview analysis done
- [ ] Can explain Milestone Project 3 architecture, every technical decision, and trade-offs in 10 minutes without AI

**Phase 4 Warning Signs:**
- Hard Constraints not met by Day 140 → Delay Phase 5 intensity; run Level 2 Escalation on failing domains
- CRS < 55% at Day 140 → Run CRS Bottleneck Analysis; spend final 10 days of Phase 4 on top 3 bottleneck topics only
- No applications submitted by Day 145 → Job Preparation domain escalated to Priority Tier 1 immediately

---

### Phase 5: Offer Acceleration (Days 151–180)

**Theme:** Application velocity + interview feedback loop. CRS ≥ 65%. Employment offer.

**Strategic Intent:**
Phase 5 is not about learning new topics. It is about converting interviews into offers. The feedback loop is: apply → interview → identify gaps → fill gaps → apply again. Every interview is data. Mahesh's 8 years of professional experience means he can navigate the human side of interviews; Phase 5 focuses on technical precision and offer mechanics.

**Phase 5 Objectives:**

| Focus Area | Target |
|------------|--------|
| Application volume | ≥ 25 total applications submitted (all quality, all tailored) |
| Live interview performance | Technical interview pass rate ≥ 50% |
| Feedback incorporation | Each rejected interview → 1 specific topic strengthened within 3 days |
| Salary negotiation | Negotiation framework ready: Floor 6 LPA, Target 8 LPA, Stretch 10 LPA |
| Referral networking | ≥ 5 warm outreach messages sent to connections in target companies |
| CRS | ≥ 65% (application-ready threshold) |
| New topic learning | Minimal — only fill gaps identified from interview feedback |

**Phase 5 Completion Criteria:**
- [ ] Employment offer received at ≥ 6 LPA
- [ ] CRS ≥ 65%
- [ ] All 4 Hard Constraints exceeded (not just met)

---

## Section 2 — Monthly Goals

> Monthly goals provide a progress checkpoint independent of phase boundaries. These are checkpoints, not plans.

---

### Month 1 (Days 1–30): Seed Every Domain

**Theme:** Establish breadth. Build the habit. Ship the first app.

| Domain | Month 1 Goal |
|--------|-------------|
| Python | Core syntax, data structures, functions solid at ML-3 |
| Backend | Django installed, first app running, understand MTV pattern |
| SQL | SELECT through JOINs — can write any join type from memory |
| DBMS | Understand what a database is, ER diagrams, relational model basics |
| OS | Understand process, thread, scheduling concepts at ML-2 |
| CN | Understand OSI layers, TCP/IP, what HTTP is at ML-2 |
| Frontend | HTML/CSS functional, JS variables/functions/loops solid |
| Cloud | Linux navigation fluent, Git workflow daily habit |
| Communication | Self-introduction polished; 15 min daily speaking practice |
| Job Prep | Browsed ≥ 20 JDs; know target roles and required skills |

**Month 1 Milestone:** Django app running locally, connected to PostgreSQL, with at least one model, one view, one URL, and code on GitHub.

---

### Month 2 (Days 31–60): Python and Backend Sprint

**Theme:** Two domains go deep. Everything else maintains momentum.

| Domain | Month 2 Goal |
|--------|-------------|
| Python | OOP mastered (ML-4); Decorators, Context Managers, Error Handling at ML-4 |
| Backend | DRF serializers and ViewSets working; JWT authentication implemented |
| SQL | Window functions and CTEs at ML-4; understand query execution |
| DBMS | Normalization (1NF through BCNF) understood; can design a normalized schema |
| OS | Processes, Threads, CPU scheduling at ML-3 |
| CN | HTTP/HTTPS, TLS handshake at ML-3; understand what actually happens in a browser request |
| Frontend | React fundamentals, useState, useEffect, useRef at ML-4 |
| Cloud | Docker: can write a Dockerfile and docker-compose for Django+PostgreSQL+Redis |
| Communication | Technical STAR stories drafted for 2 existing projects |
| Job Prep | Resume first draft written |

**Month 2 Milestone:** Authenticated DRF API (JWT), running in Docker, with React consuming one API endpoint.

---

### Month 3 (Days 61–90): Full Stack Comes Alive

**Theme:** Build the portfolio project. SQL and Frontend reach professional level.

| Domain | Month 3 Goal |
|--------|-------------|
| Python | Testing (pytest), Concurrency concepts, Backend Python patterns at ML-4 |
| Backend | Caching (Redis), Celery, query optimization — production-grade Backend patterns |
| SQL | Full PostgreSQL competency; EXPLAIN ANALYZE; JSONB; can optimize slow queries |
| DBMS | MVCC, concurrency control, recovery — ML-4 across 80% of topics |
| OS | Memory management, virtual memory, Linux practical — ML-4 on 70% |
| CN | WebSockets, CORS, security headers, rate limiting — ML-4 on 70% |
| Frontend | State management (Redux/Zustand), React Query, full API integration |
| Cloud | CI/CD pipeline (GitHub Actions), AWS EC2 + RDS deployed |
| Communication | Can narrate project architecture in 10 minutes; STAR method fluent |
| Job Prep | LinkedIn profile complete; GitHub portfolio active with ≥ 2 repos |

**Month 3 Milestone:** Full-stack application deployed on AWS — React frontend, DRF backend, PostgreSQL on RDS, Redis, Celery, GitHub Actions CI/CD, Nginx + Gunicorn.

---

### Month 4 (Days 91–120): Depth and Polish

**Theme:** Solidify all domains. CRS crosses 50%. Project ready for interviews.

| Domain | Month 4 Goal |
|--------|-------------|
| Python | ML-5 on core topics (OOP, Decorators, Async); can explain CPython internals at basic level |
| Backend | ML-5 on Tiers 1–7; system design patterns understood; production architecture fluent |
| SQL | ML-5 on key SQL topics; can solve complex SQL problems live without notes |
| DBMS/OS/CN | Each domain ≥ ML-4 on 80% of topics; interview question bank drilled |
| Frontend | ML-4 on advanced React patterns; can debug React apps independently |
| Cloud | AWS deployment independent; Terraform basics understood |
| Communication | Mock interview performance ≥ 70%; project storytelling polished |
| Job Prep | Applications begin; resume optimized per role type |

**Month 4 Milestone:** CRS ≥ 55%. Portfolio project has a live URL, polished README, architectural diagram, and decision log. Can present it in a 10-minute technical walkthrough.

---

### Month 5 (Days 121–150): Interview Mode

**Theme:** Convert knowledge to performance. Apply actively.

| Focus | Month 5 Goal |
|-------|-------------|
| Hard Constraints | All 4 met: Python ≥ 60%, Backend ≥ 60%, SQL ≥ 55%, Communication ≥ 60% |
| Applications | ≥ 10 applications submitted |
| Mock Interviews | ≥ 3 mock technical interviews completed |
| Revision | Systematic review of all domains; no regressions |
| CRS | ≥ 60% by Day 150 |

**Month 5 Milestone:** First live technical interviews happening. Interview analysis documented. One gap identified and closed per interview.

---

### Month 6 (Days 151–180): Offer Month

**Theme:** Application velocity. Interview feedback loop. Negotiate the offer.

| Focus | Month 6 Goal |
|-------|-------------|
| Applications | ≥ 25 total submitted |
| Interview performance | Improving trend across each round |
| Salary negotiation | Framework ready and practiced |
| CRS | ≥ 65% |
| Outcome | Employment offer at ≥ 6 LPA |

**Month 6 Milestone:** Signed offer letter.

---

## Section 3 — Skill Dependencies

> These are hard dependencies. The dependent topic cannot reach ML-4 until the prerequisite is at ML-3+. AI agents must enforce these when generating plans.

---

### Python Dependency Chain

```
Level 1: Syntax + Data Types + Variables
    ↓
Level 2: Data Structures (Lists, Dicts, Sets, Tuples)
    ↓
Level 3: Functions + Modules + File I/O + Error Handling
    ↓
Level 4: OOP (Classes, Inheritance, Dunder Methods)
    ↓
Level 5: Advanced Python (Decorators, Context Managers, Generators, Type Hints)
    ↓
Level 6: Concurrency (Threading, asyncio, multiprocessing)
    ↓
Level 7: Standard Library (os, pathlib, logging, datetime, re)
    ↓
Level 8: Testing (pytest, unittest, mocking)
    ↓
Level 9: Backend Python patterns (WSGI/ASGI, environ management)
```

**Critical rule:** Python Level 4 (OOP) must be at ML-3 before starting Django models or DRF class-based views. This is the most commonly violated dependency.

---

### Backend Engineering Dependency Chain

```
Tier 1: Internet Fundamentals (HTTP, DNS, TCP, REST)
    ↓
Tier 2: API Design (REST principles, status codes, request/response lifecycle)
    ↓
[REQUIRES: Python Levels 1–3 at ML-3]
    ↓
Tier 3: Django Fundamentals (MTV, settings, URLs, views)
    ↓
[REQUIRES: Python Level 4 OOP at ML-3]
    ↓
Tier 4: Django Depth (ORM, migrations, admin, signals, middleware)
    ↓
Tier 5: DRF (serializers, viewsets, routers, authentication)
    ↓
[REQUIRES: SQL Levels 1–5 at ML-3]
    ↓
Tier 6: Database Integration (query optimization, select_related, prefetch_related, N+1)
    ↓
Tier 7: Caching + Task Queues (Redis, Celery, async tasks)
    ↓
Tier 8: Architecture (12-Factor, microservices concepts, API versioning)
    ↓
Tier 9: Production (Gunicorn, Nginx, environment management, logging)
    ↓
Tier 10: Advanced Backend (gRPC, GraphQL, event-driven, service mesh awareness)
```

---

### SQL + DBMS Dependency Chain

```
SQL Levels 1–5 (SELECT through JOINs)
    ↓ (feeds into)
Backend Tier 6 (Django ORM proficiency)
    ↓
SQL Levels 6–8 (Subqueries, CTEs, Window Functions, DDL, Indexes)
    ↓
DBMS: Indexing (B-Tree, composite indexes, explain plans)
    ↓
SQL Levels 9–11 (Transactions, PostgreSQL specifics, JSONB, full-text search)
    ↓
DBMS: Transactions + ACID + Concurrency Control + MVCC
```

**Note:** DBMS theory and SQL practice reinforce each other. Study them in parallel — DBMS explains WHY; SQL shows HOW.

---

### Frontend Dependency Chain

```
HTML (semantic elements, forms, accessibility)
    ↓
CSS (Flexbox, Grid, responsive design, CSS variables)
    ↓
JavaScript Core (variables, functions, arrays, objects, loops, scope)
    ↓
JavaScript DOM + Events (querySelector, addEventListener, event bubbling)
    ↓
JavaScript Advanced (Closures, Prototypes, this keyword, Classes)
    ↓
Promises + async/await + Fetch API
    ↓
[REQUIRES: Backend Tier 5 DRF endpoints available to consume]
    ↓
React Fundamentals (JSX, props, state, component lifecycle)
    ↓
React Hooks (useState, useEffect, useRef, useContext, useCallback, useMemo)
    ↓
React Router v6
    ↓
API Integration (React Query or SWR + error/loading states)
    ↓
State Management (Redux Toolkit or Zustand)
    ↓
Advanced React (custom hooks, Error boundaries, lazy loading, code splitting)
    ↓
Testing (React Testing Library, Jest)
```

---

### Cloud and Deployment Dependency Chain

```
Linux Fundamentals (navigation, permissions, processes, systemd)
    ↓
Git (commits, branches, merge, rebase, conflict resolution)
    ↓
GitHub (remotes, pull requests, Actions basics)
    ↓
[REQUIRES: A working Django app to containerize]
    ↓
Docker (images, containers, Dockerfile, docker-compose)
    ↓
CI/CD (GitHub Actions — test, lint, build, deploy pipeline)
    ↓
[REQUIRES: Docker working, GitHub Actions pipeline set up]
    ↓
AWS Core (EC2, S3, RDS, VPC, IAM, Security Groups)
    ↓
Application Deployment (EC2 + Gunicorn + Nginx + RDS + environment variables)
    ↓
Monitoring (CloudWatch, Sentry, logging strategy)
    ↓
IaC (Terraform basics — define infrastructure as code)
```

---

### Theory Domain Dependencies (OS, CN, DBMS)

These three domains are largely parallel and self-contained. They do not block each other. Their primary dependency is:

```
DBMS → Feeds interview questions for Backend database design
OS   → Feeds interview questions for concurrency, processes, memory
CN   → Feeds interview questions for HTTP, DNS, TCP, security
```

All three must reach ML-4 on ≥ 70% of topics by Day 120. They are tested in interviews alongside practical topics. Neglecting them is one of the most common reasons career changers fail system design or back-to-basics interview rounds.

---

### Communication + Job Prep Dependencies

```
Phase 1: Basic spoken English practice + tech pronunciation
    ↓
Phase 2: Technical vocabulary + STAR method understanding
    ↓
[REQUIRES: At least 1 completed project to tell stories about]
    ↓
Phase 3: Project storytelling + mock interviews begin
    ↓
[REQUIRES: CRS ≥ 50% — sufficient knowledge to interview on]
    ↓
Phase 4: Full interview simulation + Job Prep acceleration
    ↓
Phase 5: Live interviews + negotiation
```

---

## Section 4 — Milestone Projects

> Four milestone projects mark phase transitions. Each is a required gate, not an optional enhancement. Projects are not new builds — they are natural extensions of what is being studied. The third milestone is the portfolio centrepiece.

---

### Milestone Project 1: Local Django Application (End of Phase 1, ~Day 30)

**Name:** Choose anything meaningful (Task Manager, Expense Tracker, Library Catalog, Notes App)

**Technical Requirements:**
- Django + PostgreSQL (local)
- At least 2 models with a relationship (ForeignKey or ManyToMany)
- Basic CRUD views (function-based or class-based)
- User authentication (Django built-in — login/logout/register)
- Code on GitHub with a minimal README

**What this proves:**
- Django MTV pattern understood
- ORM basics working
- Git workflow established
- Database connected and migrated

**What this does NOT need to be:**
- Production-ready
- Beautiful UI
- Deployed anywhere
- DRF-based

**Interview value:** Low on its own. High as a foundation story ("I started with X, then evolved it to Y").

---

### Milestone Project 2: Authenticated REST API (End of Phase 2, ~Day 75)

**Name:** Extend Milestone Project 1 into an API, or build a new DRF project from scratch

**Technical Requirements:**
- Django + DRF + PostgreSQL
- JWT authentication (djangorestframework-simplejwt)
- At least 4 API endpoints (list, create, retrieve, update/delete)
- Nested serializers or serializer validation logic
- Swagger / drf-spectacular API documentation
- Docker: `docker-compose up` brings the full stack (Django + PostgreSQL)
- GitHub: repo with docker-compose.yml, .env.example, and README with setup instructions

**What this proves:**
- DRF competency
- JWT authentication understood
- Docker-first development workflow
- API design principles applied

**Interview value:** Medium. Demonstrates DRF and Docker. Shows progression from Project 1.

---

### Milestone Project 3: Production Full-Stack System (End of Phase 3, ~Day 120)

**This is the primary portfolio project. It must be polished, deployed, and explainable under pressure.**

**Name:** Build something real — a domain Mahesh understands (logistics, telecom operations, supply chain, retail). Authenticity matters.

**Technical Requirements:**
- **Backend:** Django + DRF + PostgreSQL (RDS on AWS) + Redis + Celery (at least one background task)
- **Frontend:** React + React Router + API integration (React Query or Axios with state management)
- **Authentication:** JWT with refresh token rotation
- **Deployment:** EC2 + Gunicorn + Nginx + RDS + S3 (for static/media files)
- **CI/CD:** GitHub Actions — automated test + deploy on merge to main
- **Code quality:** At least one test suite (backend unit tests with pytest)
- **Documentation:**
  - README with architecture diagram
  - API documentation (drf-spectacular)
  - Architecture Decision Log (3–5 key decisions explained with trade-offs)
  - Live URL (EC2 hosted)

**What this proves:**
- Full-stack integration from frontend to cloud
- Production deployment competence
- Background jobs (Celery) understood
- CI/CD pipeline owned end-to-end
- AWS core services working together

**Interview value:** Very high. This single project can carry most technical interviews for 6–8 LPA roles. Every architectural decision must be explainable. Every component choice must be justifiable.

**Additional preparation for Milestone Project 3:**
- Practice a 10-minute architecture walkthrough out loud (no notes)
- STAR answers for: "What was the hardest bug you fixed?", "What would you change about the architecture?", "Why did you choose React over Vue?", "How does your CI/CD pipeline work?"
- Know every line in the docker-compose.yml and GitHub Actions YAML

---

### Milestone Project 4: Interview-Ready Presentation (Phase 4, ~Day 145)

**This is not a new build. It is the hardened presentation of Milestone Project 3.**

**Requirements:**
- Can explain the full architecture verbally in under 10 minutes
- Can answer all "why did you choose X?" questions for every major technology decision
- Can walk through a code review of any file in the project
- STAR format answers prepared for all key development moments
- Salary negotiation context ready: know what this project demonstrates, what roles it targets, and what it is worth

**Evidence:** Record a 10-minute solo walkthrough video (phone camera is fine). Watch it back once. Fix what sounds weak. No AI in the recording.

**Interview value:** This preparation is the difference between candidates who have a project and candidates who own their project. Interviewers can tell the difference in 3 minutes.

---

## Section 5 — Employment Readiness Gates

> Six gates mark the path from Day 1 to employed. Each gate is a binary check — pass or fail. Failing a gate does not stop progress but triggers specific remediation.

---

### Gate G-1: Foundation Established (Day 30)

| Check | Threshold | Pass Condition |
|-------|-----------|---------------|
| Study habit | ≥ 5 hours/day avg | Last 7 days of logs show ≥ 5 hr avg |
| Django running | ML-2 minimum | Milestone Project 1 exists on GitHub |
| Git workflow | Active | ≥ 15 commits in the last 30 days |
| All domains seeded | ML-2+ on all 10 | No domain still at ML-0 |

**Fail consequence:** Diagnose and fix before Phase 2 begins. A missed G-1 usually means study habit is not established — this must be resolved before volume of material increases.

---

### Gate G-2: Core Competence Confirmed (Day 75)

| Check | Threshold | Pass Condition |
|-------|-----------|---------------|
| Python DRS | ≥ 40% | ~22 topics at ML-4+ |
| Backend DRS | ≥ 35% | ~21 topics at ML-4+ |
| SQL DRS | ≥ 55% | ~28 topics at ML-4+ |
| AI Dependency | ADS trending down | Phase 2 avg ADS < Phase 1 avg ADS |
| Milestone Project 2 | Deployed locally | docker-compose up works |

**Fail consequence:** Level 2 Escalation on failing domains. Do not start Phase 3 until Python DRS ≥ 35% and Backend DRS ≥ 30%.

---

### Gate G-3: Integration Complete (Day 120)

| Check | Threshold | Pass Condition |
|-------|-----------|---------------|
| CRS | ≥ 50% | AI-computed from session logs |
| Python DRS | ≥ 55% | ~30 topics at ML-4+ |
| Backend DRS | ≥ 55% | ~33 topics at ML-4+ |
| SQL DRS | ≥ 65% | ~33 topics at ML-4+ |
| Milestone Project 3 | Live URL exists | EC2 deployment reachable |
| Frontend | ≥ 40% DRS | ~26 topics at ML-4+ |
| Cloud | ≥ 50% DRS | ~25 topics at ML-4+ |

**Fail consequence:** Level 4 Escalation (CRS Bottleneck Analysis). Delay Phase 4 application volume until CRS ≥ 50%.

---

### Gate G-4: Interview Ready (Day 150)

**This is the primary employment gate. All 4 Hard Constraints must pass.**

| Check | Threshold | Pass Condition |
|-------|-----------|---------------|
| CRS | ≥ 60% | AI-computed |
| Python DRS | ≥ 60% (Hard Constraint) | Must pass, no exceptions |
| Backend DRS | ≥ 60% (Hard Constraint) | Must pass, no exceptions |
| SQL DRS | ≥ 55% (Hard Constraint) | Must pass, no exceptions |
| Communication DRS | ≥ 60% (Hard Constraint) | Must pass, no exceptions |
| Applications submitted | ≥ 10 | Count in Job Prep logs |
| Mock interviews | ≥ 3 completed | Evidence: post-interview analysis notes |
| Milestone Project 4 | Walkthrough recorded | Video or notes evidence |

**Fail consequence:** Do not slow Phase 5 volume — continue applying. But identify the failing Hard Constraint and make it the sole focus until it passes. A single failing Hard Constraint is enough to cause systematic interview failure.

---

### Gate G-5: Application Ready (Day 165)

| Check | Threshold | Pass Condition |
|-------|-----------|---------------|
| CRS | ≥ 65% | AI-computed — Employment Status = "Application Ready" |
| Applications submitted | ≥ 20 | |
| Live interviews | ≥ 2 completed | |
| Interview gap analysis | Done | At least 1 weakness identified and addressed per interview |

**Pass consequence:** Full application mode. Referral outreach begins. Salary negotiation preparation finalized.

---

### Gate G-6: Employment Offer (Day 180)

| Check | Threshold |
|-------|-----------|
| Offer received | ≥ 6 LPA |
| CRS at offer time | ≥ 65% |

**If offer is below floor (< 6 LPA):** Do not accept. Negotiate or decline and continue. The floor exists because accepting below-floor offers in the first 6 months sets a salary baseline that is very difficult to recover from.

**If Day 180 passes without an offer:** This is not failure — it is data. Common causes: insufficient application volume, single domain bottleneck (usually Communication or Backend), or projects not polished enough. Run Gate G-4 checks again; identify the gap; extend the runway.

---

## Section 6 — Subject Priority Matrix

> How to resolve conflicts when time is limited. Higher priority domains get more time.

---

### Priority Tiers

| Tier | Domains | Rationale |
|------|---------|-----------|
| **Tier 1 — Must Master** | Python, Backend Engineering | Combined 38% CRS weight; both have Hard Constraints; every target job role tests these |
| **Tier 2 — Must Be Strong** | SQL, Communication, Frontend, Cloud | Hard Constraint (SQL, Communication); high CRS weight; directly tested in most interviews |
| **Tier 3 — Must Pass** | DBMS, Operating Systems, Computer Networks | Lower CRS weight; but tested in theory rounds; cannot be neglected below 50% DRS |
| **Tier 4 — Must Execute** | Job Preparation | Not a knowledge domain — it is action. Neglecting it means knowledge never converts to offers |

---

### Conflict Resolution Rules

When time is short on a given day and not all domains can receive full attention, apply these rules in order:

**Rule P-1:** Never sacrifice Tier 1 time for any other tier. Python and Backend always get their full daily block.

**Rule P-2:** SQL is treated as Tier 1 equivalent during Months 1–3. It is a direct multiplier on Backend competence and is tested in almost every technical interview.

**Rule P-3:** Communication cannot be deferred to "later." 15 minutes of spoken practice daily is more effective than 4 hours once a week. It compounds through consistent repetition.

**Rule P-4:** DBMS, OS, and CN are studied in rotation, not in parallel. One is active per week; the others are in maintenance revision.

**Rule P-5:** Job Preparation work begins no later than Day 60 (resume draft) and is non-negotiable from Day 90 onward (LinkedIn, GitHub, applications).

**Rule P-6:** If CRS ≥ 65% and active interviews are happening, shift time from Tier 3 domains to Communication and Job Prep. Technical theory is less urgent than interview performance at that stage.

---

### Weekly Domain Touch Frequency

| Domain | Minimum Weekly Sessions | Notes |
|--------|------------------------|-------|
| Python | 5 sessions/week | Daily, no exceptions during Months 1–4 |
| Backend Engineering | 5 sessions/week | Daily, no exceptions during Months 1–4 |
| SQL | 4 sessions/week | 3 deep study + 1 practice problem session |
| DBMS | 2 sessions/week | Rotate with OS, CN |
| Operating Systems | 2 sessions/week | Rotate with DBMS, CN |
| Computer Networks | 2 sessions/week | Rotate with DBMS, OS |
| Frontend | 3 sessions/week | More during Phase 3 when project is being built |
| Cloud & Deployment | 3 sessions/week | More during Phase 3 deployment sprint |
| Communication | 7 sessions/week | 15 min daily — this is not a study session, it is a practice habit |
| Job Preparation | 2 sessions/week from Day 60 onward | Ramps to 4–5 sessions/week in Phase 4–5 |

---

### CRS Contribution Analysis

This table shows the return-on-investment for each domain when deciding where to focus.

| Domain | CRS Weight | Topics to ML-4 for 65% CRS | Approximate Study Hours to Reach That | ROI |
|--------|-----------|----------------------------|---------------------------------------|-----|
| Backend Engineering | 20% | ~36 topics | ~180 hours | Highest |
| Python | 18% | ~33 topics | ~165 hours | Highest |
| SQL | 10% | ~28 topics | ~80 hours | High |
| Frontend | 10% | ~30 topics | ~120 hours | High |
| Cloud & Deployment | 10% | ~26 topics | ~100 hours | High |
| Communication | 10% | ~21 topics | ~60 hours | Very High (fast gains) |
| Job Preparation | 7% | ~20 topics | ~40 hours | Extreme (pure execution) |
| DBMS | 5% | ~25 topics | ~80 hours | Medium |
| Operating Systems | 5% | ~28 topics | ~90 hours | Medium |
| Computer Networks | 5% | ~30 topics | ~90 hours | Medium |

**Implication:** Communication has the highest ROI relative to study hours required. It is also the most neglected by technical learners. Prioritize it consistently.

**Implication:** Job Preparation requires almost no new knowledge — it requires action. The 40 hours is for building artifacts (resume, portfolio, LinkedIn, applications). Every hour spent here directly converts to offer probability.

---

## Section 7 — DSA Track Integration

> DSA is managed in the separate `DSA-System` folder. This section defines how it integrates with the Career OS without duplicating its management.

---

### DSA in the Career OS Context

DSA (Data Structures and Algorithms) is deliberately excluded from Career OS mastery tracking. It has its own system, its own evaluation cadence, and its own progress tracker. Career OS does not track DSA topics, does not include DSA in the CRS formula, and does not generate DSA study plans.

However, DSA is not invisible. It runs as a daily external track and interacts with Career OS in these ways:

---

### DSA Daily Time Allocation

```
Career OS daily total: 6 hours
DSA external track:    1.0 – 1.5 hours (within the 6-hour block)

Recommended allocation:
  Early morning: 1 hour DSA (fresh mind, algorithmic thinking)
  Remaining 5 hours: Career OS study per 13_SYSTEM_SIMPLIFICATION_RULES.md
```

DSA gets the first slot of the day. This is not because it is the highest priority — it is because DSA problem-solving requires a fresh mind and degrades significantly when done after 4+ hours of other study.

---

### DSA–Career OS Interaction Rules

**Rule DSA-1:** DSA time is protected. Career OS domains may not encroach on the DSA slot even during high-priority sprints (e.g., Phase 3 deployment).

**Rule DSA-2:** If a day has < 5 hours available (shortened study day), DSA is reduced to 30 minutes, not eliminated. Career OS gets the remaining time.

**Rule DSA-3:** DSA progress is NOT reported in the Career OS daily log. The 5-line log covers Career OS topics only.

**Rule DSA-4:** When an interview invite arrives (Level 5 Escalation), DSA time increases to 2 hours/day and Career OS time adjusts accordingly.

**Rule DSA-5:** The Career OS AI agent does not generate DSA plans, evaluate DSA topics, or include DSA in any CRS computation. It acknowledges DSA exists as a parallel track and respects the time allocation.

---

### DSA Readiness and Employment Gates

DSA readiness is a parallel concern to the Career OS gates. Both must be satisfied before applying:

| Requirement | Source | Gate |
|-------------|--------|------|
| CRS ≥ 65% | Career OS | G-5 |
| DSA: Easy problems fluent | DSA-System | DSA-System's own gate |
| DSA: Medium problems attempted | DSA-System | DSA-System's own gate |

Target companies at 6–8 LPA in India typically expect:
- LeetCode Easy: fluent (< 15 min)
- LeetCode Medium: solvable (< 35 min)
- LeetCode Hard: optional (bonus, not required for most 6–8 LPA roles)

---

## Section 8 — Adaptive Strategy Rules

> The roadmap is a plan. Reality will diverge. These rules govern how to adapt without losing momentum or lowering standards.

---

### If Ahead of Schedule

**Definition:** CRS is ≥ 5% above the trajectory line at any gate.

**Response:**
- Do not rush Phase transitions. Use the surplus time to increase mastery depth in completed topics (ML-4 → ML-5).
- Accelerate Job Preparation — begin applications earlier.
- Add one additional Communication practice session per week.
- Do NOT skip Phase 3's Milestone Project to get to Phase 4 faster. The project is a gate, not optional.

---

### If Behind Schedule

**Definition:** CRS is ≥ 5% below the trajectory line at any gate, OR a Hard Constraint is not met by its Phase target.

**Response:**
- Identify the single domain most behind relative to its CRS contribution.
- Run Level 4 Escalation (CRS Bottleneck Analysis).
- Reduce new topic intake to 50% of normal — more revision, more evaluation, more implementation.
- Do not delay Phase 5 applications. A real interview is better feedback than a simulated one.

---

### If a Domain Is Stalled

**Definition:** A domain has had no Complete topics in > 10 days.

**Response:** Level 2 Escalation (Section 10.2 of `13_SYSTEM_SIMPLIFICATION_RULES.md`). Identify root cause: too difficult? prerequisites missing? wrong resources?

**Most common root causes per domain:**
- Python: OOP not solid — rebuild from Dunder methods
- Backend: Django ORM confusion — usually a SQL gap causing it; fix SQL first
- SQL: Window functions — drill with a real dataset (employees, orders); abstract explanations don't work
- Frontend: JavaScript closures — must be understood before React hooks make sense
- Cloud: AWS confusion — hands-on only; reading AWS docs without clicking through the console doesn't work

---

### If Communication Is Being Neglected

**Definition:** Communication DRS < 40% at any point after Day 60, OR no speaking practice in > 3 days.

**Response:** Immediate. Communication neglect is the most common and most costly mistake in career transitions. It is also the most recoverable in a short time.

- Add one 20-minute speaking session daily until DRS recovers
- STAR answers for existing projects take 1–2 hours to draft and pay dividends in every interview
- Technical term pronunciation errors (saying "Nig-inx" instead of "Engine-X") create a negative first impression that is hard to recover from in a 45-minute interview

---

### The Telecom Advantage — When to Use It

Mahesh's telecom background is a genuine differentiator in these scenarios:

| Topic | How Telecom Helps |
|-------|------------------|
| Computer Networks | Deep operational experience with real networks — CN theory is not abstract to Mahesh |
| System Reliability + SLAs | Telecom has the most demanding uptime requirements — this context is valuable in backend discussions |
| Incident Management | Operations experience maps directly to on-call/SRE culture in software |
| Business Communication | 8 years of professional communication experience reduces the ramp-up time in the Communication domain significantly |
| Project Storytelling | Real projects with business impact are more compelling than student exercises |

In interviews: frame the telecom background as "I understand systems at scale, business requirements, and operational constraints — software engineering is my new implementation layer." This is a more compelling narrative than "career changer learning from scratch."

---

## Appendix — Phase Completion Checklist

> Use this checklist to confirm a phase is complete before declaring transition.

---

### Phase 1 → Phase 2 Transition Checklist

```
☐ Django + PostgreSQL app running locally with code on GitHub
☐ All 10 domains have at least one IN PROGRESS topic (none at NOT STARTED)
☐ SQL: can write INNER, LEFT, RIGHT, FULL OUTER JOIN from memory
☐ Git: daily commit habit established (≥ 15 commits in 30 days)
☐ Communication: self-introduction practiced and fluent
☐ 6-hour daily study habit established (avg ≥ 5 hrs over last 7 days)
☐ Daily log filed for ≥ 25 of the 30 days
```

---

### Phase 2 → Phase 3 Transition Checklist

```
☐ Milestone Project 2 complete (DRF API, JWT, Docker)
☐ Python DRS ≥ 40%
☐ Backend DRS ≥ 35%
☐ SQL DRS ≥ 55%
☐ React: useState + useEffect + API call working independently
☐ Docker-compose: Django + PostgreSQL + Redis stack runs from one command
☐ ADS trending downward in Python and Backend (Phase 2 avg < Phase 1 avg)
☐ Gate G-2 passed (all checks above + ADS check)
```

---

### Phase 3 → Phase 4 Transition Checklist

```
☐ Milestone Project 3 deployed with live URL
☐ CRS ≥ 50%
☐ Python DRS ≥ 55%
☐ Backend DRS ≥ 55%
☐ SQL DRS ≥ 65%
☐ Frontend DRS ≥ 40%
☐ Cloud DRS ≥ 50%
☐ Can explain Milestone Project 3 architecture in 10 minutes without notes
☐ GitHub portfolio has ≥ 2 quality repos
☐ Resume first draft complete
☐ Gate G-3 passed
```

---

### Phase 4 → Phase 5 Transition Checklist

```
☐ CRS ≥ 60%
☐ Python DRS ≥ 60% (Hard Constraint)
☐ Backend DRS ≥ 60% (Hard Constraint)
☐ SQL DRS ≥ 55% (Hard Constraint)
☐ Communication DRS ≥ 60% (Hard Constraint)
☐ ≥ 10 applications submitted
☐ ≥ 3 mock interviews completed with post-interview analysis
☐ Milestone Project 4 walkthrough recorded
☐ Salary negotiation framework ready
☐ Gate G-4 passed (all Hard Constraints)
```

---

### Phase 5 Completion

```
☐ CRS ≥ 65%
☐ ≥ 25 applications submitted
☐ Employment offer received at ≥ 6 LPA
☐ Gate G-5 and G-6 passed
```

---

*The 180 days are not a countdown. They are a structure. The offer comes when preparation meets consistent execution — and when Mahesh can walk into a room and prove, without AI, that he understands what he has built.*
