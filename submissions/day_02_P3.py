"""
Section 4: Debugging Questions
Each snippet below has a bug. Tell me:
What the bug is.
What the output currently is (or what error occurs).
How to fix it.
🐞 D1
Python
for i in range(5):
    print(i)
    i += 2
🐞 D2
Python
numbers = [3, 1, 4, 1, 5]
for num in numbers:
    if num == 1:
        numbers.remove(num)
print(numbers)
🐞 D3
Python
x = 10
while x > 0:
    print(x)
    if x == 5:
        break
🐞 D4
Python
for i in range(3):
    for j in range(3):
        if i == j:
            break
    print(f"Done with i={i}")
🐞 D5
Python
data = [10, 20, 30, 40]
for i in range(len(data)):
    if data[i] > 25:
        data.pop(i)
print(data)
Answer all 5, and we'll move to output prediction.

"""

# 🐞 D1

for i in range(5):
    print(i)
    i += 2

#The third line is not required if we wann print number from 1 to 4  and current program print number from 1 to 4 and exits the loop when i becomes 5


# 🐞 D2
# Python
numbers = [3, 1, 4, 1, 5]
for num in numbers:
    if num == 1:
        numbers.remove(num)
print(numbers)

#as of now in the above given program there is no bug it removes the number of 1 in the list and prints the remaining element after removing all 1's so the output is [3, 4, 5]

# 🐞 D3
# Python
# x = 10
# while x > 0:
#     print(x)
#     if x == 5:
#         break

# the loop condition will be alway true hence this loop enters into infinite loop to prevent this we can decrement the x value with each iteration to meet the contion x==5 to break the loop.


# 🐞 D4
# Python
for i in range(3):
    for j in range(3):
        if i == j:
            break
    print(f"Done with i={i}")

#Here in this program the both inner and outer loops will run with equal numbers means intially at outer i=0 then inner loop alos j=0 and due to contion i==j the inner loop exits again out loop starts next iterration and same thing happen again and again.with each outer loop iteration the print statement executes.

# 🐞 D5
# Python
# data = [10, 20, 30, 40]
# for i in range(len(data)):
#     if data[i] > 25:
#         data.pop(i)
# print(data)

#in this program the loop stats executing and whenever the element value is greter than 25 exist that element is poped from the list and only element remaings in the list which are less than equal to 25. o/p: [10,20] but Here the index out of range error occures. I dont know the concept plsm explaon

#Most of the problems dont contain the bug so i dont know why they have given as finding the bug here.



"""

---

## Section 5: Output Prediction Questions

**Predict the exact output** of each snippet. No running code — just reason it out.

---

### 📤 P1
```python
for i in range(3):
    if i == 1:
        continue
    print(i, end=" ")
print("Done")
```

### 📤 P2
```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count, end=",")
```

### 📤 P3
```python
for i in range(2):
    for j in range(2):
        print(f"{i}{j}", end=" ")
    else:
        print("inner-done", end=" ")
else:
    print("outer-done")
```

### 📤 P4
```python
nums = [5, 10, 15]
for i, n in enumerate(nums, start=2):
    print(i, n)
```

### 📤 P5
```python
a = [1, 2]
b = ['x', 'y', 'z']
for pair in zip(a, b):
    print(pair)
```

---

**Reply with your predicted outputs, and we'll move to the interview questions.**

"""

### 📤 P1
# ```python
for i in range(3):
    if i == 1:
        continue
    print(i, end=" ")
print("Done")

"""
the first iteration i will be 0 and its Printed and then 1 will be skipped due to condition and then continue statement and  2 will be printed and then loop stops and "Done" will be printed at the end.
0 2 Done Intially i thought it will printed in column type but i wans not known of end=" " then i got it correctly.
"""

### 📤 P2
# ```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count, end=",")

"""
1, 2, 4   this will be the answer 3 will not printed due the continue statement

"""

# ### 📤 P3
# ```python
for i in range(2):
    for j in range(2):
        print(f"{i}{j}", end=" ")
    else:
        print("inner-done", end=" ")
else:
    print("outer-done")

"""
00 01 inner-done 10 11 outer-done

"""

# ### 📤 P4
# ```python
nums = [5, 10, 15]
for i, n in enumerate(nums, start=2):
    print(i, n)

