# Backend Engineering Syllabus — Mahesh Career OS

> **Goal:** Become a production-capable backend developer using Python/Django.
> **Target Stack:** Python, Django, DRF, PostgreSQL, Redis, Docker.
> **Scope:** Web fundamentals through production deployment concepts.

---

## Mastery Level Structure

| Tier | Name | Capability Unlocked |
|------|------|-------------------|
| Tier 1 | Internet & Web Fundamentals | Understand how the web works |
| Tier 2 | API Design | Design and build REST APIs |
| Tier 3 | Authentication & Authorization | Secure any system |
| Tier 4 | Django Framework | Build full web applications |
| Tier 5 | Django REST Framework | Build professional REST APIs |
| Tier 6 | Database Integration | Query and optimize at scale |
| Tier 7 | Caching | Build performant systems |
| Tier 8 | Task Queues | Handle background work |
| Tier 9 | Architecture | Design scalable systems |
| Tier 10 | Production | Ship and maintain real software |

---

## Tier 1 — Internet & Web Fundamentals

> *You cannot build backend systems without understanding what happens when a browser sends a request. This is the mental model that everything else builds on.*

---

### T1.1 How the Internet Works

- **Why It Matters:** Debugging production issues, understanding latency, designing systems — all require knowing what happens at every layer.
- **Prerequisites:** None
- **Interview Importance:** High — extremely common as a "explain X" question
- **Job Importance:** Critical

Topics:
- What happens when you type `google.com` (complete walkthrough)
- Internet vs World Wide Web
- IP addresses (IPv4, IPv6)
- Domain names and DNS resolution
- Packets and packet switching
- Routers and routing
- ISPs and the physical internet
- CDNs and caching at network level
- Bandwidth vs latency

---

### T1.2 Client-Server Architecture

- **Why It Matters:** Backend development IS client-server architecture. Every request-response cycle follows this model.
- **Prerequisites:** T1.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Client vs Server roles
- Request-Response cycle (end-to-end)
- Stateless vs Stateful servers
- Server-Side Rendering vs API-based (SPA) architecture
- Thin client vs Thick client
- Peer-to-peer vs client-server
- Web server vs Application server vs Database server

---

### T1.3 HTTP Protocol

- **Why It Matters:** HTTP is the language of the web. Every API call, every web request uses HTTP. Deep HTTP knowledge separates good developers from great ones.
- **Prerequisites:** T1.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**HTTP Basics:**
- HTTP request structure (method, URL, version, headers, body)
- HTTP response structure (status line, headers, body)
- Stateless nature of HTTP

**HTTP Methods:**
- GET — retrieve resources, safe and idempotent
- POST — create resources, not idempotent
- PUT — replace entire resource, idempotent
- PATCH — partial update, not necessarily idempotent
- DELETE — remove resource, idempotent
- HEAD — headers only, no body
- OPTIONS — CORS preflight

**HTTP Status Codes:**
- 1xx — Informational (100 Continue)
- 2xx — Success (200 OK, 201 Created, 204 No Content)
- 3xx — Redirection (301 Permanent, 302 Temporary, 304 Not Modified)
- 4xx — Client Error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 405 Method Not Allowed, 409 Conflict, 422 Unprocessable Entity, 429 Too Many Requests)
- 5xx — Server Error (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout)

**Headers (Common):**
- `Content-Type`, `Content-Length`
- `Authorization`
- `Accept`, `Accept-Language`
- `Cache-Control`, `ETag`, `Last-Modified`
- `X-Request-ID`, `X-Forwarded-For`
- `CORS` headers (`Origin`, `Access-Control-Allow-Origin`)

**HTTP Versions:**
- HTTP/1.1 — persistent connections, pipelining
- HTTP/2 — multiplexing, header compression, server push
- HTTP/3 — QUIC protocol, UDP-based

---

### T1.4 HTTPS & TLS/SSL

- **Why It Matters:** Every production API uses HTTPS. Understanding TLS is required for setup and debugging.
- **Prerequisites:** T1.3
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Why HTTP is insecure (plaintext)
- What TLS provides (confidentiality, integrity, authentication)
- TLS handshake (simplified)
- SSL certificates — what they are
- Certificate Authorities (CA)
- Self-signed vs CA-signed certificates
- Let's Encrypt (free certs)
- HSTS (HTTP Strict Transport Security)
- Mixed content warnings
- Certificate pinning (awareness)

