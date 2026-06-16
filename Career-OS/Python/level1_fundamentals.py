#Topic 1:Variables,Data types & Type System
#  1. Declare one variable of each primitive type and print it

#1 integer data type.
age = 27  # age is a varibale name or Reference given to the interger data type 27.

print(type(age))

#2 string data type

name = "Mahesh"

print(type(name))

#3 float Data type

price = 25.50

print(type(price))

#4 boolean data type

is_true = True


print(type(is_true))

#5 None data type

number = None

print(type(number))

#Sequencial Data types.

lis = [1,2,3,4,5,6]

print(type(lis))

tuples = (1,2,3,4)

print(type(tuples))

dictionary = { 1 : 2, 2: 4}

print(type(dictionary))

set_data = {1,2,3,4,5,6}

print(type(set_data))



#  2. Show type conversion: str → int, int → float, bool → int

age = "27"

print(type(int(age)))

num = 27

float_con=float(num)

print(type(float_con))

is_false = False

int_con = int(is_false)

print(type(int_con))

#   3. Demonstrate type() and isinstance() on at least 3 variables

#This section not tuched fully still what i undrtsood is retuns the data type of the object assinged to a varibale.

#Whereas the isinstance inherits the property of parent class.

#  4. Add one comment explaining: which of the types above are mutable and which are immutable, and what that means

# List , set , dict are the mutable Data types where as the tuple, string are immutable.

#Mutable rererce to where the data is manipulated such as adding , altering , deleting the objects

#immutable referce to not going to change once declaired.

