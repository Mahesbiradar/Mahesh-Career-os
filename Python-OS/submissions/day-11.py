## TODAY'S ASSIGNMENT

"""
Goal: Build a small score-cleaning program that handles invalid numeric 
data without crashing.
Requirements (must complete all):

"""
#1.- [ ] Create a list called `raw_scores` with exactly these values: `"85"`, `"90"`, `"absent"`, `"76"`, `"100"`, and `"error"`. Also create empty lists called `valid_scores` and `skipped_values`.

raw_scores = ["85", "90", "absent", "76", "100", "error"]

valid_scores = []

skipped_values = []

#2. - [ ] Loop through `raw_scores`. Inside the loop, use a `try` block to convert each value to an integer.


#3.- [ ] Use `except ValueError` to handle invalid values. In this block, add the original value to `skipped_values` and print `Skipped invalid score: <value>`.

for i in raw_scores:

    try :
        num = int(i)

    except ValueError:

        skipped_values.append(i)

        print("Skipped invalid score:",i)
    
#4.- [ ] Use an `else` block for successful conversions. In this block, add the integer score to `valid_scores` and print `Accepted score: <score>`.

for j in raw_scores:

    try :
        num = int(j)

    except ValueError:

        # skipped_values.append(j)

        print("Skipped invalid score:",j)
    else:
        valid_scores.append(int(j))

        print("Accepted score:",j)
    
#5. - [ ] Use a `finally` block to print `Finished checking: <value>` for every item. After the loop, print `Valid scores:`, `Skipped values:`, and `Average score:` using the data you collected.

for k in raw_scores:

    try :
        num = int(k)

    except ValueError:

        # skipped_values.append(k)

        print("Skipped invalid score:",k)
    else:
        # valid_scores.append(k)

        print("Accepted score:",k)
    finally:
        print("Finished checking:",k)

print("Valid scores:",valid_scores)

print("Skipped values:",skipped_values)

print("Average score:",sum(valid_scores)/len(valid_scores))  #Here i used only valid score to make the average.

#Stretch (optional — do only after main requirements done):  

#6.- [ ] Add `"105"` to `raw_scores`, and after converting a score, manually `raise ValueError` if the score is greater than 100 or less than 0. Skip it the same way as the text errors.

raw_scores.append("105")

for score in raw_scores:

    try:
        num = int(score)
        if num > 100 or num < 0:
            raise ValueError
    except Exception as e:
        print(e)

## COMMUNICATION PRACTICE (15 min)

"""
Today's task: In 5 polished sentences, answer this interview-style question: 
"How do you handle invalid user input in Python?" Mention `try`, `except`, a 
specific exception type, and what message or fallback you would give the user. 
Before submitting, proofread once for complete sentences, capital `I`, correct 
spelling of "exception" and "specific", and spaces after commas.

"""

"""

I will handle the invalid user inputs using the 'try' and 'except' method.

I will handle each specific case like first I will check the type of the input
with each specific input and check the validity of the input using the 'try' and 
raise a specific error for the fallback message.
ex: suppose i want the user input in the range of 0 to 100 first I will check the 
input if its integer of not in try block and then ill raise specific exception to 
check the range of input and return the Fallback message in exception block as invalid 
input! Please enter input in the range of 0 to 100.

"""

## REVISION CHECK (answer these without looking — 2 min)

#1. Why is `student.get("phone", "Not provided")` safer than `student["phone"]` when the key might be missing?

"""
The .get method is safer than the normar key search like student["phone"] 
bacause when we check any key in dict using the normal key search if the 
key is missing in the dict then python throws the key error and program 
crashes instead we can use the .get method to prevent the crash and we can 
return the default value if key is missing using the .get method.

"""

#2.2. What syntax problem can happen when you put double quotes inside a double-quoted f-string, and how can you avoid it?

"""
the double code inside the double-quoted f-string may raise syntax error. Because the python thinks the string ends early and resilt in syntax error.
to avoid this we can use the single quotes inside the double-quoted f-string or use single-quoted f-string and use double quotes inside the f-string.

"""

## THEORY BLOCK (20 min)

"""
After watching, write 3 sentences in your own words explaining what an entity, an attribute, and a relationship mean in DBMS design.
Include this with your submission.

"""

#Entity:- Entity is anything or object which has a physical existnace.and its represented by rectangle
#attribute: attribute is caracterstics of the entity. represented by eclipse.
#relationship in dbms design: is association beetween two entity is called relation ship in DBMS design.represented by diamod shape.

#ER model is simply used for visual representation of the database schema. 


        




    
