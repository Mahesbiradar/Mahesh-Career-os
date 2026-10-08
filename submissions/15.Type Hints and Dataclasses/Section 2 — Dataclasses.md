
---

# Section 2 — Dataclasses

### **15 marks**

### Q6. Dataclass fundamentals — 4 marks

Explain what `@dataclass` gives you compared with writing a normal class manually.

Your answer should discuss at least **three** automatically generated or simplified behaviors.

Then explain why this:

```python
@dataclass
class User:
    id: int
    name: str
    age: int
```

is useful for representing backend data.

---

# Ans: The @dataclass decorator automatically generates boilerplate methods that you would otherwise have to write manually in a standard class:

• __init__ (Initializer): Automatically maps the defined type hints to instance variables so we can instantiate the class immediately (e.g., User(1, "Mahesh", 25)) without writing self.id = id repeatedly.
• __repr__ (String Representation): Provides a clean, human-readable string output when we print the object (e.g., User(id=1, name='Mahesh', age=25)), making debugging significantly easier.
• __eq__ (Equality Comparison): Automatically allows us to compare two object instances using ==. It checks if all their field values are identical, rather than checking if they occupy the same memory address.

It serves as a clean Data Transfer Object (DTO). It isolates raw data (like API requests or database rows) from business logic, making it easy to validate and convert into format-like JSON payloads.

### Q7. Predict the output — 3 marks

Consider:

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

u1 = User(101, "Mahesh")
u2 = User(101, "Mahesh")

print(u1)
print(u1 == u2)
```

What will the two `print()` statements produce?

More importantly, **why** does `u1 == u2` produce that result?

---

# Ans: O/P

("id" = 101, "name" = "Mahesh")
True


The dataclass generates the bolerplate methods such __eq__ which comapares two object instances using == it checks if all their fields values are identical. Since u1 and u2 have same values therefor it prints True.


### Q8. `default` vs `default_factory` — 4 marks

Consider:

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    roles: list[str] = field(default_factory=list)
```

Answer:

**a)** What does `default_factory=list` do?

**b)** Why is it useful for a mutable value such as a list?

**c)** What happens here?

```python
u1 = User("Mahesh")
u2 = User("Rahul")

u1.roles.append("admin")
```

What will:

```python
print(u1.roles)
print(u2.roles)
```

produce?

**d)** Explain why the two objects don't share the same list.

---

# Ans:
A: The default_factory=list provides a callable function(list) that dynamically creates brand new, empty list every single time a new user object is instantiated 

B: Python evaluates defualty arguments only once when the class is first defined, if we use a standard defualt like roles: list = [], every object would point to the same exact list in memory. defulat_factory prevents this by creating a fresh container for each instance.

C: O/P 
["admin"]
[]

D: Because the default_factory=list was used, u1 and u2 each invoked the list function independently during the their intialization this allocated two completely distinct memory addresses for their respective roles lists, ensuring changes to u1 do not leak into u2.


### Q9. `field()` + `__post_init__` — 4 marks

Consider:

```python
@dataclass
class Employee:
    name: str
    salary: float = field(repr=False)

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")
```

Answer:

**a)** What does `repr=False` do?

**b)** When is `__post_init__()` called?

**c)** Why is `__post_init__()` useful with dataclasses?

**d)** What happens when this executes?

```python
employee = Employee("Mahesh", -5000)
```

---

# Ans:

A: The @dataclass creates the boilerplate behaviour such as repr which Provides a clean, human-readable string output when printed The `repr=False` will prevent this filed during the printing. whne we print the object created by class Employee the repr=False not prints the salary field.

B: __post_init__() this method is called during the object state intialization.

C: `__post_init__() IS udeful with dataclasses for raising the exeptions.

D: Whne employee = Employee("Mahesh", -5000) this executes the __post_init__() method raises ValueError exeption because the salary is less than 0.



