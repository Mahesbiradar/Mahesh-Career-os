Great, Mahesh. Let's continue with Sections 3 & 4. We'll keep these concise but test whether you can apply the concepts independently.

# Section 3 — Coding & Debugging (10 marks)

Q11. (3 marks) — `defaultdict`

Complete the code to group usernames by role without checking whether each key already exists.

```python
from collections import defaultdict
users = [    ("Mahesh", "admin"),    ("Rahul", "user"),    ("Amit", "admin")]
# Complete the missing lines

```

Write the code that creates the appropriate dictionary and groups the usernames. State the final dictionary.

# Ans:

```python
from collections import defaultdict
users = [    ("Mahesh", "admin"),    ("Rahul", "user"),    ("Amit", "admin")]

user_dict = defaultdict(list)

for name,role in users:

    user_dict[role].append(name)

```

Q12. (3 marks) — `wraps`

The following decorator works, but has a metadata problem.

```Python
def log_call(func):    
    def wrapper(*args, **kwargs):        
        print("Calling function...")        
        return func(*args, **kwargs)    
    return wrapper
```

What import and exact code change are needed to preserve the original function's name and docstring?

# Ans:

```python

from functools import wraps

def log_call(func):

    @wraps(func)    
    def wrapper(*args, **kwargs):        
        print("Calling function...")        
        return func(*args, **kwargs)    
    return wrapper

```


Q13. (4 marks) — `lru_cache`

Find the mistake in this code and explain the correct approach.

``` Python
from functools import lru_cache
@lru_cache(maxsize=128)
def get_user(user_id, filters):    
    return fetch_user(user_id, filters)
```

Assume `filters` is a Python dictionary. Explain why the code fails when called with a dictionary and suggest a suitable fix.


# Ans:

The code fails beacause filters is paassed as a Python dictionary which is a mutable (unhashable) data type.

The lru_cache decorator works by using a hidden dictionary to store previous function inputs as keys and their returned results as values.

In Python, dictionary keys must be hashable (immutable). Because standard Python dictionaries are mutable, they cannot be hashed, resulting in a TypeError: unhashable type: 'dict'.


To fix this, you must convert the mutable dictionary into an immutable, hashable alternative before or during the caching process.


from functools import lru_cache


@lru_cache(maxsize=128)
def _get_user_cached(user_id, filters_tuple):
  # Internal cached function using the hashable tuple
  filters = dict(filters_tuple)  # Convert back to dict if fetch_user needs it
  return fetch_user(user_id, filters)


def get_user(user_id, filters):
  # Public wrapper that converts the dict to a sorted tuple of items
  filters_tuple = tuple(sorted(filters.items()))
  return _get_user_cached(user_id, filters_tuple)


If external packages are allowed, you can use frozendict, which behaves exactly like a dictionary but is completely immutable.


from functools import lru_cache
from frozendict import frozendict


@lru_cache(maxsize=128)
def get_user(user_id, filters):
  # The caller must pass filters as a frozendict(filters)
  return fetch_user(user_id, filters)
