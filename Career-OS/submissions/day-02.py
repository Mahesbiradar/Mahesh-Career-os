"""
## TODAY'S ASSIGNMENT

**Task:** Operators demonstration script  
**Time estimate:** 45 minutes  
**Difficulty:** Beginner  

### Requirements
Complete all of these:

- [ ] Demonstrate all 7 arithmetic operators with print statements showing inputs and outputs
- [ ] Show the difference between `/` and `//` clearly — use an example where the result is different (e.g. `7/2` vs `7//2`)
- [ ] Show short-circuit evaluation for `and` and `or` — use print statements that prove Python stopped early (hint: `0 and print("this should not print")`)
- [ ] Show the difference between `==` and `is` — use a list example where `==` is `True` but `is` is `False`
- [ ] **Stretch:** What does `bool(0)`, `bool("")`, `bool([])`, `bool(None)` return? Print all four and write a comment explaining what "falsy" means

### Rules During Assignment
- AI is **OFF**
- Official docs allowed: docs.python.org/3/library/stdtypes.html
- Re-read the Concept Summary above if stuck
- If stuck for 20+ minutes on one thing → note it and keep going

"""

# Operators demonstration script

# Task1:7 arithmetic operators

x,y=10,5

print(f"addition: (input x:{x},y{y} output x+y=:{x+y})")
print(f"substraction: (input x:{x},y{y} output x-y=:{x-y})")
print(f"multiplication: (input x:{x},y{y} output x*y=:{x*y})")
print(f"division: (input x:{x},y{y} output x-y=:{x/y})")
print(f"floor division: (input x:{x},y{y} output x-y=:{x//y})")
print(f"modulo: (input x:{x},y{y} output x-y=:{x%y})")
print(f"exponential: (input x:{x},y{y} output x-y=:{x**y})")

#Task 2: Diff b/w division and Floor Division

x,y=7,2

print(f"division: (input x:{x},y{y} output x-y=:{x/y})")
print(f"floor division: (input x:{x},y{y} output x-y=:{x//y})")


# Task 3: Short Circuit Evaluation

if 0 and 2:
    print("this should print")
else:
    print("this should not print")

if 5 or 2:
    print("this should print") 
else:
    print("this should not print")

# Task 4: Diff b/w is and ==

a=[1,2,3]
b=[1,2,3]

print(a == b)  #True

print(a is b)  #False 

#Task 5: What does `bool(0)`, `bool("")`, `bool([])`, `bool(None)` return? Print all four and write a comment explaining what "falsy" means

print("Task 5")
a=0
b=""
c=None
d=[]

if a:
    print(True)
else:
    print(False)

#Here int 0 is False Therefor the second Condition printed

if b:
    print(True)
else:
    print(False)

#the Empty String is nothing but False Therefor the second Condition printed


if c:
    print(True)
else:
    print(False)  

#the None is ntg but no value and False Therefor the second Condition printed


    
if d:
    print(True)
else:
    print(False)

#The Empty Sequncy Data types also False Therefor the second Condition printed


"""

## REVISION CHECK

> Answer this before starting the video. Takes 2 minutes.  
> Topic from Day 1: **Variables & Data Types**

**Question:** Without looking at your Day 1 code — what does `type("hello")` return? What does `int("28")` do? And what error do you get if you call `int("twenty")`?

Write your answer out loud or in a comment in today's file before you begin.

"""
#1: what does `type("hello")` return?

#It return <class 'str'> and this the string data type

#2: What does `int("28")` do?

# This does the Type Casting in simplte Terns it converts the String "28" to interger 28

#3: what error do you get if you call `int("twenty")`?

#it will lead to Value error bc it can converts the numbers not the Characters.

"""
## COMMUNICATION PRACTICE (15 minutes)

**Today: Refine your self-introduction**

You wrote a version on Day 1. Today, say it out loud 3 times without reading it.

Then answer this out loud (60 seconds):  
*"Operators in Python are ___. The one that surprised me was ___ because ___."*

This is technical explanation practice — you will be asked to explain code concepts in interviews. The habit starts now.

**Pronunciation drill (say each term 3 times):**  
Django (JANG-go) · PostgreSQL (post-GRESS-Q-L) · API (A-P-I) · HTTP (H-T-T-P) · Python (PIE-thon)

---

*Next lesson: DAY 3 — Strings (methods, slicing, f-strings, immutability)*

"""

# **Today: Refine your self-introduction**

# You wrote a version on Day 1. Today, say it out loud 3 times without reading it.

#Done.

# Then answer this out loud (60 seconds):  

# Operators in python are symbols which tells the python to preform the operations on Values. The one That surprised me was ** exponencial operator bcz its Produces the expo result.

# **Pronunciation drill (say each term 3 times):**  
# Django (JANG-go) · PostgreSQL (post-GRESS-Q-L) · API (A-P-I) · HTTP (H-T-T-P) · Python (PIE-thon)

#Done



# Direct proof — the print inside never executes
result = 0 and print("you will NOT see this")
print(result)   # 0

result = 5 or print("you will NOT see this either")  
print(result)   # 5




# What was asked:
print(bool(0))     # False
print(bool(""))    # False
print(bool([]))    # False
print(bool(None))  # False