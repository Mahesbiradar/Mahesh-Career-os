# Python Syllabus — Mahesh Career OS

> **Goal:** Progress from Beginner-Intermediate to Professional Python Developer.
> **Depth:** Industry-level. Covers all concepts needed for backend development, interviews, and real-world projects.
> **DSA:** Excluded. Managed separately.

---

## Level Structure Overview

| Level | Name | Mastery Goal |
|-------|------|-------------|
| Level 1 | Core Fundamentals | Run Python, write basic programs |
| Level 2 | Data Structures | Work with all built-in collections fluently |
| Level 3 | Functions & Modules | Write modular, reusable code |
| Level 4 | OOP | Design and build class-based systems |
| Level 5 | Advanced Python | Write idiomatic, Pythonic code |
| Level 6 | Concurrency | Handle async/threaded scenarios |
| Level 7 | Standard Library | Use Python's built-in ecosystem |
| Level 8 | Testing | Write and maintain test suites |
| Level 9 | Backend Python | Integrate Python with web, APIs, databases |

---

## Level 1 — Core Fundamentals

> *Foundation layer. Everything above depends on this being solid.*

---

### 1.1 Variables & Data Types

- **Why It Matters:** Python's type system is the basis of all programs. Misunderstanding types causes silent bugs in production.
- **Prerequisites:** None
- **Interview Importance:** Medium — frequently tested in warm-up rounds
- **Job Importance:** Critical — every single line of code you write involves types

Topics:
- Integer, Float, Complex
- String, Boolean, NoneType
- Dynamic typing vs static typing
- Type checking with `type()` and `isinstance()`
- Type conversion: `int()`, `str()`, `float()`, `bool()`
- Variable naming conventions (PEP 8)
- Multiple assignment
- Constants (naming convention)

---

### 1.2 Operators & Expressions

- **Why It Matters:** Operators are the mechanics of computation. Understanding precedence prevents logical bugs.
- **Prerequisites:** 1.1
- **Interview Importance:** Low-Medium
- **Job Importance:** High

Topics:
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Bitwise operators (&, |, ^, ~, <<, >>)
- Assignment operators (+=, -=, etc.)
- Identity operators (is, is not)
- Membership operators (in, not in)
- Operator precedence & parentheses
- Short-circuit evaluation

---

### 1.3 Control Flow

- **Why It Matters:** Logic branching is the core of all decision-making in software.
- **Prerequisites:** 1.1, 1.2
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `if`, `elif`, `else`
- Nested conditionals
- Ternary expressions (inline if)
- `match` statement (Python 3.10+, structural pattern matching)
- Truthiness and falsy values

---

### 1.4 Loops

- **Why It Matters:** Iteration is fundamental — almost every real program loops over data.
- **Prerequisites:** 1.3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `for` loop (iterating over sequences)
- `while` loop (condition-based)
- `range()` function
- `break` and `continue`
- `else` clause in loops
- Nested loops
- `enumerate()` and `zip()` in loops
- Loop efficiency considerations

---

### 1.5 Functions — Basics

- **Why It Matters:** Functions are the unit of code organization. Writing functions well is the difference between spaghetti and clean code.
- **Prerequisites:** 1.4
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Defining functions with `def`
- Parameters vs Arguments
- Return values
- Default parameter values
- Calling functions
- Docstrings
- Function naming (PEP 8)

---

### 1.6 Built-in Functions & Methods

- **Why It Matters:** Python's built-ins are optimized. Using them instead of hand-rolled loops makes code faster and cleaner.
- **Prerequisites:** 1.5
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- `print()`, `input()`
- `len()`, `range()`, `type()`, `isinstance()`
- `max()`, `min()`, `sum()`, `abs()`, `round()`
- `sorted()`, `reversed()`
- `enumerate()`, `zip()`, `map()`, `filter()`
- `any()`, `all()`
- `open()` (preview — covered in depth in Level 3)

---

## Level 2 — Data Structures & Collections

