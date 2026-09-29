Absolutely. We’ll do **only Sections 1 and 2 now**. No answers or hints during the assessment unless you ask.

# 🧠 Generators & Iterators — Assessment

**Total: 40 marks**

* **Section 1 — Concepts & Interview Understanding:** 20 marks
* **Section 2 — Coding:** 20 marks

Answer from memory. Don't execute the code while answering.

---

# Section 1 — Concepts & Interview Understanding

**10 questions × 2 marks = 20 marks**

Answer briefly but explain your reasoning where needed.

### Q1. Iterable vs Iterator

What is the difference between an **iterable** and an **iterator**?

Give one example of each.

---

# Ans: iterable is an object on which we can loop over. ex: list,tuple,string,set etc. and and iterator will have a method called iter which returns the iterator object.

iterator is an object with a state(which knows the curret position in sequnece) and produces one value at time this is called the lazy evaluation and  has as function called next which determins the next value in sequence. 


### Q2. `iter()` and `next()`

Consider:

```python
numbers = [10, 20, 30]
it = iter(numbers)
```

What does:

```python
next(it)
```

do?

What happens when `next(it)` is called after all three values have been consumed?

---
# Ans: when we call the next(it) here next is the function taking and it(iterater as argumet) and the next method determines the next value and returns the value 10. when next(it) is called after all three values have been consumed it raise stopiteration exception means all the elements in itebales are consumed.


### Q3. `for` loop internally

Conceptually, how does this:

```python
for x in numbers:
    print(x)
```

relate to:

```python
it = iter(numbers)

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```

Why is `StopIteration` important?

---
# Ans: the for loop Conceptually impemented as per the below mentioned code in while loop when we run any for loop the python runs the conceptual while loop in backgrod and once the iterator exusted it raise the StopIteration exception and the python safely handles the exception witout crashingbthe program. therefor StopIteration` important in the context of for loop it handles the iterable safely once the iterator is exusated.



### Q4. `yield`

What is the main difference between:

```python
return value
```

and:

```python
yield value
```

inside a function?

---
# Ans:

# return keyword exits the functions execution permanently and return the executed value. kills all the local varibles.

# Yeild keyword pauses the functions execution temporary and return the value one resumes the function execution when the next is called on the iterator obj. stores the local variables in memory.

### Q5. Generator execution

Consider:

```python
def test():
    print("A")
    yield 10
    print("B")
    yield 20

g = test()
```

At the moment `g = test()` executes:

**Does `"A"` get printed? Why or why not?**

---
# Ans: moment `g = test()` executes the generator obj is created and it will not print or return anything yet. the functions start execution once the next() is called on the generator object. 


### Q6. Pause and resume

For the same generator:

```python
print(next(g))
print(next(g))
```

Explain what happens internally between the first and second `next()` calls.

---
# Ans: when the first print(next(g)) is executes the function prints A and when the function reaches yeild 10  the yeild stops execution of the function and returns 10 and it knows its current state. and when the second print(next(g)) is executed the fucntions prints b and then once it reaches yeild stops execution and return 20


### Q7. Lazy evaluation

What does **lazy evaluation** mean in the context of generators?

Why is it useful when processing a very large amount of data?

---
# Ans:
the generators produces values one at time when it needed or requested this behaviour is called the lazy evaluation in the context of generators.

the lazy evaluation is extremely useful when processing very large amount of data bcz the lazy evaluation behaviour store the only one value at time in memory when its called and which efficiently uses the memory insted of storing th whole amount in memory.

### Q8. List comprehension vs generator expression

Compare:

```python
squares = [x * x for x in range(1000000)]
```

and:

```python
squares = (x * x for x in range(1000000))
```

What is the important difference between them?

Also, which one produces the values lazily?

---

# Ans: in above code the list comprehention processes the 1 million values and stores the these 1 million integers into the memory. the genarator expression processes the epression and stores one value at time in memory when its called.

the main diff in both the list comprehnetion and the generator expression is memory efficiency the since the generator expression processes one value at time and stores only one value at time therefor they are more effient compare to list comrehention in terms of mempory usage.

the genarator exression produces the values lazily.


### Q9. One-time consumption

Consider:

```python
g = (x for x in range(3))

print(list(g))
print(list(g))
```

What will the two `print()` statements produce?

Why?

---
# Ans: the first print statement print the list of [0,1,2] and once the second print satement executes it produces empty list []
becuse the generator expression comsume all the processed elements whne the first list(g) is called there for iterator is exusted ans has nothing to iterate over.



### Q10. Custom iterator

A custom iterator normally implements:

```python
__iter__()
__next__()
```

What should `__iter__()` return for a typical iterator object?

And what should `__next__()` do when there are no more values?

---
# Ans:

the __iter__() returns the self menas it returns the current object itself. the __next__() raise the stopiteration exeption when there are no more values.





