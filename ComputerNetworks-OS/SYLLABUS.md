# Computer Networks Syllabus — ComputerNetworks-OS

> **Goal:** Master networking theory for software engineering interviews + practical skills for backend development.
> **Focus:** OSI model, TCP/IP, HTTP/HTTPS, DNS, security, and web communication — from an application developer's perspective.
> **Scope:** Conceptual depth for interviews + practical knowledge for building and debugging web systems.

---

## Why Networking Matters for Software Engineers

Every backend developer is building networked software. Networking knowledge answers:
- Why does your API sometimes time out? (TCP, packet loss)
- Why does your HTTPS certificate expire? (TLS, PKI)
- How does load balancing work? (routing, health checks)
- Why does your app fail after DNS change? (TTL, caching)
- How do WebSockets work differently from HTTP? (protocol differences)
- What is CORS and why does the browser enforce it? (web security)

Interviewers use networking to test depth of understanding about distributed systems.

---

## Level Structure

| Level | Topic | Interview Weight |
|-------|-------|----------------|
| Level 1 | Foundations | Medium |
| Level 2 | OSI Model | Critical |
| Level 3 | TCP/IP Model | Critical |
| Level 4 | IP Addressing | High |
| Level 5 | TCP & UDP | Critical |
| Level 6 | HTTP & HTTPS | Critical |
| Level 7 | DNS | High |
| Level 8 | Web Communication Protocols | High |
| Level 9 | Routing & Infrastructure | Medium |
| Level 10 | Network Security | High |
| Level 11 | Practical Networking Tools | High (backend) |

---

## Level 1 — Foundations

---

### 1.1 What is a Network

- **Why It Matters:** Foundation for all subsequent concepts.
- **Prerequisites:** None
- **Interview Importance:** Low-Medium
- **Job Importance:** High

Topics:
- Network: interconnected devices that can communicate
- Types by size:
  - PAN (Personal Area Network): Bluetooth, USB
  - LAN (Local Area Network): home/office network
  - MAN (Metropolitan Area Network): city-scale
  - WAN (Wide Area Network): cross-country/continent
  - Internet: network of networks
- Network topologies:
  - Bus: all connected to single cable
  - Star: all connected to central switch/hub
  - Ring: each connected to next in circle
  - Mesh: every node connected to every other
  - Hybrid: combination
- Transmission modes: Simplex, Half-Duplex, Full-Duplex

---

### 1.2 Network Components

- **Why It Matters:** Understanding hardware components demystifies infrastructure design.
- **Prerequisites:** 1.1
- **Interview Importance:** Low
- **Job Importance:** Medium

Topics:
- **Hub:** broadcasts all traffic to all ports (Layer 1); creates collision domain
- **Switch:** forwards traffic only to destination port (Layer 2); uses MAC tables
- **Router:** routes traffic between networks (Layer 3); uses IP routing tables
- **Access Point (AP):** wireless connectivity
- **Firewall:** filters traffic based on rules
- **Load Balancer:** distributes traffic across servers
- **Proxy:** intermediary between client and server
- NIC (Network Interface Card): physical connection
- Modem: modulates/demodulates for WAN transmission

---

## Level 2 — OSI Model

> *The OSI model is the most fundamental concept in networking. It is tested in nearly every interview.*

---

### 2.1 Why the OSI Model Exists

- **Why It Matters:** Without a layered model, you can't reason about where a problem occurs in the network stack.
- **Prerequisites:** Level 1
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- OSI = Open Systems Interconnection
- Purpose: standardize how different systems communicate
- Benefit: modular design (change one layer without affecting others)
- Developed by ISO
- 7 layers (mnemonic: Please Do Not Throw Sausage Pizza Away — physical to application)

---

### 2.2 Layer 1 — Physical Layer

- **Why It Matters:** Transmission media, signals, bit representation.
- **Prerequisites:** 2.1
- **Interview Importance:** Low
- **Job Importance:** Low

Topics:
- Concerned with physical transmission of raw bits
- Media types: twisted pair (CAT5/6/7), coaxial, fiber optic, radio waves
- Signaling: electrical, optical, radio
- Bandwidth, throughput, latency
- Devices: hubs, repeaters
- Transmission modes
- Line coding, modulation (analog to digital)

