# Q1 — File + Exception Coding
"""
Write:

def read_numbers(filename):
    ...

Requirements:

Open the file using with
File contains one integer per line
Return a list of integers
Handle FileNotFoundError
Handle invalid integer data using ValueError
Don't allow the function to crash because of bad input

Example file:

10
20
30
abc
40

You decide what sensible behavior should happen when abc is encountered, but explain your decision.

"""

def read_numbers(filename):

    valid_integers = []

    try:

        with open(filename,"r") as file:

            list_lines = file.readlines()

            for index,line in enumerate(list_lines):

                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                try:
                    number = int(cleaned_line)       

                    valid_integers.append(number)

                except ValueError:
                    print(f"Warning: Invalid data '{cleaned_line}' on line {index + 1} skipped.")
                    continue

            return valid_integers

    except FileNotFoundError as e:
        print(f"Error: The file '{filename}' does not exist.")
        return []


filename = r"abc.txt"

print(read_numbers(filename))



# Skip and Log:
"""
when an invalid entry like "abc" encountered, the function catches the valueerror prints the warning message on console indicating the exact line number and uses continue to skip it. 
The function continue processing the rest of the file.

In real word data processing a single currupted line shoud not cause the entire program to crash or throw away the rest of the valid data. preserving the good data and skipping the inavlid entry balances the data recovery with clear error logging so the user knows exctly which line need fixing.

"""


# Q2 — Custom Exception

"""
Create:

class InsufficientBalanceError(Exception):
    pass

Then create:

class BankAccount:

Requirements:

deposit(amount)
withdraw(amount)

If withdrawal exceeds balance:

raise InsufficientBalanceError(...)

Then demonstrate handling that exception using try/except.

"""

class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self,name,balance):

        self.name = name
        self.balance = balance


    def deposit(self,amount):

        if amount <= 0:
            print("The Negative or zero amount cannot be deposited")
        else:
            self.balance += amount
            print(f"Successfully Deposited ${amount}. New balance: ${self.balance}")


    def withdraw(self,amount):

        if amount > self.balance:
            raise InsufficientBalanceError("The balance in your account is insufficient to Process this request")

        self.balance -= amount
        print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")
        

account = BankAccount("Mahesh",2000)

print(account.name)
print(account.balance)

account.withdraw(10)

try:

    print("Attempting to withdraw.....")

    account.withdraw(2500)

except InsufficientBalanceError as e:

    print(f"Transaction Denied: {e}")



# Q3 — OOP Challenge

"""
Create:

class Employee

with:

name
salary

Create:

class Developer(Employee)
class Manager(Employee)

Requirements:

Both inherit from Employee
Both override:
work()
Developer.work() prints something developer-related
Manager.work() prints something manager-related
Use super() somewhere meaningfully
Create objects and demonstrate polymorphism using a loop
"""

class Employee:

    def __init__(self,name,salary):

        self.name = name
        self.salary = salary

    def work(self):

        print("Employee works")



class Developer(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} is a Developers and  write the code, build the features, and turn ideas into working software.")



class Manager(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} is Managers and coordinate the team, remove roadblocks, and make sure everyone has what they need to succeed.")



m1 = Manager("Mahesh",2000)
m2 = Manager("Santosh",3000)

d1 = Developer("Rahul",1000)
d2 = Developer("Som",1500)


employees =[m1,d1,m2,d2]

for employee in employees:
    print(f"Name: {employee.name}")
    employee.work()
    print("-" * 20)


# Q4 — Debugging

"""
What's wrong here?

class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def increase_salary(self, amount):
        self.salary += amount

The developer wants to increase one employee's salary.

Identify the problem and fix it.

"""
# Ans:

# In the above code the increase_salary is a class method we use a class methods to alter the class level attributes but the devoloper wants to increase the salary for one empployee and salary is intance variable.

# To change the state of instance varibale we shoude use the instance method by removeing the line @classmethod we can fix the above code. Where salary will be chnages on employees developer wants using the the method.

#Corrected Code:

class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount


# Q5 — Debugging

"""
What's wrong here?

class Parent:

    def __init__(self):
        self.value = 10


class Child(Parent):

    def __init__(self):
        self.value = 20
        super().__init__()

After:

obj = Child()
print(obj.value)

what happens?

Is super() being used incorrectly? Explain precisely.

"""
# Ans:

# Yes in above code super is used incorrectly in child classes we shoud use super before any child specific state is intialized.

# in above code when the obj is created using the child class it intially intializes the object state using __init__ and this menthod consist of value attribute and it has value 20.

# Then the next line is super().__init__() when this is called. this jumps to parent class constructur inside the paremt __init__ the self.value = 10 executes. because self refers to the exact same object 10 oviriddes the 20 we just set.

# if we want the child value to be 20 as the final we must always call super().__init__() first before defining child specific attributes.

# corrected code:

class Parent:

    def __init__(self):
        self.value = 10


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.value = 20


obj = Child()
print(obj.value)


# Q6 — Output Prediction

"""

Predict the exact output:

class A:

    value = 10

    def __init__(self):
        self.value = 20


class B(A):

    value = 30

    def __init__(self):
        super().__init__()


a = A()
b = B()

print(A.value)
print(a.value)
print(B.value)
print(b.value)

Then explain the lookup/instance behavior.

"""

# Ans:

# 10
# 20
# 30
# 20

# Here in above code the Class a has class variable value and it value is 10 but when the objects were creted using this class the object also has same attribute value and its value is 20 so the class variable value is overidded for intance atrribute value.Employee

