# 🧪 Hands-on — Exercise 1: Typed Functions


# Task 1 — Basic annotations


def add(a: int, b:int) -> int:

    return a + b


def format_user(name: str, age: int) -> str:

    return f"{name} is {age} years old"

print(format_user("Mahesh",28))


def calculate_average(numbers: list[int]) -> float:

    return sum(numbers)/len(numbers)

print(calculate_average([10, 20, 30, 40]))



# 🧪 Exercise 2 — Collection Types

def count_frequencies(items: list[str]) ->dict[str,int]:

    result = {}

    for i in items:
        result[i] = result.get(i,0)+1

    return result


print(count_frequencies(["python", "java", "python", "go", "java", "python"]))



def get_username(user_id: int) -> str | None:

    return "Mahesh" if user_id < 900 else None

print(get_username(199))
print(get_username(999))


# 🧪 Exercise 4 — Dataclass Basics

from dataclasses import dataclass, field

@dataclass
class User:

    id : int
    name : str
    email : str
    age : int


user1 = User(101,"Mahesh","Mahesh@gmail.com",28)
user2 = User(102,"Rakesh","rakesh@gmail.com",30)

print(user1)
print(user2)

# 🧪 Exercise 5 — default + default_factory

@dataclass
class Product:

    id : int
    name : str
    price : float
    tags : list[str] = field (default_factory=list)


p1 = Product(1, "Laptop", 50000)
p2 = Product(2, "Mouse", 800)

p1.tags.append("electronics")

print(p1.tags)
print(p2.tags)

# 🧪 Exercise 6 — field() + __post_init__

@dataclass
class Employee:

    id : int
    name : str
    salary : float = field(repr=False)
    department : str = field(default="General")

    def __post_init__(self):

        if self.salary < 0:
            raise ValueError


e1=Employee(101, "Mahesh", 50000)

# e2 = Employee(102, "Rahul", -5000)

# print(e1.salary)

# print(e1)


# 🚀 Exercise 7 — Backend Mini Task

from typing import Any

@dataclass
class APIResponse:

    status_code : int
    message : str
    data : dict[str,Any] | None = None



def process_response(response: APIResponse) -> None:

    print(f"--- Processing Response ({response.status_code}) ---")
    print(f"Message: {response.message}")
    
    if response.data is not None:
        print("Data Received:")
        for key, value in response.data.items():
            print(f"  - {key}: {value}")

    else:
        print("Data: No data payload attached.")

    print("-" * 35 + "\n")


success_response = APIResponse(status_code=200,message="User fetched successfully",data={"id": 101, "name": "Mahesh", "role": "Developer"})

failure_response  = APIResponse(status_code=404, message="User not found")


process_response(success_response)
process_response(failure_response)


    