---

### 2.3 Layer 2 — Data Link Layer

- **Why It Matters:** MAC addresses, ARP, and Ethernet work here. VLANs, switches operate at this layer.
- **Prerequisites:** 2.2
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- Frames: unit of data at this layer
- **MAC Address:** 48-bit hardware address (e.g., 00:1A:2B:3C:4D:5E)
  - First 3 bytes = OUI (manufacturer)
  - Last 3 bytes = device ID
- Error detection: CRC, checksum
- Flow control (stop-and-wait, sliding window)
- **ARP (Address Resolution Protocol):**
  - Maps IP address to MAC address
  - ARP request (broadcast) + ARP reply (unicast)
  - ARP cache
  - Gratuitous ARP
  - ARP poisoning (security attack)
- Devices: switches, bridges
- Protocols: Ethernet (802.3), WiFi (802.11), PPP

---

### 2.4 Layer 3 — Network Layer

- **Why It Matters:** IP addresses live here. This is how packets are routed across the internet.
- **Prerequisites:** 2.3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Packets: unit of data at this layer
- **IP (Internet Protocol):** addressing and routing
- IPv4 address: 32-bit, dotted decimal (192.168.1.1)
- IPv6 address: 128-bit, colon-hex notation
- **IP header:** source IP, destination IP, TTL, protocol, checksum
- **TTL (Time To Live):** decremented at each hop; prevents loops
- **Routing:** process of forwarding packets toward destination
- **ICMP (Internet Control Message Protocol):**
  - Error reporting: destination unreachable, time exceeded
  - `ping` uses ICMP Echo Request/Reply
  - `traceroute` uses TTL expiration
- **NAT (Network Address Translation):**
  - Translates private IP to public IP
  - Conserves IPv4 address space
  - Types: static, dynamic, PAT (Port Address Translation)
- Devices: routers

---

### 2.5 Layer 4 — Transport Layer

- **Why It Matters:** TCP and UDP live here. All application-level protocols (HTTP, DNS, SMTP) use TCP or UDP.
- **Prerequisites:** 2.4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Segments: unit of data at this layer
- End-to-end communication
- Port numbers: identify applications (0-1023 well-known, 1024-49151 registered, 49152-65535 ephemeral)
- **TCP:** reliable, connection-oriented
- **UDP:** unreliable, connectionless
- Multiplexing/demultiplexing using ports
- Common ports: HTTP(80), HTTPS(443), SSH(22), FTP(21), SMTP(25), DNS(53), PostgreSQL(5432), Redis(6379)

---

### 2.6 Layers 5-7 — Session, Presentation, Application

- **Why It Matters:** Application layer is where HTTP, DNS, SMTP live. Session and Presentation are often merged conceptually.
- **Prerequisites:** 2.5
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:

**Layer 5 — Session:**
- Manages sessions between applications
- Session establishment, maintenance, termination
- RPC, SQL sessions

**Layer 6 — Presentation:**
- Data formatting, encryption, compression
- SSL/TLS negotiation occurs here
- Character encoding (ASCII, UTF-8)
- Serialization (JSON, XML)

**Layer 7 — Application:**
- Protocols: HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, SSH, Telnet
- User-facing services
- Data: messages/data streams

---

### 2.7 Data Encapsulation & Decapsulation

- **Why It Matters:** Understanding how data flows through layers is essential for debugging network issues.
- **Prerequisites:** 2.1-2.6
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Encapsulation: each layer adds its own header (and sometimes trailer)
  - Application: data
  - Transport: segment = TCP header + data
  - Network: packet = IP header + segment
  - Data Link: frame = MAC header + packet + MAC trailer
  - Physical: bits
- Decapsulation at receiving end: reverse order, each layer strips its header
- PDU (Protocol Data Unit) at each layer

---

## Level 3 — TCP/IP Model

---

### 3.1 TCP/IP Model Overview