# and class b inherts from class a and class b also oviriddes the class variable value with value 30 and when the object is created using the class b  when super() is called durning object state intialization it jumps to parent class __init__ and it has its own attribute called value and value is 20 Therefor objects created using b also has value = 20.


# Q7 — Output + MRO

# Predict:

class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(A):

    def show(self):
        print("C")
        super().show()


class D(B, C):
    pass


obj = D()
obj.show()


"""
Give:

Exact output
D's MRO
Explain why super() behaves the way it does.

"""

# Ans =:

B
C
A

# The MRO of Class D is: D -> B -> C -> A -> object

"""
When we call obj.show() python starts walking throw D's MRO Chain.

1.step 1 it looks at D. D doesnt have show(), so it passes the call to next class in the MRO:B
2.Step 2 B.show() runs and prints B.
3.Step 3 inside B.Show(), super().show() is encountered.pythin looks the MRO chain realative to the original object(D). The Class after B in D's MRO is C. Therfor it jumps to C.show()
4.Steo 4 C.show() runs and prints C.
5.Step 5 inside C.show(), super().show() is called. The class after C in D's MRO is A.
6.Step 6: A.show() runs, prints A, and the execution chain finishes

"""

# This is what i learned when i confused intially i thought MRO visits B and using super visits A and then C and A. lIKE WISE BUT READING Above i reminded prev MRO chain.

# the above given steps are written with help of seen answer.


# Q8 — Mini Project 🧩

"""
Build a small Employee Management System.

Your system should have:

Employee
Developer
Manager

Requirements:

Employee
name
employee_id
salary
Developer

Additional:

language
Manager

Additional:

team_size
Methods

Every employee should have:

display_info()
calculate_bonus()

Use overriding so that developers and managers can have different bonus calculations.

Also:

Use inheritance
Use super()
Demonstrate polymorphism
Use a custom exception called:
InvalidSalaryError
Reject negative salary
Store multiple employees in a list
Iterate over them and call the same methods

This is the main integration problem for today's revision.

"""

class InvalidSalaryError(Exception):
    pass



class Employee:

    bonus_percentage = 0.10

    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        if salary < 0:
            raise InvalidSalaryError("Initialization Failed: Salary cannot be negative. Received: {salary}. Please enter a positive amount or 0 for unpaid positions.")
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: {self.salary}")

    
    def calculate_bonus(self):
        return self.salary*self.bonus_percentage


class Developer(Employee):

    bonus_percentage = 0.20


    def __init__(self, name, employee_id, salary,language):
        super().__init__(name, employee_id, salary)
        self.language = language


    def display_info(self):
        super().display_info()
        print(f"Language: {self.language}")

    def calculate_bonus(self):
        return self.salary * self.bonus_percentage
    

class Manager(Employee):

    bonus_percentage = 0.30

    def __init__(self, name, employee_id, salary,team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size


    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")

    def calculate_bonus(self):
        return self.salary * self.bonus_percentage


    
employee_data = [
    {"type": "Developer", "name": "Rahul", "id": "DEV101", "salary": 75000, "extra": "Python"},
    {"type": "Manager", "name": "Mahesh", "id": "MGR201", "salary": 95000, "extra": 8},
    {"type": "Developer", "name": "Som", "id": "DEV102", "salary": -12000, "extra": "Java"}, # ⚠️ Trapped!
    {"type": "Manager", "name": "Santosh", "id": "MGR202", "salary": 110000, "extra": 15}
]

employees = []


print("=== STEP 1: INITIALIZING EMPLOYEES ===")



for data in employee_data:

    try:

        if data["type"] == "Developer":
            emp = Developer(data["name"], data["id"], data["salary"], data["extra"])
        elif data["type"] == "Manager":
            emp = Manager(data["name"], data["id"], data["salary"], data["extra"])

        employees.append(emp)

        print(f"Successfully added {data['type']}: {data['name']}")

    except InvalidSalaryError as e:
        print(f"❌ Skipped {data['name']}: {e}")
        continue

print("\n=== STEP 2: RUNNING POLYMORPHISM REPORT ===")


for emloyee in employees:
    emloyee.display_info()
    bonus = emloyee.calculate_bonus()
    print(f"Calculated Bonus: ${bonus:,.2f}")
    print("-" * 30)


# Note the main logic and all program is build by me but the statements in print i have used Ai for better Messagges.
    

# Q9 — Interview

"""
Answer this as if I'm interviewing you:

"What is the difference between inheritance and composition? When would you prefer composition?"

Don't give a textbook definition only. Give a backend-oriented example.

"""
# To answer above question i have not come across the composition as of now. 

# About inharitance where the child classes inherits the data and methods from the parent class.

# Here i need to work or do one thing keep one small session on this to explain composition and then  diff b/w comp and inhe


# Q10 — Interview

"""
Answer:

"Explain the four major OOP concepts in Python: encapsulation, abstraction, inheritance, and polymorphism."

You have to clearly distinguish encapsulation vs abstraction this time.

"""

# Ans:

# encapsulation : is practice of bundeling data and methods that operate on that data inot a single unit called class and controlling the state aceess of the object.
# The main goal is data security and integrity.

# abstraction : Hinding complexity
# Exposing the essesntials while hinding the actull implementation. the goal is complexity reduction It allows the user to know what the object does without needing to know how it does it.

# inheritance : Code Reuse
# Allows new class to adopt the attributes and methods of an existing class. this eliminates redundant code and creates a natural "Is-A" hierarchy.


# polymorphism : Many formns one interface:
# Is a method which provides a same inteface to the objects which have diffrent behaviour.This allows a single, unified interface to handle different types of objects.









   