---

### T1.5 URLs & URIs

- **Why It Matters:** Every API endpoint is a URL. Understanding URL structure is fundamental to API design.
- **Prerequisites:** T1.3
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- URL structure: scheme://host:port/path?query#fragment
- URI vs URL vs URN
- URL encoding (percent encoding)
- Query string parameters
- Path parameters vs query parameters — when to use each
- URL normalization
- Absolute vs relative URLs
- URL design best practices

---

### T1.6 Cookies

- **Why It Matters:** Cookies power session-based authentication, user preferences, and tracking. Required for understanding auth systems.
- **Prerequisites:** T1.3
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- What cookies are (key-value pairs stored in browser)
- Cookie attributes: `Domain`, `Path`, `Expires`, `Max-Age`
- Security attributes: `Secure`, `HttpOnly`, `SameSite`
- Session cookies vs persistent cookies
- Third-party cookies
- Cookie size limits
- Cookie-based authentication flow
- CSRF attacks and SameSite protection

---

### T1.7 Sessions

- **Why It Matters:** Server-side session management is one of the two major authentication paradigms. Django uses sessions by default.
- **Prerequisites:** T1.6
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Stateful authentication concept
- Session ID — what it is
- Session storage: in-memory, database, Redis, filesystem
- Session lifecycle (create, validate, expire, destroy)
- Django sessions framework
- Session security considerations
- Sessions vs JWT (tradeoffs)

---

## Tier 2 — API Design

---

### T2.1 What is an API

- **Why It Matters:** Backend developers build APIs. You need to be able to explain and design them fluently.
- **Prerequisites:** Tier 1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- API definition (Application Programming Interface)
- Why APIs exist (separation of concerns, third-party integration)
- Types of APIs (REST, GraphQL, gRPC, SOAP)
- Public vs Private vs Partner APIs
- API contracts
- Forward vs backward compatibility

---

### T2.2 REST Architecture

