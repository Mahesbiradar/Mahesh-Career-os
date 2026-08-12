# Section 1 — Concept Questions (10)

## Easy

### Q1.

What is a **string** in Python?

Cover:

* What type of data it stores.
* How it is created.
* Whether it is mutable or immutable.

---
## Ans:String in python is immutable collection of sequence of text characters. it can be created in two way one is str() or simply inside the double qoutes write any text or keep it empty also. Strings are immutable.

### Q2.

Explain the difference between **indexing** and **slicing**.

Given:

```python
text = "Python"
```

Write the output of:

```python
text[0]
text[-1]
text[1:4]
text[:3]
text[3:]
```

---
## Ans: The diff b/w the indexing and slicing is the indexing on string returns the specific single 1 char substring on that index. In slicing it returns the subtring in range which is written inside the slicing means what is the start and what is the end.
text[0] - P
text[-1] - n
text[1:4] - yth
text[:3]  - pyt
text[3:]  - hon

### Q3.

What is **string immutability**?

Why does the following code produce an error?

```python
name = "Mahesh"
name[0] = "R"
```

How would you correctly change `"Mahesh"` to `"Rahesh"`?

---
## Ans: string immutibilty is property of python objects where the object cannot be mofified or changes once its declaired.

to fix the above code we can use the replace method of string which return the new string.

name1 = name.replace('M','R')

## Medium

### Q4.

Explain the difference between the following string methods:

* `upper()`
* `lower()`
* `capitalize()`
* `title()`

Give one example of each.

---
## Ans: 1.the upper() method is used to convert all alpha chars to uppercase ex: name = "mahesh"   print(name.upper()) # MAHESH
2.lower() similar to the upper case lower case is used to lower all the aplha chars in string.  name = "MAHESH"  Using lower mahesh
3.capitalize() is used to converts the First char of the string to Upper case and force all other chars to lower case.text = "learning PYTHON is FUN"  print(text.capitalize())  # "Learning python is fun"
4.title() is used to convers the first char of each word in string to uppercase and all other chars to lower.
text = "learning PYTHON is FUN" print(text.title())  # "Learning Python Is Fun"
### Q5.

What is the difference between:

```python
split()
```

and

```python
join()
```

When would you use each?

Give one example of both.

---
## Ans: split() breaks the single string into a list of smaller strings, while join() takes a list of smaller strings and glues them into a single string.

Use split() when you have a long piece of text (like user input, a CSV file row, or a paragraph) and you need to break it down into individual words or data pieces to process them one by one

sentence = "Python is fun"

# Splits by whitespace by default
words_list = sentence.split() 

print(words_list)  
# Output: ['Python', 'is', 'fun']

Use join() when you have multiple strings stored inside a list, array, or tuple, and you need to combine them into a single, clean sentence or data row separated by a specific character (like a space, comma, or hyphen).

words_list = ['Python', 'is', 'fun']

# The string before .join() is the separator used between items
clean_sentence = " ".join(words_list) 

print(clean_sentence)  
# Output: "Python is fun"

### Q6.

Explain the difference between:

```python
find()
```

and

```python
index()
```

What happens when the substring is not found?

---
## Ans : Both these methods are used to find the substring in string but the find() method return -1 id substring not found in the string but in index() method it raises the valueerror when substring not found. both of these methods retruns the first index of the substring when it found in substring.


### Q7.

What is an **f-string**?

Why is it generally preferred over string concatenation?

Write an example.

---

## Ans : An f-string (formatted string literal) is a string prefixed with 'f' or 'F' that allows you to embed Python expressions directly inside curly braces {}.Python evaluates these expressions at runtime and automatically formats them into the string.

Why f-strings are Preferred Over ConcatenationBetter Readability: You see the final sentence structure clearly without breaking the text apart with multiple quotes and + symbols.Automatic Type Conversion: You do not need to manually wrap numbers or booleans in str() to prevent type errors.Higher Performance: Python optimizes f-strings at the bytecode level, making them faster than both + concatenation and the older .format() method.Inline Expressions: You can run math, call methods, or execute logic directly inside the curly braces