> *Python's built-in collections are extraordinarily powerful. Mastering them is what separates beginners from professionals.*

---

### 2.1 Strings

- **Why It Matters:** 80%+ of web backend work involves processing strings — URLs, JSON keys, user input, logs, templates.
- **Prerequisites:** Level 1
- **Interview Importance:** High — very common in coding rounds
- **Job Importance:** Critical

Topics:
- String immutability
- Indexing & slicing (`s[0]`, `s[1:4]`, `s[-1]`, `s[::2]`)
- String methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.find()`, `.count()`, `.startswith()`, `.endswith()`, `.format()`
- f-strings (Python 3.6+) — preferred modern formatting
- Multi-line strings
- Raw strings (`r"..."`)
- String comparison and sorting
- `str.encode()` / `bytes.decode()` (encoding basics)

---

### 2.2 Lists

- **Why It Matters:** Lists are Python's workhorse data structure. You'll use them in every project.
- **Prerequisites:** 2.1
- **Interview Importance:** High — commonly used in interview solutions
- **Job Importance:** Critical

Topics:
- Creating, accessing, slicing
- Mutability
- Methods: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.copy()`, `.clear()`
- Nested lists
- List comprehensions (`[x for x in range(10) if x % 2 == 0]`)
- `sorted()` with key argument
- Unpacking (`a, b, c = [1, 2, 3]`)
- List vs Array comparison

---

### 2.3 Tuples

- **Why It Matters:** Tuples represent fixed data — function return values, database rows, coordinate pairs. They're faster than lists and can be dict keys.
- **Prerequisites:** 2.2
- **Interview Importance:** Medium
- **Job Importance:** Medium-High

Topics:
- Creating tuples
- Immutability
- Unpacking
- Named tuples (preview of `collections.namedtuple`)
- Tuple vs List: when to use which
- Tuples as dictionary keys

---

### 2.4 Dictionaries

- **Why It Matters:** Dictionaries are how Python represents structured data — JSON responses, database rows, configurations, caches. Extremely common in backend work.
- **Prerequisites:** 2.2
- **Interview Importance:** High — heavy use in interview solutions
- **Job Importance:** Critical

Topics:
- Creating dictionaries
- Accessing, adding, updating, deleting keys
- Methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.setdefault()`, `.update()`, `.pop()`, `.copy()`
- Dictionary comprehensions
- Nested dictionaries
- Iterating over dicts
- `dict` as a namespace pattern
- Merging dicts (`{**d1, **d2}` and `|` operator)

---

### 2.5 Sets

- **Why It Matters:** Sets provide O(1) membership testing and are essential for deduplication and set math operations (union, intersection).
- **Prerequisites:** 2.4
- **Interview Importance:** Medium-High
- **Job Importance:** Medium

Topics:
- Creating sets (literal and `set()`)
- Set operations: union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`)
- Methods: `.add()`, `.remove()`, `.discard()`, `.pop()`, `.update()`
- Set comprehensions
- Frozen sets
- Set vs List for membership testing (O(1) vs O(n))

---

## Level 3 — Functions, Modules & File Handling

---

### 3.1 Functions — Intermediate

- **Why It Matters:** Advanced function features (args, kwargs, closures) are the building blocks of Python frameworks and libraries.
- **Prerequisites:** Level 2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `*args` (variable positional arguments)
- `**kwargs` (variable keyword arguments)
- Keyword-only arguments (after `*`)
- Positional-only arguments (before `/`)
- Argument order rules
- Lambda functions
- First-class functions (functions as arguments)
- Returning functions
- Higher-order functions

---

### 3.2 Scope & Namespace

- **Why It Matters:** Scope bugs are a common source of errors that are hard to debug without understanding LEGB.
- **Prerequisites:** 3.1
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- LEGB Rule (Local, Enclosing, Global, Built-in)
- `global` keyword
- `nonlocal` keyword
- Variable shadowing
- Namespace vs Scope
- `dir()` and `vars()`

---