- **Why It Matters:** REST is the dominant paradigm for web APIs. Understanding its constraints explains why APIs are designed the way they are.
- **Prerequisites:** T2.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**REST Constraints (Fielding's 6):**
1. Client-Server separation
2. Statelessness — server stores no client context
3. Cacheability
4. Uniform Interface
5. Layered System
6. Code on Demand (optional)

**Resource Design:**
- Resources as nouns (not verbs)
- URI design: `/users/{id}/orders/{order_id}`
- Plural vs singular resource naming
- Resource relationships in URLs
- Avoiding RPC-style URLs

**REST Maturity Model (Richardson):**
- Level 0 — HTTP as a transport
- Level 1 — Resources
- Level 2 — HTTP verbs
- Level 3 — Hypermedia (HATEOAS)

---

### T2.3 RESTful API Design

- **Why It Matters:** Poor API design creates maintenance nightmares. Good design makes APIs intuitive, consistent, and evolvable.
- **Prerequisites:** T2.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Resource naming conventions
- URL hierarchy depth (keep shallow)
- Query parameters for filtering, sorting, searching
- Response structure consistency
- Envelope pattern vs plain responses
- Partial responses (field selection)
- API versioning strategies (URL path, header, query param)
- Error response format (consistent error objects)
- OpenAPI / Swagger documentation
- API-first design approach

---

### T2.4 Pagination

- **Why It Matters:** Every API that returns lists needs pagination. Without it, large datasets crash servers.
- **Prerequisites:** T2.3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Why pagination is mandatory
- Page Number Pagination (`?page=2&page_size=20`)
- Limit-Offset Pagination (`?limit=20&offset=40`)
- Cursor-Based Pagination (for large datasets, real-time data)
- Response metadata (count, next, previous, total)
- DRF pagination classes
- Performance implications of OFFSET at scale

---

### T2.5 Rate Limiting

- **Why It Matters:** Rate limiting prevents API abuse, DDoS, and ensures fair usage. Every production API has it.
- **Prerequisites:** T2.3
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Why rate limiting is needed
- Strategies: fixed window, sliding window, token bucket, leaky bucket
- Response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`
- 429 Too Many Requests
- DRF throttling
- Rate limiting by user vs by IP
- Redis for rate limit counting

---

### T2.6 API Documentation

- **Why It Matters:** APIs without documentation can't be used by others (or by you in 3 months).
- **Prerequisites:** T2.3
- **Interview Importance:** Low-Medium
- **Job Importance:** High

Topics:
- OpenAPI Specification (OAS / Swagger)
- YAML vs JSON for OpenAPI
- `drf-spectacular` for auto-generation
- Swagger UI
- ReDoc
- Documenting authentication, parameters, responses, error codes

---

## Tier 3 — Authentication & Authorization

---

### T3.1 Authentication vs Authorization

- **Why It Matters:** These are confused constantly. Getting them wrong is a security vulnerability.
- **Prerequisites:** Tier 1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Authentication: "Who are you?" — identity verification
- Authorization: "What can you do?" — permission checking
- Authentication factors (something you know, have, are)
- Multi-Factor Authentication (MFA)
- Authentication before authorization
- Common mistakes (authentication as authorization)

---

### T3.2 Password Security

- **Why It Matters:** Storing plain-text passwords is a career-ending security failure. This is fundamental.
- **Prerequisites:** T3.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Never store plain-text passwords
- Hashing vs Encryption (difference)
- Salting (prevents rainbow table attacks)
- bcrypt algorithm (adaptive, slow by design)
- argon2 (recommended modern algorithm)
- Django's password hasher
- Password strength requirements
- Breach detection (Have I Been Pwned API)

---

### T3.3 Session-Based Authentication

- **Why It Matters:** Django's default auth system uses sessions. You must understand how to implement, secure, and debug it.
- **Prerequisites:** T1.7, T3.2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Login flow (credential → session ID → cookie)
- Django's `authenticate()` and `login()`
- Django's `logout()`
- `request.user`
- Session expiry
- Remember me functionality
- Concurrent sessions
- Session fixation attack prevention

---

### T3.4 JWT — JSON Web Tokens

- **Why It Matters:** JWT is the dominant token mechanism for SPAs, mobile apps, and microservices. DRF SimpleJWT is the standard.
- **Prerequisites:** T3.1, T3.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**JWT Structure:**
- Header (algorithm, type)
- Payload (claims: sub, iat, exp, custom)
- Signature

**JWT Types:**
- Access Token — short-lived (15min-1hr)
- Refresh Token — long-lived (days-weeks)

**JWT Lifecycle:**
- Login → generate access + refresh tokens
- API request → send access token in `Authorization: Bearer <token>` header
- Access token expired → use refresh token to get new access token
- Logout → revoke refresh token

**Security:**
- JWT signing algorithms (HS256 vs RS256)
- Token expiry
- Token revocation challenges
- Where to store tokens (HttpOnly cookie vs localStorage)
- JWT vs session tradeoffs

**Implementation:**
- `djangorestframework-simplejwt`
- Custom claims
- Blacklisting tokens

---

### T3.5 OAuth 2.0

- **Why It Matters:** "Login with Google/GitHub" is OAuth. Social login is a standard feature in modern applications.
- **Prerequisites:** T3.4
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- OAuth 2.0 purpose (delegated authorization)
- Roles: Resource Owner, Client, Authorization Server, Resource Server
- Authorization Code Flow (web apps)
- Authorization Code + PKCE (mobile/SPA)
- Client Credentials Flow (machine-to-machine)
- Access Token, Refresh Token, ID Token (OIDC)
- OpenID Connect (OIDC) — authentication on top of OAuth
- `django-allauth` for social login
- Scope-based permissions

---

### T3.6 Role-Based Access Control (RBAC)

- **Why It Matters:** Every application with multiple user types needs RBAC. It's the standard permission model.
- **Prerequisites:** T3.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Roles vs Permissions (roles are groups of permissions)
- Django's permission system
- `user.has_perm('app.action_model')`
- Django Groups
- Custom permission classes in DRF
- Object-level permissions
- `django-guardian` for object-level permissions
- Attribute-Based Access Control (ABAC) — awareness

---

### T3.7 Security Vulnerabilities

- **Why It Matters:** Backend developers are the last line of defense. Knowing attack vectors lets you build secure systems.
- **Prerequisites:** Tier 1, Tier 3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- SQL Injection — parameterized queries prevention
- XSS (Cross-Site Scripting) — output escaping, CSP
- CSRF (Cross-Site Request Forgery) — CSRF tokens, SameSite cookies
- IDOR (Insecure Direct Object Reference)
- Broken Authentication
- Sensitive Data Exposure
- Security Misconfiguration
- Django security checklist
- OWASP Top 10 awareness

---

## Tier 4 — Django Framework

---

### T4.1 Django Project Structure

- **Why It Matters:** Understanding project layout is the first step to navigating any Django codebase.
- **Prerequisites:** Python Level 4+
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `django-admin startproject` output
- `manage.py` — command interface
- `settings.py` — configuration
- `urls.py` — URL routing
- `wsgi.py` / `asgi.py`
- Apps vs Project
- `django-admin startapp` output
- App structure (models, views, urls, admin, serializers)
- Settings splitting (base, dev, prod)

---

### T4.2 Django Settings & Configuration

- **Why It Matters:** Misconfigured settings cause security vulnerabilities and deployment failures.
- **Prerequisites:** T4.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `INSTALLED_APPS`
- `DATABASES` configuration
- `MIDDLEWARE`
- `STATIC_ROOT`, `MEDIA_ROOT`
- `SECRET_KEY` security
- `DEBUG` flag — never True in production
- `ALLOWED_HOSTS`
- `TIME_ZONE` and `USE_TZ`
- `CORS_ALLOWED_ORIGINS`
- Django settings with environment variables
- Settings for testing

---

### T4.3 URL Routing

- **Why It Matters:** URL routing maps HTTP requests to handlers. Every API endpoint requires a URL config.
- **Prerequisites:** T4.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `urlpatterns` list
- `path()` and `re_path()`
- Path converters (`<int:pk>`, `<str:slug>`, `<uuid:id>`)
- `include()` for app-level URLs
- URL namespacing
- URL reversing (`reverse()`, `reverse_lazy()`)
- URL ordering (first match wins)

---

### T4.4 Views

- **Why It Matters:** Views are where business logic lives. Understanding FBVs and CBVs is essential for reading Django code.
- **Prerequisites:** T4.3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**Function-Based Views (FBVs):**
- Request object (method, GET, POST, body, user, FILES)
- `HttpResponse`, `JsonResponse`
- `render()`, `redirect()`
- HTTP method branching
- `@require_http_methods` decorator
- `@login_required` decorator

**Class-Based Views (CBVs):**
- `View` base class
- `dispatch()` method
- `get()`, `post()`, etc.
- Built-in generic views (`TemplateView`, `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`)
- Mixins
- CBV vs FBV tradeoffs

---

### T4.5 Django ORM

- **Why It Matters:** Django ORM is the primary way to interact with the database. Every Django developer needs deep ORM knowledge.
- **Prerequisites:** T4.4, SQL knowledge
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**Model Definition:**
- `models.Model`
- Field types (CharField, IntegerField, DateTimeField, BooleanField, TextField, DecimalField, UUIDField, etc.)
- Field options (null, blank, default, unique, db_index)
- `Meta` class (ordering, constraints, db_table)
- `__str__` method

**Relationships:**
- `ForeignKey` (many-to-one) — `on_delete` options
- `ManyToManyField`
- `OneToOneField`
- Reverse relations and `related_name`

**QuerySets:**
- `all()`, `filter()`, `exclude()`
- `get()` vs `filter()` (single vs multiple)
- `create()`, `save()`, `delete()`
- Chaining querysets
- `first()`, `last()`, `count()`
- `exists()`
- `values()`, `values_list()`
- `annotate()` and `aggregate()`
- `order_by()`

**Lookup Expressions:**
- `field__exact`, `field__iexact`
- `field__contains`, `field__icontains`
- `field__startswith`, `field__endswith`
- `field__gt`, `field__gte`, `field__lt`, `field__lte`
- `field__in`, `field__range`
- `field__isnull`
- `field__date`, `field__year`, `field__month`

**Q Objects:**
- `Q()` for complex OR/AND queries
- Combining Q objects (`|`, `&`, `~`)

**F Expressions:**
- Atomic database operations
- Avoiding race conditions

**Optimization:**
- `select_related()` — prevents N+1 for ForeignKey/OneToOne
- `prefetch_related()` — prevents N+1 for ManyToMany/reverse FK
- `only()` and `defer()` — column selection
- `QuerySet.explain()` — query analysis
- Identifying N+1 with `django-debug-toolbar`

**Transactions:**
- `transaction.atomic()`
- `select_for_update()`
- Savepoints

---

### T4.6 Migrations

- **Why It Matters:** Migrations are how schema changes are managed in production. Getting them wrong breaks databases.
- **Prerequisites:** T4.5
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `makemigrations` vs `migrate`
- Migration files (operations, dependencies)
- `RunPython` for data migrations
- `RunSQL`
- Squashing migrations
- Migration conflicts and resolution
- Fake migrations
- Zero-downtime migration strategies
- Rollback considerations
- Initial data with fixtures

---

### T4.7 Django Admin

- **Why It Matters:** Django admin provides instant CRUD interfaces. Customizing it is a common interview and job task.
- **Prerequisites:** T4.5
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Registering models
- `ModelAdmin` customization
- `list_display`, `list_filter`, `search_fields`
- `readonly_fields`
- Custom actions
- Inline admins
- Custom forms in admin
- Admin security (keeping it protected)

---

### T4.8 Middleware

- **Why It Matters:** Middleware processes every request and response. Authentication, logging, CORS, session management — all middleware.
- **Prerequisites:** T4.4
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Request-response middleware cycle
- Django's built-in middleware (SecurityMiddleware, SessionMiddleware, CommonMiddleware, CSRF, AuthenticationMiddleware)
- Writing custom middleware (function-style and class-style)
- Middleware ordering importance
- CORS middleware (`django-cors-headers`)
- Request logging middleware

---

### T4.9 Static & Media Files

- **Why It Matters:** Every web application serves static files (CSS, JS) and user uploads. Misconfiguring this breaks production.
- **Prerequisites:** T4.2
- **Interview Importance:** Low-Medium
- **Job Importance:** High

Topics:
- `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS`
- `collectstatic` command
- `MEDIA_URL`, `MEDIA_ROOT`
- Serving media in development
- `ImageField` and `FileField`
- Serving static files in production (Nginx, WhiteNoise, S3)
- CDN integration

---

### T4.10 Django Authentication System

- **Why It Matters:** Django ships with a complete auth system. Using it properly saves enormous time.
- **Prerequisites:** T4.5, Tier 3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `AbstractUser` vs `AbstractBaseUser`
- Custom User model (must do before first migration)
- User creation and management
- `authenticate()`, `login()`, `logout()`
- `@login_required`, `LoginRequiredMixin`
- Password change and reset views
- Email confirmation (django-allauth)
- `request.user.is_authenticated`

---

## Tier 5 — Django REST Framework (DRF)

---

### T5.1 DRF Overview & Setup

- **Why It Matters:** DRF is the standard for building REST APIs in Django. Nearly every Django API job uses it.
- **Prerequisites:** Tier 4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Installation and `REST_FRAMEWORK` settings
- `DEFAULT_AUTHENTICATION_CLASSES`
- `DEFAULT_PERMISSION_CLASSES`
- `DEFAULT_PAGINATION_CLASS`
- DRF's request object (`request.data`, `request.query_params`)
- Browsable API

---

### T5.2 Serializers

- **Why It Matters:** Serializers are the core of DRF. They handle validation, deserialization (input), and serialization (output).
- **Prerequisites:** T5.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**Serializer:**
- Field types and options
- `validate_<field>()` method
- `validate()` method (cross-field)
- `create()` and `update()` methods
- `to_representation()` override

**ModelSerializer:**
- `Meta.model` and `Meta.fields`
- `read_only_fields`, `extra_kwargs`
- Auto-generated fields from model
- `depth` option

**Nested Serializers:**
- Nested read-only serializers
- Writable nested serializers
- SerializerMethodField
- Serializer inheritance

**Performance:**
- Avoiding N+1 in serializers
- `source` parameter
- Optimizing queryset for serializer

---

### T5.3 Views & ViewSets

- **Why It Matters:** DRF provides multiple view layers — choosing the right one affects code complexity and flexibility.
- **Prerequisites:** T5.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**APIView:**
- HTTP method handlers (`get`, `post`, etc.)
- Manual serializer usage
- Manual queryset filtering
- Full control

**Generic Views:**
- `ListAPIView`, `CreateAPIView`, `RetrieveAPIView`, `UpdateAPIView`, `DestroyAPIView`
- `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`
- `queryset` and `serializer_class` attributes
- `get_queryset()` override
- `perform_create()`, `perform_update()`

**ViewSets:**
- `ViewSet` (manual)
- `ModelViewSet` (full CRUD)
- `ReadOnlyModelViewSet`
- Custom actions with `@action`
- Routers

**When to use what:**
- APIView → full control, complex logic
- Generic views → CRUD with customization
- ViewSets + Routers → pure CRUD at scale

---

### T5.4 Routers

- **Why It Matters:** Routers auto-generate URL patterns for ViewSets. They reduce URL boilerplate by 80%.
- **Prerequisites:** T5.3
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `DefaultRouter` vs `SimpleRouter`
- Registering ViewSets
- Auto-generated URL patterns
- Nested routers (`drf-nested-routers`)
- Custom route naming

---

### T5.5 Permissions

- **Why It Matters:** Every API endpoint needs permission logic. DRF's permission system is flexible and composable.
- **Prerequisites:** T5.3, T3.6
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Built-in permission classes: `IsAuthenticated`, `IsAdminUser`, `AllowAny`, `IsAuthenticatedOrReadOnly`
- Custom permission classes (`has_permission`, `has_object_permission`)
- Object-level permissions
- Composing permissions (`AND`, `OR` — DRF 3.9+)
- Permission class ordering
- Row-level security patterns

---

### T5.6 Authentication in DRF

- **Why It Matters:** API authentication is different from session auth. DRF supports multiple schemes simultaneously.
- **Prerequisites:** T5.5, T3.4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `SessionAuthentication`
- `TokenAuthentication` (DRF built-in)
- `JWTAuthentication` (SimpleJWT)
- Basic Authentication (testing only)
- Custom authentication backends
- Multiple authentication classes (DRF tries each in order)
- `request.auth` and `request.user`

---

### T5.7 Throttling

- **Why It Matters:** API abuse protection. Required for production APIs exposed to the internet.
- **Prerequisites:** T5.3, T2.5
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `AnonRateThrottle`
- `UserRateThrottle`
- `ScopedRateThrottle`
- Custom throttle classes
- Rate limit configuration
- Response headers

---

### T5.8 Filtering & Search

- **Why It Matters:** Every API that returns lists needs filtering. Without it, clients must download everything and filter client-side.
- **Prerequisites:** T5.3
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `django-filter` integration
- `DjangoFilterBackend`
- `SearchFilter` (icontains on specified fields)
- `OrderingFilter`
- Custom filter backends
- Filter by related field
- Complex filter sets

---

## Tier 6 — Database Integration

---

### T6.1 ORM vs Raw SQL

- **Why It Matters:** ORMs handle 90% of queries, but raw SQL is needed for complex analytics, bulk operations, and optimization.
- **Prerequisites:** Tier 4, SQL knowledge
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- When ORM is sufficient
- When raw SQL is better
- `Manager.raw()` — raw SQL returning model instances
- `connection.cursor()` — fully raw SQL
- Parameterized queries (SQL injection prevention)
- Django's queryset to SQL (`queryset.query`)

---

### T6.2 Query Optimization

- **Why It Matters:** Slow queries kill applications. Optimization is one of the most valuable backend skills.
- **Prerequisites:** T6.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- N+1 problem (the most common Django performance issue)
- `select_related()` for ForeignKey/OneToOne
- `prefetch_related()` for ManyToMany/reverse FK
- `only()` and `defer()` for column selection
- `values()` and `values_list()` for lightweight queries
- Database indexes (when to add, how to analyze)
- `QuerySet.explain()` for query plans
- `django-debug-toolbar` for query inspection
- Bulk operations (`bulk_create`, `bulk_update`)
- `update()` vs `.save()` for single-field updates

---

### T6.3 Connection Pooling

- **Why It Matters:** Opening a new DB connection for every request is expensive. Pooling dramatically improves throughput.
- **Prerequisites:** T6.1
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- What connection pooling is
- `django-db-geventpool`
- `pgBouncer` (external pooler)
- Pool size configuration
- Connection timeouts
- Production recommendations

---

## Tier 7 — Caching

---

### T7.1 Caching Concepts

- **Why It Matters:** Caching is the most powerful performance tool. The difference between a slow API and a fast one is often just caching.
- **Prerequisites:** Tier 4
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Cache-aside pattern
- Read-through cache
- Write-through cache
- Write-behind (write-back) cache
- Cache invalidation (the hardest problem in CS)
- TTL (time-to-live)
- Cache stampede (thundering herd)
- Cache hit ratio

---

### T7.2 Redis

- **Why It Matters:** Redis is the universal caching layer in Python backends. Also used for Celery broker and session storage.
- **Prerequisites:** T7.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Redis data structures (String, List, Hash, Set, Sorted Set)
- GET, SET, EXPIRE, DEL, TTL
- Redis as a cache (vs database)
- Redis persistence (RDB, AOF)
- Redis pub/sub (awareness)
- Redis in Docker for development
- `django-redis` integration
- Redis Cluster (awareness)

---

### T7.3 Django Cache Framework

- **Why It Matters:** Django's cache framework provides a uniform interface over multiple backends.
- **Prerequisites:** T7.2
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Cache backends (Redis, Memcached, database, filesystem, dummy)
- `cache.get()`, `cache.set()`, `cache.delete()`
- `cache.get_or_set()`
- `cache_page` decorator (full-page caching)
- Template caching
- Low-level caching pattern
- Cache key design

---

## Tier 8 — Task Queues & Background Processing

---

### T8.1 Celery

- **Why It Matters:** Long-running tasks (email sending, image processing, report generation) cannot block HTTP requests. Celery is the Python standard.
- **Prerequisites:** Python Level 6 (concurrency), Redis
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Why background tasks (don't block requests)
- Celery architecture (worker, broker, result backend)
- Task definition (`@app.task`)
- `delay()` and `apply_async()`
- Task configuration (retries, max_retries, countdown)
- Task result handling
- Task monitoring (Flower)
- Celery Beat (scheduled tasks)
- Periodic tasks with crontab
- Django integration (`django-celery-beat`, `django-celery-results`)
- Task idempotency
- Task chaining and groups

---

## Tier 9 — Architecture & Design

---

### T9.1 12-Factor App

- **Why It Matters:** The 12-Factor methodology defines how to build production-ready cloud applications. Industry standard.
- **Prerequisites:** Tier 4-8
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
1. Codebase — one codebase, many deploys
2. Dependencies — explicit declaration
3. Config — store in environment
4. Backing services — treat as attached resources
5. Build, Release, Run — strictly separate stages
6. Processes — stateless, share-nothing
7. Port binding — self-contained
8. Concurrency — scale out via processes
9. Disposability — fast startup, graceful shutdown
10. Dev/prod parity — keep environments similar
11. Logs — treat as event streams
12. Admin processes — run as one-off processes

---

### T9.2 API Design Patterns

- **Why It Matters:** Well-designed APIs are maintainable, scalable, and easy to consume.
- **Prerequisites:** Tier 2, Tier 5
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Service layer (business logic separate from views)
- Repository pattern (database access layer)
- Command/Query separation (CQRS concept)
- Domain objects vs data transfer objects
- Facade pattern for complex operations
- Event-driven patterns

---

## Tier 10 — Production Backend Concepts

---

### T10.1 Production Environment

- **Why It Matters:** Development settings are not production settings. Many security vulnerabilities come from not knowing the difference.
- **Prerequisites:** Full Tier 4
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `DEBUG = False` in production
- WSGI server (Gunicorn) vs development server
- Gunicorn configuration (workers, threads, timeout)
- Nginx as reverse proxy
- Process supervision (systemd, supervisor)
- Zero-downtime deployment
- Health check endpoints
- Graceful shutdown

---

### T10.2 Logging & Error Tracking

- **Why It Matters:** In production, logs are your only window into what's happening.
- **Prerequisites:** Python Level 7 (logging)
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- Django's logging configuration
- Structured logging (JSON format)
- Log levels in production
- Sentry integration
- Error alerting
- Performance monitoring
- Log aggregation (ELK stack concepts, CloudWatch)

---

### T10.3 Performance & Scaling

- **Why It Matters:** Production systems face real load. Every backend developer must know basic performance patterns.
- **Prerequisites:** Full Tier 9
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Response time benchmarks (P50, P95, P99)
- Database bottlenecks
- Cache bottlenecks
- Horizontal scaling (stateless design)
- Vertical scaling limits
- Load balancing
- Database read replicas
- CDN for static assets
- Profiling Django with `django-silk`

---

*This is the knowledge inventory for Backend Engineering. Roadmap and scheduling are managed separately.*
