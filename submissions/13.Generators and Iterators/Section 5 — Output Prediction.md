
# Section 5 — Output Prediction

**15 marks — 5 × 3 marks**

**Rules:** Don't execute the code. Predict the output and explain briefly why.

---

### Q1 — Basic Iterator

```python
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))
print(next(it))

for x in it:
    print(x)
```

**What is the exact output?**

---

# Ans: O/P
 
10
20
30

### Q2 — Generator Pause/Resume

```python
def demo():
    print("Start")
    yield 10
    print("Middle")
    yield 20
    print("End")
    yield 30

g = demo()

print("A")
print(next(g))
print("B")
print(next(g))
print("C")
```

What is the exact output, in order?

---
# Ans: O/P

A
Start
10
B
Middle
20
C

### Q3 — Generator Expression Consumption

```python
g = (x * 2 for x in range(4))

print(next(g))
print(list(g))
```

What is the output?

Explain why the list doesn't contain all four values.

---

# Ans:  O/P

0
[1,4,6]

During the first print(next(g)) the genarator expression processed the 0 and therefor in the next line while stoing all the yeilded value in list not contains the zero in lazy evaluation the processed items were discareded.

### Q4 — Generator + Function

```python
def numbers():
    for i in range(1, 4):
        yield i

g = numbers()

for x in g:
    print(x * 10)

print(list(g))
```

What is the output?

Why does the final `list(g)` behave that way?

---

# Ans: O/P

10
20
30
[]

Because in the g has exusted when the for loop executes and no more iteme left therefor empty list is printed.

### Q5 — Custom Iterator State

```python
class Counter:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 3:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


c = Counter()

print(next(c))
print(next(c))

for x in c:
    print(x)

print(list(c))
```

What is the exact output?

Pay particular attention to the **state of `c`** when the `for` loop begins.

---
# Ans: O/P

1
2
3
[]


When the for loop begins the current variable with state 3 and the condition for stop iteration not exucutes and next() method increments current state to 4 and return value 3 in the next iteration for loop exist because of the next() raise the stop itaration and safely exists the loop without crashing the the program.