### 3.3 Recursion

- **Why It Matters:** Required for tree traversal, certain algorithms, and interview questions. Also shows depth of function understanding.
- **Prerequisites:** 3.1
- **Interview Importance:** High (interview circles)
- **Job Importance:** Medium

Topics:
- Base case & recursive case
- Call stack mechanics
- Recursion depth limits (`sys.setrecursionlimit`)
- Memoization preview
- Recursion vs iteration tradeoffs
- Tail recursion (Python doesn't optimize it — why this matters)

---

### 3.4 Modules & Packages

- **Why It Matters:** Real-world Python is organized into modules and packages. You can't work on a professional project without this.
- **Prerequisites:** 3.1
- **Interview Importance:** Low-Medium
- **Job Importance:** Critical

Topics:
- `import` statement forms (`import x`, `from x import y`, `from x import *`)
- `__name__` and `if __name__ == "__main__"`
- Creating your own modules
- Package structure (`__init__.py`)
- Relative imports
- `sys.path` and module resolution
- pip and third-party packages
- Virtual environments (venv)
- `requirements.txt`

---

### 3.5 File Handling

- **Why It Matters:** Reading configs, writing logs, parsing CSVs, processing uploads — file I/O is everywhere in backend systems.
- **Prerequisites:** 3.4
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `open()` function — modes (r, w, a, rb, wb)
- Reading: `.read()`, `.readline()`, `.readlines()`
- Writing: `.write()`, `.writelines()`
- Context manager (`with open(...) as f`)
- Why context managers matter (resource management)
- File paths — absolute vs relative
- `pathlib.Path` (modern approach)
- Binary files
- CSV files (`csv` module)
- JSON files (`json.load`, `json.dump`)
- Encoding (UTF-8)

---

### 3.6 Exception Handling

- **Why It Matters:** Production code fails. Proper exception handling is what separates hobby projects from professional software.
- **Prerequisites:** 3.5
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `try`, `except`, `else`, `finally`
- Catching specific exceptions
- Catching multiple exceptions
- Exception hierarchy (`BaseException` → `Exception` → specific)
- `raise` keyword
- Re-raising exceptions
- Custom exception classes
- Exception chaining (`raise X from Y`)
- When NOT to catch exceptions
- Logging exceptions properly

---

### 3.7 Iterators & Generators

- **Why It Matters:** Python's iteration protocol powers `for` loops, comprehensions, `map`, `filter`. Generators are essential for memory-efficient data processing.
- **Prerequisites:** 3.6
- **Interview Importance:** High — commonly asked
- **Job Importance:** High

Topics:
- Iterator protocol (`__iter__`, `__next__`)
- `iter()` and `next()` built-ins
- Creating custom iterators
- `StopIteration` exception
- Generator functions (`yield`)
- Generator expressions (`(x for x in range(10))`)
- `yield from`
- Lazy evaluation — why it matters for large datasets
- `itertools` preview

---

## Level 4 — Object-Oriented Programming

> *OOP is the architecture language of Python backends. Django, DRF, and virtually all frameworks are built on OOP patterns.*

---

### 4.1 Classes & Objects

- **Why It Matters:** Python's entire ecosystem is built on classes. You cannot read Django's source or understand frameworks without solid OOP.
- **Prerequisites:** Level 3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `class` keyword
- Class vs instance
- `__init__` constructor
- `self` parameter
- Instance attributes
- Instance methods
- String representation (`__str__`, `__repr__`)
- Object identity vs equality (`is` vs `==`)

---

### 4.2 Class vs Instance vs Static Methods

- **Why It Matters:** Django models use all three. Understanding which to use is an interview and code quality question.
- **Prerequisites:** 4.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Instance methods (take `self`)
- Class methods (`@classmethod`, `cls` parameter)
- Static methods (`@staticmethod`)
- When to use each
- Factory pattern using `@classmethod`
- Utility functions using `@staticmethod`

---

### 4.3 Inheritance

- **Why It Matters:** Django's CBVs, DRF's ViewSets, all use deep inheritance. You must understand it to customize framework behavior.
- **Prerequisites:** 4.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Single inheritance
- `super()` function
- Method overriding
- Multiple inheritance
- MRO (Method Resolution Order)
- `__mro__` attribute and `C3 Linearization`
- Diamond problem
- Mixin pattern
- Composition vs Inheritance

---

### 4.4 Encapsulation & Access Control

- **Why It Matters:** Encapsulation is about designing safe, maintainable interfaces. Python's convention-based approach is different from Java — interviewers test this.
- **Prerequisites:** 4.3
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Public, Protected (`_`), Private (`__`) conventions
- Name mangling with `__`
- Properties (`@property`, `@setter`, `@deleter`)
- Descriptor protocol (advanced)
- Why Python uses convention not enforcement

---

### 4.5 Polymorphism & Duck Typing

- **Why It Matters:** Python uses duck typing universally. Understanding this is the key to writing flexible, extensible code.
- **Prerequisites:** 4.4
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Polymorphism via method overriding
- Duck typing ("if it walks like a duck...")
- Abstract Base Classes (ABC)
- `abc.abstractmethod`
- Interfaces via ABCs
- `isinstance()` vs duck typing in practice

---

### 4.6 Magic / Dunder Methods

- **Why It Matters:** Magic methods are how Python's built-in operators work with custom objects. Django models define `__str__`. DRF serializers rely on these patterns.
- **Prerequisites:** 4.5
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `__str__` and `__repr__`
- `__len__`, `__getitem__`, `__setitem__`, `__delitem__`
- `__iter__` and `__next__`
- `__contains__`
- `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
- `__add__`, `__sub__`, `__mul__` (operator overloading)
- `__call__` (callable objects)
- `__enter__` and `__exit__` (context managers)
- `__hash__`
- `__slots__` (memory optimization)

---

## Level 5 — Advanced Python

> *This is what separates intermediate developers from professionals. Required for reading frameworks, writing clean APIs, and passing senior-level interviews.*

---

### 5.1 Decorators

- **Why It Matters:** Django views use `@login_required`. DRF uses `@api_view`. Flask uses `@app.route`. Decorators are everywhere in web frameworks.
- **Prerequisites:** Level 4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Functions as first-class objects (review)
- Closure pattern
- Basic decorator structure
- `functools.wraps` — why it's required
- Decorators with arguments
- Class-based decorators
- Stacking decorators
- Built-in decorators: `@property`, `@classmethod`, `@staticmethod`, `@abstractmethod`, `@dataclass`
- Practical use cases: logging, timing, caching, authentication, retry logic

---

### 5.2 Context Managers

- **Why It Matters:** Used for file handling, database connections, transaction management, locks — all critical backend patterns.
- **Prerequisites:** 4.6 (magic methods), 5.1
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- `with` statement
- `__enter__` and `__exit__`
- Exception suppression in `__exit__`
- `contextlib.contextmanager` decorator
- `contextlib.suppress`
- Nested context managers
- Django's `transaction.atomic()` as a context manager

---

### 5.3 Closures & Higher-Order Functions

- **Why It Matters:** Closures power decorators, callbacks, and functional patterns. Common in interview questions and frameworks.
- **Prerequisites:** 3.2, 5.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Closure definition
- Free variables
- `__closure__` attribute
- `nonlocal` in closures
- Factory functions using closures
- Callback patterns
- `functools.partial`

---

### 5.4 Comprehensions

- **Why It Matters:** Comprehensions make Python code concise and fast. Django querysets and data transformation rely on them heavily.
- **Prerequisites:** Level 2 (collections)
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- List comprehensions (with conditions, nested)
- Dict comprehensions
- Set comprehensions
- Generator expressions (memory efficiency)
- When comprehensions become unreadable — refactoring to loops
- Nested comprehensions (use sparingly)

---

### 5.5 Type Hints & Annotations

- **Why It Matters:** Modern Python codebases require type hints. They're the standard in professional teams. mypy, pyright, FastAPI all rely on them.
- **Prerequisites:** Level 4
- **Interview Importance:** Medium-High
- **Job Importance:** High (growing requirement)

Topics:
- Basic type hints (`int`, `str`, `float`, `bool`, `None`)
- `Optional[X]` (Union with None)
- `List[X]`, `Dict[K, V]`, `Tuple[X, Y]`
- `Union[X, Y]`
- `Any`
- `Callable`
- `TypeVar` (generic types)
- `from __future__ import annotations`
- Return type hints
- mypy basics
- Python 3.10+ union syntax (`X | Y`)

---

### 5.6 Dataclasses

- **Why It Matters:** Dataclasses replace boilerplate classes. They're used in modern Python APIs, configuration objects, and data models.
- **Prerequisites:** Level 4, 5.5
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `@dataclass` decorator
- Auto-generated `__init__`, `__repr__`, `__eq__`
- `field()` for default factories
- `frozen=True` for immutable dataclasses
- `__post_init__`
- Inheritance with dataclasses
- Dataclasses vs NamedTuples vs Pydantic models

---

### 5.7 Collections Module

- **Why It Matters:** These specialized containers solve common problems more efficiently than regular dicts/lists. Interviewers test knowledge of them.
- **Prerequisites:** Level 2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `Counter` — counting elements, most common
- `defaultdict` — dict with default values
- `OrderedDict` — ordered dict (less needed in Python 3.7+)
- `deque` — double-ended queue, O(1) at both ends
- `namedtuple` — lightweight immutable struct
- `ChainMap` — combining multiple dicts

---

### 5.8 Functools & Itertools

- **Why It Matters:** These modules unlock functional programming patterns and efficient iteration. Common in data processing pipelines.
- **Prerequisites:** 5.3, 3.7
- **Interview Importance:** Medium-High
- **Job Importance:** Medium-High

Topics (functools):
- `partial`
- `reduce`
- `lru_cache` / `cache`
- `wraps`
- `total_ordering`
- `cached_property`

Topics (itertools):
- `chain`
- `cycle`
- `repeat`
- `count`
- `islice`
- `product`
- `combinations`
- `permutations`
- `groupby`
- `zip_longest`

---

## Level 6 — Concurrency & Performance

> *Required for building real backend systems — web servers, background workers, data pipelines.*

---

### 6.1 Threading

- **Why It Matters:** I/O-bound tasks (API calls, file reading) benefit from threading. Understanding threading prevents race conditions in production.
- **Prerequisites:** Level 5
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `threading.Thread`
- `start()`, `join()`, `daemon` threads
- Thread safety
- `Lock`, `RLock`
- `Semaphore`
- `Event` and `Condition`
- `threading.local` (thread-local storage)
- Race conditions and how to prevent them
- Thread pools (`concurrent.futures.ThreadPoolExecutor`)

---

### 6.2 Multiprocessing

- **Why It Matters:** CPU-bound tasks require multiprocessing to bypass the GIL. Data processing, image manipulation, computation-heavy tasks.
- **Prerequisites:** 6.1
- **Interview Importance:** Medium-High
- **Job Importance:** Medium

Topics:
- The GIL (Global Interpreter Lock) — what it is and why it matters
- `multiprocessing.Process`
- Process pools (`concurrent.futures.ProcessPoolExecutor`)
- `Queue` for inter-process communication
- Shared memory
- `Pool.map()` and `Pool.starmap()`
- When to use threads vs processes

---

### 6.3 Async Programming

- **Why It Matters:** Modern Python backends (FastAPI, async Django) use async heavily. Understanding asyncio is increasingly required.
- **Prerequisites:** 3.7 (generators), 6.1
- **Interview Importance:** High (growing)
- **Job Importance:** High (growing)

Topics:
- Event loop concept
- Coroutines (`async def`)
- `await` keyword
- `asyncio.run()`
- `asyncio.gather()` — concurrent coroutines
- `asyncio.create_task()`
- `async for` and `async with`
- Difference: async vs threading vs multiprocessing
- `aiohttp` and `httpx` for async HTTP
- When async helps and when it doesn't

---

## Level 7 — Standard Library

---

### 7.1 os & sys

- **Why It Matters:** Environment manipulation, path management, and process control are daily backend developer tools.
- **Prerequisites:** Level 5
- **Interview Importance:** Low-Medium
- **Job Importance:** High

Topics:
- `os.path` (join, exists, dirname, basename)
- `os.getcwd()`, `os.listdir()`, `os.makedirs()`
- `os.environ` and `os.getenv()`
- `os.remove()`, `os.rename()`
- `sys.argv`
- `sys.path`
- `sys.exit()`
- `sys.stdin`, `sys.stdout`, `sys.stderr`

---

### 7.2 datetime

- **Why It Matters:** Every backend application handles dates and times — APIs, logging, scheduling, user data.
- **Prerequisites:** Level 3
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `datetime.date`, `datetime.time`, `datetime.datetime`
- `timedelta`
- `.now()`, `.utcnow()`, `.today()`
- Timezone awareness (`pytz`, `zoneinfo`)
- Formatting (`.strftime()`) and parsing (`.strptime()`)
- ISO 8601 format
- Unix timestamp conversion

---

### 7.3 Regular Expressions (`re`)

- **Why It Matters:** Input validation, log parsing, string extraction — regex is unavoidable in backend development.
- **Prerequisites:** 2.1 (strings)
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- `re.match()`, `re.search()`, `re.findall()`, `re.sub()`, `re.split()`
- Pattern syntax: `.`, `*`, `+`, `?`, `^`, `$`, `[]`, `{}`, `()`
- Character classes (`\d`, `\w`, `\s`)
- Groups and capturing
- Non-greedy matching
- Compiled patterns (`re.compile()`)
- Lookahead and lookbehind (advanced)

---

### 7.4 logging

- **Why It Matters:** Print statements are not production code. Proper logging is mandatory in professional applications.
- **Prerequisites:** Level 3
- **Interview Importance:** Low-Medium
- **Job Importance:** Critical

Topics:
- Logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `logging.basicConfig()`
- Logger hierarchy
- Handlers (StreamHandler, FileHandler, RotatingFileHandler)
- Formatters
- `logging.getLogger(__name__)` pattern
- Structured logging (JSON logs)
- Django logging configuration

---

### 7.5 json

- **Why It Matters:** JSON is the lingua franca of web APIs. Every backend developer handles JSON constantly.
- **Prerequisites:** Level 2
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `json.loads()` (string to dict)
- `json.dumps()` (dict to string)
- `json.load()` (file to dict)
- `json.dump()` (dict to file)
- Custom serializers (`default` parameter)
- `indent` and `sort_keys` for readability
- Handling non-serializable types (datetime, Decimal)

---

## Level 8 — Testing

---

### 8.1 Unit Testing with `unittest`

- **Why It Matters:** Every professional team uses tests. Writing testable code forces better design.
- **Prerequisites:** Level 4 (OOP)
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `TestCase` class
- `setUp()` and `tearDown()`
- Assertion methods (`assertEqual`, `assertRaises`, `assertTrue`, etc.)
- Test discovery
- Test suites
- Running tests

---

### 8.2 Pytest

- **Why It Matters:** Pytest is the de facto standard for Python testing in professional environments.
- **Prerequisites:** 8.1
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- Pytest basics (writing test functions)
- Assertions (plain `assert` with introspection)
- Fixtures (`@pytest.fixture`)
- Fixture scope (function, class, module, session)
- `conftest.py`
- Parametrize (`@pytest.mark.parametrize`)
- Markers (`@pytest.mark.skip`, `@pytest.mark.xfail`)
- Plugins ecosystem
- `pytest-django`
- Running specific tests

---

### 8.3 Mocking

- **Why It Matters:** Backend tests must mock external dependencies (databases, APIs, email services) to be fast and reliable.
- **Prerequisites:** 8.2
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- `unittest.mock.Mock`
- `unittest.mock.MagicMock`
- `unittest.mock.patch` (decorator and context manager)
- Patching at the right level
- `return_value` and `side_effect`
- Checking mock calls
- `patch.object`
- `mock_open`

---

### 8.4 Test Coverage

- **Why It Matters:** Coverage metrics tell you how much of your code is tested. Industry standard is 80%+.
- **Prerequisites:** 8.2
- **Interview Importance:** Low
- **Job Importance:** Medium-High

Topics:
- `pytest-cov`
- Coverage reports (terminal, HTML)
- Branch coverage
- What coverage does NOT tell you
- Excluding files from coverage

---

## Level 9 — Python for Backend

> *The bridge between Python language skills and professional backend development.*

---

### 9.1 Virtual Environments & Dependency Management

- **Why It Matters:** Every professional Python project uses virtual environments. Not knowing this makes you unable to set up a project.
- **Prerequisites:** 3.4
- **Interview Importance:** Low
- **Job Importance:** Critical

Topics:
- `venv` creation and activation
- `.venv` directory convention
- pip commands (install, freeze, install -r)
- `requirements.txt` vs `pyproject.toml`
- `pipenv` and `poetry` (awareness)
- Dependency pinning
- Virtual env in production vs Docker

---

### 9.2 Environment Variables & Configuration

- **Why It Matters:** Secrets (API keys, DB passwords) must never be hardcoded. This is a security and professionalism requirement.
- **Prerequisites:** 7.1
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- `os.environ`
- `.env` files
- `python-dotenv`
- `django-environ`
- 12-factor app config principle
- Separating config from code

---

### 9.3 HTTP Requests with `requests` & `httpx`

- **Why It Matters:** Consuming third-party APIs is a core backend skill — payment gateways, SMS, external data sources.
- **Prerequisites:** Level 5
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- GET, POST, PUT, PATCH, DELETE requests
- Request headers and authentication
- Query parameters
- Request body (JSON, form data)
- Response handling (status code, `.json()`, `.text`)
- Timeouts
- Session objects (connection reuse)
- Error handling
- `httpx` (async-capable alternative)
- Retry logic

---

### 9.4 JSON & Data Serialization

- **Why It Matters:** APIs exchange JSON. ORMs return Python objects that must be serialized. This is the core of all API work.
- **Prerequisites:** 7.5, Level 4
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- Python objects ↔ JSON (round-trip)
- Custom JSON encoders/decoders
- `Decimal` handling
- `datetime` serialization
- Pydantic for data validation and serialization (awareness)
- DRF serializers (covered in Backend Engineering)

---

### 9.5 Database Connectivity

- **Why It Matters:** Direct database access (without an ORM) is required for migrations, raw queries, and performance-critical code.
- **Prerequisites:** Level 4, SQL knowledge
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `psycopg2` for PostgreSQL
- Connection and cursor
- Executing queries (parameterized queries — SQL injection prevention)
- Fetching results (fetchone, fetchmany, fetchall)
- Committing and rolling back
- Connection pools (`psycopg2.pool`)
- SQLAlchemy Core (conceptual)
- Django ORM vs raw SQL tradeoffs

---

### 9.6 Project Structure & Packaging

- **Why It Matters:** Professional Python projects follow structure conventions. Interviewers look for this in GitHub portfolios.
- **Prerequisites:** 3.4, all levels
- **Interview Importance:** Low
- **Job Importance:** High

Topics:
- Flat vs nested project layout
- `src/` layout
- `pyproject.toml` structure
- `setup.py` / `setup.cfg` (legacy)
- `__init__.py` purpose
- Application factory pattern
- Configuration classes
- Constants and settings separation

---

*This syllabus is the knowledge inventory for Python. Roadmap and scheduling are managed separately.*
