## TODAY'S ASSIGNMENT


#- [ ] Create a class called `Employee` with two class variables: `raise_amount = 1.04` and `num_of_employees = 0`.

class Employee:

    raise_amount = 1.04
    num_of_employees = 0

# - [ ] Add an `__init__` method that accepts `first_name`, `last_name`, `role`, and `monthly_salary`, stores them as instance attributes, and increases `Employee.num_of_employees` by 1.

    def __init__(self,first_name,last_name,role,monthly_salary):
        
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.monthly_salary = monthly_salary

        Employee.num_of_employees += 1

#- [ ] Add a method called `full_name` that returns the employee's first and last name together, and a method called `apply_raise` that updates `monthly_salary` using `self.raise_amount`.

    def full_name(self):

        return f"{self.first_name} {self.last_name}"
    
    def apply_raise(self):

        self.monthly_salary = int(self.monthly_salary * self.raise_amount)

# - [ ] Create two different `Employee` objects. Print both employees using the labels `Employee 1:` and `Employee 2:`, and print the shared count using the exact label `Total employees:`. 


employee1 =Employee("Mahesh", "Biradar","RF Engineer",45000)
employee2 =Employee("Rahul", "Patil", "Rigger", 30000)


print(f"Employee 1: full name: {employee1.full_name()}, role: {employee1.role}, monthly salary: {employee1.monthly_salary}")
print(f"Employee 2: full name: {employee2.full_name()}, role: {employee2.role}, monthly salary: {employee2.monthly_salary}")

print(f"Total employees: {Employee.num_of_employees}")

# - [ ] Set only employee 1's `raise_amount` to `1.10`, call `apply_raise()` on both employees, then print the exact labels `Employee 1 raise amount:`, `Employee 2 raise amount:`, `Employee 1 salary after raise:`, and `Employee 2 salary after raise:`.

employee1.raise_amount = 1.10

employee1.apply_raise()
employee2.apply_raise()

print(f"Employee 1 raise amount: {employee1.raise_amount}")
print(f"Employee 2 raise amount: {employee2.raise_amount}")
print(f"Employee 1 salary after raise: {employee1.monthly_salary}")
print(f"Employee 2 salary after raise: {employee2.monthly_salary}")

# Stretch (optional — do only after main requirements done):

# - [ ] Change `Employee.raise_amount` to `1.06`, create a third employee after the change, and print all three employees' raise amounts to show which values come from the class and which value was overridden on one object.

Employee.raise_amount = 1.06

employee3 =Employee("Sunil", "Patil","RF Engineer",45000)

print(f"Employee 1 raise amount: {employee1.raise_amount}")
print(f"Employee 2 raise amount: {employee2.raise_amount}")
print(f"Employee 3 raise amount: {employee3.raise_amount}")


## REVISION CHECK (answer these without looking — 2 min)

# 1. What does `self` refer to inside an instance method?

"""
self referce to current object(instance) that is calling the method.

self always refers to the specific object that called the method.
"""

#2. If two `Employee` objects have different roles, why does changing one object's role not automatically change the other object's role?

"""
Bcz role is intance variable and each object has its own sperate copy of instance variables.

"""

## COMMUNICATION PRACTICE (15 min)

"""
Today's task: In 6 polished sentences, answer this interview-style question: 
"What is a class variable, and how is it different from an instance variable?" 
Include the words `class variable`, `instance variable`, `shared`, `object`, and `override`. 
Before submitting, proofread once for complete sentences, capital `I`, correct spelling of "variable" and "instance", and spaces after commas.

"""

"""
A class varibale is data stored on class itself so evey object can use the same defualt value.
ex: total num of employess so this is class variable all objects share the same value.
changing the class varible applys to all object unless the individuall object override

instance variable belongs to each object individually. Each obejct have its own seperate copy of instances.
ex: first_name,last_name updating one objects instace variable doent affect the other objects.

"""

## THEORY BLOCK (20 min)

"""
There are mainly 5 states where process has been created and executed through these states.
1.New - Where process is created and stored in the secondary memory.
2.Ready- In this state the process is in the queue in the ram and the from new state to ready state the LTS is responsible to maove the processes from new state to ready state.
3.Running- In this state the process is executes which means all the instructions in process are excuted by the cpu.and other resources also allocated to the process.
4.Terminated- Once the process is done with execution then in the termination state all the allocated resources to the process are deallocated.
5.wait/Block-During the process is in running state and if the process requires additional resources or require service by I/O devices then these kind of process are pushed to wait/block state once all the resources are available these processes are again put in the queue in ready state and then executed in the running state.

To shedule and push all the processes in diffrent states there are mainly three sheduler are responsible.

1.Long term sheduler- Shedules the Processes and push the process from the New state to ready state.
2.Short term sheduler - Shedules the Processes and push process from the ready state to running state.
3.Medium term sheduler - Manages the process to shedule and push from the running state to the wait /block state and from there to the ready state.

"""