- **Why It Matters:** TCP/IP is the actual model the internet uses. OSI is theoretical; TCP/IP is practical.
- **Prerequisites:** Level 2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- TCP/IP = 4 layers (some say 5)
- **Network Access / Link Layer:** OSI Layers 1+2
- **Internet Layer:** OSI Layer 3 (IP, ICMP, ARP)
- **Transport Layer:** OSI Layer 4 (TCP, UDP)
- **Application Layer:** OSI Layers 5+6+7 (HTTP, DNS, SMTP)
- OSI vs TCP/IP comparison
- Why TCP/IP is the practical reference model

---

## Level 4 — IP Addressing

---

### 4.1 IPv4 Addressing

- **Why It Matters:** Every backend developer configures IP addresses, security groups, and VPCs.
- **Prerequisites:** Level 3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- 32-bit addresses, dotted decimal notation
- Address classes (A, B, C, D, E) — historical context
- **Private IP ranges (RFC 1918):**
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
- Public vs private IP addresses
- **Subnet Mask:** defines network vs host portion
  - 255.255.255.0 = /24
  - 255.255.0.0 = /16
  - 255.0.0.0 = /8
- **CIDR (Classless Inter-Domain Routing):**
  - 192.168.1.0/24: 256 addresses, 254 usable
  - Network address (all 0s), Broadcast address (all 1s)
  - Number of hosts = 2^(32-prefix) - 2
- Subnetting calculations
- Loopback: 127.0.0.1

---

### 4.2 IPv6

- **Why It Matters:** IPv6 adoption is growing. Cloud providers increasingly require IPv6 awareness.
- **Prerequisites:** 4.1
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- 128-bit addresses, colon-separated hex
- Why IPv6 (IPv4 exhaustion)
- Address shortening rules (:: for consecutive zeros)
- Address types: unicast, multicast, anycast (no broadcast)
- Loopback: ::1
- Link-local: fe80::/10
- IPv6 header improvements
- Dual-stack deployment

---

### 4.3 DHCP

- **Why It Matters:** DHCP automatically assigns IP addresses. Understanding it helps debug connectivity issues.
- **Prerequisites:** 4.1
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- DHCP: Dynamic Host Configuration Protocol
- DORA process: Discover → Offer → Request → Acknowledge
- DHCP lease time
- DHCP options (gateway, DNS, domain name)
- Static vs dynamic IP assignment
- DHCP relay for multi-subnet networks

---

## Level 5 — TCP & UDP

> *The most tested transport layer knowledge for software engineers.*

---

### 5.1 TCP — Transmission Control Protocol

- **Why It Matters:** HTTP, HTTPS, WebSockets all use TCP. Understanding TCP explains latency, retransmission, and connection overhead.
- **Prerequisites:** Level 3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**TCP Characteristics:**
- Connection-oriented (must establish connection before data)
- Reliable delivery (acknowledgments, retransmission)
- Ordered delivery (sequence numbers)
- Full-duplex (bidirectional)
- Flow control (receiver controls sender speed)
- Congestion control (network capacity awareness)

**TCP Header (key fields):**
- Source Port, Destination Port
- Sequence Number
- Acknowledgment Number
- Control flags: SYN, ACK, FIN, RST, PSH, URG
- Window Size (for flow control)
- Checksum

**Three-Way Handshake (Connection Establishment):**
1. Client → Server: SYN (seq=x)
2. Server → Client: SYN-ACK (seq=y, ack=x+1)
3. Client → Server: ACK (ack=y+1)
- After handshake: connection is ESTABLISHED
- Purpose: synchronize sequence numbers, verify connectivity

**Four-Way Handshake (Connection Termination):**
1. Client → Server: FIN
2. Server → Client: ACK
3. Server → Client: FIN
4. Client → Server: ACK
- TIME_WAIT state: client waits 2*MSL before fully closing
- Purpose: ensure server receives final ACK

**TCP State Machine:**
- Key states: LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT_1, FIN_WAIT_2, TIME_WAIT, CLOSE_WAIT, LAST_ACK, CLOSED

**Reliability Mechanisms:**
- Sequence numbers and acknowledgments
- Cumulative ACK
- Selective ACK (SACK)
- Retransmission timeout (RTO)
- Fast retransmit (3 duplicate ACKs → retransmit without waiting for timeout)

