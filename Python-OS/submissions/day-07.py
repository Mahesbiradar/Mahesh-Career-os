## TODAY'S ASSIGNMENT

"""
Goal: Demonstrate function definitions with `return`, default parameters, and functions calling other functions — with exact output formatting.

"""

#1. - [ ] Define a function `greet(name)` that RETURNS (does not print inside the function) the string `f"Hello, {name}!"`. Call it once with your own name and print the returned value — output must be exactly `Hello, Mahesh!` (use your own name in place of Mahesh).

def greet(name):

    """The function returns greeting with name passed in argument to the parameter name"""

    return f"Hello, {name}!"

print(greet("Mahesh"))

#2.- [ ] Define a function `add(a, b)` that returns the sum of the two arguments. Call it twice with two different number pairs and print each result using the exact format `Sum: 8` (label, colon, space, then the result — nothing else).

def add(a, b):
    """This function takes two arguments as parameter a and b and then returns the sum of a+b"""

    return a+b

print("Sum:",add(10,5))
print("Sum:",add(5,3))


#3.- [ ] Define a function `power(base, exponent=2)` with a default value for `exponent`. Call it once passing only `base` (relying on the default) and once passing both `base` and a different `exponent`. Print both results using the exact format `Result: 9`.

def power(base, exponent=2):

    return f"Result: {base**exponent}"


print(power(3)) #with base ommiting the defualt parametere expo
print(power(3,exponent=3))

#4.- [ ] Define a function `square(n)` that returns `n * n`. The function body itself must NOT contain a `print()` statement — only `return`. Call `square()` on a number and print the returned value using the exact format `Square: 16`.

def square(n):

    return n*n

print("Square:",square(4))
print("Square:",square(9))


#.5- [ ] Define a function `introduce(name, age)` that calls your `greet(name)` function from requirement 1 inside its own body, then also prints the age using the exact format `Age: 24`. Call `introduce()` once. This must demonstrate one function calling another — do not just copy the greet logic again inline.

def introduce(name, age):

    #calling greet function

    # greetings = greet(name)

    return f"{greet(name)}, Age: {age}"


print(introduce("Mahesh",28))

#Stretch (optional — do only after main requirements done):

# 6.- [ ] Define a function `total(*args)` that returns the sum of any number of arguments passed to it. Call it with 4 numbers and print the result using the exact format `Total: 30`.

def total(*args):

    totalsum = sum (args)


    return f"Total: {totalsum}"

print(total(10,15,3,2))

## COMMUNICATION PRACTICE (15 min)

"""
Task: Explain "functions" as if an interviewer just asked: *"Can you explain what a function is and why we use them?"*

Write a short explanation (4–6 sentences) covering:
- What a function is, in your own words
- Why you'd use one instead of repeating code
- One concrete example from today's assignment (e.g., `greet`, `add`, or `power`)

"""

# Can you explain what a function is and why we use them?

# What a function is, in your own words

# A function is reusable block of code used to preform a single or a specific task. a function is defined with def greet(name): and a body.

# Why you'd use one instead of repeating code

# i'd use a function to reduce the redundancy in the program. ex: if i have to add two number at multple places in single program instead of writing a code for adding two number i'd use the function. This removes the unneccesary wrtting same code at multiple locations.

# Examples of function

def greet(name):

    """This function returns the greeting with user passed argument name"""

    return f"Hello, {name}!"

print(greet("Mahesh Kumar"))


## REVISION CHECK (answer these without looking — 2 min)

#1. What is the actual difference between using `continue` inside a loop and wrapping the rest of your loop body in an `if` condition to skip an item?

# The main diffrence is suppose we are using the continue to skip the curremt iteration once the continue statement executes then it immedeatly jumps to next iteration whereas in if we use conditionals to skip the iteration it skips the taks warapped inside the conditional but if any code block exist after the conditional statement it will also executes but in continue any block of code after the continue not going to execute it simply jumps to next iteration.

#2.2. If a spec requires the exact output `Result: 9`, what's wrong with writing `Result:9` (no space) or `result: 9` (lowercase r)?

# Since the spec requires the excat output as 'Result: 9' then skipping space or writing lowercase is wrong bcz the specs requires the exact same output and what we are writting inside the f" string it will going to return the same what we written.










