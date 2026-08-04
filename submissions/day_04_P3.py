"""
# Debugging Question 1 (Easy)

What is the bug?

```python
student = {
    "name": "Mahesh",
    "age": 22
}

print(student["city"])
```

Answer:

1. What error occurs?
ans:python will raise the keyerror.
2. Why?
ans:Since the dict dont have the key "city" Therefor the key error occures
3. Fix it.
ans: we can use dict.get["key"] to avaoid the crashing of entire Program .get will handle it safely if the key exist it perfomrs the intended operation or else it will simply move on to next.

---

# Debugging Question 2 (Easy)

```python
marks = {}

subjects = ["Math", "Science", "English"]

for subject in subjects:
    marks[subject] = marks[subject] + 1

print(marks)
```

Answer:

1. Why does it fail?
marks[subject] = marks[subject] + 1  here we are trying to update the marks of the subject by adding 1 to that but here dict is empty and it will raise keyerror.

2. Fix it without using `if`.

not sure

3. Fix it using `get()`.

here we can fix but still i have not undertsood the problems statement do we wanna update the marks by 1 or do we wann map the subject frequncy. if frequncy then

marks[subject] = marks.get(subject,0) + 1


---

# Debugging Question 3 (Medium)

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = {}

for num in numbers:
    unique.add(num)

print(unique)
```

Answer:

1. Why does this crash?
ans: if this is to check the unique values then we shoud use set not the dict and .add works on set not with dict.
2. Correct the code.
unique = set()

3. Why is your solution correct?
Since our task is to capture the unique elements from the list Therfor we can use set bcz set removes the Duplicate values bcz the hash value of same elements will be same.

---

# Debugging Question 4 (Medium)

```python
student = {
    "name": "Mahesh",
    "age": 22
}

for key, value in student.keys():
    print(key, value)
```

Answer:

1. Why does this fail?
ans:Here in print statement we are trying to access both key and value using the method dict.keys() this will not work to access the values. it will work if we want to access the keys only.
2. What should be changed?
ans: in the place of student.keys() it shoud be student.items():  this enable access to both keys and values
3. Explain the difference between `keys()` and `items()`.
ans: keys() are used to access the keys in the dictionary but the items() is used to access both key and value.
---

# Debugging Question 5 (Hard)

```python
students = {
    "Mahesh": 90,
    "Rahul": 80,
    "Anjali": 95
}

highest = 0
topper = ""

for name, marks in students.items():

    if marks >= highest:
        highest = marks
        topper = name

print(topper)
```

The program prints:

```text
Anjali
```

It works for the current data.

However, your manager says:

> "This program is wrong."

### Tasks

1. Explain why your manager is correct.
ans: Since as per given data the code works but in case multiple candidates have same marks which are heights like anjali at that time the above program will keep only the first highest candidate only not all topers therefor this is wrong.
2. Give an input where this program produces an incorrect result.
ans:  suppose will add another candidate called  "rakshit":95   still the program prints the anjali bcs it cannot handle multiple candidates.
3. Fix the program so it handles **multiple toppers** correctly.
ans: will use list to store multiple topers.

students = {
    "Mahesh": 90,
    "Rahul": 80,
    "Anjali": 95
}

highest = 0
topper = []

for name, marks in students.items():

    if marks >= highest:
        highest = marks
        topper = [name]
    elif highest == marks:
        topper.append(name)
        
print(topper)

---

## Submission Format

"""


"""

# Section 5 — Output Prediction (5 Questions)

**Rules**

* ❌ Don't run the code.
* ✅ Predict the exact output.
* ✅ If an error occurs, mention the error and explain why.

---

## Question 1 (Easy)

```python
student = {
    "name": "Mahesh",
    "age": 22
}

print(student.get("city"))
print(student.get("city", "Not Found"))
```

**What is the output?**
print(student.get("city")) this line doesnot print anything bcz there is no key "city" exist in dict.

print(student.get("city", "Not Found"))   # Not Found

---

## Question 2 (Easy)

```python
numbers = [1, 2, 2, 3, 3, 4]

unique = set(numbers)

print(unique)
print(len(unique))
```

**What is the output?**

> **Note:** For the first `print`, don't worry about the exact order of elements.

print(unique)  # {1,2,3,4}
print(len(unique))  # 4 


---

## Question 3 (Medium)

```python
marks = {}

subjects = ["Math", "Science", "Math", "English"]

for subject in subjects:
    marks[subject] = marks.get(subject, 0) + 1

print(marks)
```

**What is the output?**

print(marks)    #{"Math":2, "Science":1, "English":1}

---

## Question 4 (Medium)

```python
student = {
    "name": "Mahesh",
    "age": 22
}

for item in student.items():
    print(item)
```

**What is the output?**

('name', 'Mahesh')
('age', '22')


---

## Question 5 (Hard)

```python
students = {
    "Mahesh": [80, 90],
    "Rahul": [70, 60]
}

for name, marks in students.items():

    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 75:
        print(name, "Pass")
    else:
        print(name, "Fail")
```

**What is the output?**

Mahesh, Pass
Rahul, Fail

---

# Section 6 — Interview Questions (5)

Answer these as if you're in a Python backend interview.

Try to keep each answer to **2–5 sentences**.

---

## Question 1

### What is the difference between a dictionary and a set?

Explain:

* Storage
* Access
* Use cases

ans: Dictionary is used to store the relational data in key and value pair  and set is used to store the unique elements of data.
we can access the element on both data structure in O(1) time complexity. the dict is used to store the related data such as "name:mahesh" and the set is used when data integrity is required means unique data need to stiored.

---

## Question 2

### Why are dictionary lookups generally **O(1)**?

Explain the role of hashing in simple terms.

Ans: In dict the python stores the data in hashtable which is optimized to access the data therefor the lookups are generally O(1).

---

## Question 3

### What is hashability?

Why can a tuple usually be used as a dictionary key, but a list cannot?

ans: hashablity in python is the object has a fixed value that never changes and this can be used for hashing which mean like tuple is immutable if all objects are hasble then we can use these as keys in dict but lists are immutable and they cannot be hashed bcz the object can be changed therfor the cannot be Hashed.

---

## Question 4

### Explain the difference between these methods:

```python
dict.get()
```

```python
dict.keys()
```

```python
dict.values()
```

```python
dict.items()
```

Give one practical use case for each.

dict.get() is used to lookup the elements in dict
dict.keys() is used to access the keys in the dict.
dict.values() is used to access the values of all elemenst in the dict.
dict.items() is used to access both key and values in dict.


---

## Question 5 (Scenario-Based)

You're building a backend API for an e-commerce website.

Every product has:

```python
{
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "stock": 12
}
```

### Why would you choose a **dictionary** to represent a product instead of:

* List
* Tuple
* Set

Explain your reasoning as if you're answering an interviewer.

ans: Now let me do resoning for the dictionary Now by seeing the data its related data each product has varius parameters Therefor its dictinary is made to store the related data.
now if we try to store this data in list then we shoud use multiple list to store the ids,name's,price and stock and we need to store in the sequnce to we can access these by index  Therfor its difficuld  to manage and access.
now if we think about the tuple again we need to store as list inside the tuple bcz if we store as immutable then we coudnot update the product. so this is also not efficent data structure to store this kind of info.
set will remove duplicate values suppose we have two products which has same stock then this will result in dataloss of data integrity issues therefor we cannot use set for this kind of data.
Dict is efficient way to store this kind of data.
---

"""