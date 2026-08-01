#  Here are your **10 Control Flow revision questions**. Answer them in any format you like — short explanations, code snippets, or bullet points. I'll check each one, explain any mistakes, and then we'll move to the coding assignments.

# ---

# ### Easy (1–3)

# **Q1.** What is the key difference between using multiple independent `if` statements versus using an `if-elif-else` chain? In what situation does this distinction actually change the output?

# **Q2.** What are the start, stop, and step values when you call `range(2, 10, 2)`? Write out the exact sequence of numbers it generates.

# **Q3.** In a `while` loop, what happens if the condition never becomes `False`? Name one practical technique to prevent accidental infinite loops when reading user input or processing data.

# ---

# ### Medium (4–7)

# **Q4.** Explain the difference between `break` and `continue` using a single conceptual loop example (you can describe it in words; no need for full code). What happens to the current iteration in each case?

# **Q5.** What is the purpose of the `else` block attached to a `for` or `while` loop? Under what exact condition does it execute, and under what exact condition does it get skipped?

# **Q6.** What problem does `enumerate()` solve that a plain `for` loop does not? Write a single line of Python showing how to iterate over a list `names = ["Alice", "Bob", "Carol"]` using `enumerate()` to access both the index and the value.

# **Q7.** What does `zip()` do when given two lists of different lengths? Name the function from the `itertools` module that allows you to iterate until the *longest* iterable is exhausted instead of the shortest.

# ---

# ### Hard (8–10)

# **Q8.** If you use `break` inside an inner loop, which loop(s) does it terminate? Describe two different techniques to break out of *multiple* nested loops from the innermost loop.

# **Q9.** The `for-else` pattern is famously used for "search" loops. Explain how it works: what executes if the loop finds what it's looking for (and uses `break`), versus what executes if the loop finishes naturally without finding anything?

# **Q10.** You need to iterate over two lists simultaneously, keep track of the iteration count, and skip to the next pair when a certain condition is met (without exiting the loop). Which control flow tools would you combine, and what would the loop structure look like conceptually?


# ### Easy (1–3)

# **Q1.** What is the key difference between using multiple independent `if` statements versus using an `if-elif-else` chain? In what situation does this distinction actually change the output?

"""
Ans: the key diffrence is the independent if statement check every contion. while an if_elif_else chain stops checking as soon as it finds one true condition.
When a single input satisfies more than one condition, multiple if statements will execute multiple blocks, whereas an if-elif chain will only execute the first matching block
"""
# **Q2.** What are the start, stop, and step values when you call `range(2, 10, 2)`? Write out the exact sequence of numbers it generates.

"""
start value will be 2 the loop stops at after 8 because the stoping value is excluded and step value is 2 .
2
4
6
8
"""
# **Q3.** In a `while` loop, what happens if the condition never becomes `False`? Name one practical technique to prevent accidental infinite loops when reading user input or processing data.

"""
In while loop if condition never becomes False the loop enters into infinite loop. We can use the break with specific condition to prevent the infinite loop or 1. Input Validation with a Maximum Attempt Counter.

"""

# ### Medium (4–7)

# **Q4.** Explain the difference between `break` and `continue` using a single conceptual loop example (you can describe it in words; no need for full code). What happens to the current iteration in each case?
"""
The Break statement is used to exit the loop whereas the continue is used to skip the current iteration.
ex: In specific if in program there is condition under that condition break is used if that condition becomes true then loop is exited. in continue its will skip all the thing after the continue statement and jumps to the next iteration.
"""

# **Q5.** What is the purpose of the `else` block attached to a `for` or `while` loop? Under what exact condition does it execute, and under what exact condition does it get skipped?

"""
The purpose of the else block attached to a for or while loop is to execute code only if the loop completed its cycle naturally without being prematurely to stop.

The else block executes if: the loop finishes all its iterations naturally(for a for loop),The loop condition becomes False (for a while loop).The loop never runs at all (e.g., iterating over an empty list or a while condition that is False from the start).

The else block is skipped if:The loop is terminated prematurely by a break statement. An exception (error) is raised inside the loop that halts execution. A return statement is executed inside the loop (if the loop is inside a function).

"""

# **Q6.** What problem does `enumerate()` solve that a plain `for` loop does not? Write a single line of Python showing how to iterate over a list `names = ["Alice", "Bob", "Carol"]` using `enumerate()` to access both the index and the value.

"""
using the enumerate() we can access both tyhe index and the value of that element where as in plain for loop we can access one of those index or value.

for index,value in enumerate(names):

"""

# **Q7.** What does `zip()` do when given two lists of different lengths? Name the function from the `itertools` module that allows you to iterate until the *longest* iterable is exhausted instead of the shortest.

"""
When given two lists of different lengths, the standard zip() function stops iterating as soon as the shortest list is completely exhausted. Any remaining elements in the longer list are completely ignored and cut off.
To iterate until the longest iterable is exhausted, use the zip_longest() function from the itertools module.
"""





