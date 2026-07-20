## TODAY'S ASSIGNMENT

"""
Goal: Show you can create a list and modify it correctly using the core list methods, then read it back with a loop and slicing.

"""
#1.- [ ] Create a list called `movies` containing at least 5 string items (any movies you like)

movies = ["don", "dhurander", "alpha", "border", "kgf"]

#2.- [ ] Use `append()` to add one new movie to the end of `movies`, then print the full list with the label `After append:`

movies.append("kantara")

print(f"After append:",movies)

#3.- [ ] Use `insert()` to add a movie at index `0`, then print the full list with the label `After insert:

movies.insert(0,"baby")

print(f"After insert:",movies)

#4.- [ ] Use `remove()` to delete one specific movie by name (pick one already in the list), then print the full list with the label `After remove:`

movies.remove("alpha")

print(f"After remove:",movies)

#5.- [ ] Use a `for` loop with `enumerate()` to print every remaining movie in the format `1. Inception` (number starts at 1, not 0), with the label `Final list:` printed on the line before the loop starts

print("Final list:")

for index, movie in enumerate(movies,start=1):

    print(f"{index}. {movie}")


# Stretch (optional — do only after main requirements done):

#6.- [ ] Use `.sort()` to sort `movies` alphabetically, print the sorted list with the label `Sorted:`, then use slicing to print only the first 3 items of the sorted list with the label `Top 3:`

movies.sort()

print(f"Sorted: {movies}")

print(f"Top 3: {movies[0:3]}")


## COMMUNICATION PRACTICE (15 min)

# Self-introduction

"""
I'm Mahesh Biradar, I'm final year B.Tech student at Dr. Ambedkar Institute 
of technology with CGPA of 8.64. And I'm immediate joiner.

Before Engineering, I spent 8 years in telecom operations. Managing 15 to 20 
teams, coordinating 6000+ sites for rollout programs and directly reporting 
to senior leadership in Reliance Jio.

Last year, I've transitioned into tech. I completed Web Development internship
at Agriaddict and built Agrisakhi. A live Full Stack platform. Using the React.js, Django, and PostgreSQL. 
And I delivered newjjroadlines.com as freelancing product. Which is serving client right now.

I speak English, Kannada, Hindi, Marathi.

"""

#1. In a function, what's the difference between returning a value and printing it?

"""
In a function returning value can be used for the any other operations 
suppose the function returing a interget then we can use that value and 
perform any operation on that value.

Whereas the print in the function is used to display the things which 
are passed in the print method. and we cannot use the things which are 
priting to perform operations such as return function.

"""

#2. If a function has a parameter with a default value, what happens when you call the function without passing that argument?.

"""
if a function has a prameter with default value and if i call a 
function without passing that argument. Then function takes the 
defualt value given in parameter as argument.

"""

