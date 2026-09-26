
# Section 1 — Concepts & Interview Questions

**10 questions | 20 marks**

Difficulty increases gradually.

### Q1 — Basic comprehension

Explain in your own words what a **list comprehension** is.

Also explain the difference between:

```python
[x * 2 for x in numbers]
```

and:

```python
[x for x in numbers if x % 2 == 0]
```

---

# Ans: List comprehension is a way of creating list from iterable optionaly with transformation or filetring in compact way.

the first block of code creating list by transforming each element in numbers (iterable). This is transformation

the scond block of code also creating list and filtering only true value by looping over the numbers.This is filtration.

### Q2 — Filtering vs conditional expression

What is the difference between these two?

```python
result = [x for x in numbers if x > 5]
```

```python
result = [x if x > 5 else 0 for x in numbers]
```

Use a small example to show the difference in their outputs.

---
# Ans:These two code blocks represents the conditional filtering and conditional comprehention in List comprehentions.

Where conditional filtering filter out the falsy values and keeps only truthy values whereas the conditional comprehention transforms each item in iterable using conditionals if/else.

numbers = [1,2,3,4,5,6,7,8,9]

the first block of code produces list of elements which are greter than 5 in a iterable.ex: [6,7,8,9]

the second block of code produces the list with elemenets which are less <= 5 become zero and greter than 5 becomes same elements. ex: [0,0,0,0,0,6,7,8,9]


### Q3 — Dictionary comprehension

Consider:

```python
employees = {
    "Mahesh": 60000,
    "Rahul": 45000,
    "Amit": 80000,
    "Priya": 55000
}
```

Explain what this does:

```python
result = {
    name: salary
    for name, salary in employees.items()
    if salary >= 55000
}
```

Specifically explain:

1. Why `.items()` is used.
2. What becomes the key.
3. What becomes the value.
4. What the `if` does.

---
# Ans: in brief the above comprehention code returns the dict with name and salary as key value pair for those whose salary is >=55000 from the employees dist.

1..items() returns the key value in dict as tuple and this is used to access all the objects in dict as key and value.
2.in result dict the name becomes the key.
3.salary becomes the value
4.if filters the items from employees dict and retunr only items which are >= 55000

### Q4 — Set comprehension

Why would you use a **set comprehension** instead of a list comprehension?

For example:

```python
result = {len(word) for word in words}
```

What important property of sets affects the result?

---
# Ans: set comprehentions are used when we need to transform the iterable along with o/p shoud be unique we use set. instead of list because list can contain the dupllicate values but set keep only unique elements.

In above code block the set will transform the words iterable as counts the len if each item and store only unique len values are strored in set result.

The set has importan property which is keeping only unique elements in collection.


### Q5 — Nested comprehension

Explain how Python evaluates this:

```python
result = [
    value
    for row in matrix
    for value in row
]
```

Given:

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

What is the output?

More importantly, explain **which `for` happens first conceptually**.

---

# Ans: The python evaluates the code as follows here the first loop for row in matrix is outer loop where it iterates all the lists in a matrix whereas the second loop iterates each item in list. so basically the above code flattens the 2-d matrix into single matrix.

the o/p of the above code is 

result = [1,2,3,4]

The first for loop happens first conceptually. Here firts the first for loop start executing and then the second loop takes place for rach netsed list in matrix once iterated all items of one nested list then it goes tow outer loop. likewise.

### Q6 — Comprehension + previous topics

You have:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Explain the difference between:

```python
[x ** 2 for x in numbers if x % 2 == 0]
```

and:

```python
[x ** 2 if x % 2 == 0 else x for x in numbers]
```

This question is testing whether you can distinguish **filtering** from **conditional transformation**.

---
# Ans: The frst list comprehentions code demonstarates the conditional filterting where it squres the elements in numbers while are even means divisible by 2 remove all odd numbers.

The socond comprehnetion demonstare the conistional transformation where it transaforms each element in numbers and squares only the even numbers.


### Q7 — Engineering judgment

Would you always replace a normal `for` loop with a comprehension?

Explain **when a normal loop is better** than a comprehension.

Give one example where using a comprehension would make the code less readable.

---
# Ans: Ill not replace a normal for loop with comprehension "I'll use a comprehension only to transform or filter an iterable when it is simple and readable." 

A normal loop is better when the code involved nested loops and comlex logic. 

matrix = [[1, 2], [3, 4]]


suppose i want to flatten the above 2-d matrix with 1d.along with keeping only even numbers and number which are > 0 for this use case 

result = [value for raw in matrix for value in raw if value % 2 == 0 and value > 0] this is difucult to read and debug insted we can use the normal for loop here.

result = []

for raw in matrix:

    for value in raw:

        if value % 2 == 0 and value > 0:

            result.append(value)

Now this code is more readable and easy for debugging than comprehention.


### Q8 — Dictionary duplicate keys

Consider:

```python
names = ["A", "B", "A"]
scores = [80, 90, 95]

result = {
    name: score
    for name, score in zip(names, scores)
}
```

What happens to the first `"A": 80`?

Why?

What will the final dictionary contain?

---
# Ans: Here in above comprehention takes two lists and maps names list items as key and scores list items as values creating dict with name:scores.

but the list contains duplicate name A. So when the comprehnetion iteates over the second A then in dict the value of a is ovireiide with new value 95 becuase dict allows only unique keys.

the final dict contains

result = {"A":95,"B":90}



### Q9 — Backend-oriented question

Suppose an API returns:

```python
users = [
    {"id": 101, "name": "Mahesh", "active": True},
    {"id": 102, "name": "Rahul", "active": False},
    {"id": 103, "name": "Amit", "active": True},
]
```

You need a lookup structure:

```text
user_id → username
```

but **only for active users**.

Explain how you would design the comprehension.

Then explain why a dictionary is more appropriate here than a list.

---
# Ans:

To make a lookup structure which contains the active users where ID as key and Username as value.

we can use the dict comprehension as follows

result ={ 
    user["id"]:user["name"] 
    for user in users
    if user["active"]
}

Here to store the related data as key value pair the dictionary is more appropriate because list donest stire related values.

### Q10 — Interview-level reasoning

An interviewer gives you:

```python
numbers = [1, 2, 3, 4]

result = [
    x * 2
    for x in numbers
    if x % 2 == 0
]
```

They ask:

> "Can you write the equivalent normal `for` loop and explain exactly how the comprehension maps to it?"

Do that.

Then answer:

> "What happens if `numbers` is an empty list?"

---

# Ans:


result = []

for x in numbers:

    if x % 2 == 0:

        result.append(x*2)

Here this is equevalent normal for loops for above given comprehention code where both are iterating over numbers and filtering the items which are even and and then transforming these element while skipping the falsy elements means odd elements.

When the numbers is a empty list the normal for loop skips the code block and doent raise an error similarly comprehention also skips the numbers and returns empty list withoud raising the error.



