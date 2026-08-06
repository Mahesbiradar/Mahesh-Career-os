
# Remaining Assessment (Compact Version)

## Section 4 — Debugging (3 Questions)

### Q1

Find the bug.

```python
text = "Python"

text[0] = "J"

print(text)
```
Answer:

1. What error occurs?
2. Why?
3. Fix it correctly.

---
# ans : Here python raises typeerror bcz strings are immutable therefor value assignement is not legal.
we can create one more object to do the same by adding two strings
text = "j" + text[1:] 

### Q2

```python
sentence = "Python is fun"

words = sentence.split()

print(words.join("-"))
```

Answer:

1. Why does this fail?
2. Correct the code.
3. Explain why your correction works.

---
## ans: Here in print statement we are using .join method but words is a list and list dont have any method like .join Therefor what we can do is we can pass the list to the method to work.

print(" ".join(words))

this works because the .join is the string method to join the list of words here we are passing the list to method not running the method on list.

### Q3

```python
sentence = "python python java python"

words = sentence.split()

frequency = {}

for word in words:

    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] = 1

print(frequency)
```

Answer:

1. What is the logical bug?
2. Correct only the incorrect line.
3. What is the final output?

---

## ans: Here in if statement not is unnessesarily and the inside if statement thereshoud be += 1 to increment the count. with exiting code will update the frequncy of each word only one time bcz even else statement also overitted the frequncy to 1
if word in frequency:
        frequency[word] += 1

{"python":3, "java":1}

# Section 5 — Output Prediction (3 Questions)

### Q1

```python
text = "  Python Programming  "

clean = text.strip()

print(clean[0])
print(clean[-1])
print(clean[7:])
```

Predict the output.

---
## ans:
P
g
Programming

### Q2

```python
sentence = "Python is easy"

words = sentence.split()

print(words)
print("-".join(words))
```

Predict the output.

---
## ans: 
['Python','is','easy']

Python-is-easy

### Q3

```python
text = "Backend"

print(text[:4])
print(text[4:])
print(text[::-1])
```

Predict the output.

---
## ans:
Back
end
dnekcab

# Section 6 — Interview Questions (3 Questions)

### Q1

What is the difference between:

* `split()`
* `join()`

When would you use each in backend development?

---


### Q2

Why are strings immutable in Python?

What advantages does immutability provide?

---

### Q3 (Scenario Based)

Suppose an API receives:

```text
Mahesh,Bangalore,Python,Django
```

Explain the complete flow to convert this into:

```python
{
    "name": "Mahesh",
    "city": "Bangalore",
    "language": "Python",
    "framework": "Django"
}
```

Mention how you would use:

* `split()`
* Lists
* Dictionaries

and why this approach is useful.

---

