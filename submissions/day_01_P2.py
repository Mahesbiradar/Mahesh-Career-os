"""

## Section 4: 5 Debugging Questions

For each snippet, **identify the bug**, **explain why it happens**, and **provide the corrected code**.

**D1.**
```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2
print("Sum is:", sum)
```
*User enters 10 and 20. Expected output: `Sum is: 30`. What goes wrong?*

**D2.**
```python
a, b = 10, 20
mean = a + b / 2
print("Mean:", mean)
```
*Expected output: `Mean: 15.0`. What is actually printed?*

**D3.**
```python
x = 5
if x = 5:
    print("x is five")
```
*What error does this produce?*

**D4.**
```python
score = 100
score =+ 10
print("Final score:", score)
```
*The programmer expected `110`. What is actually printed?*

**D5.**
```python
total = 257
subjects = 3
average = total // subjects
print("Average marks:", average)
```
*Expected a precise average like `85.666...`. What is printed instead?*

---

## Section 5: 5 Output Prediction Questions

Predict the exact output of each code snippet. **Explain your reasoning.**

**P1.**
```python
x = 5
y = 2.0
z = x / y
print(type(z))
```

**P2.**
```python
a = 3
b = 2
print(a ** b ** 2)
```

**P3.**
```python
x = 10
y = x
x += 5
print(y)
```

**P4.**
```python
print(0.1 + 0.2 == 0.3)
```

**P5.**
```python
a = [1, 2]
b = a
a = a + [3]
print(b)
```

---

## Section 6: 5 Interview-Style Questions

**I1.** What is the difference between **mutable** and **immutable** data types in Python? Give two examples of each.

**I2.** Python caches small integers (typically -5 to 256). What does this mean, and why does the following behave the way it does?
```python
a = 257
b = 257
print(a is b)   # What does this print? Why?
```

**I3.** What is the difference between using `//` (floor division) and `int()` to convert a float to an integer? Give an example where they produce **different** results.

**I4.** Why is `eval()` dangerous when processing user input for arithmetic operations? What safer alternatives would you use?

**I5.** Python is **dynamically typed**. What are the practical advantages and disadvantages of this compared to a statically typed language like Java or C++?

---

**👉 Type your answers for Sections 4, 5, and 6 below. I'll check everything, give you your final score, weak areas, revision plan, and readiness verdict!**

"""


## Section 4: 5 Debugging Questions

"""For each snippet, **identify the bug**, **explain why it happens**, and **provide the corrected code**.

# **D1.**
# ```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2
print("Sum is:", sum)
```
# *User enters 10 and 20. Expected output: `Sum is: 30`. What goes wrong?*"""

#ans: both num1 and num2 the user inputs will be string bcz the input always return string therefor we have to covert the input to int to make working code.

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# sum = int(num1) + int(num2)
# print("Sum is:", sum)


"""
D2.

a, b = 10, 20
mean = a + b / 2
print("Mean:", mean)

Expected output: Mean: 15.0. What is actually printed?

"""
# The output of the above code will be Mean: 20.0. bcz the division has the higher precendece than the + therfor 10 + (20/2) = 10+10=20 to make this correct we have to add parenthesis (a+b)/2

a, b = 10, 20
mean = (a + b) / 2
print("Mean:", mean)

"""
D3.
x = 5
if x = 5:
    print("x is five")
What error does this produce?

"""
# ans: This will produce the synatax error bcz the = is assignement operator if we need to check the equality we shoud use == .

x = 5
if x == 5:
    print("x is five")

"""
D4.

score = 100
score =+ 10
print("Final score:", score)
The programmer expected 110. What is actually printed?

"""
# ans: The printed value is 10 bcz python interpret =+ as = and + both as seperate operatod = as assignment and + as positive number there for the intial value 100 is overriten by 10

score = 100
score += 10
print("Final score:", score)

