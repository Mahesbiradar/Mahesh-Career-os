# Section 6 — Final Interview Round

**15 marks — 5 × 3 marks**

Answer these as if you're sitting in a Python/backend interview. Keep each answer reasonably concise but technically accurate.

### Q1 — Core Understanding

An interviewer asks:

> **"What is the difference between an iterable, an iterator, and a generator?"**

Explain it in your own words and give a simple example.

---
# Ans: 

iterable: are collecetion on which we can iterate or loop over ex: list,tuple,string,range etc.
iterator: is an object with a state(knows it current position during the traversal of a collection). and featches the next item every time we call next(obj).
generator: generators are the convinent way to create iterators.it uses yeild keyword to return values one by one, pausing its state automatically to save memory.

Examples;

# 1. Iterable: A standard list. We can loop over it multiple times.

my_iterable  = [1,2,3,4,5,6,7,8,9]

# 2. Iterator: created from the iterable. It holds the state of where we are

my_iterator = iter(my_iterable)

print(next(my_iterator)) # 1
print(next(my_iterator)) # 2

generator: A function that acts as an iterator factory.

def my_generator():

    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 1


### Q2 — Backend Application

> **"You have to process 20 million database records. Why might you choose a generator instead of loading all records into a Python list?"**

Give a practical backend explanation.

---

# Ans: to process 20 million database records i would choose a generator because generators processes/produces value as lazy evaluation means processes records one by one when its needed or requested which saves memoey space effectively. wheras processing 20 million records and storing in list will store all 20 million reconds upfrond in the memory.Using the generators as soon as the record perocessed and the loop moves to next iteration,the old records referance count drops to zero . the python garbage collector can reclaim that memory immediately.



### Q3 — `yield`

> **"What exactly happens when Python encounters `yield` inside a generator?"**

Explain what happens to the function's execution state and what happens when `next()` is called again.

---
# Ans:

When python encounters yield inside a genarator it puses the generator function temeporary and returns the value and once the next() is called again the generator function resumes its execution and the next method given the next value in collection and once it encounters yield puses the function ans retunrs value. This bahaviour is called lazy evaluation.

### Q4 — Custom Iterator

An interviewer asks:

> **"Why would you ever create a custom iterator when Python generators are much easier to write?"**

Give at least **two situations/reasons** where a custom iterator can make sense.

---
# Ans: custome iterators are preferred over the generator in senarios when state preservation,encapsulation of bunisses logic, or reusibility as a class with custom methods.


### Q5 — Engineering Judgment

You are reviewing this code:

```python
def get_active_users(users):
    return [user for user in users if user["active"]]
```

A developer says:

> "Let's change every list comprehension into a generator because generators use less memory."

Would you agree with that approach?

Explain your answer and when you would choose a list versus a generator.

---

# Ans: About the approach I completely disagree just beacuse the generators use less memory.

I would choose a list versus a generator depends on dataset size and how the application needs to consume the data.

i would choose list comrehention if datasets are small to medium.when multiple passes are needed or when ordering or indexing matters.

i would choose genarators if datasets are large or unbounded or if we need to implement pipeline processing.



