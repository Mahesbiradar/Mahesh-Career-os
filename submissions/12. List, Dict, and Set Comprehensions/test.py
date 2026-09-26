employees = {
    "A": 50000,
    "B": 70000,
    "C": 80000
}

result = {
    name: salary * 2
    for name, salary in employees.items()
    if salary >= 70000
}

print(result)