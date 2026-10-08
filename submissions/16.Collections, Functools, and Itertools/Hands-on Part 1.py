# Exercise 1 — Log Status Analyzer

"""
logs = [
    200, 200, 404, 500,
    200, 404, 403, 500,
    200, 500
]

Using Counter:
1. Count every status code.
2. Find the two most common status codes.
3. Find the count of 404.
4. Check what happens when you access a status that doesn't exist, such as 302.

"""

from collections import Counter

logs = [
    200, 200, 404, 500,
    200, 404, 403, 500,
    200, 500
]


counter = Counter(logs)

print(counter.most_common(2))

print(counter[404])

print(counter[302])


# Exercise 2 — Group Users by Role


"""
Given:
users = [    ("Mahesh", "admin"),    ("Rahul", "user"),    ("Anita", "admin"),    ("Kiran", "user"),    ("Priya", "manager"),]


Using:
defaultdict


create:
{    "admin": ["Mahesh", "Anita"],    "user": ["Rahul", "Kiran"],    "manager": ["Priya"]}


Do not manually check:
if role not in ...


The purpose is to practice defaultdict.

"""

from collections import defaultdict

users = [
    ("Mahesh", "admin"),
    ("Rahul", "user"),
    ("Anita", "admin"),
    ("Kiran", "user"),
    ("Priya", "manager"),
]

users_dict = defaultdict(list)


for name,role in users:

    users_dict[role].append(name)


print(users_dict)


# Exercise 3 — Unique Permissions

"""
Given:
permissions = [    ("Mahesh", "read"),    ("Mahesh", "write"),    ("Mahesh", "read"),    ("Rahul", "read"),    ("Rahul", "delete"),    ("Rahul", "read"),]


Using:
defaultdict(set)


produce:
{    "Mahesh": {"read", "write"},    "Rahul": {"read", "delete"}}
"""

permissions = [
    ("Mahesh", "read"),
    ("Mahesh", "write"),
    ("Mahesh", "read"),
    ("Rahul", "read"),
    ("Rahul", "delete"),
    ("Rahul", "read"),
]


users = defaultdict(set)

for name , permisson in permissions:

    users[name].add(permisson)

print(users)


# Exercise 4 — Named API Result

"""
Create a namedtuple called:
APIResult

with:
status_code
message

Create:
result = APIResult(200, "Success")


Then access both values using field names, not indexes.

"""

from collections import namedtuple


APIResult = namedtuple("APIResult",("status_code","message"))

result = APIResult(200, "Success")


print(result.message)
print(result.status_code)

