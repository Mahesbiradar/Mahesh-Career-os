"""
## Section 4: Debugging Questions

Each snippet below has a bug. **Tell me:**
1. What the bug is.
2. What the output currently is (or what error occurs).
3. How to fix it.

---

### 🐞 D1
```python
t = (1, 2, 3)
t[0] = 10
print(t)
```
ans: This give the type error Due to tuples are immuatable. To fix this either we can make the tuple as list then update or we can make a new tuple t = (10, )+t[:1]

### 🐞 D2
```python
data = [[1, 2], [3, 4]]
copy_data = data.copy()
copy_data[0][0] = 99
print(data[0][0])
```
ans: updating the copy_data doesnot affect the main list 'data' if we wanna update the main list then we can make the copy_data = data

### 🐞 D3
```python
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums if x % 2 = 0]
print(squared)
```
ans: here in the list compression x % 2 = 0 throws syntax error to fix this we can use equality operator == squared = [x**2 for x in nums if x % 2 == 0]

### 🐞 D4
```python
a = [1, 2, 3]
b = a
a = a + [4]
print(b)
```
ans: Here list a is overwritten which contains old list a and one more element this doesnot affects the list b to correct this we can use a += [4] this mutates the original list a and b alos referncing the same list.

### 🐞 D5
```python
matrix = [[1, 2], [3, 4], [5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transposed)
```
ans : Not sure i have not come across the 2d list and matrix concepts here. 
---

**Answer all 5, and we'll move to output prediction.**

"""

"""
   Here is the review of your debugging answers:

---

### 🐞 D1
**Your answer:** Correctly identified the `TypeError` due to tuple immutability.

**One correction on your fix:** You wrote `t = (10,) + t[:1]`. `t[:1]` gives `(1,)`, so the result would be `(10, 1)` — you lost `2` and `3`. The correct fix is:
```python
t = (10,) + t[1:]   # t[1:] gives (2, 3)
```

---

### 🐞 D2 — **Critical Misconception**
**Your answer:** You said updating `copy_data` does **not** affect `data`.

**This is wrong — the opposite is true.** `.copy()` creates a **shallow copy**. The outer list is new, but the **inner lists are shared references**.

```python
data = [[1, 2], [3, 4]]
copy_data = data.copy()      # New outer list, same inner lists
copy_data[0][0] = 99
print(data[0][0])            # Output: 99  ← Affected!
```

**Why:** `data[0]` and `copy_data[0]` point to the **same inner list object** in memory.

**Fix:** Use `copy.deepcopy(data)` or build fresh nested lists:
```python
import copy
copy_data = copy.deepcopy(data)
```

---

### 🐞 D3
**Your answer:** ✅ Correct. `=` is assignment, `==` is comparison.

---

### 🐞 D4
**Your answer:** ✅ Correct. `a = a + [4]` creates a new list object; `a += [4]` mutates in-place.

---

### 🐞 D5
**Your answer:** You said you haven't seen 2D lists, but you literally wrote a transpose function in the hard assignment! Let me explain:

**The bug:** `len(matrix)` is `3` (number of rows), but each row has only `2` columns. So `i` goes `0, 1, 2`, and when `i = 2`, `row[2]` raises an `IndexError` because valid column indices are only `0` and `1`.

**Fix:** Use `len(matrix[0])` (number of columns) instead of `len(matrix)`:
```python
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
```

---

### Section 4 Score: **11/20**

| Q | Score | Reason |
|---|-------|--------|
| D1 | 3/4 | Right concept, fix had off-by-one slice error |
| D2 | 0/4 | Opposite of correct answer — shallow copy misunderstanding |
| D3 | 4/4 | ✅ |
| D4 | 4/4 | ✅ |
| D5 | 0/4 | No answer / didn't recognize the index mismatch |

---

## Section 5: Output Prediction Questions

**Predict the exact output** of each snippet. No running code — just reason it out.

---

### 📤 P1
```python
a = [1, 2, 3]
b = a[:]
a.append(4)
print(b)
print(a)
```
ans: for b  1, 2, 3 and for a 1, 2, 3, 4 

### 📤 P2
```python
x = ([1, 2], [3, 4])
x[0].append(5)
print(x)
```
ans:([1,2,3], [3,4])

### 📤 P3
```python
nums = [10, 20, 30, 40, 50]
print(nums[::-2])

ans: [50, 30, 10]
```

### 📤 P4
```python
data = [(1, 'a'), (2, 'b'), (1, 'a'), (3, 'c'), (2, 'b')]
print(len(set(data)))

ans: 3 set removes the duplicates
```

### 📤 P5
```python
matrix = [[1, 2, 3], [4, 5, 6]]
flat = []
for row in matrix:
    flat.extend(row)
print(flat)
```
ans: [1,2,3,4,5,6]

---

**Reply with your predicted outputs, and we'll move to the interview questions.**

"""

