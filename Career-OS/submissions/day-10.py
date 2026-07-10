## TODAY'S ASSIGNMENT

"""
Goal: Show you can create, read, update, delete, safely access, and loop 
through dictionary data.

"""

# Requirements (must complete all):

#1.- [ ] Create a dictionary called `student` with exactly these keys: `"name"`, `"age"`, `"course"`, and `"city"`, then print it with the label `Original profile:`

student = {"name":"Mahesh", "age":28, "course":"python", "city":"Bangalore"}

print(f"Original profile: {student}")

#2. - [ ] Print the student's name using `student["name"]` with the label `Student name:`

print(f"Student name: {student['name']}")

#3.- [ ] Add a new key `"email"` and update the `"city"` value to a different city, then print the dictionary with the label `Updated profile:`

student.update({"city":"mysore", "email":"abc@gmail.com"})

print(f"Updated profile: {student}")

#4.- [ ] Use `.get()` to read a missing key called `"phone"` with the default value `"Not provided"`, then print it with the label `Phone:`

print(f"Phone: {student.get('phone','Not provided')}")

#5.- [ ] Remove the `"age"` key, then loop through `student.items()` and print every remaining key-value pair under the label `Final profile:`

del student["age"]

for key,value in student.items():

    print(f"Final profile: {key}:{value}")

print(f"Final profile: {student}")

#in above assignment not cleared when to print inside the loop or after the loop so i written both.

# Stretch (optional — do only after main requirements done):

#- [ ] Create a second dictionary called `skill_scores` with at least 3 skills and numeric scores. Loop through it and print only the skills with a score of 7 or higher.

skill_scores = {"python": 8, "DSA":6, "Backend":5, "communication":9}

for key,value in skill_scores.items():

    if value >= 7:
        print(f"{key} : {value}")

## COMMUNICATION PRACTICE (15 min)


"""
Python dictionary is data structure used to store the related data in key value pairs.
I will use dictionary in my projects to store the user profiles ex: I have used this data type in the project called newjjroadline.com
where the three type of user group exist drivers,co-ordinators,admin  therefor i have used this data type to store all the details of these user groups as key value pair.

"""

## REVISION CHECK (answer these without looking — 2 min)

# 1. Why can you not change an item inside a tuple after creating it?

"""
Because in python tuples are immutable means once it created not able to modify.
and the tuples are made for the purpose of immutibility ex: i want to store some data and i want this data cant be changed therefor I will use tuple.

"""
# 2. What is the difference between `{}` and `set()` when creating an empty collection?

"""
If we are creating a empty collection and if we initialize that collection with {} then empty dictionary will be created.
whereas if we initialize the collection with set() the empty set is created.

"""

## THEORY BLOCK (20 min)

"""
DBMS defined as Data base management system used to store the data in structured way in form of tables. DBMS Helps users to perform the crud operations on this data.
the advantage of choosing the DBMS over the plain files by applications is DBMS helps perfoming the operations over data without the redundancy,inconsistancy and storing all the data in centeralized way.

"""



