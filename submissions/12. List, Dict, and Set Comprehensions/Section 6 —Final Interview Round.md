# Section 6 — Final Interview Round

### 5 questions | 10 marks

Answer these **as if you're speaking to an interviewer**. Keep each answer concise.

### Q24

**When would you choose a list comprehension over a normal `for` loop?**

# Ans:  I woud choose a list comprehention over normal `for` loop when performing a simple transformations or filtering over iterable.it allows me to write cleaner,consize and readble code.


### Q25

**What's the difference between filtering and conditional transformation in a comprehension?**

# Ans: filtering in comprehension is to filter out the elemenents in a iterable based on the written condition. whereas the conditional transformation is used to transform each item in iterable based on the condition.

ex: [1,2,3,4,5,6] if i want to make new collection of only even number ill use comprehension filtering where it remove the odd number. ill use conditional transformation when i want to square a even number and keep the odd number as it is.

### Q26

**Can a dictionary comprehension have duplicate keys? What happens?**

# Ans:No, a dictionary comprehension cannot contain duplicate keys because Python dictionary keys must be unique. If a comprehension evaluates to a key that already exists, no error is thrown; instead, the new value simply overwrites the old value

### Q27

**Explain this nested comprehension in simple words:**

```python
result = {
    skill
    for employee in employees
    for skill in employee["skills"]
}
```

# Ans: This is set comprehension that extracts a flat, unique collection of all employee skills across the entire company.
 it operates like a nested loop: it first iterates through each employee in the employees list, then drills down into the nested employee["skills"] list for that person. Because it uses set syntax, any duplicate skills across different employees are automatically filtered out, leaving only a unique set of individual skills."

### Q28

An interviewer says:

> "Your code works, but your comprehension is 3 lines long and difficult to understand. Would you still use it?"

How would you respond?

---

"If a comprehension becomes difficult to understand or requires three or more lines of complex logic, I would refactor it into a standard for loop. 
While comprehensions are great for simple operations, a clean, multi-line for loop with descriptive variable names is much easier for read, debug, and maintain.