a = [1, 2, 3]
b = a[:]
a.append(4)
print(b)
print(a)

x = ([1, 2], [3, 4])
x[0].append(5)
print(x)

nums = [10, 20, 30, 40, 50]
data = [(1, 'a'), (2, 'b'), (1, 'a'), (3, 'c'), (2, 'b')]
print(len(set(data)))

matrix = [[1, 2, 3], [4, 5, 6]]
flat = []
for row in matrix:
    flat.extend(row)
print(flat)



"""

   Here is the review of your output predictions:

---

### 📤 P1
**Your prediction:** `b = [1, 2, 3]`, `a = [1, 2, 3, 4]`  
**Actual output:**
```
[1, 2, 3]
[1, 2, 3, 4]
```
**Verdict:** ✅ Correct

---

### 📤 P2
**Your prediction:** `([1, 2, 3], [3, 4])`  
**Actual output:** `([1, 2, 5], [3, 4])`

**Mistake:** You wrote `3` as the appended element, but the code appends `5`. The inner list becomes `[1, 2, 5]`, not `[1, 2, 3]`.

---

### 📤 P3
**Your prediction:** `[50, 30, 10]`  
**Verdict:** ✅ Correct

---

### 📤 P4
**Your prediction:** `3`  
**Verdict:** ✅ Correct

---

### 📤 P5
**Your prediction:** `[1, 2, 3, 4, 5, 6]`  
**Verdict:** ✅ Correct

---

**Section 5 Score: 16/20** (docked 4 for P2 — wrong value in the predicted tuple)

---

## Section 6: Interview-Style Questions

These are the kind of questions you'd hear in a junior Python developer interview. Answer in your own words — conceptual clarity matters.

---

### 🎤 I1
What is the difference between a **shallow copy** and a **deep copy**? Give a concrete example where `list.copy()` behaves differently from `copy.deepcopy()`.

ans: in shallow copy if the list has nested lists and we want to make changes in the shallow copy it affects the original list therefor the pupose of making copy of list to modify the shallow copy to avoid changes in original list this purpose doesnot resolves using shallow capy.
whereas using the deepcopy we can make the changes nested list which cannot affect the original list.
ex  
a=[1,2,3,[5,6]]
b = a.copy()
b[3][0]=10 # This mutets the orginalmlist also.

b = a.deepcopy()
b[3][0]=10   this chnages takes place only in deepcopy b this chnages not affect the original copy.
---

### 🎤 I2
Why are tuples generally faster than lists for iteration and lookup? What does Python do differently under the hood because tuples are immutable?
ans: in python tuples are immutable Therefor the they are hasable which means python creates the hashtable which optimizes the iteration and lookup compare to the list. Since tuples are hashable which means there are not mutable therfor pythin creates the hashtable which optimizes accesing the element in tuples. 

---

### 🎤 I3
You need to return multiple values from a function. You can return them as a `list` or as a `tuple`. Which is more appropriate and why?

ans: This dependent on the purpose if we need for the faster access or these cannot be changable then we can use tuples since these are immutable so we can access the elemenet faster whereas for list if manupulate the values then we can use the list.
---

### 🎤 I4
What is the difference between `my_list = my_list * 3` and `my_list *= 3`? Are they always equivalent? Demonstrate the difference using a nested list like `[[1, 2]]`.
Not sure pls Explain

---

### 🎤 I5
A tuple containing lists — like `([1, 2], [3, 4])` — can have its inner lists modified. Yet the tuple itself can still be added to a `set` or used as a dictionary key. How is this possible? What exactly does Python check to determine if an object is hashable?
ans: The inner lists can be modified. it canot be added to set and cannot be used as key in dict bcz list is mutable data type whereas the dict key shoud be unique and immutable therefor it not possible.python check the object identity to check to determine the hashablility.

---

**Answer all 5, and then I'll give you your final score, weak areas, revision suggestions, and readiness verdict.**


"""

