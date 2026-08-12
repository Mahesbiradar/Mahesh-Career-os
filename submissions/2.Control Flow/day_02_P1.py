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
# ### Hard (8–10)

# **Q8.** If you use `break` inside an inner loop, which loop(s) does it terminate? Describe two different techniques to break out of *multiple* nested loops from the innermost loop.

"""
When you use a break statement inside an inner loop, it terminates only the innermost loop that currently contains it. The outer loops will continue running exactly where they left off

Technique 1: Using a Flag Variable (Boolean Flag)
This is a universal approach across almost all programming languages. You set a boolean variable to True inside the inner loop, break the inner loop, and then check that flag in the outer loops to break them as well.
Technique 2: Extracting Logic into a Function with return
This is often considered the cleanest and most "Pythonic" approach. By wrapping your nested loops inside a dedicated function, a single return statement immediately halts all execution inside the function, effectively breaking out of every loop level instantly.

"""

# **Q9.** The `for-else` pattern is famously used for "search" loops. Explain how it works: what executes if the loop finds what it's looking for (and uses `break`), versus what executes if the loop finishes naturally without finding anything?
"""
The for-else pattern works by treating the else block as a conditional branch that only runs if the loop completed its natural lifecycle. Think of it as a "did not hit a break" block.

Scenario 1: The loop FINDS the item (Hits break)When the loop successfully finds the target item and executes a break statement:The loop terminates immediately.The program skips the else block entirely.Execution moves directly to the code below the for-else structure.
Scenario 2: The loop FINISHES naturally (No break)When the loop searches through the entire iterable but never finds the target item:The loop finishes running its last iteration naturally.The program instantly executes the code inside the else block.

"""

# **Q10.** You need to iterate over two lists simultaneously, keep track of the iteration count, and skip to the next pair when a certain condition is met (without exiting the loop). Which control flow tools would you combine, and what would the loop structure look like conceptually?

"""
To solve this, you would combine three control flow and sequence-handling tools: zip(), enumerate(), and continue.The Combined Toolszip(): Pairs the items of the two lists together so you can iterate over them simultaneously.enumerate(): Wraps the zipped pairs to automatically generate and track the iteration count (index).continue: Skips the rest of the code block for the current iteration and immediately moves to the next pair when your condition is met.Conceptual Loop Structure

list_one = ["A", "B", "C", "D"]
list_two = [10, 20, 30, 40]

# Wrap the zipped lists inside enumerate to track the count
for count, (item_one, item_two) in enumerate(zip(list_one, list_two)):
    
    # 1. Define the skip condition
    if item_two == 20: 
        print(f"Skipping index {count}...")
        continue  # Skips directly to the next pair (C, 30)
        
    # 2. Process the valid pairs here
    print(f"Index {count}: Processing {item_one} with {item_two}")

"""









