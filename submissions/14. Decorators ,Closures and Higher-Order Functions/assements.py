# Exercise 1 — Higher-Order Function

"""
Create:

def calculate(operation, a, b):
    ...

It should accept a function such as:

def add(a, b):
    return a + b

and:

def multiply(a, b):
    return a * b

Then demonstrate both.

"""

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b

def calculate(operation, a, b):

    return operation(a,b)

print(calculate(add,10,15))
print(calculate(multiply,10,15))


"""
Exercise 2 — Closure

Create:

def multiplier(n):
    ...

It should return a function that multiplies its input by n.

Expected:

double = multiplier(2)
triple = multiplier(3)

print(double(10))   # 20
print(triple(10))   # 30

Then explain what variable is captured by the closure

"""

def multiplier(n):

    def wrapper(k):

        return n * k

    return wrapper


double = multiplier(2)
triple = multiplier(3)

print(double(10))   # 20
print(triple(10))   # 30

# The enclosing variable n is captured by the clousre.


"""
Exercise 3 — Stateful Closure

Create:

def counter():
    ...

Expected:

c = counter()

print(c())  # 1
print(c())  # 2
print(c())  # 3

You must use nonlocal.

"""

def counter():

    count = 0

    def wrapper():

        nonlocal count

        count += 1

        return count

    return wrapper


c = counter()

print(c())
print(c())
print(c())
print(c())
print(c())
print(c())


"""
Exercise 4 — partial()

Given:

def power(base, exponent):
    return base ** exponent

Use functools.partial() to create:

square
cube

such that:

square(5)  # 25
cube(5)    # 125

"""

from functools import partial


def power(base,exponent):

    return base ** exponent


square = partial(power,exponent=2)
cube = partial(power,exponent=3)


print(square(5))
print(cube(5))



"""
Exercise 5 — Basic Decorator

Create:

@logger
def greet(name):
    return f"Hello {name}"

The decorator should print:

Function started
Function finished

and must return the original result.

Use:

*args
**kwargs

"""


def logger(func):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = func(*args, **kwargs)

        print(result) # Optional if we want to print the function result just after the first print statement.

        print("Function finished")

        return result

    return wrapper


@logger
def greet(name):
    return f"Hello {name}"


greet("Mahesh")



"""
Exercise 6 — functools.wraps

Modify Exercise 5 to use:

from functools import wraps

Then verify:

print(greet.__name__)

returns:

greet

"""

from functools import wraps

def logger(func):


    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Function started")

        result = func(*args, **kwargs)

        print(result) # Optional if we want to print the function result just after the first print statement.

        print("Function finished")

        return result

    return wrapper


@logger
def greet(name):
    return f"Hello {name}"


greet("Mahesh")

print(greet.__name__)



"""
Exercise 7 — Decorator With Arguments

Create:

@repeat(3)
def greet():
    print("Hello")

Expected:

Hello
Hello
Hello

This is the most important exercise. Make sure you understand why there are three nested levels.

"""

from functools import wraps

def repeat(times):
    def decorator_func(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            result = None

            for _ in range(times):
                result = func(*args, **kwargs)

            return result

        return wrapper
    
    return decorator_func



@repeat(10)
def greet():
    print("Hello")

greet()


"""
Exercise 8 — Multiple Decorators

Create:

@uppercase
@logger
def greet():
    return "hello mahesh"

Make it produce:

HELLO MAHESH

Then explain the order in which the decorators are applied and executed.

"""

from functools import wraps


def logger(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Log:Function Execution started")
        result = func(*args, **kwargs)
        print(f"Log: function Execution stoped")
        return result

    return wrapper


def uppercase(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs).upper()

        return result

    return wrapper


@uppercase
@logger
def greet():
    return "hello mahesh"

print(greet())



"""
Exercise 9 — Class Decorator

Create:

@add_info
class User:
    def __init__(self, name):
        self.name = name

The decorator should add:

user.info()

which prints:

User: Mahesh

"""


def add_info(cls):

    def info(self):
        print(f"User: {self.name}")

    cls.info = info

    return cls

@add_info
class User:

    def __init__(self,name):

        self.name = name


user = User("Mahesh")

user.info()


