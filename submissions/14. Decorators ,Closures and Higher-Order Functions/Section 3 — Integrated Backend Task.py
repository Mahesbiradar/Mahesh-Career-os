
# Section 3 — Integrated Backend Task


"""
**20 marks**

Now we're going to combine everything.

## Q15 — Authenticated Function Wrapper

**10 marks**

Imagine you're building a backend system.

You have:

```python
def get_user_data(user_id):
    return f"Data for user {user_id}"
```

Create a decorator:

```python
require_role(required_role)
```

so that you can write:

```python
@require_role("admin")
def delete_user(user_id):
    return f"User {user_id} deleted"
```

The decorator should expect the function call to provide:

```python
user_role
```

through a keyword argument.

Example:

```python
delete_user(101, user_role="admin")
```

should execute successfully.

But:

```python
delete_user(101, user_role="user")
```

should **not execute the original function** and should return:

```text
"Access denied"
```

### Requirements

Your implementation must demonstrate:

* decorator with arguments
* closure capturing `required_role`
* `*args`
* `**kwargs`
* `functools.wraps`
* returning the original function's result
* blocking unauthorized execution

---


"""
from functools import wraps

def require_role(required_role):

    def decorator_func(func):

        @wraps(func)
        def wrapper(*args,**kwargs):

            user_role = kwargs.pop('user_role',None)

            if required_role == user_role:

                result = func(*args,**kwargs)
            else:

                result = f"Access denied"

            return result


        return wrapper

    return decorator_func


@require_role("admin")
def delete_user(user_id):
    return f"User {user_id} deleted"


delete_user(101, user_role="admin")
delete_user(105, user_role="admin")


# Here i learned one thing during the function call we are passing the two argumets user id and user role so intailly im confused witjoutextracting and removing keyword agrumnet in wrapper before original call its giving errors so i used AI help here remaing all thinhs are retunr by me.

"""
## Q16 — Closure + Decorator Combination

**10 marks**

Create a decorator:

```python
@limit_calls(3)
def process():
    return "Processing..."
```

The decorated function should be allowed to execute **only 3 times**.

Expected behavior:

```python
print(process())  # Processing...
print(process())  # Processing...
print(process())  # Processing...
print(process())  # Limit exceeded
print(process())  # Limit exceeded
```

### Requirements

You must implement the call counter using a **closure**.

You should therefore have the conceptual structure:

```text
limit_calls(3)
      ↓
captures limit = 3
      ↓
decorator(func)
      ↓
wrapper()
      ↓
closure remembers call_count
```

**Do not use a global variable.**

"""

def limit_calls(times):


    def decorator_func(func):

        count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):

            nonlocal count

            if count < times:

                result = func(*args,**kwargs)

                count += 1
            else:
                result = f"Limit exceeded"

            return result

        return wrapper

    return decorator_func




@limit_calls(3)
def process():
    return "Processing..."


print(process())
print(process())
print(process())
print(process())
print(process())