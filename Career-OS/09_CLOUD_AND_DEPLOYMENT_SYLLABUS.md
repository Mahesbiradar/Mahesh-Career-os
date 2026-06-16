# Cloud & Deployment Syllabus — Mahesh Career OS

> **Goal:** Achieve professional-level DevOps and Cloud skills for a backend developer.
> **Target Stack:** Linux, Git, GitHub, Docker, GitHub Actions, AWS Core Services.
> **Focus:** Practical deployment of Python/Django applications to production.

---

## Level Structure Overview

| Level | Name | Capability Unlocked |
|-------|------|-------------------|
| Level 1 | Linux Fundamentals | Navigate and operate Linux servers |
| Level 2 | Git & Version Control | Manage code professionally |
| Level 3 | GitHub | Collaborate and automate via GitHub |
| Level 4 | Docker | Containerize any application |
| Level 5 | CI/CD | Automate testing and deployment |
| Level 6 | Cloud Fundamentals (AWS) | Deploy to cloud infrastructure |
| Level 7 | Application Deployment | Deploy Django to production |
| Level 8 | Infrastructure as Code | Provision infrastructure programmatically |
| Level 9 | Monitoring & Observability | Know what's happening in production |

---

## Level 1 — Linux Fundamentals

> *Every backend server runs Linux. This is the operating environment for everything you will deploy.*

---

### 1.1 Linux File System Hierarchy

- **Why It Matters:** You cannot navigate a server without knowing the directory structure.
- **Prerequisites:** None
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- Root filesystem (`/`)
- `/bin` — essential user binaries (ls, cp, mv)
- `/sbin` — system binaries (root-only)
- `/etc` — configuration files (nginx, postgresql, ssh)
- `/home` — user directories (`/home/ubuntu`, `/home/mahesh`)
- `/root` — root user's home
- `/var` — variable data (logs: `/var/log`, databases, mail spools)
- `/tmp` — temporary files (cleared on reboot)
- `/usr` — user programs, libraries
  - `/usr/bin` — non-essential user binaries
  - `/usr/local` — locally installed programs
- `/opt` — optional third-party software
- `/proc` — virtual filesystem (process info, kernel params)
- `/sys` — virtual filesystem (hardware/kernel state)
- `/dev` — device files (disk: `/dev/sda`, terminal: `/dev/tty`)
- `/mnt`, `/media` — mount points

---

### 1.2 Core Commands

- **Why It Matters:** These are used every single time you touch a Linux server. You cannot work as a backend developer without them.
- **Prerequisites:** 1.1
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:

**Navigation:**
- `pwd` — print working directory
- `ls` — list directory contents
  - `ls -la` — long format, show hidden
  - `ls -lh` — human-readable sizes
- `cd` — change directory (`cd ~` home, `cd -` previous)
- `find / -name "filename"` — search for file
- `locate filename` — faster indexed search

**File Operations:**
- `cp source dest` — copy
- `mv source dest` — move/rename
- `rm file` — remove (use carefully!)
- `rm -rf dir` — remove directory recursively (dangerous)
- `mkdir -p path/to/dir` — create directory and parents
- `touch file` — create empty file
- `ln -s target link` — symbolic link

**File Content:**
- `cat file` — display file contents
- `less file` — paginated view (q to quit, / to search)
- `head -n 50 file` — first 50 lines
- `tail -n 50 file` — last 50 lines
- `tail -f /var/log/nginx/error.log` — follow log in real time
- `wc -l file` — count lines

**Search:**
- `grep "pattern" file` — search in file
- `grep -r "pattern" directory` — recursive search
- `grep -i "pattern"` — case insensitive
- `grep -n "pattern"` — show line numbers
- `grep -E "regex"` — extended regex
- `awk '{print $1}' file` — column extraction
- `sed 's/old/new/g' file` — text substitution

**Archives:**
- `tar -czf archive.tar.gz directory/` — create gzip tar
- `tar -xzf archive.tar.gz` — extract gzip tar
- `zip -r archive.zip directory/` — zip
- `unzip archive.zip` — unzip

---

### 1.3 File Permissions

- **Why It Matters:** Permission errors block application startup, prevent log writing, and cause security holes.
- **Prerequisites:** 1.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Permission model: Owner | Group | Others (each: read/write/execute)
- `ls -la` output: `-rwxr-xr-x 1 user group size date name`
- Numeric notation: r=4, w=2, x=1
  - `chmod 755 file` → owner: rwx, group: r-x, others: r-x
  - `chmod 644 file` → owner: rw-, group: r--, others: r--
  - `chmod 600 ~/.ssh/id_rsa` → SSH key requires 600
  - `chmod 777 file` → avoid! (full access to everyone)
