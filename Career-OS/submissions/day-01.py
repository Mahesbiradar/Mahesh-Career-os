"""
## TODAY'S ASSIGNMENT

**Task:** Build a personal profile program  
**Time estimate:** 45 minutes  
**Difficulty:** Beginner  

### Requirements
Complete all of these:

- [ ] Create variables for: your name (str), your age (int), your years of experience (int), your target salary in LPA (float), and whether you are currently employed (bool)
- [ ] Print a formatted profile using f-strings that outputs all five values in one readable block (see expected output below)
- [ ] Ask the user to input a name and age using `input()`. Convert age to int. Print: "Hello [name], you will be [age+1] next year."
- [ ] Check the type of each of your five variables using `type()` and print them — confirm each is the type you expect
- [ ] **Stretch:** What happens if someone types "twenty" instead of a number in the age input? Try it. Note what error you get. Write a comment in your code explaining what the error means.


### Expected Output (for the profile block)
```
=== My Profile ===
Name: Mahesh Biradar
Age: 28
Experience: 8 years
Target Salary: 6.5 LPA
Currently Employed: False

"""

#Personal profile program.

name = "Mahesh Biradar"

age = 29

year_of_experience = 8

target_salary_lpa = 6.5

currently_employed = False

print(f"=== My Profile ===\nName: {name}\nAge: {age}\nExperience: {year_of_experience} years\nTarget Salary: {target_salary_lpa} LPA\nCurrently Employed: {currently_employed}")


#Task two 

print(type(name))
print(type(age))
print(type(year_of_experience))
print(type(target_salary_lpa))
print(type(currently_employed))


#Task three 

full_name = input("Enter your full name: ")

age = int(input("Enter Your age: "))

print(f"Hello {full_name}, You will be {age+1} next year")


#Task 4 

# print(int(input("Enter Twenty Here and see the Error.")))


"""
Enter Twenty Here and see the Error.Twenty
Traceback (most recent call last):
  File "d:\Dev\Mahesh Career os\Career-OS\submissions\day-01.py", line 64, in <module>
    print(int(input("Enter Twenty Here and see the Error.")))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'Twenty'
PS D:\Dev\Mahesh Career os> 

"""


"""
## COMMUNICATION PRACTICE (15 minutes)

**Today: Self Introduction**

Hi im Mahesh Biradar, I have 8 years of Experiance in Telecom Newtwork operations, Which gives me strong Foundations of System,debugging
and working under pressure. Im transitioning to software engineering, Now im bulding Backend sytems usoing python and Django.
Im targeting Backend and Full stack roles to apply my both system and new devlopment skills.


"""


# Now the Day 1 is finished.

#My review about the system Here i followed wnat i supposed to do but for the python topics the resources you suggest on udemy is not available then i visited you tube and saw video.

#communication is ok but not seems Intresting.