"""
2 5
3 10
4 15
"""
# ### 📤 P5
# ```python
a = [1, 2]
b = ['x', 'y', 'z']
for pair in zip(a, b):
    print(pair)

"""
(1, 'x')
(2, 'y')

"""

"""
  Here is the review of your output predictions:

---

### 📤 P1
```python
for i in range(3):
    if i == 1:
        continue
    print(i, end=" ")
print("Done")
```

**Your prediction:** `0 2 Done`  
**Actual output:** `0 2 Done`  
**Verdict:** ✅ Correct

---

### 📤 P2
```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count, end=",")
```

**Your prediction:** `1, 2, 4`  
**Actual output:** `1,2,4,5,`

**Mistake:** You stopped at `4`. The loop condition is `count < 5`. Let's trace:
- `count=4` → becomes `5`, `5 < 5` is `False`, but the check happens at the **top** of the loop. The iteration where `count` becomes `5` still executes fully before the condition is re-checked. So `5` gets printed too.

---

### 📤 P3
```python
for i in range(2):
    for j in range(2):
        print(f"{i}{j}", end=" ")
    else:
        print("inner-done", end=" ")
else:
    print("outer-done")
```

**Your prediction:** `00 01 inner-done 10 11 outer-done`  
**Actual output:** `00 01 inner-done 10 11 inner-done outer-done`

**Mistake:** The `else` attached to the **inner** `for` loop runs **every time** the inner loop completes naturally. Since the outer loop runs twice (`i=0` and `i=1`), the inner `else` prints `"inner-done"` twice. Only the outer `else` runs once at the very end.

---

### 📤 P4
```python
nums = [5, 10, 15]
for i, n in enumerate(nums, start=2):
    print(i, n)
```

**Your prediction:**
```
2 5
3 10
4 15
```
**Verdict:** ✅ Correct

---

### 📤 P5
```python
a = [1, 2]
b = ['x', 'y', 'z']
for pair in zip(a, b):
    print(pair)
```

**Your prediction:**
```
(1, 'x')
(2, 'y')
```
**Verdict:** ✅ Correct

---



## Section 6: Interview-Style Questions

These are the kind of questions you'd hear in a junior Python developer interview. Answer in your own words — conceptual clarity matters more than perfect syntax.

---

### 🎤 I1
What is the difference between `is` and `==` in Python? Give a practical example where `a == b` is `True` but `a is b` is `False`.
ans : in python is used to check the identity of the object which means memory location of the object and == operator is used to check the value equality of two objects
examples: suppose we have Two list a = [1,2,3,4] and b = [1,2,3,4]  Here the value of both objects are same but both are diffrent objects and stored at diffrent location in the memery.
Now if we check a == b this gives True bcz == operator checks the value equality and if we check a is b then it becomes False becaise is operator check the identity of both obeject and both objects were stored at diffrent locations hence is will return False

---

### 🎤 I2
Explain what happens under the hood when you write `for x in some_object:`. What does Python require `some_object` to implement for this to work?
ans: the some object can we any data structure or any range of values where the loop can iterate over. still the question not fully undertsood.

---

### 🎤 I3
You have a large list and need to filter out even numbers. Compare these two approaches:
```python
# Approach A
result = []
for n in numbers:
    if n % 2 != 0:
        result.append(n)

# Approach B
result = [n for n in numbers if n % 2 != 0]
```
Which is preferred and why? Are there any scenarios where Approach A might be necessary?

ans:If we have specific cases like above problem ill prefere approch b bcz its compact but both approches are good but if we want evaluate multiple contions then approch a might be necessary bcz we can evaluate multiple contionals and all but if go with approch b then its will be complex and not readable.

---

### 🎤 I4
What are the scoping rules for variables inside a `for` loop in Python? If you declare `x = 5` before a loop, and inside the loop you do `for x in range(10):`, what is the value of `x` after the loop finishes?

ans: scoping rules for variables inside the for loop are these variable are local variable which means we cannot access these varialbes outside the loop. The value of x after the loop finished is x = 5 because x varibel declared outside the loop is global variable and the x used in for loop is local varible so there is no effect of local x varibel on global variable.
---

### 🎤 I5
Describe the difference between an **iterator** and an **iterable**. Why can you only iterate over a file object once unless you re-open it?

ans : Not sure.

---

**Answer all 5, and then I'll give you your final score, weak areas, revision suggestions, and readiness verdict.**

"""
