## TODAY'S ASSIGNMENT

# - [ ] Use a `for` loop with `range()` to print numbers 1 to 10. Each line must be exactly: `Number: 1`, `Number: 2`, ... `Number: 10` (no extra spaces, no trailing space before the number)

for i in range(1,11):
    print(f"Number: {i}")
#- [ ] Use a `while` loop to count down from 5 to 1 (one number per line), then print `Liftoff!` after the loop ends. Must use a loop — no repeated print statements


x=5

while x > 0:

    print(x)
    x -= 1
print("Liftoff!")

# - [ ] Create a list of at least 5 items. Use a `for` loop with `break` to stop as soon as you find a specific target item, printing exactly: `Found: <item>`

items = [1,2,3,6,8,9]

target = 6


for item in items:

    if item == target:
        print(f"Found: <{item}>")
        break

# - [ ] Loop through numbers 1 to 20. Use `continue` to skip even numbers, and print odd numbers exactly as: `Odd: 1`, `Odd: 3`, etc.

for num in range(1,20):

    if num % 2 != 0:
        print(f"Odd: {num}")

# - [ ] Create one empty list and one non-empty list. For each, use `if <list_name>:` directly (no `not`, no `!= []`, no `len() == 0`) to print exactly `List is empty` or `List has items`. Your code must demonstrate both cases running.

nums=[]

if nums:
    print("List has items")
else:
    print("List is empty")

# Stretch (optional — do only after main requirements done):
# - [ ] Use a nested loop to print a multiplication table (1 through 5) for a number of your choice, formatted exactly as: `3 x 4 = 12`


for i in range(3,4):

    for j in range(1,6):

        print(f"{i} x {j} = {i*j}")

## COMMUNICATION PRACTICE (15 min)

#1. While i was working in pune my manager told me we are going to meet the customer regarding RF project. 
# But the Project specific details i was not aware and later on reaching at customer office they told me who is going to co-ordinate the team to be intrviewed shortly with technical team.

#2.Since i was not aware the project details but my manager told i have one sample report of the task that we need to perform on this Project and He forwarded the Doc.
# I have Only 30m before going to face the interview.

#3.Then i started Reading all the details of the task seen the pics in the report and with my previous knowledge i alinged all the things and got ready for the interview.

#4.The interview went good and im qualified for the co-ordinator role to lead our team for that project. 1hr Before i was not aware of the Task and Project and From the Next day i was Training Engineers in my team for the Project.



#### REVISION CHECK (answer these without looking — 2 min)

#1. not is inverter and if i use 'if not name != "": alter condition to opposite if name is not equals to empty of falsy.
#Since this we made simple thing complecated insted we can is 'if name:' if the name is true it will execute else not.

#2. if age = 0 and the condition is 'if age: this evaluate to False? Since Python retunr False while the values are 0,{},[],"".There for these things to be kept in mind when Checking the truthiness.







