
## 🔥 Targeted Weak-Area Assessment

**Don't run the code. Don't look at notes.**
Answer from memory.

### Part A — Quick Concept Check

**Q1.** In one or two sentences, explain the difference between:

```python
raise ValueError("Invalid age")
```

and

```python
except ValueError:
```

---
# Ans: The raise statement raises/generates the Exception ValueError in above mentioned code and the except ValueError Caches/Handles the ValueError.


**Q2.** Which exception will be caught?

```python
class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong")
except Exception:
    print("A")
except MyError:
    print("B")
```

What is printed, and **why**?

---
# Ans: Here the except Exception will be caught. 
A
is printed and the base exception caught erlier than the custome exeption therefor the base exception prints A and second execpt doent executes.

**Q3.** What is wrong with this ordering?

```python
try:
    ...
except Exception:
    ...
except FileNotFoundError:
    ...
```

How should it be ordered?

---
# Ans: order of the exceptions catching is wrong in above code is wrong.If we catch bases exeption then no other exceptions will be executed any other exeption after the base exeption.

try:
    ...
except FileNotFoundError:
    ...
except Exception:
    ...
### Part B — Exception Flow

**Q4.** What is the output?

```python
try:
    raise ValueError("Bad value")

except TypeError:
    print("Type")

except ValueError:
    print("Value")

finally:
    print("Done")
```

---
# Ans: 
Value
Done



**Q5.** What happens here?

```python
class PaymentError(Exception):
    pass

try:
    raise PaymentError("Payment failed")

except ValueError:
    print("Value error")
```

Does the program print anything? What happens to `PaymentError`?

---
# Ans:
if we consider the above program then it will not print anything bcz we have raised the PaymentError but we havend handeled this exception therefor and we have one more exception which is valueError from the perspective of above code we have not generated the valueError Exception therefor the except Volue Error block not executes.

### Part C — The Important Loop Problem

**Q6.** Consider:

```python
numbers = ["10", "20", "abc", "40"]

try:
    for number in numbers:
        value = int(number)
        print(value)

except ValueError:
    print("Invalid number")
```

What exactly gets printed?

Then explain **why `40` is never processed**.

---

# Ans:
10
20
Invalid number

here in above code after the two iternation on 2nd index we while conversting string abc to interger is invalid and Therfore the ValueError Exception occures and loop terminates Here and 40 is never processed.

**Q7.** Now look at:

```python
numbers = ["10", "20", "abc", "40"]

for number in numbers:
    try:
        value = int(number)
        print(value)

    except ValueError:
        print("Invalid number")
        continue
```

What gets printed?

Explain the **difference in exception scope** between Q6 and Q7.

---
# Ans:

10
20
Invalid number
40

Here the diffrence b/w the exception scope b/w q6 and q7 is in q7 if we get any invalid condition will terminateds the loop by raising and handling exception but whereas in the q7 we raise the exception and hadles by skipping the invalid iteration in loop and continues the loop.

### Part D — Custom Exception

**Q8.** Complete this:

```python
class InsufficientBalanceError(________):
    pass
```

What should go inside the parentheses?

Then explain **why**.

---
# Ans:

Exception 

should go inside the parentheses

The Exception class is base class where the cutome class inherits.


**Q9.** Write a function:

```python
def withdraw(balance, amount):
    ...
```

Requirements:

* If `amount <= 0`, raise an appropriate exception.
* If `amount > balance`, raise a custom `InsufficientBalanceError`.
* Otherwise return the remaining balance.

You don't need to handle the exceptions inside the function.

---
# Ans:

balance = some amoutnt
def InsufficientBalanceError(Exception):
    Pass

def withdraw(balance, amount):

    balance -= amount

    return balance

try:
   withdrwarl_amount = input("Enter the Amount:")

   if withdrwarl_amount == 0:
        raise ValueError

   if  withdrwarl_amount > balance:
        raise InsufficientBalanceError("Insuficient amount")
except InsufficientBalanceError as e:
    print(e)

except ValueError:
    Print("Amout shoud be greter Than Zero")

else:
    balance = withdraw(balance,withdrwarl_amount)


### Part E — Final Interview Trap 🎯

**Q10.**

You are processing **10,000 records**:

```python
for record in records:
    process(record)
```

One record may contain invalid data.

Which structure is better?

### A

```python
try:
    for record in records:
        process(record)
except ValueError:
    continue
```

### B

```python
for record in records:
    try:
        process(record)
    except ValueError:
        continue
```

Choose **A or B**, and explain **exactly why**.

---
# Ans :

Here ill choose B as better structure for Processing 10,000 records. bcz if choose structure a it may simply exits the processing if any invalid conidtion occurs but if we choose option b it will skip the invalid record and continue Processing other records.

### ⏱️ Target

This should take you around **10–15 minutes**.

Send me **Q1–Q10**. I'll grade only these weak areas and tell you whether the gaps are now closed.




One Last 2-Minute Challenge

I don't want to give you another 10-question assessment. Just solve this one because it directly targets Q9.

Challenge

Write only these two things:

class InsufficientBalanceError(Exception):
    ...

and:

def withdraw(balance, amount):
    ...

Requirements:

amount <= 0 → ValueError
amount > balance → InsufficientBalanceError
valid withdrawal → return remaining balance
Do not use try/except inside withdraw()

That's your final check.



class InsufficientBalanceError(Exception):
    Pass


def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("The amopunt canot be less than or eqal to Zero")
    
    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance to withrdwa")
    
    return balance - amount

in erlier Challenge i thought i shoud raise and catch the exception outside the functions thats why i written the same.



