
"""
### 🏗️ Mini Project: Student Gradebook Manager

Build a command-line gradebook system. Each student record is a **tuple** `(name, roll_number)` — immutable ID. Grades are stored in a **list of lists** (2D structure).

**Requirements:**

1. **Data Structure:** Maintain a list `gradebook` where each element is:
   ```python
   (student_tuple, [subject1_score, subject2_score, subject3_score])
   ```
   Example:
   ```python
   gradebook = [
       (("Alice", 101), [85, 90, 78]),
       (("Bob", 102), [72, 88, 91]),
       (("Carol", 103), [95, 85, 88]),
   ]
   ```

2. **Menu Loop:** Use a `while` loop to show a menu:
   ```
   1. Add Student
   2. Display All Students (with averages)
   3. Find Topper
   4. Exit
   ```

3. **Add Student (Option 1):**
   - Take name and roll number, create a tuple.
   - Take 3 subject scores as a list.
   - Append `(tuple, list)` to `gradebook`.
   - Validate: scores must be 0–100. If invalid, print error and use `continue`.

4. **Display All (Option 2):**
   - Use `enumerate()` to print numbered rows.
   - Calculate average using operators (`sum / len`).
   - Print: `1. Alice (101) - Scores: [85, 90, 78] - Avg: 84.33`

5. **Find Topper (Option 3):**
   - Iterate with `for` loop.
   - Track the highest average.
   - Print topper's name, roll number, and average.
   - Handle empty gradebook gracefully.

6. **Exit (Option 4):** Break the loop.

**Bonus:** Add Option 5 — "Remove Student by Roll Number". Search the list, and if found, remove that entry. If not found, print `"Student not found"`.

---

**Write the full program and share it. Once you're done, we'll move to debugging.**

"""
def print_gradebook(data_list):
    if not data_list:
        return print("Gradebook is empty")

    for index, ((name, roll), scores) in enumerate(data_list, start=1):
        avg = sum(scores) / len(scores)
        print(f"{index}. {name} ({roll}) - Scores: {scores} - Avg: {avg:.2f}")

def find_topper(data):
    if not data:
        return print("Gradbook is empty")
        
    s_name= None
    rollnumber = None
    highest_average = float("-inf")

    for index,((name,roll),score) in enumerate(data):

        avg = sum(score)/len(score)
        if avg > highest_average:
            highest_average = avg
            s_name = name
            rollnumber = roll
    print(f"{s_name} ({rollnumber}) -Avg: {highest_average:.2f}")

def remove_student(databook,rollnum):
    if not databook:
        return print("Gradebook is empty")


    target_roll = rollnum

    for student in databook:

        (name,roll),scores = student

        if roll == target_roll:
            databook.remove(student)
            return print(f"Removed {name} ({roll}) successfully.")
            
    else:
        return print("Student not found.")



gradebook = [
    (("Alice", 101), [85, 90, 78]),
    (("Bob", 102), [72, 88, 91]),
    (("Carol", 103), [95, 85, 88]),
]

def add_student(data):

        name = input("Enter the student Name: ").strip()
        rollnumber = int(input("Enter the student Roll number: "))

        for index,((name,roll),scores) in enumerate(data):

             if roll == rollnumber:
                return print("Student alredy Exist With given roll number")


        sub1 = int(input("Enter subject1 Marks: "))
        if sub1 < 0 or sub1 > 100:
            return print("Invalid score")
        sub2 = int(input("Enter subject2 Marks: "))
        if sub2 < 0 or sub2 > 100:
                    return print("Invalid score")
        sub3 = int(input("Enter subject3 Marks: "))
        if sub3 < 0 or sub3 > 100:
                    return print("Invalid score")
    
        gradebook.append(((name, rollnumber), [sub1,sub2,sub3]))


while True:

    option = input("1. Add Student\n2. Display All Students (with averages)\n3. Find Topper\n4. Exit \n5. Remove :\n").strip()

    if option == "1":
        add_student(gradebook)
    elif option == "2":
        print_gradebook(gradebook)
    elif option == "3":
        find_topper(gradebook)
    elif option == "4":
        break
    elif option== "5":
        rollnum = int(input("Enter the student Roll number to delete: "))
        remove_student(gradebook,rollnum)

    
    
"""
  Here is the review of your mini project:

---

### ✅ What's Working Well
- **Data structure** is correct: list of `(tuple, list)` pairs.
- **Menu loop** with `while True` and option handling is clean.
- **`print_gradebook`** uses `enumerate` and tuple unpacking correctly.
- **`find_topper`** tracks the highest average properly.
- **Roll number uniqueness check** in `add_student` is a nice touch.

---

### ⚠️ Issues to Fix

**1. `add_student` — Missing `continue` requirement**
The spec said: *"Validate: scores must be 0–100. If invalid, print error and use `continue`."*

You used `return` instead of `continue`, which exits the entire function. Since `continue` only works inside a loop, you needed to wrap the score inputs in a `for` or `while` loop:

```python
scores = []
for i in range(1, 4):
    score = int(input(f"Enter subject {i} Marks: "))
    if score < 0 or score > 100:
        print("Invalid score")
        continue  # skips to next subject? No, that doesn't make sense here either.
```

Actually, the better pattern for "retry until valid" is a `while` loop per subject. The `continue` requirement likely meant skipping the append if any score is invalid — but your `return` approach works functionally, just not with the requested control flow.

**2. `remove_student` — Mutating while iterating (Conceptual bug)**
```python
for student in databook:
    ...
    databook.remove(student)
```
You found the student, removed them, and `return`ed immediately. Because you exit the function right after removal, this happens to work here. But this is the same dangerous pattern from D2. The safe way:
```python
for i, ((name, roll), scores) in enumerate(databook):
    if roll == target_roll:
        del databook[i]
        return print(f"Removed {name} ({roll}) successfully.")
```

**3. Variable shadowing bug**
```python
name = input("Enter the student Name: ")
...
for index, ((name, roll), scores) in enumerate(data):
```
The `name` in the loop shadows the outer `name`. If a student exists, you return before using `name` again, so it doesn't break here — but it's dangerous and confusing.

**4. Typos**
- `"Gradbook is empty"` → `"Gradebook is empty"`
- `"alredy Exist"` → `"already exists"`

---

**Section 3 Score: 16/20**

---

"""

             


    


    

    



    


