## TODAY'S ASSIGNMENT

# Goal: Show you can create and unpack a tuple, and use sets with intersection/union operations to compare two collections.

#Requirements (must complete all):

#- [ ] Create a tuple called `coordinates` with exactly 3 numbers (x, y, z), then print it with the label `Coordinates:`

coordinates = (10, 15, 20)

print(F"Coordinates: {coordinates}")

#-- [ ] Unpack `coordinates` into three variables `x`, `y`, `z`, then print them with the label `Unpacked:` in the exact format `x=1, y=2, z=3` (using your actual values)

x , y , z = coordinates

print(f"Unpacked: x={x}, y={y}, z={z}")

#- [ ] Create two sets, `python_skills` and `java_skills`, each with at least 4 string items, with at least 2 items overlapping between them

python_skills = {"List", "Dict", "Set", "Tuple"}

java_skills = {"Array", "Dict", "Set", "String"}

# - [ ] Use `&` to find the skills common to both sets, then print the result with the label `Common skills:`

common_skills = python_skills & java_skills

print(f"Common skills: {common_skills}")

#- [ ] Use `|` to combine both sets into all unique skills, then print the result with the label `All skills:`

all_skills = python_skills | java_skills

print(f"All skills: {all_skills}")


# Stretch (optional — do only after main requirements done):

# - [ ] Use `-` to find skills that are in `python_skills` but not in `java_skills`, then print the result with the label `Python only:`

python_only = python_skills - java_skills

print(f"Python only: {python_only}")


# ## COMMUNICATION PRACTICE (15 min)

"""
Today's task: In 3-4 sentences, explain the difference between a list and 
a tuple, as if answering it in an interview. Before submitting, proofread 
it once: check that every sentence is a complete sentence (not a fragment 
ending in a period where it should be joined with a comma), and that no 
sentence starts with "And". Also double-check spelling on any word you're 
unsure of.
"""

"""
Ans:-

-List in python is a ordered mutable collection written with the square brackets [].
 mutable means we can add, remove and update the elements inside the list.


-Tuple in python is a ordered immutable collection written with the paranthesis ().
 immutable means once the tuple is created then we are not able to insert,delete, 
 update the elements inside the tuple. 

* Therefor the list is used where insertion,updation and deletion of data is 
  required whereas the tuple is used where altering the data prohibited.

"""

## REVISION CHECK (answer these without looking — 2 min)

# 1. What's the difference between `append()` and `insert()` on a list?

"""
Both are the list methods where the append() adds the element in list 
after the last element in existing list. But the insert() adds the element 
at the specific index while inserting the element the user has to pass 
the data and the index where the data to be inserted.and all the element 
from the inderted index are shifted right to inserted element means all 
the elements are incremented by 1 index 

"""

# 2. What does `enumerate()` give you when looping over a list, and why is it more useful than a plain `for item in list` loop when you also need the position?

"""
enumerate() function gives both the index and the value of that index when 
looping over the List its useful than the plain 'for item in list' bcz this 
loop gives each item in list with each iteration but for the application 
where the index and value required while looping over a list enumerate() 
gives both without a complex syntax ex: for index,value in enumerate(List):

"""

