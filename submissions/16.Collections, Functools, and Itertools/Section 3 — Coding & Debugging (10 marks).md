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

def log_call(func):    
    def wrapper(*args, **kwargs):        
        print("Calling function...")        
        return func(*args, **kwargs)    
    return wrapper

```


Q13. (4 marks) — `lru_cache`

Find the mistake in this code and explain the correct approach.

```
from functools import lru_cache@lru_cache(maxsize=128)def get_user(user_id, filters):    return fetch_user(user_id, filters)
```

Assume `filters` is a Python dictionary. Explain why the code fails when called with a dictionary and suggest a suitable fix.

