ROUND 1 — Concepts + Short Problems

Answer these without notes.

## Q1 — Data Structures

You need to store:

A student's marks:
85, 92, 76, 92

Which Python data structure would you choose and why?

## Ans:

I would choose List as it allows duplicates and mutability to perform operations on marks.

if i have to store the marks as key value pair against the student name and then marks the i woud choose the Dict where i can store the student name as key and marks as values in list.

## Q2 — List

Explain the difference between:

append()
extend()

Give one example of each.

# Ans:

Append is used to adding the object in list at the end. Whereas the extend method iterates over iterable and then add each element in iterable to the target list.

Ex:  

list = [1,2,4]

list.append(5)  # [1,2,4,5]
list.append([6,7])  # [1,2,4,5,[6,7]]

list.extend([6,7]) # [1,2,3,4,6,7]

## Q3 — Tuple

What does immutability mean for a tuple?

Also explain why you might use a tuple instead of a list.

## Ans: immutability meand once the tuple is declared we can mutate the tuple means we cant add update or remove the object in the tuple.

ill use tuple where i need to store the collection of which need to be stable or immutbale which means user not able to modify the data. once declaired.

## Q4 — Dictionary

What's the difference between:

data["name"]

and:

data.get("name")

What happens if "name" doesn't exist?

## Ans:

serching with key without the get method can lead to key error if key doesnt exist if we use get method to serach a key if keydoent found it will handle the error safely. the get retuns None if key not found in program instead of crashing the program.


## Q5 — Set

Why would a set generally be preferred over a list for a task like:

if user_id in active_users:

Also explain why duplicates disappear from a set.

## the set is preffered over list for the task given above.
1.fastlookup searching element in set can cost O(1) whereas in list it may cost O(n)
2.Set stores unique elements as for above task the users shoud be unique and but list store duplicates also.

Set stores only the uniuqe elements and set is designed to store the unique itesm Therefor duplicates disappear in set.

# Q6 — Hashability 🔥

What does hashable mean?

Why can this be a dictionary key:

"Mahesh"

but this cannot:

[1, 2, 3]

## Ans: hashable object has stable hash value during its lifetime and can be used as dictionary key and set element.

The "Mahesh" is string and strings are immutable Therefor string can be dictionary keys where as the list is mutable which means it can be alterable therefor list cannot be dictionary keys. as hasble objects shoud be stable and immutable.


## Q7 — Functions

Explain the difference between a parameter and an argument using:

def calculate(a, b):
    return a + b

calculate(10, 20)

# Ans:  Parameters are the varibles in the function call whereas the arguments are the actull values passed while calling the function.parameters are used as placeholders.

in above example the in function defination a and b are the parameters and in function call 10,20 are the arguments passing to function.


## Q8 — *args / **kwargs

Explain:

def test(*args, **kwargs):
    ...

What are the types of args and kwargs inside the function?

## ans: In python functions *args and **kwargs allows to pass arbitary number of postional and keyword agruments.

*args allows arbitary number of positional arguments and stores packs in tuple.

**kwars allows arbitary number of keyword argumenst and store these in dict.

## Q9 — Packing vs Unpacking 🔥

Explain the difference between:

def test(*args):
    ...

and:

numbers = [10, 20, 30]
test(*numbers)

Use the words packing and unpacking correctly.

## Ans: In above function called test *args packs the arbitary number of postional arguments into tuple and while calling the function *numbers unpacks the postional arguments.


## Q10 — LEGB

Explain what LEGB stands for and give a simple example showing why Python needs this lookup rule.

## ans: LEGB Stands for Local,Enclosed,Global,Built in . Python uses this rule for variable name resolving order. where it first searches the variable in local function and then goes to enclosed function if not found in local and then searches in global level and then built in level.

## Q11 — Lambda

What is a lambda function?

Why might you use:

sorted(students, key=lambda x: x[1])

instead of writing a separate named function?

## Ans: Lambda is unanemous function in pythone its used to write expression in short.

ill use lambda function for above given example insetad of a seperate function bcz it does same work in short expression and it improved readablity whene we have to transform data with single expression.


## Q12 — map/filter/reduce

Explain the purpose of each:

map
filter
reduce

Don't just give definitions — tell me what kind of problem each is useful for.

##: map fnction is used to transform a collection of data for ex: map(lambda x:x^2,list) here map function iterates over iterable and transaforms the collection retuns the list.

## : filter function is used to transform elemenets where contion is true and retuns the only tuthy values.

ex: filter(lambda x:x%2==0,list)

## Reduce function transfoms the entire collection in to a single element.

ex: reduce(lambda x,y:x*y,numbers)


## Q13 — Module vs Package

Explain the difference between:

module
package

using this structure:

users/
    __init__.py
    models.py
    services.py

## ans : Module is nothing but python file contains python code. and package provides a way to manage modules in directore structure.

in above stucture users is directory stucutre which storesd the python modules such as models.py ,services.py and __init__.py.

## Q14 — Virtual Environment 🔥

You're working on two backend projects:

Project A → Django 4
Project B → Django 5

Why would you create separate virtual environments?

What problem could occur if both projects use the same global Python environment?

## Ans: if im working on two backend project called a and b ill use seperate virtual environment bcz virtual envirnment provides isolated python environment and it installing dependenciesn would not affect the another project.

suppose if install the dependecnies in global environment if i installed the dependecies for project a then project b will be affected as it needs Django 5 but globaly i have installed the 4 there for createting seperate virtula envirment would rescoves the conflicts.


# Q15 — Backend Scenario 🔥

You clone a Django project from GitHub.

You see:

requirements.txt

You create:

python -m venv venv

Then activate it.

What would you normally do next, and why?

# Ans: Ill install all the dependencies listed in teh requirement file.

using the command pip install -r requirements.txt

Here after creating the vertuall invironment the next thing which is neccesary to install the external dependencies of the project without the dependecnies project will not run.





