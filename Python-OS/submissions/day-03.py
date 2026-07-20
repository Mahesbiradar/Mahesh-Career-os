"""
1. **f-string labels must match the operation** — `f"x + y = {x+y}"` not `f"x-y = {x+y}"` for addition
2. **Short-circuit proof means a direct expression** — `print(False and print("runs"))` shows short-circuit, not an if/else block
3. **bool() usage** — `bool(0)`, `bool("")`, `bool([])` called directly, not wrapped in if/else

These are not major — your concept understanding was solid. Watch out for these in today's code.

"""

#1 

x=10
y=5

print(f"x + y = {x+y} x - y = {x-y} x * y = {x*y} x / y = {x/y} x // y = {x//y} x % y = {x%y} x ** y = {x**y}")

#2.

print( False and print("runs"))
print( False or print("runs"))

#3.

print("bool")
print(bool(0))
print(bool(False))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(None))

## TODAY'S ASSIGNMENT

print("TODAY'S ASSIGNMENT")

#1 - [ ] Create a variable `sentence = "  Python is a powerful programming language  "` (with leading/trailing spaces)

sentence = "  Python is a powerful programming language  "

#2 - [ ] Use `.strip()` to remove the spaces, store in a new variable, print with label `"Stripped:"`

striped_sentence = sentence.strip()

print(f"Stripped: {striped_sentence}")

#3 - [ ] Use slicing to extract the word `"powerful"` from the stripped sentence. Print with label `"Sliced word:"`

print(f"{striped_sentence.find("powerful")}")  # used to find the index.

sliced_word = striped_sentence[12:20]    # Here used the starting and ending index.

print(f"Sliced word: {sliced_word}")

#4 - [ ] Use `.upper()` and `.lower()` on the stripped sentence. Print both with correct labels

print(f"Striped sentence lower case: {striped_sentence.lower()},Striped sentence upper case: {striped_sentence.upper()}")

#5 - [ ] Use `.replace()` to replace `"powerful"` with `"beautiful"`. Print with label `"Replaced:"`

replaced_word = striped_sentence.replace("powerful","beautiful")

print(f"Replaced: {replaced_word}")

#6 - [ ] Use `.split()` to split the stripped sentence into a list of words. Print the list with label `"Words list:"` and print the word count with label `"Word count:"`

world_list = striped_sentence.split()

print(f"Words list:{world_list}")

print(f"Word count:{len(world_list)}")

#7 - [ ] Demonstrate immutability: print the original `sentence` variable after all the above operations and confirm it has not changed. Add a comment `# immutability proof`

print(sentence)    #immutability proof  but for each method i used seperate varibale Therefor Directly i cant show the proof but its immutable even if we perform any method on original string.

# **Stretch (optional — only after all above are done):**

#8 - [ ] Ask the user to input a sentence. Use `.startswith()` to check if it starts with "I" or "i". Print result with a clear f-string label.

user_input = input ("Enter your Message: ")


if user_input.startswith(("i", "I")):

    print(f" the user input starts with I or i")


## COMMUNICATION PRACTICE (15 min)

"""
**Today's task:** Rewrite your Day 1 self-introduction as a 
**professional email** to a hiring manager.

"""

"""
subject: Application for backend Devloper Role - Mahesh Biradar

Dear Hiring Manager,

I'm Mahesh biradar, I have 8 years of experiance in telecom network operations,I'm Transitining into software engineering. 
I'm building backend systems using Python and Django. the last experaince build my foundations in sytem, debugging and working under pressure.
Now im targeting backend or fullstack roles where i can appaly my both system and new devolopmenet skills.

Requesting you to kindly review my application.

Thank You!.

Regards,
Mahesh Biradar

"""

## REVISION CHECK (2 min — answer without looking)

#1. What is the difference between `//` and `/` in Python? What does `7 // 2` return?

"""
The Difference Between the floor Division and division in python is.
the floor (//) division returns the integer whereas the division return the float value.
 "7//2" returns 3 which is integer number.

"""

#2. You write `print(False and risky_function())`. Does `risky_function()` get called? What is this behaviour called, and why does it happen?


"""
1.in print statement the risky_function() is not called.

2.Since the and operator return true only all conditions are true since in above print statement False comes earlier 
therefor the and function not at all call any other function if it gets false on intial

3.In specific the name of the Behaviour i dont Know but i guess its Falsy behaviour.
"""


    



