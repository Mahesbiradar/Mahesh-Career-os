"""
---

## Section 2: Coding Assignments

Solve these three and share your code. I'll review each for correctness, edge cases, and style.

---

### 🟢 Easy: List Rotator

Write a function `rotate_list(items, k)` that rotates a list to the **right** by `k` positions.

**Requirements:**
- `k` can be larger than the list length.
- If `items` is empty, return an empty list.
- Do **not** modify the original list in-place; return a new list.
- Use list slicing.

**Examples:**
```python
rotate_list([1, 2, 3, 4, 5], 2)   # [4, 5, 1, 2, 3]
rotate_list([1, 2, 3, 4, 5], 7)   # [4, 5, 1, 2, 3]  (7 % 5 = 2)
rotate_list([], 3)                # []
```

---
"""
def rotate_list(nums,k):

    if not nums:
        return nums

    num = k % len(nums)

    left = 0
    right = len(nums)-1

    while left < right:

        nums[left],nums[right] = nums[right],nums[left]

        left += 1
        right -= 1

    left = num
    right = len(nums)-1

    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        
        left += 1
        right -= 1

    return nums

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 7))
print(rotate_list([], 3))




"""
### 🟡 Medium: Tuple Frequency Counter

Write a function `most_common_pair(pairs)` that takes a list of 2-element tuples and returns the tuple that appears most frequently.

**Requirements:**
- If there is a tie, return **any one** of the most frequent tuples.
- If the list is empty, return `None`.
- Use a dictionary to count frequencies (not `collections.Counter`).
- Do **not** modify the input list.

**Examples:**
```python
most_common_pair([(1, 2), (3, 4), (1, 2), (5, 6), (1, 2)])  # (1, 2)
most_common_pair([(1, 1), (2, 2), (1, 1), (2, 2)])          # (1, 1) or (2, 2)
most_common_pair([])                                         # None
```

---

"""

def most_common_pair(pairs):

    if not pairs:
        return None

    freq_counter = {}

    for i in pairs:
        freq_counter[i] = freq_counter.get(i,0)+1

    most_common = None
    freq = 0

    for key,value in freq_counter.items():

        if value > freq:
            most_common = key
            freq = value
    return most_common

print(most_common_pair([(1, 2), (3, 4), (1, 2), (5, 6), (1, 2)]))

print(most_common_pair([(1, 1), (2, 2), (1, 1), (2, 2)]))

print(most_common_pair([]))



"""
### 🔴 Hard: Matrix Transpose with Validation

Write a function `transpose(matrix)` that takes a list of lists (2D matrix) and returns its transpose.

**Requirements:**
- Validate that all rows have the **same length**. If not, raise a `ValueError` with the message `"All rows must have the same length"`.
- If the matrix is empty (`[]`), return `[]`.
- Use **nested list comprehensions** (no explicit `for` loops with `.append()`).
- The original matrix must not be modified.

**Examples:**
```python
transpose([[1, 2, 3], [4, 5, 6]])
# [[1, 4], [2, 5], [3, 6]]

transpose([[1, 2], [3, 4], [5, 6]])
# [[1, 3, 5], [2, 4, 6]]

transpose([])  # []
```
"""

def transpose(matrix):

    if not matrix:
        return []


    row_length = len(matrix[0])

    for i in matrix:

        if len(i) != row_length:
            raise ValueError("All rows must have the same length")


    return [[matrix[r][c] for r in range(len(matrix))] for c in range(row_length)]

print(transpose([[1, 2, 3], [4, 5, 6]]))

print(transpose([[1, 2], [3, 4], [5, 6]]))

print(transpose([]))



