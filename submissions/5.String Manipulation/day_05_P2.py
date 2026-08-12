"""

# Section 2 — Coding Assignments

## Rules

* ✅ Use only the topics you've learned:

  * Variables
  * Control Flow
  * Lists & Tuples
  * Dictionaries & Sets
  * String Manipulation
* ❌ Do **not** use:

  * Regular Expressions (`re`)
  * Advanced libraries
  * Built-in shortcuts like `reversed()`
* ✅ Focus on writing clean, readable code.
* ✅ Think about edge cases.

---

# Assignment 1 — Easy ⭐

## String Analyzer

Given:

```python
text = "  Python Programming  "
```

Write a program to:

1. Remove leading and trailing spaces.
2. Print the string in uppercase.
3. Print the string in lowercase.
4. Print the number of characters (after stripping spaces).
5. Print the first character.
6. Print the last character.
7. Print the substring `"Programming"` using slicing.
8. Check whether `"Python"` exists in the string.

### Expected Skills

* `strip()`
* `upper()`
* `lower()`
* `len()`
* Indexing
* Slicing
* `in`

---

# Assignment 2 — Medium ⭐⭐

## Word Statistics

Given:

```python
sentence = "Python is easy and Python is powerful"
```

Write a program to:

1. Split the sentence into words.
2. Count the total number of words.
3. Count how many times each word appears.
4. Print only repeated words.
5. Join the words back using `" | "` as the separator.

### Expected Output (Example)

```text
Python : 2
is : 2

Python | is | easy | and | Python | is | powerful
```

### Expected Skills

* `split()`
* `join()`
* Dictionary frequency counting
* Loops

---

# Assignment 3 — Hard ⭐⭐⭐

## Employee Record Formatter

You are given:

```python
employees = [
    "Mahesh,Backend Engineer,Bangalore",
    "Rahul,Frontend Developer,Pune",
    "Anjali,Data Analyst,Hyderabad",
    "Sneha,Backend Engineer,Bangalore"
]
```

Write a program that:

### Part A

Convert each string into:

```python
["Mahesh", "Backend Engineer", "Bangalore"]
```

using `split()`.

---

### Part B

Create a dictionary like:

```python
{
    "Mahesh": {
        "role": "Backend Engineer",
        "city": "Bangalore"
    },
    ...
}
```

---

### Part C

Print every employee as:

```text
Name : Mahesh
Role : Backend Engineer
City : Bangalore
```

using **f-strings**.

---

### Part D

Find how many employees belong to each city.

Expected example:

```python
{
    "Bangalore":2,
    "Pune":1,
    "Hyderabad":1
}
```

---

### Part E

Create a set containing all unique roles.

Example:

```python
{
"Backend Engineer",
"Frontend Developer",
"Data Analyst"
}
```

---

## Expected Skills

This assignment combines:

* `split()`
* `join()`
* Lists
* Dictionaries
* Nested dictionaries
* Sets
* f-strings
* Frequency counting
* Loops

"""



# Assignment 1 — Easy ⭐

text = "  Python Programming  "

def string_analyzer(string):

    # Remove leading and trailing spaces.
    new_text = string.strip()

    # Print the string in uppercase.

    print(new_text.upper())

    # Print the string in lowercase.

    print(new_text.lower())

    # Print the number of characters (after stripping spaces).

    print(len(new_text)) #includes the whitespaces b/w words.
    print(len(new_text.replace(" ",""))) # removes whitespace b/w words

    # Print the first character.

    print(new_text[0])

    # Print the last character.

    print(new_text[-1])

    # Print the substring "Programming" using slicing.

    print(text[9:])

    # Check whether "Python" exists in the string.

    print("Python" in new_text)


string_analyzer(text)


# Assignment 2 — Medium ⭐⭐

# Word Statistics

sentence = "Python is easy and Python is powerful"


def word_statistics(string):

    # 1.Split the sentence into words.

    words = string.split()

    # Count the total number of words.

    count_words = len(words)

    # Count how many times each word appears.

    freq_words ={}

    for word in words:
        freq_words[word] = freq_words.get(word,0)+1

    # Print only repeated words.

    for word,freq in freq_words.items():

        if freq > 1:
            print(f"{word} : {freq}")

    # Join the words back using " | " as the separator.

    joined_word = " | ".join(words)

    print(joined_word)

    

word_statistics(sentence)


# Assignment 3 — Hard ⭐⭐⭐

# Employee Record Formatter


employees = [
    "Mahesh,Backend Engineer,Bangalore",
    "Rahul,Frontend Developer,Pune",
    "Anjali,Data Analyst,Hyderabad",
    "Sneha,Backend Engineer,Bangalore"
]


def employee_record_formatter(data):


    employees_data = []

    for i in data:

        employees_data.append(i.split(","))

    print(employees_data)

employee_record_formatter(employees)

def convert_to_dict(data):
    employee_dict = {}

    for i in data:
        name,role,city = i.split(",")

        employee_dict[name] = {"role":role,"city":city}

        print(f"Name : {name}\nRole : {role}\nCity : {city}")

    return employee_dict

convert_to_dict(employees)


def count_of_citys(employees):

    cities = {}

    for i in employees:
        name,role,city = i.split(",")
        cities[city] = cities.get(city,0)+1

    return cities

cities_data = count_of_citys(employees)

print(cities_data)

unique_cities = set(cities_data)

print(unique_cities)



