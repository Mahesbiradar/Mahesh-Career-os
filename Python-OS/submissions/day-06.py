## TODAY'S ASSIGNMENT

#1.- [ ] Use a `for` loop with `range()` to print numbers 1 to 15. Each line must be exactly: `Count: 1`, `Count: 2`, ... `Count: 15` (no extra spaces, no trailing space before the number)

for i in range(1,16):

    print(f"Count: {i}")

#2.- [ ] Use a `while` loop to count UP from 1 to 5 (one number per line), then print `Done!` after the loop ends. Must use a loop — no repeated print statements

x = 1

while x < 6:

    print(x)
    x +=1

print("Done!")

#3.- [ ] Create a list of at least 6 items. Use a `for` loop with `break` to stop as soon as you find a specific target item. Print exactly `Found: 6` style output — i.e. `Found: ` followed immediately by the item's actual value and nothing else. No angle brackets, no extra punctuation. (If your target is `7`, the printed line must be exactly `Found: 7`.)

nums = [1,3,6,8,9,4]

for num in nums:

    if num == 6:
        print(f"Found: {num}")

        break
    print(num)

#4.- [ ] Loop through numbers 1 to 25 using `range(1, 26)`. You must use the `continue` keyword: if a number is even, `continue` immediately. The `print(f"Odd: {num}")` line must be a separate, unconditional statement that runs after the `continue` check — not wrapped in its own `if`.

for num in range(1,26):

    if num % 2 == 0:
        continue
    
    print(f"Odd: {num}")

#5.- [ ] Create two separate lists: one empty, one with at least 3 items. For EACH list, use `if <list_name>:` directly (no `not`, no `!= []`, no `len() == 0`) to print exactly `List is empty` or `List has items`. Both checks must run in your code and both outputs must appear when the file is executed.

nums=[]

nums2=[2,3,4]


if nums:
    print(f"List has items")
else:
    print(f"List is empty")

if nums2:
    print(f"List has items")
else:
    print(f"List is empty")

#Stretch (optional — do only after main requirements done):

#6.- [ ] Use a nested loop to print multiplication tables (1 through 5) for TWO different numbers of your choice, formatted exactly as: `4 x 3 = 12`


for i in range(1,5):

    if i % 2 ==0:

        for j in range(1,11):

            print(f"{i} x {j} = {i*j}")

#Why i used the if statement in outer loop is bcz you told use two number of your choise b/w 1 to 5 Therefor i printed table for even number in 1 to 5


### COMMUNICATION PRACTICE (15 min)

#Task: Answer this behavioral question using explicit STAR labels:

# *"Tell me about a time you had to solve a problem under pressure or with limited information."*

#Situation: I have to take the Handover of my senior colleague who is leaving the organization os same day and He explained the taks overview in 30m.

#Task: The task is to Analyze the UBR offender links in the Entire Karnataka circle and give the solution to each offender link thorough the Proper analysis.

#Action: Since I had only Half day to prepare the report and present it in the VC with senior Leadership. Now the Main task is to analyze all the 400 links since each link would take 10-15 min if had to analyze the actuall route Cause and i have limited time what is did is I identified the old links which which were part of 4-5 weeks and mapped the action plans what the senior mapped and then worked out only the new links which were added in the current week and found the root cause and Mapped solution for all the links.

#Result: Report and data were ready before the VC started and Then presented in the vc with all the issue's and solution of all the links and organized the owners where the solution is pending and Taken the timeline from then and The VC went Very well from my end.


## REVISION CHECK (answer these without looking — 2 min)

#1. If the assignment requires you to use `continue`, why doesn't writing `if num % 2 != 0: print(...)` satisfy that requirement, even though the output looks the same?

#Now the main diffrence using the conditional statement and the continue is if we use conditional statement the condition works and again anything after the condition also executes apart from the condition but if we use the continue any thing after the continue is not going to execute the continue simply jumps to next iteration after it executed.

#2. If a target item's value is `6` and the spec says print exactly `Found: 6`, what's wrong with writing `print(f"Found: <{item}>")`? What would it actually print?

# the `print(f"Found: <{item}>")` is print 'Found: <6>' This is wrong the item is wrapped inside the angle brackets since the spec demands the print shoud be 'Found: 6'