- Symbolic notation:
  - `chmod u+x file` — add execute for owner
  - `chmod g-w file` — remove write from group
  - `chmod o=r file` — set others to read only
  - `chmod a+r file` — add read for all
- `chown user:group file` — change owner and group
- `chown -R ubuntu:ubuntu /var/www` — recursive
- `chgrp group file` — change group only
- `umask` — default permission mask
- Special bits:
  - Setuid (4): run as file owner
  - Setgid (2): run as file group
  - Sticky bit (1): only owner can delete in shared directory

---

### 1.4 Process Management

- **Why It Matters:** Production servers run many processes. Knowing how to manage them is fundamental.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `ps aux` — all processes with CPU/memory
- `top` / `htop` — interactive process monitor
- `kill -15 PID` — graceful termination (SIGTERM)
- `kill -9 PID` — force kill (SIGKILL, cannot be caught)
- `killall process_name` — kill by name
- `pkill pattern` — kill by pattern
- Process background/foreground:
  - `command &` — run in background
  - `Ctrl+Z` — suspend
  - `bg` — resume in background
  - `fg` — bring to foreground
  - `jobs` — list background jobs
- `nohup command &` — immune to hangup (survive terminal close)
- `disown` — detach from shell
- `nice -n 10 command` — run with lower priority
- `renice +10 PID` — change priority of running process

---

### 1.5 Systemd & Service Management

- **Why It Matters:** Django + Gunicorn, Nginx, PostgreSQL, Redis — all managed as systemd services in production.
- **Prerequisites:** 1.4
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `systemctl start service` — start service
- `systemctl stop service` — stop service
- `systemctl restart service` — restart
- `systemctl reload service` — reload config without restart
- `systemctl status service` — check status
- `systemctl enable service` — start on boot
- `systemctl disable service` — don't start on boot
- `systemctl is-active service` — check if active
- `journalctl -u service` — view service logs
- `journalctl -u service -f` — follow logs
- `journalctl -u service --since "1 hour ago"`
- Writing a systemd service file (`.service` unit)
- Service unit file structure: `[Unit]`, `[Service]`, `[Install]`

---

### 1.6 Networking Commands

- **Why It Matters:** Debugging connectivity on servers requires these tools.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `ip addr` — show network interfaces and IPs
- `ip route` — show routing table
- `ss -tulpn` — show listening ports and processes (modern netstat)
- `netstat -tulpn` — legacy (still widely used)
- `ping host` — test connectivity
- `curl -v URL` — verbose HTTP request
- `wget URL` — download file
- `ssh user@host` — connect to remote server
- `scp source dest` — secure copy (file transfer)
- `rsync -avz source dest` — sync files (faster than scp for large dirs)
- `ufw status` — Ubuntu firewall status
- `ufw allow 80/tcp` — allow port
- `iptables -L` — show firewall rules

---

### 1.7 Shell Scripting for DevOps

- **Why It Matters:** Deployment scripts, health checks, backup scripts — all require shell scripting.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Shebang: `#!/bin/bash`
- Script execution: `chmod +x script.sh && ./script.sh`
- Variables: `NAME="Mahesh"`, `echo $NAME`
- Command substitution: `DATE=$(date +%Y%m%d)`
- Exit codes: `$?`, `exit 0` (success), `exit 1` (error)
- Conditionals: `if [ $? -eq 0 ]; then ... fi`
- String tests: `[ -z "$var" ]` (empty), `[ -n "$var" ]` (not empty)
- File tests: `[ -f file ]` (exists, regular), `[ -d dir ]` (directory)
- For loops: `for item in $(cat list.txt); do ... done`
- While loops: `while [ condition ]; do ... done`
- Functions
- Argument handling: `$1`, `$2`, `$@`, `$#`
- Redirection: `>` (overwrite), `>>` (append), `2>&1` (stderr to stdout)
- Cron syntax: `* * * * * command` (minute hour day month weekday)

---

## Level 2 — Git & Version Control

---

### 2.1 Git Fundamentals

- **Why It Matters:** Git is the universal version control system. Not knowing Git is disqualifying.
- **Prerequisites:** None
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- What is version control (snapshots, history, collaboration)
- `git init` — initialize repository
- `git clone URL` — clone remote repository
- **Git Object Model:**
  - Blob (file content)
  - Tree (directory)
  - Commit (snapshot + metadata + parent)
  - Tag
