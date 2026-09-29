# Section 4 — Debugging

**15 marks**

For each problem:

1. Identify the mistake.
2. Explain why it is a problem.
3. Give the corrected code.

---

### Q1 — Generator not producing values

**3 marks**

```python
def numbers(n):
    for i in range(1, n + 1):
        return i

g = numbers(5)

for x in g:
    print(x)
```

The developer expects:

```text
1
2
3
4
5
```

but it doesn't happen.

**What is wrong? Fix it.**

---
# Ans: In above code the function start iteration from one and immedeatly returns 1 and exists the function due to return keyword and the g contains the value 1 and its integer and therefor runiing a loop over and integer will produces the typeerror bcz interger are not iterables.

here to if the devoloper need the lazy evaluation behaviour using the generator function he must replace the return keyword with yeild which return the value and puases the function temeporarily. and then start executes once next is called on object.

to fix the above code which produces range of number s 1 to n here is fixed code.


```python
def numbers(n):
    for i in range(1, n + 1):
        yield i

g = numbers(5)

for x in g:
    print(x)
```

### Q2 — Generator consumed

**3 marks**

```python
g = (x * 2 for x in range(5))

first = list(g)
second = list(g)

print(first)
print(second)
```

Output:

```text
[0, 2, 4, 6, 8]
[]
```

The developer expected both lists to contain the values.

**Why does this happen? How would you fix it if the values need to be iterated over twice?**

---
# Ans:

The first print(list(g)) statement stored all the elements yeiled by the generator expression during this process all the element of these expression were dicarded and the iteartor exusted therefor the Thesre no more elements were remained in the genarator expression and trying to make a list by passing the exusted generator will result in empty list only.

if the yeilded values of the genarator experession need to iterated then we have to copy the first list ans assigne the same to the second list.

first = list(g)
second = first.copy

this will gives the same copy of the first list to second.


### Q3 — Broken custom iterator

**3 marks**

```python
class CountUp:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            return None

        value = self.current
        self.current += 1
        return value
```

Used as:

```python
for x in CountUp(3):
    print(x)
```

The program doesn't terminate correctly.

**What is wrong with `__next__()`? Fix it.**

---
# Ans: in python iterator protocol, returning None does not stop the loop.

when a for loop interacts with iterator it expects the __next__() method to explicitly raise stop iteration  exception when it runs out of elements. becuase the above program return none instaed of raising the the exeption, the for loop treats none as valid yeilded value. it assign x = None, prints it and requests another value endlesly, traping the program in an infinite loop.

to fix this we must replace with the raise StopIteration.

 def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value
```

### Q4 — Generator expression vs list

**3 marks**

A developer writes:

```python
numbers = [x * 2 for x in range(100000000)]
```

because they want to process the numbers one by one.

**What is the problem with this approach?**

Rewrite it using a generator expression.

---

# Ans: The above given code is an list comprehention where it stores all the processed values in the memory as a list.

if we want to process the numbers one by one we shoud desing lazy evaluation behaviour by writing the above code in generator expression by replacing the square baracates by parenthesis.

Corrected Code:

numbers = (x * 2 for x in range(100000000))


### Q5 — Backend debugging

**3 marks**

Consider:

```python
def active_users(users):
    return [user["id"] for user in users if user["active"]]

users = get_users_from_database()

for user_id in active_users(users):
    process_user(user_id)
```

Suppose `get_users_from_database()` returns **10 million users**.

The developer says:

> "I'm processing them one by one, so this is memory efficient."

Is that statement correct?

If not, rewrite `active_users()` so that it actually processes the IDs lazily.

---

# Ans:

In above code the active_users looping over the users and then iterating over each user and then storing all these active user in list and afterpriocessing the 10 million users it retusn the list containg 10 million users records.

As the devoloper state he want the to process them one by one but the above code not does so. and this is not the correct statement. 

to fix this and process users one by one we shoud implement the generator function or genarator expression.


def active_users(users):
    return (user["id"] for user in users if user["active"])


