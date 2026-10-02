def make_counter():

    count = 0

    def increment(step=1):
        nonlocal count
        count += step
        return count

    return increment


counter1 = make_counter()
counter2 = make_counter()

print(counter1())
print(counter1(5))
print(counter2())
print(counter1())