- **Three Areas:**
  - Working Directory (modified files)
  - Staging Area (Index) — `git add`
  - Repository (committed) — `git commit`
- `.gitignore` — files to exclude
- `git status` — see what's changed
- `git diff` — see changes in detail
- `git log` — view commit history
  - `git log --oneline --graph` — visual branch history
- `git show` — show commit details
- `git blame file` — who changed each line

---

### 2.2 Staging & Committing

- **Why It Matters:** Good commit hygiene makes codebases readable and debugging possible.
- **Prerequisites:** 2.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `git add file` — stage specific file
- `git add .` — stage all changes (use carefully)
- `git add -p` — interactive staging (patch)
- `git commit -m "message"` — commit with message
- Commit message conventions (Conventional Commits, Angular)
- Atomic commits (one logical change per commit)
- `git commit --amend` — modify last commit (only local!)
- `git reset HEAD file` — unstage file
- `git checkout -- file` — discard working directory changes

---

### 2.3 Branching

- **Why It Matters:** Branching enables parallel development, feature isolation, and safe experimentation.
- **Prerequisites:** 2.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `git branch` — list branches
- `git branch branch-name` — create branch
- `git checkout branch-name` — switch branch
- `git checkout -b branch-name` — create and switch
- `git switch branch-name` (modern syntax)
- `git switch -c branch-name` — create and switch
- `git branch -d branch-name` — delete branch (safe)
- `git branch -D branch-name` — force delete
- HEAD pointer
- Detached HEAD state

---

### 2.4 Merging & Rebasing

- **Why It Matters:** Integrating work from multiple branches is a daily operation. Understanding merge vs rebase is essential.
- **Prerequisites:** 2.3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**Merging:**
- `git merge branch-name` — merge into current branch
- Fast-forward merge (linear history, no merge commit)
- 3-way merge (creates merge commit)
- `git merge --no-ff` — force merge commit
- `git merge --squash` — combine all commits into one

**Conflict Resolution:**
- Conflict markers in files (`<<<<<<<`, `=======`, `>>>>>>>`)
- `git mergetool` — graphical merge
- `git merge --abort` — cancel merge
- Manual resolution → `git add` → `git commit`

**Rebasing:**
- `git rebase main` — replay commits on top of main
- Interactive rebase: `git rebase -i HEAD~3`
  - pick, squash, fixup, reword, drop
- Rebase vs Merge: rebase creates linear history
- Golden rule: never rebase shared/public branches

---

### 2.5 Remote Operations

