# Cloud-OS — Knowledge Rules

## CHAPTER ORGANIZATION
One file per concept.
```
notes/
  Deployment Fundamentals.md
  Git.md
  Docker.md
  Docker Compose.md
  Linux Basics.md
  Nginx.md
  CI_CD.md
  Environment Variables.md
  SSL.md
  Monitoring.md
  Scaling.md
```

## NOTE FILE STRUCTURE
```
# [Topic] (Cloud & Deployment)

## Why It Matters
- Engineering problem it solves
- Where it fits in the deployment pipeline

## Core Concept
- Plain English: how code goes from laptop to production
- Architecture insight

## Deployment Flow Diagram
[ASCII: Developer → GitHub → CI/CD → Server → Docker → App → User]

## Key Commands / Config
[Minimal example — max 10 lines]

## Backend Connection
[How this deployment concept supports a Django/Python backend]

## Interview Questions
⭐ most frequently asked

## Common Confusions ⚠
- Image vs Container
- Docker vs Virtual Machine
- CI vs CD
- HTTP vs HTTPS
- Proxy vs Reverse Proxy

## 30-Second Interview Revision
[5 bullet points]
```

## TEACHING STYLE
- Problem → Why technology exists → Architecture → Commands/Config → Production example
- Never begin with commands — teach the engineering reason first
- Always answer: how does code leave my laptop and reach users?
- Connect everything to backend deployment

## QUALITY CHECK
Failed if: cloud taught as commands only, architecture missing, security ignored, production thinking absent.
Succeeds when: learner can explain the complete path from code to production.
