# Exercise 5 — partial

"""
Create:
def calculate_price(price, tax_rate):    ...


Then use partial() to create:
calculate_gst = ...


where the tax rate is fixed at 18%.

Test:
calculate_gst(1000)calculate_gst(5000)


"""

from functools import partial


def calculate_price(price, tax_rate):

    return price * tax_rate



calculate_gst = partial(calculate_price,tax_rate = 1.18)


print(calculate_gst(1000))
print(calculate_gst(5000))


# Exercise 6 — reduce

"""
Given:
numbers = [5, 10, 15, 20]

Use reduce() to calculate the total.
Then use reduce() to calculate the product:
5 × 10 × 15 × 20

Do not use sum() for the first one.

"""
from functools import reduce

numbers = [5, 10, 15, 20]


total_sum = reduce(lambda a,b : a+b,numbers)

print(total_sum)

product_numbers = reduce(lambda a,b : a * b,numbers)

print(product_numbers)

# Exercise 7 — wraps

"""
Create a decorator:
def log_call(func):    ...


It should print:
Calling function...

before executing the original function.
Use @wraps.

Then:
@log_calldef greet(name):   Greets a user.    return f"Hello {name}"


Verify:
print(greet.__name__)print(greet.__doc__)


You should demonstrate that the original function metadata is preserved.

"""

from functools import wraps

def log_call(func):

    @wraps(func)
    def wrapper(name):
        print("Calling function...")
        result = func(name)
        return result

    return wrapper


@log_call
def greet(name):
    """Greets a user."""
    return f"Hello {name}"

message = greet("mahesh")
print(message)

print(greet.__name__) 
print(greet.__doc__)   


# Exercise 8 — lru_cache


from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):

    if n<=1 :
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
print(fibonacci(20))
print(fibonacci(30))

print(fibonacci.cache_info())


# hits: The number of times the functions was called with a value it already computed. instead of re-runing the mathematical steps, • Python instantly looked up the answer in the cache and returned it, saving time.

# misses: The number of times function was called with values it  had not seen before. When a miss occurs, Python has to run the actual body of your code, calculate the result, and store it in the cache.

# maxsize: The upper limit of how many results the cache can store before it starts throwing away old data. Because you set maxsize=None, the cache is unbounded—it will grow infinitely to store every single unique input it receives, and it will never discard an entry.

# currsize: The current number of entries sitting in the cache right now. Because maxsize=None, currsize will always equal the total number of unique arguments passed to the function so far.