- **Why It Matters:** Collaboration requires pushing and pulling from remote repositories.
- **Prerequisites:** 2.4
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `git remote -v` — list remotes
- `git remote add origin URL` — add remote
- `git fetch` — download remote changes (don't merge)
- `git pull` — fetch + merge
- `git pull --rebase` — fetch + rebase
- `git push origin branch-name` — push branch
- `git push -u origin branch-name` — set upstream tracking
- `git push --force-with-lease` — safe force push (not `--force`)
- `git remote prune origin` — clean up deleted remote branches

---

### 2.6 Git Workflows

- **Why It Matters:** Teams operate on agreed workflows. Knowing the common ones helps you integrate into any team.
- **Prerequisites:** 2.5
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**GitFlow:**
- `main` (production), `develop` (integration), `feature/*`, `release/*`, `hotfix/*`
- Structured, suits release-based projects
- Considered heavy for continuous delivery

**GitHub Flow:**
- `main` + feature branches
- PRs merge to main
- Simple, suits continuous delivery
- Most common in web development teams

**Trunk-Based Development:**
- All developers commit to trunk (main) frequently
- Feature flags for incomplete work
- Requires strong CI/CD
- Used at Google, Netflix, most FAANG

**Forking Workflow:**
- Each developer forks the repo
- PRs from fork to upstream
- Used in open source

---

### 2.7 Git Advanced

- **Why It Matters:** These commands appear regularly and are tested in senior interviews.
- **Prerequisites:** 2.5
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `git stash` — save uncommitted changes temporarily
  - `git stash pop` — restore and remove
  - `git stash apply` — restore without removing
  - `git stash list`
  - `git stash drop`
- `git cherry-pick commit-hash` — apply specific commit to current branch
- `git revert commit-hash` — create new commit undoing a commit (safe for public branches)
- `git reset --soft HEAD~1` — undo last commit, keep changes staged
- `git reset --mixed HEAD~1` — undo last commit, keep changes unstaged
- `git reset --hard HEAD~1` — undo last commit, discard changes (destructive)
- `git bisect` — binary search through history to find introducing commit
- `git reflog` — recover lost commits
- `git tag v1.0.0` — create tag
- `git tag -a v1.0.0 -m "Release"` — annotated tag

---

## Level 3 — GitHub

---

### 3.1 GitHub Repository Management

- **Why It Matters:** GitHub is the universal platform for code collaboration and the foundation of your developer portfolio.
- **Prerequisites:** Level 2
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- Repository creation and settings
- README.md importance and writing
- `.gitignore` templates
- License selection
- Repository visibility (public/private)
- Forking vs cloning
- Issue templates
- Repository topics and description

---

### 3.2 Pull Requests & Code Review

- **Why It Matters:** Pull requests are the standard collaboration mechanism in professional teams.
- **Prerequisites:** 3.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Creating pull requests
- PR title and description conventions
- PR templates
- Requesting reviewers
- Code review process:
  - Comments on specific lines
  - Suggesting changes
  - Approve vs Request Changes vs Comment
- Draft PRs
- PR size conventions (keep PRs small)
- Merge strategies: merge commit, squash, rebase
- Branch protection rules:
  - Require PR before merge
  - Require CI checks to pass
  - Require review approvals
  - Require up-to-date branch

---

### 3.3 GitHub Actions (CI/CD)

- **Why It Matters:** GitHub Actions is the most accessible CI/CD platform. Every project should have automated testing and deployment.
- **Prerequisites:** 3.1, Level 1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**Concepts:**
- Workflow: automated process defined in YAML
- Event: trigger for workflow (push, pull_request, schedule, workflow_dispatch)
- Job: set of steps on a runner
- Step: individual task (action or shell command)
- Runner: machine that executes jobs (GitHub-hosted: ubuntu-latest, windows, macos)
- Action: reusable unit (from marketplace or custom)
- Context: workflow data (`github`, `env`, `jobs`, `steps`)

**YAML Syntax:**
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest
```

**Common Workflows:**
- Run tests on PR
- Build and push Docker image
- Deploy to AWS
- Release creation
- Linting and formatting checks

**Actions Marketplace:**
- `actions/checkout` — clone repository
- `actions/setup-python` — install Python version
- `actions/setup-node` — install Node version
- `docker/login-action` — login to Docker registry
- `aws-actions/configure-aws-credentials` — AWS auth

**Secrets & Environment Variables:**
- `${{ secrets.SECRET_NAME }}`
- Repository secrets vs organization secrets vs environment secrets
- `env:` for environment variables

**Matrix Strategy:**
- Test on multiple Python/OS versions

**Artifacts:**
- Upload/download build artifacts between jobs

**Caching:**
- `actions/cache` for pip, npm, Docker layers

---

### 3.4 GitHub for Portfolio

- **Why It Matters:** Recruiters and interviewers look at GitHub profiles. A strong profile is a competitive advantage.
- **Prerequisites:** 3.1
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Profile README
- Contribution graph (green squares)
- Pinned repositories (choose best projects)
- Consistent commit activity
- Writing good READMEs:
  - Project title and description
  - Tech stack badges
  - Setup instructions
  - Screenshots/demo
  - API documentation
  - License
- GitHub Pages for portfolio site

---

## Level 4 — Docker

---

### 4.1 Containers vs Virtual Machines

- **Why It Matters:** Understanding why containers exist explains all of Docker's design decisions.
- **Prerequisites:** Level 1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Virtual Machine: full OS with hypervisor overhead
- Container: processes isolated via Linux namespaces and cgroups
- Container advantages: faster startup, lower overhead, portable
- VM advantages: stronger isolation, different kernels
- Container ≠ VM (common misconception)
- Docker vs Podman vs containerd
- Open Container Initiative (OCI) standards

---

### 4.2 Docker Architecture

- **Why It Matters:** Knowing how Docker works internally helps you understand images, layers, and networking.
- **Prerequisites:** 4.1
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Docker Engine: client-server architecture
- Docker Daemon (`dockerd`) — background service
- Docker Client (`docker`) — CLI
- Docker Hub — default image registry
- Image: read-only template (layers stacked)
- Container: running instance of image (writable layer on top)
- Registry: store and distribute images
- Union file system (overlay2 on Linux)
- Layer caching — why layer order matters

---

### 4.3 Dockerfile

- **Why It Matters:** Dockerfiles define how to build images. Every application you deploy needs one.
- **Prerequisites:** 4.2, Level 1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**Instructions:**
- `FROM image:tag` — base image
- `WORKDIR /app` — set working directory
- `COPY source dest` — copy files
- `ADD source dest` — copy + extract archives (prefer COPY)
- `RUN command` — execute during build
- `ENV VAR=value` — set environment variable
- `ARG name=default` — build-time variable
- `EXPOSE port` — document port (doesn't publish)
- `VOLUME /path` — declare mount point
- `CMD ["executable", "arg"]` — default command (overrideable)
- `ENTRYPOINT ["executable"]` — container entrypoint
- `HEALTHCHECK CMD curl -f http://localhost/ || exit 1`
- `USER username` — run as non-root

**Best Practices:**
- Use specific base image tags (not `latest`)
- Minimize layers (combine RUN commands with `&&`)
- Order layers: least changed → most changed (cache efficiency)
- `.dockerignore` file
- Multi-stage builds (reduce final image size)
- Run as non-root user
- Don't store secrets in Dockerfile

**Python Django Dockerfile Example Pattern:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
```

**Multi-Stage Build:**
```dockerfile
# Build stage
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Final stage
FROM python:3.11-slim
COPY --from=builder /root/.local /root/.local
COPY . /app
```

---

### 4.4 Docker Commands

- **Why It Matters:** Day-to-day Docker usage requires these commands.
- **Prerequisites:** 4.3
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:

**Images:**
- `docker build -t name:tag .` — build image
- `docker images` — list images
- `docker rmi image` — remove image
- `docker pull image:tag` — pull from registry
- `docker push image:tag` — push to registry
- `docker tag source target` — tag image
- `docker image prune` — remove unused images

**Containers:**
- `docker run --name name -p 8000:8000 -d image` — run container
- `docker run -it image bash` — interactive shell
- `docker ps` — running containers
- `docker ps -a` — all containers (including stopped)
- `docker stop container` — graceful stop
- `docker kill container` — force stop
- `docker rm container` — remove stopped container
- `docker rm -f container` — remove running container
- `docker logs container` — view logs
- `docker logs -f container` — follow logs
- `docker exec -it container bash` — shell into running container
- `docker inspect container` — detailed info
- `docker stats` — resource usage
- `docker system prune -a` — remove everything unused

**Volumes:**
- `docker volume create name` — create volume
- `docker volume ls` — list volumes
- `docker run -v volume_name:/path container` — mount volume
- `docker run -v $(pwd):/app container` — bind mount

**Networks:**
- `docker network ls` — list networks
- `docker network create network_name` — create network
- `docker run --network network_name container` — use network

---

### 4.5 Docker Compose

- **Why It Matters:** Multi-container applications (Django + PostgreSQL + Redis + Celery) need Docker Compose to run locally.
- **Prerequisites:** 4.4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**docker-compose.yml structure:**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/dbname
    depends_on:
      - db
      - redis
    command: python manage.py runserver 0.0.0.0:8000

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=dbname
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  celery:
    build: .
    command: celery -A project worker -l info
    depends_on:
      - redis
      - db

volumes:
  postgres_data:
```

**Commands:**
- `docker compose up` — start all services
- `docker compose up -d` — detached mode
- `docker compose down` — stop and remove containers
- `docker compose down -v` — also remove volumes
- `docker compose logs -f` — follow all logs
- `docker compose exec service command` — run command in service
- `docker compose build` — rebuild images
- `docker compose ps` — list services

**Patterns:**
- `env_file:` — load environment from `.env`
- `healthcheck:` — service health
- Service dependencies with `depends_on` + `condition: service_healthy`
- Override files (`docker-compose.override.yml` for local dev)

---

## Level 5 — CI/CD

---

### 5.1 CI/CD Concepts

- **Why It Matters:** CI/CD is standard in professional software development. Understanding it is expected by employers.
- **Prerequisites:** Level 3, Level 4
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- **Continuous Integration (CI):**
  - Automatically build and test on every commit
  - Detect integration issues early
  - Maintain a deployable main branch
- **Continuous Delivery (CD):**
  - Every commit is deployable to production
  - Deployment is manual trigger
- **Continuous Deployment:**
  - Every passing commit automatically deploys to production
- Benefits: faster release cycles, fewer bugs, reduced risk
- Pipeline stages: Source → Build → Test → Package → Deploy

---

### 5.2 GitHub Actions Deep Dive

- **Why It Matters:** GitHub Actions is the most common CI/CD tool for open source and startups.
- **Prerequisites:** 3.3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics (extending 3.3):

**Django CI Pipeline:**
```yaml
name: Django CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Cache pip
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: pip-${{ hashFiles('requirements.txt') }}
      - run: pip install -r requirements.txt
      - run: python manage.py test
        env:
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/test_db
```

**Deployment Pipeline:**
- Build Docker image
- Push to ECR (AWS) or DockerHub
- SSH deploy or ECS task update

**Deployment Strategies:**
- **Rolling:** update instances one by one
- **Blue-Green:** two identical environments, switch traffic
- **Canary:** route small % traffic to new version first

---

### 5.3 Environment Management

- **Why It Matters:** Professional applications have multiple environments. Managing them correctly prevents deploying dev code to production.
- **Prerequisites:** 5.1
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- Environment types: development, staging, production
- Environment parity (keep environments similar — 12-Factor #10)
- GitHub Environments (required reviewers, deployment protection rules)
- Environment-specific secrets
- Database per environment
- Feature flags for environment-specific behavior
- Configuration management: environment variables, `.env` files, secrets manager

---

## Level 6 — Cloud Fundamentals (AWS)

---

### 6.1 Cloud Computing Model

- **Why It Matters:** Understanding what cloud computing provides helps you choose the right services.
- **Prerequisites:** Level 5
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- On-premise vs Cloud: capital expense vs operational expense
- Shared responsibility model (AWS manages infrastructure; you manage data)
- **IaaS (Infrastructure as a Service):** EC2, VPC — raw compute/network
- **PaaS (Platform as a Service):** Elastic Beanstalk, RDS — managed platform
- **SaaS (Software as a Service):** end-user applications
- Cloud benefits: scalability, availability, cost efficiency, global reach
- AWS Global Infrastructure:
  - Regions: geographic areas (us-east-1, ap-south-1)
  - Availability Zones (AZ): isolated data centers within a region
  - Edge Locations: CDN endpoints

---

### 6.2 IAM (Identity & Access Management)

- **Why It Matters:** IAM controls who can do what in AWS. Security starts here.
- **Prerequisites:** 6.1
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- IAM Users: long-term credentials (human users)
- IAM Groups: collection of users with shared permissions
- IAM Roles: temporary credentials (EC2 instance role, Lambda role, cross-account)
- IAM Policies: JSON documents defining permissions
- Policy types: AWS managed, customer managed, inline
- Principle of least privilege
- Access keys vs role-based access (prefer roles)
- MFA for IAM users
- `aws configure` — CLI credentials setup
- Service control policies (SCP) in Organizations
- IAM best practices

---

### 6.3 EC2 (Elastic Compute Cloud)

- **Why It Matters:** EC2 is the foundational compute service. Django applications often run on EC2.
- **Prerequisites:** 6.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Instance types: t2/t3 (general), m5 (compute), r5 (memory), c5 (CPU)
- Instance lifecycle: launch, start, stop, reboot, terminate
- AMI (Amazon Machine Image): template for instances
- Key pairs: SSH access
- Security Groups: virtual firewall (stateful, allow-only rules)
- Elastic IP: static public IP
- User data: bootstrap scripts on first launch
- EC2 placement groups
- Auto Scaling Groups (ASG): automatically adjust instance count
- Launch templates
- Spot instances: cheaper, interruptible
- Reserved instances: 1-3 year commitment, cheaper

---

### 6.4 S3 (Simple Storage Service)

- **Why It Matters:** Django media files, static files, backups, and data lake storage all use S3.
- **Prerequisites:** 6.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Buckets: containers for objects
- Objects: files + metadata
- Object key: unique identifier within bucket (acts as file path)
- Storage classes: Standard, Standard-IA, Glacier, Glacier Deep Archive
- Bucket policies vs ACLs
- Versioning
- Server-side encryption (SSE-S3, SSE-KMS)
- Pre-signed URLs (temporary access)
- CORS configuration for direct uploads
- Static website hosting
- S3 with Django: `django-storages` + `boto3`
- Lifecycle policies (auto-move to cheaper storage)

---

### 6.5 RDS (Relational Database Service)

- **Why It Matters:** Managed PostgreSQL on RDS is the production database for most Django applications.
- **Prerequisites:** 6.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- RDS benefits: automated backups, patching, failover
- Supported engines: PostgreSQL, MySQL, MariaDB, Oracle, SQL Server
- Instance types and storage
- Multi-AZ deployment (automatic failover)
- Read replicas (horizontal read scaling)
- Parameter groups and option groups
- Security: VPC, security groups, encryption at rest
- Backups: automated (1-35 days retention) + manual snapshots
- Connecting from EC2: endpoint + port + credentials
- Performance Insights
- RDS vs Aurora (Aurora: managed, 5x faster, more expensive)

---

### 6.6 VPC (Virtual Private Cloud)

- **Why It Matters:** VPC is the network container for all AWS resources. Every production deployment uses one.
- **Prerequisites:** 6.2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- VPC: isolated virtual network
- CIDR block: IP range for VPC (10.0.0.0/16)
- Subnets: subdivision of VPC
  - Public subnet: has internet gateway route
  - Private subnet: no direct internet access
- Internet Gateway (IGW): internet access for VPC
- NAT Gateway: outbound internet for private subnets
- Route tables: define traffic routing
- Security Groups: instance-level firewall (stateful)
- Network ACLs: subnet-level firewall (stateless)
- VPC Peering: connect two VPCs
- Common pattern: public subnet (load balancer) + private subnets (app servers, database)

---

### 6.7 Load Balancers (ELB)

- **Why It Matters:** Load balancers distribute traffic across multiple instances for availability and scale.
- **Prerequisites:** 6.3, 6.6
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- ALB (Application Load Balancer): HTTP/HTTPS, path-based routing, host-based routing
- NLB (Network Load Balancer): TCP/UDP, ultra-high performance, static IP
- Target groups: set of instances/containers/IPs
- Health checks: deregister unhealthy targets
- SSL/TLS termination at load balancer
- Sticky sessions
- ALB access logs

---

### 6.8 Route 53

- **Why It Matters:** DNS management for your domain in AWS.
- **Prerequisites:** Networks — DNS knowledge
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Hosted zones
- DNS record management
- Routing policies: Simple, Weighted, Latency-based, Failover, Geolocation
- Health checks and DNS failover
- Domain registration
- Alias records (Route 53 extension — free queries)
- `www` + apex domain setup

---

### 6.9 CloudWatch

- **Why It Matters:** Monitoring and alerting for AWS resources and your applications.
- **Prerequisites:** 6.3
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- Metrics: collected for AWS resources (CPU, network, disk)
- Custom metrics: send application metrics
- Logs: collect application logs
- Log groups and log streams
- Log Insights: query logs
- Alarms: trigger on metric threshold
- Dashboards: visualize metrics
- CloudWatch agent on EC2: collect OS-level metrics
- Pricing: logs retention cost

---

## Level 7 — Application Deployment

---

### 7.1 Deploying Django to Production

- **Why It Matters:** The complete production deployment is the most critical practical skill.
- **Prerequisites:** Full Level 4, Level 6
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**Application Server:**
- WSGI: Python web server interface standard
- Gunicorn: Python WSGI HTTP server
  - `gunicorn project.wsgi:application --bind 0.0.0.0:8000`
  - Workers: `2 * num_cpus + 1` (rule of thumb)
  - Worker classes: sync, gthread, gevent, uvicorn (async)
  - Timeout configuration
  - Access and error logging
- uWSGI: alternative (more complex, more powerful)

**Nginx as Reverse Proxy:**
- Why Nginx (handles static files, TLS, load balancing, compression)
- Basic Nginx configuration for Django
- `proxy_pass http://127.0.0.1:8000`
- Static files served directly by Nginx
- Gzip compression
- Rate limiting in Nginx
- Security headers

**Complete Stack:**
```
Client → Nginx (port 80/443) → Gunicorn (port 8000) → Django → PostgreSQL
                                                              → Redis (cache, Celery broker)
                                                              → S3 (media/static)
```

**Deployment Checklist:**
- `DEBUG = False`
- `ALLOWED_HOSTS` set correctly
- Database credentials in environment variables
- `SECRET_KEY` in environment variable
- `collectstatic` run
- Migrations applied
- SSL certificate installed
- Nginx serving static/media files
- Gunicorn running as systemd service
- Firewall configured

---

### 7.2 SSL/TLS Setup

- **Why It Matters:** Production sites must use HTTPS.
- **Prerequisites:** 7.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- Let's Encrypt: free, automated SSL certificates
- `certbot` CLI tool
  - `certbot --nginx -d domain.com -d www.domain.com`
  - Auto-renewal with cron or systemd timer
- Nginx SSL configuration (certbot modifies automatically)
- Certificate expiry monitoring
- `SECURE_SSL_REDIRECT = True` in Django
- `SECURE_HSTS_SECONDS` in Django settings

---

### 7.3 Zero-Downtime Deployment

- **Why It Matters:** Production deployments cannot take the application offline.
- **Prerequisites:** 7.1
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Why zero-downtime matters
- Gunicorn graceful reload (`kill -HUP PID`)
- Blue-Green deployment on EC2
- Database migrations without downtime:
  - Backward-compatible migrations
  - Multi-phase migration approach
  - Django `--fake-initial`
- Load balancer draining connections before update

---

## Level 8 — Infrastructure as Code (Awareness Level)

---

### 8.1 Terraform Basics

- **Why It Matters:** IaC is the professional standard for cloud provisioning. Awareness required; deep expertise not needed at junior level.
- **Prerequisites:** Level 6
- **Interview Importance:** Medium
- **Job Importance:** Medium (growing)

Topics:
- IaC concept: describe infrastructure in code, version control it
- Terraform HCL syntax basics
- `terraform init`, `terraform plan`, `terraform apply`, `terraform destroy`
- Providers (AWS provider)
- Resources: `resource "aws_instance" "web" { ... }`
- Variables and outputs
- State file (`.tfstate`) — keep in S3 backend
- Modules: reusable infrastructure components
- Workspaces: multiple environments
- Drift detection

---

### 8.2 AWS CloudFormation (Awareness)

- **Why It Matters:** AWS native IaC tool. Many enterprise AWS environments use CloudFormation.
- **Prerequisites:** 8.1
- **Interview Importance:** Low-Medium
- **Job Importance:** Low-Medium

Topics:
- CloudFormation templates (YAML/JSON)
- Stacks
- Resources, Parameters, Outputs, Conditions
- Change sets (preview before apply)
- CDK (Cloud Development Kit): define CloudFormation with Python/TypeScript

---

## Level 9 — Monitoring & Observability

---

### 9.1 The Three Pillars of Observability

- **Why It Matters:** You can't manage what you can't measure. Production systems require observability.
- **Prerequisites:** Level 7
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- **Logs:** timestamped events from your application
- **Metrics:** numerical measurements over time (CPU, request rate, error rate)
- **Traces:** end-to-end path of a request through distributed systems
- Difference: logs tell you what happened, metrics tell you how much, traces tell you where

---

### 9.2 Application Logging

- **Why It Matters:** Logs are your only window into production problems.
- **Prerequisites:** 9.1, Python logging
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- Structured logging (JSON format) vs unstructured text
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Django logging configuration in `settings.py`
- What to log: requests, responses (sanitized), errors, important events
- What NOT to log: passwords, tokens, PII
- Log aggregation:
  - CloudWatch Logs (AWS)
  - ELK Stack (Elasticsearch, Logstash, Kibana) — awareness
  - Loki + Grafana — awareness
- Log retention policies

---

### 9.3 Error Tracking with Sentry

- **Why It Matters:** Sentry catches production errors with stack traces before users report them.
- **Prerequisites:** 9.2
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Sentry SDK integration with Django: `sentry_sdk.init(dsn=...)`
- Error capture with context
- Issue grouping and deduplication
- Alert rules and notifications
- Performance monitoring
- Source maps for frontend
- Environments (production vs staging)
- Sentry vs Rollbar vs Bugsnag

---

### 9.4 Metrics & Alerting

- **Why It Matters:** Metrics trigger alerts before outages become severe.
- **Prerequisites:** 9.1
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Key metrics to monitor:
  - Response time (P50, P95, P99)
  - Error rate (4xx, 5xx)
  - Request throughput
  - Database query time
  - CPU and memory utilization
  - Celery queue depth
- CloudWatch Alarms
- SNS notifications (email, Slack integration)
- Grafana dashboards (conceptual)
- Prometheus (conceptual)
- Uptime monitoring: UptimeRobot, Pingdom

---

### 9.5 Performance Profiling

- **Why It Matters:** Django applications slow down. Knowing how to find and fix bottlenecks is a production skill.
- **Prerequisites:** Level 7
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `django-debug-toolbar` for development
- N+1 query detection
- `django-silk` — production profiling
- Python `cProfile` and `profile`
- `py-spy` — sampling profiler (minimal overhead)
- APM tools: New Relic, Datadog, Elastic APM
- Database query analysis with `EXPLAIN ANALYZE`

---

*This is the knowledge inventory for Cloud & Deployment. Roadmap and scheduling are managed separately.*
