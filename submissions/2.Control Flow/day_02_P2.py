

## Section 2: Coding Assignments

# Solve these three and share your code. I'll review each one for correctness, edge cases, and style.



### 🟢 Easy: Number Categorizer

"""Write a function `categorize_numbers(numbers)` that takes a list of integers and returns a dictionary with three keys: `"positive"`, `"negative"`, and `"zero"`. Each key maps to a list of all numbers from the input that fall into that category.

**Requirements:**
- Use a `for` loop.
- Use `if / elif / else`.
- If the input list is empty, return empty lists for all three keys.

**Example:**
```python
categorize_numbers([3, -1, 0, 5, -2, 0])
# Returns: {"positive": [3, 5], "negative": [-1, -2], "zero": [0, 0]}

"""

def categorize_numbers(numbers):

    dictionary={"positive":[],"negative":[],"zero":[]}
    
    if not numbers:
        return dictionary
    else:

        for num in numbers:
            if num == 0:
                dictionary['zero'] += [num]
            elif num > 0:
                dictionary['positive'] += [num]
            else:
                dictionary['negative'] += [num]
        return dictionary

print(categorize_numbers([3, -1, 0, 5, -2, 0]))




"""
### 🟡 Medium: Prime Finder with `for-else`

Write a function `is_prime(n)` that returns `True` if `n` is prime, `False` otherwise.

**Requirements:**
- Numbers less than 2 are not prime.
- Use a `for` loop to check divisibility from `2` up to `int(n ** 0.5) + 1`.
- Use the **`for-else` pattern**: the `else` block runs only if the loop completes without finding a divisor.
- Use `break` immediately when a divisor is found.

Then write `primes_between(start, end)` that returns a list of all primes between `start` and `end` (inclusive), using `range()` and your `is_prime()` function.

**Example:**
```python
is_prime(17)            # True
is_prime(18)            # False
primes_between(10, 20)  # [11, 13, 17, 19]

"""

# Write a function `is_prime(n)` that returns `True` if `n` is prime, `False` otherwise.


def is_prime(n):

    if n < 2:
        return False

    for i in range(2,int(n**0.5)+1):

        if n % i == 0:
            break

    else:
        return True

    return False

# Then write `primes_between(start, end)` that returns a list of all primes between `start` and `end` (inclusive), using `range()` and your `is_prime()` function.


def primes_between(start, end):

    prime_nums =[]


    for i in range(start,end):

        if is_prime(i):
            prime_nums.append(i)

    return prime_nums

print(is_prime(17))           
print(is_prime(18))

print(primes_between(10, 20)) 


"""

### 🔴 Hard: Student Grade Processor

Write `process_student_records(names, scores, attendance)` that processes three parallel lists.

**Requirements:**
- Iterate using `enumerate(zip(names, scores, attendance))`.
- Use `continue` to skip students with attendance `< 75%`.
- Use `continue` to skip students with invalid scores (not 0–100). Print a warning: `Warning: Invalid score for {name} at index {index}`.
- Use `if/elif/else` to assign grades: **A** (90+), **B** (80–89), **C** (70–79), **D** (60–69), **F** (<60).
- Count how many students received each grade.
- Return: `{"grade_counts": {"A": x, ...}, "processed": [(index, name, grade), ...]}`

**Example:**
```python
names = ["Alice", "Bob", "Carol", "Dave", "Eve"]
scores = [92, 45, 88, 101, 76]
attendance = [80, 90, 70, 85, 78]

# Carol skipped (attendance 70%)
# Dave skipped (score 101 invalid) + warning printed
# Result:
# {
#   "grade_counts": {"A": 1, "F": 1, "C": 1},
#   "processed": [(0, "Alice", "A"), (1, "Bob", "F"), (4, "Eve", "C")]
# }
```
---

**Post your code for all three assignments, and I'll review them before we move to the mini project.**


"""

def process_student_records(names, scores, attendance):

    grade_counts = {"A":0,"B":0,"C":0,"D":0,"F":0}
    processed = []

    for index,(name,score,attend) in enumerate(zip(names,scores,attendance)):

        if attend < 75:
            continue

        if score < 0:
            print(f"Warning: Invalid score for {name} at index {index}")
            continue
        
        elif score > 100:
            print(f"Warning: Invalid score for {name} at index {index}")
            continue


        grade = None

        if score >= 90:
            grade = "A"
        elif score >= 80 and score <= 89:
            grade = "B"
        elif score >= 70 and score <= 79:
            grade = "C"
        elif score >= 60 and score <= 69:
            grade = "D"
        else:
            grade = "F"

        
        grade_counts[grade] += 1

        processed.append((index,name,grade))


    return {"grade_counts":grade_counts,"processed":processed}



        

        
        

        



