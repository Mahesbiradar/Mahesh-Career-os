# 🐍 Python Revision Session: Variables, Data Types, and Operators
# Great choice! We'll go section by section. Please answer the 10 questions below, and I'll check each one, explain any mistakes, and then we'll move to coding assignments.

# Section 1: 10 Questions (Easy → Medium → Hard)
# 🔹 Easy
# Q1. What is the data type of x = 5? What is the data type of y = 5.0? Name the built-in function you would use to check the type of a variable at runtime.
# ans:- data type of x = 5 is integer. data type of y = 5.0 is float  the built in function to check the type of variable is 'type(variable)'. 
# Q2. Explain the difference between = and == in Python. What does each one do?
#ans: = is the assignment operator and == is to check the equality. = is used to assign the value and == is used to check the equality.
# Q3. What does the // operator do? How is it different from /? Give a one-line example showing both.
#ans: (//) operator is used for floor division. floor division return the whole number and division returns the floot number. 5/2 = 2.5(decimal) 5//2 = 2 whole number.

# 🔸 Medium

# Q4. What happens when you run "5" + 5 in Python? Why does it happen? Show two different ways to modify this expression so that the result is the integer 10.
#ans:python raiser the typeerror bcz "5" is the string and 5 is the int and int cannot be concatinated with string.  one way is to make by type conversion making sting to int int("5") second way is by removing the double qoutes.
# Q5. What is the output of 3 ** 2 ** 1? Explain the operator precedence rule that determines this result.
#:ans o/p: 9, right-to-left associativity rule for exponentiation.
# Q6. After running the following code, what are the final values of a and b?
# Python
# a, b = 5, 10
# a, b = b, a
#ans: a = 10 b = 5
# Q7. What is the difference between is and ==? Give a concrete example in Python where == returns True but is returns False.
# # is used for to check the identity and == is used to check the equality and membership. 
# ex:
# a = [1,2,3]
# b = [1,2,3]

# print(a == b)
# print(a is b)
#Explanation everying in python is object here a is stored specific locationa and b is stored as another location so == is checking the equality and membership and is checking identity meand both belongs to same memory location or not.

# 🔺 Hard
# Q8. What is the result of True + True + False? Explain why Python produces this result (think about how booleans relate to numbers).
#ans: o/p 2, in python the boolen True equals to 1 and false equals to 0 Therefor the pythone interpret T+T+F as 1+1+0=2
# Q9. Consider this code:
# Python
# x = [1, 2, 3]
# y = x
# y[0] = 10

# What is x[0] after this runs? What underlying concept (related to variables and memory) explains this behavior? If you wanted y to be an independent copy of x, how would you create it?
#ans: X[0]=10 , Here x has the reference of the list and y also pointing to the same list therefor changing any y[0] or any other index will modify the origina list. if a wanter y to be independent then ill use sliciong method to copy the list y = x[:] or ill use method y = x.copy().

# Q10. What is the output of ~5 in Python? Explain how the bitwise NOT (~) operator works, and why the result is not simply -5 but something else.

#ans: The output of ~5 in Python is -6. The ~ operator flips all binary bits (1s become 0s, 0s become 1s).Two's Complement: Python uses this system to store negative numbers, where the flipped bits represent -6. It is not -5 because flipping all bits changes the number's magnitude, not just its positive/negative sign.



# Section 2: 3 Coding Assignments

"""
🔹 Easy — "Type Showcase & Conversion"
Create a single Python script that:
Creates 5 variables: one each of int, float, str, bool, and complex.
Prints each variable and its type using type().
Demonstrates explicit type conversion (where logically possible):
Convert the float → int
Convert the int → float
Convert the bool → int
Convert the int → str
Print the results.
"""

# 1. Create 5 variables of different types

a = 10
b = 5.2
c = "Mahesh"
d = True
e = complex(2,4)

# 2. Print each variable and its type using type()

print(f"{a} is {type(a)}")
print(f"{b} is {type(b)}")
print(f"{c} is {type(c)}")
print(f"{d} is {type(d)}")
print(f"{e} is {type(e)}")

# 3. Explicit type conversion

float_to_int = int(b)
int_to_float = float(a)
bool_to_int = int(d)
int_to_str = str(a)

# 4. Print the conversion results
print(float_to_int)
print(int_to_float)
print(bool_to_int)
print(int_to_str)

"""
🔸 Medium — "Digit Extractor"
Write a program that:
Takes a 3-digit positive integer (e.g., 472) and stores it in a variable.
Uses only arithmetic operators (//, %, *, +, etc.) to extract the hundreds, tens, and units digits into separate variables.
Prints each digit on a new line.
Reconstructs the reverse number (e.g., 274) using only operators and prints it.
Constraints: No string indexing, no str(), no loops, no lists.

"""


number = 472

hundreds = number // 100

tens = (number % 100)//10

units = number % 10

print("Hundreds digit:", hundreds)
print("Tens digit:", tens)
print("Units digit:", units)

reversed_number = ((units*100) + (tens*10) + hundreds)

print("Reversed number:", reversed_number)

"""
🔺 Hard — "Safe Expression Evaluator"
Write a program that:
Takes three inputs from the user: num1, operator, num2.
Example: num1 = 15, operator = "//", num2 = 4
Based on the operator string, performs the correct arithmetic operation using only variables and operators (no eval(), no exec()).
Must handle: +, -, *, /, //, %, **
Includes basic error handling: if the user enters an invalid operator, print "Unsupported operator". If division by zero occurs, print "Cannot divide by zero".
Prints the result rounded to 2 decimal places if it's a float.
Constraints: No eval(), no functions (def), no loops. Use only if/elif/else and variables.

"""

# num1 = float(input("Enter first number (num1): "))
# operator = input("Enter operator (+, -, *, /, //, %, **): ").strip()
# num2 = float(input("Enter second number (num2): "))


# result = None 

# error_message = ""

# if operator in ("/", "//", "%") and num2 == 0:
#     error_message = "Cannot divide by zero"
# elif operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     result = num1 / num2
# elif operator == "//":
#     result = num1 // num2
# elif operator == "%":
#     result = num1 % num2
# elif operator == "**":
#     result = num1 ** num2
# else:
#     error_message = "Unsupported operator"

# if error_message:
#     print(error_message)
# else:

#     result = round(result,2)

#     if result == int(result):
#         print("Result:", int(result))
#     else:
#         print("Result:", result)





