## TODAY'S ASSIGNMENT

"""
**Goal:** Write a grade classifier program that uses `if / elif / else`, `and` / `or`, 
short-circuit evaluation, and falsy value checks — with a specific, 
correct f-string label on every print statement.

**Requirements (must complete all):**


"""

#1- [ ] Ask the user to input a score (0–100) using `input()`. Convert it to `int`. Store in variable `score`.

score = int(input("Enter your Score Between(O-100): "))

#2 - [ ] Use `if / elif / else` to classify the score:
#   - 90–100 → `"A"`
#   - 80–89 → `"B"`
#   - 70–79 → `"C"`
#   - 60–69 → `"D"`
#   - below 60 → `"F"`
#   - Print result with label exactly: `f"Grade: {grade}"`

#7- [ ] Add input validation: if the user enters a score below 0 or above 100, 
# print `f"Invalid score: {score}"` and do not classify it. Use a single `if` check at the top before the grade classification block.

if score<0 or score > 100:
    print(f"Invalid score: {score}")
elif score >= 90 and score <= 100:
    grade= "A"
    print(f"Grade: {grade}")
elif score >= 80 and score <= 89:
    grade= "B"
    print(f"Grade: {grade}")
elif score >= 70 and score <= 79:
    grade= "C"
    print(f"Grade: {grade}")
elif score >= 60 and score <= 69:
    grade= "D"
    print(f"Grade: {grade}")
else:
    grade= "F"
    print(f"Grade: {grade}")


#3 - [ ] Add a condition using `and`: if score is between 85 and 95 (inclusive), 
# print `f"Distinction range: True"` or `f"Distinction range: False"`

if score >=85 and score<=95:
    print(f"Distinction range: True")
else:
    print(f"Distinction range: False")
    
#4 - [ ] Add a condition using `or`: if score is below 40 or above 95, 
# print `f"Extreme score: True"` or `f"Extreme score: False"`

if score <40 or score>95:
    print(f"Extreme score: True") 
else:    
    print(f"Extreme score: False")

#5 - [ ] Demonstrate short-circuit evaluation with `and`: write `result = score > 50 and score < 100`. 
# Print `f"Short-circuit result: {result}"`. Add a comment on the line: `# short-circuit: if score > 50 is False, second check is skipped`

result= score > 50 and score < 100

print(f"Short-circuit result: {result}")  ## short-circuit: if score > 50 is False, second check is skipped`


#6- [ ] Demonstrate falsy check: ask user for their name with `input()`. 
# Use `if name:` (not `if name != ""`). If name is empty, print `f"Name: not provided"`. If name is given, print `f"Name: {name}"`


name = input("Enter Your name: ")

if name:
    print(f"Name: {name}")

else:
    print(f"Name: not provided")
     


## COMMUNICATION PRACTICE (15 min)

"""
**Today's task:** Answer this STAR behavioral question in writing.

**Question:** *"Tell me about a time you solved a problem under pressure."*

Use the STAR format:
```
Situation: [1–2 sentences — what was the context?]
Task:       [1 sentence — what was your responsibility?]
Action:     [2–3 sentences — what did YOU specifically do?]
Result:     [1–2 sentences — what was the outcome? Numbers if possible.] 

"""
# what was the context?
"""
I was working on project called RF survey. samsung was the customer and we have Deployed our 15 Team on ground
one fine Day cutomer asked about 1 site Which is Priority site but we are not aware of this and our nearest team from that site is about 160km.
and not able to travel to site as they have Diffrent plan but cutomer asking immedetly within 2hrs they wanted report.

"""
# what was your responsibility?

"""
Now my responsibility is to fulfill the requirement since i checked with all the teams and other vendors also.
No one Has team near to that sit and the are is Hilly Terrain and remote area.

"""
# what did YOU specifically do?

"""
I tried my best will all teams and vendors then come to conclution ill not get any manpower so i thougt what else i can i do to fix this.
Then i called the land owner wher the survey has to be done and then i asked him about the smartphone and I DID vc and guided him what are all things we needed to close this survey
With proper guidance and all i got all the required pics from the land owner.

"""

# what was the outcome? Numbers if possible.

"""
Since the outcome is not able to quantify but we are able to delever the Required report withing the customer requirement 
and with all the quality aspects and its got accepted.

"""

## REVISION CHECK (2 min — answer without looking)

# Topic from yesterday: **Day 3 — Strings**

# 1. What does `"  hello  ".strip()` return? Does it change the original string?

# the "  hello  ".strip() retuns (hello) | No it doen't chnage the original string instead it retund copy of the string.

# 2. You write `s = "backend engineer"`. What does `s[8:16]` return?

#s[8:16] returns engineer  since starting number is inclusive and ending is exclusive.


