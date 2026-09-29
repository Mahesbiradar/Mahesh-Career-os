# Section 2 — Coding


"""
**20 marks**

Write the code yourself. Focus on clean, readable Python rather than clever code.

---

## Q11 — Easy — 5 marks

Write a generator function:

```python
count_even(n)
```

that generates all even numbers from `2` through `n`.

Example:

```python
for x in count_even(10):
    print(x)
```

Expected:

```text
2
4
6
8
10
```

**Requirements:**

* Must use `yield`
* Should not create a list containing all the numbers

---

"""

def count_even(n):

    for num in range(2,n+1):

        if num % 2 == 0:
            yield num

for i in count_even(10):
    print(i)


""""

## Q12 — Medium — 7 marks

You receive user records:

```python
users = [
    {"id": 101, "active": True},
    {"id": 102, "active": False},
    {"id": 103, "active": True},
    {"id": 104, "active": False},
    {"id": 105, "active": True},
]
```

Write a generator:

```python
active_user_ids(users)
```

that yields only the IDs of active users.

Expected values:

```text
101
103
105
```

Then show how you would consume the generator using a `for` loop.

**Constraint:** Do not create a separate list of active users.

---

"""

users = [
    {"id": 101, "active": True},
    {"id": 102, "active": False},
    {"id": 103, "active": True},
    {"id": 104, "active": False},
    {"id": 105, "active": True},
]

def active_user_ids(users):

    for user in users:

        if user["active"]:
            yield user["id"]


active_user = active_user_ids(users)

for userid in active_user:
    print(userid)

"""

## Q13 — Hard — 8 marks

Create a custom iterator class:

```python
class CountDown:
```

It should:

* Start from a number supplied to `__init__`
* Return the current number each time `next()` is called
* Count downward by 1
* Stop after returning `1`
* Raise `StopIteration` when exhausted
* Work with a `for` loop

Example:

```python
countdown = CountDown(5)

for number in countdown:
    print(number)
```

Expected:

```text
5
4
3
2
1
```

Your class should correctly implement the iterator protocol.

---
"""


class CountDown:

    def __init__(self,start):

        self.current = start

    def __iter__(self):
        return self

    def __next__(self):

        value = self.current

        if self.current < 1:
            raise StopIteration

        self.current -= 1

        return value


countdown = CountDown(10)


for number in countdown:
    print(number)