**Flow Control:**
- Sliding window
- Window size advertisement
- Zero window (receiver buffer full)
- Window scaling

**Congestion Control:**
- Slow Start: exponential growth of congestion window (cwnd)
- Congestion Avoidance: linear growth after threshold
- Fast Recovery
- CUBIC, BBR (modern algorithms)

---

### 5.2 UDP — User Datagram Protocol

- **Why It Matters:** DNS, video streaming, gaming, QUIC all use UDP. Knowing when UDP is better than TCP is a design skill.
- **Prerequisites:** 5.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Connectionless (no handshake)
- No reliability (no ACKs, no retransmission)
- No ordering
- No flow or congestion control
- Low overhead (8-byte header vs TCP's 20+)
- UDP header: Source Port, Dest Port, Length, Checksum

**When UDP is preferred:**
- Real-time: video/audio calls (latency > reliability)
- DNS queries (short, application handles retry)
- DHCP
- Games (old state is useless)
- Multicast/broadcast
- QUIC (implements reliability in application layer)

**TCP vs UDP Summary:**

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Required | None |
| Reliability | Yes | No |
| Ordering | Yes | No |
| Speed | Slower | Faster |
| Overhead | High | Low |
| Use cases | HTTP, FTP, SSH | DNS, Video, Games |

---

### 5.3 Ports & Sockets

- **Why It Matters:** Every server you write listens on a port. Understanding sockets is fundamental.
- **Prerequisites:** 5.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Port: 16-bit number identifying application/service
- Socket: (IP + Port) = endpoint for communication
- Socket pair: (source IP, source port, dest IP, dest port) uniquely identifies a TCP connection
- `bind()`, `listen()`, `accept()`, `connect()`, `send()`, `recv()`, `close()`
- Backlog queue in `listen()`
- SO_REUSEADDR option
- Port exhaustion (ephemeral port limit)
- Common ports: 22 (SSH), 25 (SMTP), 53 (DNS), 80 (HTTP), 443 (HTTPS), 5432 (PostgreSQL), 6379 (Redis), 8000/8080 (dev servers)

---

## Level 6 — HTTP & HTTPS

> *The language of the web. Every backend developer must know HTTP deeply.*

---

### 6.1 HTTP/1.1

- **Why It Matters:** HTTP/1.1 is still widely used and the foundation for understanding HTTP/2 and HTTP/3.
- **Prerequisites:** Level 5
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- HTTP/1.1 features over HTTP/1.0:
  - Persistent connections (keep-alive): reuse TCP connection for multiple requests
  - Pipelining: send multiple requests without waiting (limited adoption)
  - Chunked transfer encoding
  - Virtual hosting (Host header)
  - Cache control
- HTTP message format (request and response)
- HTTP methods (covered in Backend Engineering syllabus)
- HTTP status codes (covered in Backend Engineering syllabus)
- **Head-of-line blocking:** later requests blocked by slow earlier request

---

### 6.2 HTTP/2

- **Why It Matters:** HTTP/2 is the current standard. Understanding it explains performance improvements.
- **Prerequisites:** 6.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Binary framing layer (not text-based like HTTP/1.1)
- **Multiplexing:** multiple requests/responses over single TCP connection simultaneously
- Eliminates head-of-line blocking at HTTP layer
- **Header compression (HPACK):** reduces header overhead
- **Server Push:** server can proactively send resources
- Stream prioritization
- Same-domain limit: HTTP/1.1 has 6 connections limit; HTTP/2 needs only 1
- Performance improvements vs HTTP/1.1
- Requires TLS in practice (browsers mandate HTTPS for HTTP/2)

---

### 6.3 HTTP/3

- **Why It Matters:** HTTP/3 is the emerging standard. Understanding it shows awareness of modern web performance.
- **Prerequisites:** 6.2
- **Interview Importance:** Medium-High
- **Job Importance:** Medium

Topics:
- Built on QUIC (UDP-based, not TCP)
- Why UDP? TCP head-of-line blocking at transport layer (packet loss blocks all streams)
- QUIC provides its own reliability, ordering, congestion control
- 0-RTT connection establishment (faster handshake)
- Connection migration (mobile: switch WiFi to cellular without reconnect)
- Current adoption status

---

### 6.4 HTTPS & TLS

- **Why It Matters:** Every production API uses HTTPS. TLS is the security layer.
- **Prerequisites:** 6.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**Why HTTPS:**
- HTTP is plaintext (MITM attacks, eavesdropping)
- HTTPS = HTTP over TLS (Transport Layer Security)
- TLS provides: Confidentiality, Integrity, Authentication

**TLS Handshake (TLS 1.3 simplified):**
1. Client Hello (supported cipher suites, random, TLS version)
2. Server Hello (chosen cipher, random, certificate)
3. Certificate verification (client validates server's cert)
4. Key exchange (asymmetric crypto to establish shared secret)
5. Session keys derived (symmetric encryption begins)
6. Handshake complete

**Certificates:**
- X.509 certificate format
- Certificate fields: subject, issuer, validity, public key
- Certificate chain: end-entity → intermediate → root CA
- Certificate Authorities (Let's Encrypt, DigiCert, Comodo)
- Certificate validation (not expired, chain trusted, domain matches)
- SAN (Subject Alternative Name) for multiple domains

**Cipher Suites:**
- Key exchange algorithm (ECDHE)
- Authentication algorithm (RSA, ECDSA)
- Encryption algorithm (AES-128-GCM)
- Hash algorithm (SHA256)

**TLS Versions:**
- TLS 1.0, 1.1: deprecated (insecure)
- TLS 1.2: current minimum standard
- TLS 1.3: preferred (faster, more secure)

**HTTPS Setup:**
- `certbot` with Let's Encrypt
- Certificate renewal (90-day validity)
- HSTS (HTTP Strict Transport Security): browser only uses HTTPS

---

### 6.5 HTTP Headers Deep Dive

- **Why It Matters:** Headers control caching, auth, CORS, content negotiation — all critical backend behaviors.
- **Prerequisites:** 6.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**Request Headers:**
- `Host`: target server (required in HTTP/1.1)
- `Authorization`: credentials (`Bearer`, `Basic`)
- `Content-Type`: format of request body
- `Accept`: acceptable response formats
- `Accept-Language`: preferred language
- `User-Agent`: client software identification
- `Cookie`: client-stored data
- `If-Modified-Since`, `If-None-Match`: conditional requests
- `X-Request-ID`: request tracing

**Response Headers:**
- `Content-Type`: format of response body
- `Content-Length`: size of body
- `Set-Cookie`: send cookie to client
- `Cache-Control`: caching directives
- `ETag`: resource version identifier
- `Last-Modified`: resource modification time
- `Location`: redirect target (3xx)
- `WWW-Authenticate`: auth challenge (401)
- `Retry-After`: rate limit recovery (429)
- `Strict-Transport-Security`: HSTS

**CORS Headers:**
- `Origin`: requesting origin
- `Access-Control-Allow-Origin`
- `Access-Control-Allow-Methods`
- `Access-Control-Allow-Headers`
- `Access-Control-Max-Age`

---

### 6.6 CORS — Cross-Origin Resource Sharing

- **Why It Matters:** CORS errors are among the most common errors frontend developers face. Backend developers must configure CORS correctly.
- **Prerequisites:** 6.5
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Same-Origin Policy: browsers block requests to different origins by default
- Origin = scheme + host + port (http://example.com:80)
- CORS: mechanism to relax Same-Origin Policy selectively
- Preflight request (OPTIONS method): browser asks server if cross-origin request is allowed
- Simple request: GET/POST with simple content types — no preflight
- Non-simple request: custom headers, PUT, DELETE — requires preflight
- Credentialed requests (cookies with cross-origin)
- `Access-Control-Allow-Credentials: true` + specific origin (not `*`)
- `django-cors-headers` configuration
- Common CORS mistakes

---

## Level 7 — DNS

---

### 7.1 DNS Architecture

- **Why It Matters:** Every internet request starts with DNS. DNS failures bring down entire applications.
- **Prerequisites:** Level 4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- DNS: Domain Name System — translates domain names to IP addresses
- Hierarchical namespace:
  - Root (`.`)
  - TLDs: `.com`, `.org`, `.in`, `.io`
  - Second-level domains: `google.com`, `github.com`
  - Subdomains: `api.example.com`, `www.example.com`
- DNS components:
  - **DNS Resolver (Recursive Resolver):** ISP or public (8.8.8.8 Google, 1.1.1.1 Cloudflare)
  - **Root Name Servers:** 13 root servers (A through M)
  - **TLD Name Servers:** manage `.com`, `.org`, etc.
  - **Authoritative Name Servers:** hold actual DNS records for a domain

---

### 7.2 DNS Resolution Process

- **Why It Matters:** "What happens when you type a URL" question always involves DNS resolution.
- **Prerequisites:** 7.1
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- Step-by-step DNS resolution:
  1. Browser cache check
  2. OS cache check (hosts file: /etc/hosts)
  3. Resolver cache check
  4. Query root name server (finds TLD server)
  5. Query TLD name server (finds authoritative server)
  6. Query authoritative name server → gets IP address
  7. Resolver caches result; returns to client
- Recursive vs Iterative queries
- DNS caching at each level
- TTL (Time To Live): how long to cache a DNS record
- Negative caching (NXDOMAIN responses also cached)
- Low TTL for quick propagation (e.g., during migration)
- High TTL for stable, high-traffic domains

---

### 7.3 DNS Record Types

- **Why It Matters:** Backend developers configure DNS records for deployments, email, domain verification.
- **Prerequisites:** 7.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- **A Record:** domain → IPv4 address
- **AAAA Record:** domain → IPv6 address
- **CNAME Record:** domain → another domain (alias); cannot coexist with other records at apex
- **MX Record:** specifies mail servers for domain; priority value
- **TXT Record:** arbitrary text; used for SPF, DKIM, domain verification
- **NS Record:** specifies authoritative name servers for domain
- **PTR Record:** reverse DNS (IP → domain name)
- **SRV Record:** service location (host, port, priority, weight)
- **SOA Record:** Start of Authority; administrative info
- **CAA Record:** Certificate Authority Authorization; restricts which CAs can issue certs for domain

---

### 7.4 DNS Security

- **Why It Matters:** DNS attacks are real and impactful (DNS hijacking, cache poisoning).
- **Prerequisites:** 7.3
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:
- **DNS Cache Poisoning:** injecting malicious DNS data into resolver cache
- **DNS Hijacking:** redirecting DNS queries to malicious server
- **DNS Amplification DDoS:** use DNS for traffic amplification attacks
- **DNSSEC:** digitally sign DNS records (zone signing)
- **DNS over HTTPS (DoH):** encrypted DNS queries via HTTP
- **DNS over TLS (DoT):** encrypted DNS queries via TLS

---

## Level 8 — Web Communication Protocols

---

### 8.1 WebSockets

- **Why It Matters:** Real-time features (chat, live dashboards, collaborative editing) use WebSockets. Every modern web app developer needs this.
- **Prerequisites:** Level 6 (HTTP)
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- WebSocket: full-duplex, persistent connection over TCP
- Upgrade from HTTP:
  - Client sends `Upgrade: websocket` header
  - Server responds with `101 Switching Protocols`
  - Connection is now a WebSocket
- WebSocket vs HTTP:
  - HTTP: request-response, client-initiated, new connection per request (HTTP/1.1)
  - WebSocket: bidirectional, server can push without client request, single persistent connection
- Frames: text, binary, ping, pong, close
- Heartbeat (ping/pong) to keep connection alive
- Use cases: chat, real-time notifications, live prices, collaborative tools, gaming
- Django Channels for WebSocket support
- Scaling WebSockets (sticky sessions, pub/sub with Redis)

---

### 8.2 Long Polling & Server-Sent Events

- **Why It Matters:** Fallback techniques when WebSockets aren't appropriate. Understanding the evolution helps choose correctly.
- **Prerequisites:** 8.1
- **Interview Importance:** Medium
- **Job Importance:** Medium

Topics:

**Polling:**
- Client repeatedly requests for updates at fixed intervals
- Simple but wasteful (many empty responses)
- High latency (max = poll interval)

**Long Polling:**
- Client sends request; server holds it open until event or timeout
- Lower latency than polling
- Still half-duplex (server → client only within request)
- Request overhead on each poll cycle

**Server-Sent Events (SSE):**
- Server streams events over single HTTP connection
- One-directional (server → client only)
- `Content-Type: text/event-stream`
- Built-in reconnection
- Simple API (`EventSource` in browser)
- Good for: notifications, feeds, live updates

**Comparison:**

| Method | Direction | Overhead | Complexity | Use Case |
|--------|-----------|----------|-----------|----------|
| Polling | Server→Client | High | Low | Simple, infrequent updates |
| Long Polling | Server→Client | Medium | Medium | Low-latency, simple |
| SSE | Server→Client | Low | Low | One-way streams |
| WebSocket | Bidirectional | Low | High | Real-time, interactive |

---

### 8.3 REST vs GraphQL vs gRPC

- **Why It Matters:** Modern APIs use multiple paradigms. Understanding tradeoffs is required for system design interviews.
- **Prerequisites:** Level 6 (HTTP), REST concepts
- **Interview Importance:** High
- **Job Importance:** High

Topics:

**REST:**
- Resources as URLs, HTTP verbs for operations
- Stateless, cacheable, widely understood
- Over-fetching / Under-fetching problems
- Multiple round trips for related data

**GraphQL:**
- Client specifies exactly what data it needs
- Single endpoint (`/graphql`)
- No over/under-fetching
- N+1 problem on server side
- Complex caching
- Great for complex data graphs, mobile apps

**gRPC:**
- Protocol Buffer serialization (binary, compact)
- HTTP/2-based
- Strongly typed contracts (`.proto` files)
- Generated client/server code
- 10x faster than JSON/REST for internal services
- Browser support limited (use grpc-web)
- Best for internal microservice communication

---

## Level 9 — Routing & Network Infrastructure

---

### 9.1 Routing

- **Why It Matters:** Cloud networking, VPCs, and security groups all involve routing concepts.
- **Prerequisites:** Level 4
- **Interview Importance:** Medium
- **Job Importance:** Medium-High

Topics:
- Routing: selecting path for packets to travel
- Routing table: (network prefix → next hop)
- Static routing: manually configured
- Dynamic routing: routing protocols
- **Distance Vector (RIP):** share routing table with neighbors, use hop count metric
- **Link State (OSPF):** flood topology to all routers, use Dijkstra's algorithm
- **BGP (Border Gateway Protocol):** routing between autonomous systems (internet-scale)
- Default route (0.0.0.0/0): catch-all
- Longest prefix match

---

### 9.2 Proxies & Load Balancers

- **Why It Matters:** Every production application uses load balancers. Understanding them is required for system design.
- **Prerequisites:** 9.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**Forward Proxy:**
- Client → Proxy → Internet
- Hides client identity
- Use: corporate networks, content filtering, caching

**Reverse Proxy:**
- Client → Reverse Proxy → Server(s)
- Hides server identity
- Use: Nginx, CDN, load balancing, SSL termination

**Load Balancing:**
- Layer 4 (Transport) Load Balancing: routes based on IP/port (fast, limited intelligence)
- Layer 7 (Application) Load Balancing: routes based on HTTP content (URL, headers, cookies)
- Algorithms:
  - Round Robin: each request to next server in rotation
  - Weighted Round Robin: proportional to server capacity
  - Least Connections: route to server with fewest connections
  - IP Hash: same client always hits same server (session persistence)
  - Random
- Health checks: remove unhealthy servers from pool
- Session persistence (sticky sessions)
- AWS ALB (Application Load Balancer) and NLB (Network Load Balancer)

---

## Level 10 — Network Security

---

### 10.1 Common Network Attacks

- **Why It Matters:** Backend developers must design systems to resist common attacks.
- **Prerequisites:** Level 6
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- **Man-in-the-Middle (MITM):** attacker intercepts communication
  - Prevention: HTTPS, certificate pinning
- **DDoS (Distributed Denial of Service):** overwhelm server with traffic
  - Types: volumetric, protocol (SYN flood), application layer
  - Mitigation: rate limiting, CDN, WAF, cloud DDoS protection
- **DNS Spoofing/Cache Poisoning:** fake DNS responses
  - Prevention: DNSSEC, DoH
- **ARP Poisoning:** poison ARP cache to redirect traffic
- **SSL Stripping:** downgrade HTTPS to HTTP
  - Prevention: HSTS

---

### 10.2 Encryption Concepts

- **Why It Matters:** Understanding encryption helps you choose the right algorithm and understand TLS.
- **Prerequisites:** Level 6
- **Interview Importance:** High
- **Job Importance:** High

Topics:

**Symmetric Encryption:**
- Same key for encryption and decryption
- Fast (100x faster than asymmetric)
- Key distribution problem
- Algorithms: AES-128, AES-256, ChaCha20

**Asymmetric Encryption (Public Key Cryptography):**
- Public key (shared) + Private key (secret)
- Encrypt with public key, decrypt with private key
- Sign with private key, verify with public key
- Slower than symmetric
- Algorithms: RSA, ECC (ECDSA, ECDH)

**Hybrid Encryption (used in TLS):**
- Asymmetric to exchange symmetric key
- Symmetric for bulk data encryption

**Hashing:**
- One-way function (cannot reverse)
- Same input always produces same output
- Collision resistance
- Algorithms: SHA-256, SHA-3, Blake2

**Digital Signatures:**
- Hash the document, encrypt with private key
- Verify: decrypt with public key, compare with hash

---

### 10.3 Firewalls & WAF

- **Why It Matters:** Every production deployment uses firewalls (AWS Security Groups). WAFs protect web applications.
- **Prerequisites:** 10.1
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- **Firewall:** filters traffic based on rules (IP, port, protocol)
  - Stateless: filter each packet independently
  - Stateful: track connection state
  - Next-Gen: application-aware
- **AWS Security Groups:** stateful firewall (allow inbound/outbound rules)
- **Network ACLs (NACLs):** stateless, subnet-level rules
- **WAF (Web Application Firewall):**
  - Operates at Layer 7
  - Blocks: SQL injection, XSS, path traversal, bot traffic
  - AWS WAF, Cloudflare WAF

---

## Level 11 — Practical Networking Tools

---

### 11.1 Network Diagnostic Commands

- **Why It Matters:** Production debugging requires knowing these tools.
- **Prerequisites:** Level 10
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `ping target`: test connectivity (ICMP echo)
- `traceroute target` (Linux) / `tracert` (Windows): path tracing
- `nslookup domain`: basic DNS query
- `dig domain`: detailed DNS query (preferred over nslookup)
  - `dig A example.com`
  - `dig MX example.com`
  - `dig +trace example.com` (full resolution)
- `netstat -tulpn`: listening ports and connections
- `ss -tulpn`: modern replacement for netstat
- `curl -v URL`: verbose HTTP request (shows headers)
- `curl -I URL`: headers only
- `wget URL`: download file
- `telnet host port`: test TCP connectivity
- `nc` (netcat): versatile TCP/UDP tool
- `tcpdump`: capture packets on interface
- `nmap host`: port scanning and host discovery
- `ifconfig` / `ip addr`: network interface info
- `route -n` / `ip route`: routing table

---

### 11.2 API Testing Tools

- **Why It Matters:** Backend developers use these daily.
- **Prerequisites:** Level 6
- **Interview Importance:** Low
- **Job Importance:** Critical

Topics:
- **Postman:** GUI API testing client
  - Collections, environments, variables
  - Pre-request scripts, tests
  - Mock servers
- **curl:** command-line HTTP client
  - GET, POST, PUT, DELETE examples
  - Headers (`-H`)
  - Request body (`-d`)
  - Authentication (`-u`, Bearer token)
  - SSL bypass for dev (`-k`)
- **HTTPie:** user-friendly curl alternative
- **Insomnia:** Postman alternative

---

*This is the knowledge inventory for Computer Networks. Roadmap and scheduling are managed separately.*