"""
D5.
Python
total = 257
subjects = 3
average = total // subjects
print("Average marks:", average)
Expected a precise average like 85.666.... What is printed instead?

"""
#The printed output is 85 bcz in above code the floor division is used and floor devision retuns only the devisor part it ignores the decimal(remainder part) to print precise average we shoud use / division operator
total = 257
subjects = 3
average = total / subjects
print("Average marks:", average)


# Section 5: 5 Output Prediction Questions

# Predict the exact output of each code snippet. Explain your reasoning.

"""
P1.
Python
x = 5
y = 2.0
z = x / y
print(type(z))
"""
# ans:<class 'float'> the division operator produces the precise value including the Decimal part also There for x/y produces the float value.

"""
P2.
Python
a = 3
b = 2
print(a ** b ** 2)
"""
# ans: 81  the precedence operates from right to left because the exponentiation operator (**) is right-associative. therfor 3**(2*2)= 3*3*3*3= 81

"""
P3.
Python
x = 10
y = x
x += 5
print(y)
"""
# ans: 10  bcz y and x are referring to same object 10 and once x +=5 is evaluated int are immutable in python therefor python evaluated x +=5 which is 15 and created new object 15 and x referese to objcet 15 now but y still refering to the old object 10

"""
P4.
Python
print(0.1 + 0.2 == 0.3)

"""

# ans: False im not sure about the resoning since python calcukated 0.2 + 0.3 = 3000000000004 which is sloghlty larger than 3 there for is produces false.

"""
P5.
Python
a = [1, 2]
b = a
a = a + [3]
print(b)

"""
#ans [1, 2] b still refering to old list [1, 2] in the expression a = a +[3] the + operator cretes fresh list and a referencing the new list a = [1, 2, 3]


"""
Section 6: 5 Interview-Style Questions
I1. What is the difference between mutable and immutable data types in Python? Give two examples of each.
I2. Python caches small integers (typically -5 to 256). What does this mean, and why does the following behave the way it does?
Python
a = 257
b = 257
print(a is b)   # What does this print? Why?
I3. What is the difference between using // (floor division) and int() to convert a float to an integer? Give an example where they produce different results.
I4. Why is eval() dangerous when processing user input for arithmetic operations? What safer alternatives would you use?
I5. Python is dynamically typed. What are the practical advantages and disadvantages of this compared to a statically typed language like Java or C++?
"""
"""
## I1. Mutable vs. Immutable

* Difference: Mutable objects can change their content in-place without altering their memory address. Immutable objects cannot be changed; modifying them creates a completely new object in memory.
* Mutable Examples: list, dict
* Immutable Examples: int, str

## I2. Integer Caching & is Comparison

* Meaning: Python pre-creates integer objects from -5 to 256 in memory to save time. Any variable assigned in this range points to the exact same object.
* Output: False
* Why: 257 falls outside the cached range. Python creates two distinct object instances with different memory addresses. The is operator checks identity (memory location), so it returns False.

## I3. // (Floor Division) vs. int()

* Difference: // rounds down toward negative infinity. int() truncates the decimal part, moving toward zero.
* Divergent Example: Using -3.5
* -4 / 2 or -3.5 // 1 evaluates to -4.0 (rounded down).
   * int(-3.5) evaluates to -3 (truncated).

## I4. eval() Danger & Alternatives

* Danger: eval() executes arbitrary string input as Python code. Malicious users can exploit this to run unauthorized commands or wipe your file system.
* Safer Alternatives: Use ast.literal_eval() for safely parsing basic literals, or a dedicated math parsing library like sympy.

## I5. Dynamic vs. Static Typing

* Advantages: Faster prototyping, cleaner code with fewer boilerplate declarations, and higher flexibility since functions can accept any object type.
* Disadvantages: Type errors are caught at runtime instead of compile time, code completion (IDE) is less precise, and execution is generally slower due to runtime type-checking overhead.

"""