name = "Alice"
age = 30

# Must convert age to a string manually
message = "Hello, my name is " + name + " and I am " + str(age) + " years old."
print(message)

name = "Alice"
age = 30

# Clean, readable, and fast
message = f"Hello, my name is {name} and I am {age} years old."
print(message)

## Hard

### Q8.

Suppose you have:

```python
sentence = "Python is powerful"
```

Without changing the original string,

write code to produce:

```text
PYTHON IS POWERFUL
```

Explain why the original string remains unchanged.

---
## Ans:
sentence = "Python is powerful"
uppercase_sentence = sentence.upper()
print(uppercase_sentence)

The original string remains completely unchanged because strings in Python are immutable.Memory Preservation: Once a string object is created in your computer's memory, its contents can never be modified, edited, or reordered in place.New Object Creation: When you call a string method like .upper(), Python creates a brand-new string object in a different memory location, populates it with the modified text, and returns it.Variable Isolation: The variable sentence continues to point to the original lowercase string until you explicitly overwrite it.


### Q9.

Explain the difference between:

```python
strip()
```

```python
lstrip()
```

```python
rstrip()
```

Give one practical use case for each.

---

By default, these methods remove whitespace characters (spaces, tabs \t, and newlines \n), but you can also pass specific characters into them to be stripped away.

1. strip()Removes characters from both the beginning and the end of the string.Practical Use Case: Cleaning up raw user input. Users often accidentally hit the spacebar before or after typing their username or email address.Example:pythonuser_input = "   admin_user   "
clean_username = user_input.strip()
print(f"'{clean_username}'")  
# Output: 'admin_user'

2. lstrip()Removes characters only from the left side (the beginning) of the string.Practical Use Case: Standardising data logs or cleaning up indentation. For example, if you are reading code or configuration text files line-by-line and want to remove leading indentations to process the text from the start.Example:pythonlog_line = "    ERROR: Connection failed"
clean_log = log_line.lstrip()

print(clean_log)  
# Output: "ERROR: Connection failed"

3. rstrip()Removes characters only from the right side (the end) of the string.Practical Use Case: Cleaning up text files. When reading a text file line-by-line in Python using a loop, each line automatically comes with a hidden newline character (\n) at the very end. rstrip() cleans this up without breaking indentation at the front.Example:pythonfile_line = "Processing data... \n"
clean_line = file_line.rstrip()

print(f"'{clean_line}'")  
# Output: 'Processing data... '


### Q10.

Suppose you're building a backend API.

A client sends:

```text
Mahesh,Bangalore,Python,Django
```

Explain how you would use:

* `split()`
* Lists
* `join()`

to process this data and generate:

```text
Mahesh | Bangalore | Python | Django
```

Why is this approach useful in backend development?

---

# 1. Receive the raw string from the client
raw_data = "Mahesh,Bangalore,Python,Django"

# 2. Use split() to break the string by commas into a list
data_list = raw_data.split(",")  
# Resulting List: ['Mahesh', 'Bangalore', 'Python', 'Django']

# 3. Use join() to glue the list items back together using " | " as the separator
formatted_data = " | ".join(data_list)

print(formatted_data)
# Output: Mahesh | Bangalore | Python | Django

Data Sanitization and Validation: Between splitting and joining, having the data in a list allows you to inspect it. You can check if the email format is correct, verify that fields are not empty, or strip accidental spaces from individual values.Format Interoperability: APIs constantly deal with mismatched formats. This technique lets you easily ingest data in one format (like a CSV row) and transform it into another format required by logs, legacy systems, or third-party services.Database Readiness: Splitting a comma-separated string into a list makes it ready to be mapped directly into different columns of a database table (e.g., Name, Location, Language, Framework).




