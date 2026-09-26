
# Section 4 — Debugging

### **5 questions | 25 marks**

For each question, don't just give the corrected code.

Explain:

1. **What is wrong?**
2. **Why is it wrong?**
3. **What happens when the code runs?**
4. **How would you fix it?**

This is important because backend interviews often test whether you can **diagnose** code rather than simply write it.

---

## Q14 — Conditional expression placement

```python
numbers = [1, 2, 3, 4, 5]

result = [
    x
    for x in numbers
    if x % 2 == 0
    else 0
]

print(result)
```

What's wrong?

Fix it so that:

* even numbers remain unchanged
* odd numbers become `0`

Expected:

```text
[0, 2, 0, 4, 0]
```

---
# Ans:
Here in the above given code block the conditiona if else block placement is wrong bcz for conditional transformation the sytax shoud be

[expression_if_true if condition else expression_if_false for value in iterable]

above code will produce the syntax error.

we can fix this using above given synatax to produce the expected result.

result = [
    x if x % 2 == 0 else 0
    for x in numbers   
]


## Q15 — Dictionary comprehension bug

```python
employees = {
    "Mahesh": 60000,
    "Rahul": 45000,
    "Amit": 80000
}

result = {
    name
    for name, salary in employees.items()
    if salary >= 60000
}

print(result)
```

The developer wanted:

```python
{
    "Mahesh": 60000,
    "Amit": 80000
}
```

but doesn't get that.

Explain the problem and fix it.

---
# Ans: Not the problems with above code is as of now its sent comprehention to because the dict comprehention shoud keep the key:value in expression. but here only name is there so it becomes set comprehention and produces unique employee name who has salary >= 60000.

To fix this we can make changes in code as follows.


result = {
    name:salary
    for name, salary in employees.items()
    if salary >= 60000
}


## Q16 — Nested comprehension bug

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    [x ** 2 for x in matrix]
    for row in matrix
]

print(result)
```

The developer wants to square every value while preserving the matrix structure.

Expected:

```python
[
    [1, 4, 9],
    [16, 25, 36],
    [49, 64, 81]
]
```

Identify exactly what is wrong with the inner comprehension.

---

# Ans: In above code block in the inner comprehension we are trying to square the list itself rather than element inside the list. this will produce an typeerror.

beacuse in outer loop we have accessed the inner list as row so in inner list our iterable shoud be row not the matrix itself.

to fix the above code we shoud change the iterable name to row instead of matrix.


result = [
    [x ** 2 for x in row]
    for row in matrix
]

## Q17 — Backend data bug

```python
users = [
    {"id": 101, "name": "Mahesh", "active": True},
    {"id": 102, "name": "Rahul", "active": False},
    {"id": 103, "name": "Amit", "active": True},
]

active_users = {
    user["name"]: user["id"]
    for user in users
    if user["active"]
}

print(active_users)
```

The requirement is:

```text
user_id → username
```

not:

```text
username → user_id
```

Explain whether the comprehension is syntactically correct.

If it is syntactically correct, why is it still a bug?

Fix it.

---

If we go with sytax and other things the code is correct and produces the result but it will not produce te o/p as per the requiredmnt.

because as per above code the dict elements are mapped as the key is name and value is user_id but the requirement is user_id -> username

so to fix this bug we shoud interchange the  user["name"]: user["id"]  to user["id"]: user["name"]

active_users = {
    user["id"]: user["name"]
    for user in users
    if user["active"]
}


## Q18 — Comprehension vs mutation

```python
numbers = [1, 2, 3, 4, 5]

result = [
    numbers.append(x * 10)
    for x in numbers
]

print(numbers)
print(result)
```

This is intentionally tricky.

Explain:

1. What is the developer probably trying to do?
2. Why is using a comprehension here a bad idea?
3. What happens to `numbers`?
4. What happens to `result`?
5. How would you write this more safely?

**Do not just say "don't do this." Explain the underlying problem.**

---

# Ans:
1.The devoloper trying to multiply the each element in the numbers by 10 and add those values back into the numbers list using a concise syntax.

2.Comprehensions  are strictly designed for pure expressions that resturn new data withodu side effects.using comprehentions here is bad idea for two major resons. a.Infinite Loop:here we are mutating the exact same list that we are currently iterating over the this will goes into infinite loop until the system runs out of memory. B.list comprehentions save the expression evaluates to. Beacuse .append() mutates a list inplace and returns None. The comprehention wastefully builds a list of empty values.

3.The numbers will grow infiniteky untill python crashes with a memory error.

4.the result list is never fully printed because the program crashes first.and the result list contains the endless stream of None values.

5.To write this safely .


result = [
    x * 10
    for x in numbers
]

or is the devoloper wants to append the tranformed data back to originla list.

numbers.extend(result)

# Note: In this answer i got what the underlying happeing infinity loop and endless steamd of none in result but for proper answer i use AI only for this answer only.




