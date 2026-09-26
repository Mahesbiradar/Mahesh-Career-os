# Section 5 — Output Prediction

### 5 questions | 15 marks

**Don't run the code. Predict the exact output.**

### Q19

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers if x % 2]

print(result)
```

What is the output, and why?

---

# Ans: O/P [2,6,10]

beacuse The conition x % 2 in python 0 evaluates to False and 1 or any other number Evaluated to True.

Therefor when the remainder is zero the comprehention filtering out those elements like 2 and 4 because 2 % 2 become 0.


### Q20

```python
data = ["python", "django", "python", "redis"]

result = {word: len(word) for word in data}

print(result)
```

What is the output?

What happens because `"python"` appears twice?

---
# Ans:
{"python":6, "django":6, "redis":6}

When python appears twice it overidded the prev value since dict will strore only uinuqe key when same key appears it just overidded old value with new doent store same key as twice.

### Q21

```python
matrix = [[1, 2], [3, 4]]

result = [
    [x * 10 for x in row if x % 2 == 0]
    for row in matrix
]

print(result)
```

Exact output?

---
# Ans: 

result = [[20],[40]]


### Q22

```python
numbers = [1, 2, 3]

result = [
    x if x > 1 else 0
    for x in numbers
]

print(result)
```

Exact output?

---

# Ans:

result = [0, 2, 3]


### Q23

```python
employees = {
    "A": 50000,
    "B": 70000,
    "C": 80000
}

result = {
    name: salary * 2
    for name, salary in employees.items()
    if salary >= 70000
}

print(result)
```

Exact output?

---
# Ans: 

result = {
    "B": 140000,
    "C": 160000
}

