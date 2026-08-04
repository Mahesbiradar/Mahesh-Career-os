

# Section 1 — Concept Questions (10)

## Easy

### Q1.

What is the difference between a **list** and a **dictionary**?
Cover:

* How elements are accessed in each.
* Time complexity of lookup (average case).
* One real-life use case for each.

---

## ans: Both list and dict are mutable data types but in list the elements are accesed through index and in dict elemnets are accessed throught key and dict store data as key value pair. But in list elements are store as there values.realted data stored in dict as key and value pair 
* in list Elements are accessed through index and in dict elements are accessed though the Keys.
* The time complexity of of lookpu in list is O(n) and o(1) in dict.
* suppose if we wanna store sequncial data then we ca use list = [1,2,3,4,5,6] so on and if we wanna store related data then we can use dict as dictionary ={"name":"mahesh","age":20,"city":"Bangalore"} 

### Q2.

Create the following dictionary in Python.

```python
student = {
    "name": "Mahesh",
    "age": 22,
    "branch": "ENTC"
}
```

Then write code to:

1. Print the branch.
2. Change age to 23.
3. Add CGPA = 8.64.
4. Remove the age key.

---
## ans: 
1. Print the branch.
print(student["branch"])   # ENTC
2. Change age to 23.
student["age"] = 23
3. Add CGPA = 8.64.
student["CGPA"] = 8.64
4. Remove the age key.
del student["age"]


### Q3.

What is the difference between:

```python
dict.get(key)
```

and

```python
dict[key]
```

When would you use each?

---
## ans:Both will do the same but main diffrence is if we use second one and if the key doent exist then the code will crash but if we use first one it will safely handle even if key doesnt exist in dict.

1.If im not sure either the eixts in dict or not ill use dict.get(key)
2.When im sure that the key exist in dict ill use dict[key]

## Medium

### Q4.

Explain the difference between:

* `keys()`
* `values()`
* `items()`

Write one example loop using each.

---
## ans:while looping over the dict if we want access only the keys then we use keys() or when we want only the values then we use values() or we want to access both the keys and values then we use items()

for key in dict.keys():
for value in dict.values():
for key,value in dict.items():


### Q5.

What will be the output?

```python
student = {
    "name": "Mahesh",
    "age": 22
}

student["age"] = 25
student["city"] = "Bangalore"

print(student)
```

Explain what happened.

---
## ans: 
o/p
{'name': 'Mahesh', 'age': 25, 'city': 'Bangalore'}

While the the dict is initialized it has two key,value pairs one is name and age. and then the age is updated and then one more key,value pair added in the dict.

### Q6.

Suppose you have:

```python
marks = {
    "A": 90,
    "B": 85,
    "C": 92
}
```

Write Python code to print:

```
A -> 90
B -> 85
C -> 92
```

using the best loop.

---
```python
marks = {
    "A": 90,
    "B": 85,
    "C": 92
}

for key,value in marks.items():

    print(f"{key} -> {value}")

### Q7.

What is a **set**?

Explain:

* Why duplicates are removed.
* Why indexing is not allowed.
* One practical use case.

---

## ans: set stores unordered and uniuqe sequnce of elements and its mutable data type its is intiallized as set().
* set contains only the unique elemenet therefor all the duplicates removed.
* since set is unordered data type which means all the elements in set has no sequence of fix order Therefor indexing is not allowed.
* To store the unique elements or removing the duplicates and preforming the fast membership testing.

## Hard

### Q8.

Explain the difference between:

```python
set
```

and

```python
frozenset
```

Why does Python provide both?

---
## ans: set is mutable data type which means we can add or remove the element and it unhasable but frozenset is immutable and hasable.

## python provides the frozenset bcz computer memory and some data structure required concept called hashability to protect data intergrity,python only allows immutable objects as hashable.

### Q9.

What is **hashability**?

Answer the following:

Can these be dictionary keys?

```python
10
```

```python
"hello"
```

```python
(1,2)
```

```python
[1,2]
```

```python
{1,2}
```

Explain **why** for each.

---
## Hashability is property of python object that means it has fixed value called (hash value) that never changes during its entire lifetime.

10 can be used as dict key bcz integres are immutable and Therefor thses are hasable.
"hello" is also used as dict key since strings are also immutable.
(1,2) is also used as dict key bcz tuples alos immutable.
[1,2] cannot be used as dict key since list are mutable.
{1,2} this also cannot be dict key dict also mutable.

### Q10.

Suppose you need to count the frequency of every word in a paragraph.

Would you use:

* List
* Tuple
* Dictionary
* Set

Explain why the chosen data structure is the best, and why the others are not.

## ans: I would use dictionary becuase we can store it as like word as key and values as its frequncy therefor and its O(1) time comp for lookup in dict. 




