class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()

print(isinstance(car, Car))
print(isinstance(car, Vehicle))
print(isinstance(Car, Vehicle))
print(issubclass(Car, Vehicle))