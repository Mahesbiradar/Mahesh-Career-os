
---

# Section 1 — Concept Questions

## Easy

### Q1. Function Basics

What is a function in Python?

Explain:

* Why we use functions.
* `def`
* Parameters
* Arguments
* `return`

Give a simple example.

---

## Ans: Function in python allows us to reduce the code redundancy which mean we can eliminate code duplicacy using the function suppose are are doing same thing to do a specific task as multile locations in a problems instead of writing same code multiple time we simply write a function defined by def and then function name and followed by parenthisis for the paratmeters and colun so by defining the funtion we can call the function to do a task at multiple locations in program no need to write the entire code block.

The 'def' keyword tell the python that this is the function defination. 
Parameteres are the inputs for the function which we use to process or to do a specific task. and parameeters are definded in the function defination.
arguments are the inputs we pass while calling the function.
The function return the value which we can use to assign that value to new variable to process further in program.


### Q2. Parameters vs Arguments

What's the difference between a **parameter** and an **argument**?

Consider:

```python
def greet(name):
    return f"Hello {name}"

greet("Mahesh")
```

Identify the parameter and argument.

---
## Ans:
Parameteres are the objects defined in the function defination and arguments are the actully inputs or function which we pass to function as inputs.
Here in above example the name in function defination is the parameter.
and the "Mahesh" while calling the greet function is the argument.

### Q3. `return` vs `print`

What's the difference between:

```python
def add(a, b):
    print(a + b)
```

and

```python
def add(a, b):
    return a + b
```

Why is `return` generally more useful when building reusable functions?

---
## Ans: The basic diff b/w the print and the return is the print functions displays the intendent thing for the humans to see which the return keywords gives the value processed by the function so we can use that value in program.

In the above example in first on the print adds two variable a and b and prints the result to display which the return keyword also adds both variables and send back the result to program so computer can use same value in the program.

the return is generally more useful becuase we can use the values which were process by the function and these values are useful in programming to so more things.

## Medium

### Q4. Local vs Global Scope

Explain the difference between **local** and **global** variables.

What will happen here?

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

Give the output and explain why.

---

## Ans: The local variable has function scope and the global variable has global scope which means we can access global varible anywhere in the program. where as the local varibles are limited scope to function where they have initialized.

In the above program the x = 10  where x is the global varible and it has assigned value of 10. again in the functon x is assigned with value of 20. in function the print statement displays the value of x = 20 as per LEGB rule. once the function is called the function displays x value is 20 and the print statement outside function displays the x as 10 bcz the local x assignment has no impact on global x. 

### Q5. LEGB Rule

What does **LEGB** stand for?

Explain each level:

* Local
* Enclosing
* Global
* Built-in

You don't need a complicated example—focus on understanding the lookup order.

---
## Ans: The LEGB stands for Local Enlosing global and built in.

# Now Lets explore how it works. 

we have one function and we are processing some operation on varibles as x so python first chekc wheater the x varible intialized inside the same function or not if yes then it takes that local varibel value or else again it starts then outside function if the function encloed in another function then it searches for the outr function varibel x if its intialed then it uses the same value. then if x is not in both local or Enclosing function then it goes and serches in global and if it exist then it used or again it searches for the built in.

So it it gives the priority which mentioned above in LEGB Order.

### Q6. Default & Keyword Arguments

Explain the difference between:

```python
def greet(name, city="Bangalore"):
    ...
```

and calling it using:

```python
greet("Mahesh")
```

versus:

```python
greet(city="Pune", name="Mahesh")
```

Why are keyword arguments useful?

---

## Ans: In above Program the name is  parameter and city is defult parameter. Now while the greet function is called by passing the  argument. as per function defination it required two arguments still it executes bcz the another argument is defult value. and in second time now both arguments are passed and now function overiddex the defualt value of defualt argument with the passed value while calling the function.

The keyword arguments are useful bcz suppose in first call if we pass only one argument and in function defination if have two keyword arguments only the python will raise the error bcz it need two argument so is we use defualt agrguments then wven if dont pass value againsta defult argument staill it works becuse it has an defulat value to use.

### Q7. `*args` and `**kwargs`

Explain:

```python
def test(*args):
    ...
```

and

```python
def test(**kwargs):
    ...
```

What data types do `args` and `kwargs` become inside the function?

Give one practical use case for each.

---

## Ans:
In the first function call the *args parameter accepts arbitary number of positional parameters means user call pass any number of parameters. and in second function defination **kwargs means used can pass arbitary number of keyword argumnet. the number of values like dict  key value pairs.

inside the function *args become tuple and **kwargs becomes dictionary.

def print_shopping_list(*args):
    # args behaves like a tuple: ('apples', 'milk', 'bread')
    print("Items to buy:")
    for item in args:
        print(f"- {item}")

# You can pass 2 items or 3 items easily
print_shopping_list("apples", "milk", "bread")


def print_pet_names(**kwargs):
    # kwargs behaves like a dictionary: {'dog': 'Buddy', 'cat': 'Whiskers'}
    for pet_type, pet_name in kwargs.items():
        print(f"The {pet_type} is named {pet_name}.")

# You pass information using key=value syntax
print_pet_names(dog="Buddy", cat="Whiskers")


## Hard

### Q8. Argument Unpacking

What is happening here?

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

print(add(*numbers))
```

And here:

```python
def display(name, age):
    print(name, age)

student = {
    "name": "Mahesh",
    "age": 22
}

display(**student)
```

Explain the difference between `*` and `**` unpacking.

---

## Ans:

Here in above program the while calling add fucntion the list is packed and passed as tuple and inside the fucntion thes tuple is unpacked with three varibels a,b and c and these the function adding these varibales value and returning the sum. * is used to pack list and passed as tuple.

in the second function call the student is deictionary conatins key value pairs and its passed as **kwars as keyword argument and the function unpacks the dictionary and use the dict keys as argumennts.


### Q9. Lambda + map/filter

Explain what these do:

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

What will `squares` and `even_numbers` contain?

When would you use `lambda` with `map()` or `filter()`?

---
## Ans: Here the lambda function loops through the elemenet in the list and squres each element. and the maps functions produces the squred number into the list.


The squares cobtains: [1,4,9,16,25]
O/p: [1,4,9,16,25]

In the second example the lamnda finction iterates over the list called number and check the each element is even or not and the filter function filters all dd number ans the add makes the list of only even numbers.

The even_numbers contais [2,4]
O/P: [2,4]

when i need to perform a quick, simple data transformation or filtering task that only requires a single line of code.

i will Lambda with map combination when i want to modify every single item in a list in the exact same way.

ill Use Lambda with filter combination when i want to keep some items and throw away others based on a True/False condition.

### Q10. Scope + Mutable Data

Consider:

```python
numbers = [1, 2, 3]

def modify(data):
    data.append(4)

modify(numbers)

print(numbers)
```

Why can the function modify the original list even though `numbers` wasn't declared `global`?

Now compare that with:

```python
x = 10

def modify():
    x = 20

modify()

print(x)
```

Why does the second example behave differently?

---

## Ans: Why can the function modify the original list even though `numbers` wasn't declared `global`?

To naswer This in this function There is no local variable called numbers therfor python accessed the global number and modified the same after the calling the function the number is now contains the modified data and it will displays the modified data.


In the second function x is intiallizex and assigned value globally and localy inside the function. Now while calling the function python fist search for the local varible x and it founds here in function but id doenot affect the global x value even when calling the function and then printing the x it will display the global value only.


