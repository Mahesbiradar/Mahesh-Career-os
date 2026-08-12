# Section 4 — Debugging ⭐⭐⭐

# Q1 — Mutation vs Reassignment

numbers = [1, 2, 3]

def update(data):
    data.append(4)
    data = [10, 20]

update(numbers)

print(numbers)

#1. What is the output?
[1, 2, 3, 4]

#2.Why does append(4) affect the original list?

# ans:In functon call data.append(4) here data refering the same object where number is refering there for it appends the 4 in the same object and therefor its affects the original list.

# Why does data = [10, 20] NOT replace numbers?

# Ans: Here data.append the data refering the global object numbers but the data = [10,20] here data is not refering the global object number here python creates the local varible called data and it contains [10, 20] therefor data = [10, 20] not replace the numbers.


# Q2 — **kwargs Bug

# def create_profile(**details):

#     profile = {}

#     for key, value in details:
#         profile[key] = value

#     return profile


# result = create_profile(
#     name="Mahesh",
#     city="Bangalore"
# )

# print(result)

# This is commented out bcz the remaining functions will not run after this.

# 1. What is the bug?

# Ans: inside the function in loop iterating over the dict and it shoud be details.items():
#2.What error occurs?

#. Ans: Not sure but i think value error.

#3.Fix the code.

 
def create_profile(**details):

    profile = {}

    for key, value in details.items():
        profile[key] = value

    return profile


result = create_profile(
    name="Mahesh",
    city="Bangalore"
)

print(result)


#4. What will the final output be?

# ans:  { 'name':'Mahesh','city':'Bangalore'}

# Q3 — Function Contract

def apply_discount(total, discount=0):

    return total * discount / 100


price = apply_discount(2000, 10)

print(f"Final price: {price}")


#1. What is wrong with the function?

#ans : af of now the function returning only the dicounted amount.

#2. What should it return?

# ans: as per the requirement the function shoud return the total amount after discount 

#3. Fix it.


def apply_discount(total, discount=0):

    discount = total * discount / 100

    return total-discount


price = apply_discount(2000, 10)

print(f"Final price: {price}")


# Section 5 — Output Prediction ⭐⭐⭐

# Q1 — Default Arguments

def greet(name, city="Bangalore"):
    return f"{name} lives in {city}"


print(greet("Mahesh"))
print(greet("Rahul", "Pune"))


# ans the first function call prints 'Mahesh lives in Bangalore' and second function call prints 'Rahul lives in Pune'


# Q2 — *args

def calculate(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(calculate(10, 20))
print(calculate(1, 2, 3, 4))


# Ans: the first function call returns 30 and then second one returns 10.

# The numbers inside the function is tuple.

# Q3 — return vs print

def add(a, b):
    print(a + b)


result = add(10, 20)

print(result)

# What is the exact output?

# ans:  first line will be 30 and then None 

# Explain why None appears.

# ans: inside the function we are used print but we are not returning anything while the function is called it prints the sum of a + b but return None and the result varibels stires the None therfor the printing the result will prints the None. if we return the a + b then the result will prints the 30.

# Q4 — Unpacking

def display(name, age, city):
    print(f"{name} | {age} | {city}")


student = {
    "name": "Mahesh",
    "age": 22,
    "city": "Bangalore"
}

display(**student)


# Predict the output.

# ans: Mahesh | 22 | Bangalore

# Explain what **student does.

# the **student unpack the dictionary into the keyword arguments for example here in code display (name = "Mahesh", age = "22", city = "Bangalore")

# Q5 — Mutation

numbers = [1, 2, 3]

def modify(data):
    data.append(4)
    return data


result = modify(numbers)

print(result)
print(numbers)

# Predict the exact output.

# ans:  [1, 2, 3, 4]  again [1, 2, 3, 4]


  


"""
# Section 6 — Interview Questions 🎯

### Q1. `return` vs `print`

You're asked:

> "Why should a reusable backend function generally return a value instead of printing it?"

Explain the difference and give a small example.

# Ans: Bcz returing the value is useful for further operations in program the program can use same value of other operations. whereas the printing just displays the things thats is if we want to use the value of that operation we cannot do the same using the print.

ex: def add(a,b):
        print(a+b)
Here the add function prints the sum of a + b but this functions doent return anything but if we retunrn the value 
        return a+b
this can be used in program for other operations also.

---

### Q2. Scope & LEGB

An interviewer asks:

> "What is the LEGB rule in Python, and why is it important?"

Explain **Local → Enclosing → Global → Built-in** in your own words.

# ans: LEGB Rule in python describes the priority of the varibles and scope. This is important bcz without priortizing the things data discripancy may occur and there will be no standard practice.

In python functions as per the LEGB rule the python priortize the local variable if exist or it may check for enclosing varibel then global and built in.
---

### Q3. `*args` vs `**kwargs`

Explain the difference between:

```python
def process(*args, **kwargs):
    ...
```

Cover:

* What each accepts
* What type each becomes inside the function
* One practical backend use case

---
## Ans: *args are used for arbitary positional parameters and **kwargs are used for the arbitary keyword parameters.
*args accepts the postional argumentes and **kwargs accept keyword arguments.
*args becomes tuple inside the function and **kwargs become dictionary.
# Dont have exposure to use these in the backend so not sure.


### Q4. Mutation vs Reassignment ⭐

This is your most important question from today's assessment.

An interviewer asks:

> "If I pass a list to a function and call `.append()` on it, why can the original list change without using `global`?"

Then explain why this behaves differently:

```python
x = 10

def modify():
    x = 20
```

Keep your answer focused on **object mutation vs name reassignment**.

---

##Ans: The original list changes because the local varible created by the function refering to the same object and appending that list inside the function mutates the original object without using the global also.

Here in above code the gloabl x object and the x inside the functions are different objects Therefor. its behaves differenty in function the x is created at diffrent memory location and assigned 20 as value so here reassignment to global x not takes place.


### Q5. Scenario-Based — Backend API ⭐⭐⭐

You're building a user-registration API.

You want a function:

```python
create_user(
    "Mahesh",
    "mahesh@example.com",
    city="Bangalore",
    skills=["Python", "Django"]
)
```

to return:

```python
{
    "name": "Mahesh",
    "email": "mahesh@example.com",
    "city": "Bangalore",
    "skills": ["Python", "Django"]
}
```

The interviewer asks:

> "How could you design the function using parameters, default arguments, `*args`, or `**kwargs`? Which approach would you choose and why?"

Don't just write code. **Explain your design decision.**

---

def create_user(name, email, *, city="Unknown", skills=None):
    return {
        "name": name,
        "email": email,
        "city": city,
        "skills": skills if skills is not None else []
    }

ill use this approch here name and email will be postional argument and then ill use *args to handel additional postional details if required and then use the defulat parameneter city and the ill use **kwargs. for keyword argumnets.

"""

