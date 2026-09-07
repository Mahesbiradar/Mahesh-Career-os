"""

# 🟣 SECTION 3 — HOLISTIC MINI PROJECT

### ⏱️ Target time: 20–25 minutes

## 🚗 Mini Project: Vehicle Management System

Build a small **Vehicle Management System**.

The main focus is:

> **Inheritance + Method Overriding + Polymorphism**

Your previous topics should be used naturally where they make sense.

---

## Requirements

### 1. Base Class — `Vehicle`

Create:

```python
class Vehicle:
```

It should contain:

```text
vehicle_number
brand
price
```

as instance attributes.

Add:

```python
display_details()
```

which displays the vehicle information.

---

### 2. Child Classes

Create:

```python
class Car(Vehicle):
```

and:

```python
class Truck(Vehicle):
```

Use `super()` in their constructors.

Add one additional attribute to each:

```text
Car → doors
Truck → load_capacity
```

---

### 3. Method Overriding

Both `Car` and `Truck` should override:

```python
display_details()
```

Use:

```python
super().display_details()
```

inside the overridden methods and then display their additional information.

---

### 4. Polymorphism ⭐

Create:

```python
vehicles = [
    Car(...),
    Truck(...),
    Car(...),
    Truck(...)
]
```

Then write:

```python
def display_all_vehicles(vehicles):
    ...
```

The function should simply do:

```python
for vehicle in vehicles:
    vehicle.display_details()
```

### Restriction

Don't use:

```python
if isinstance(vehicle, Car):
```

inside this function.

I want you to demonstrate actual polymorphism.

---

## 5. Static Method

Add this to `Vehicle`:

```python
@staticmethod
def is_valid_price(price):
    ...
```

A price should be valid only if it is greater than `0`.

Use it when creating/validating vehicle data.

---

## 6. Class Method

Add:

```python
@classmethod
def from_string(cls, data):
    ...
```

The input will look like:

```text
V101,Toyota,1500000
```

The method should split the string and create a `Vehicle` object.

You can assume the base `Vehicle` constructor accepts:

```text
vehicle_number
brand
price
```

You don't need to create a separate child object through `from_string()`.

---

## 7. File Handling + Exceptions

Create a file such as:

```text
vehicles.txt
```

with:

```text
V101,Toyota,1500000
V102,Tata,800000
V103,Honda,1200000
V104,Ford,invalid
```

Read the file using:

```python
with open(...)
```

For invalid numeric data:

```text
invalid
```

catch the appropriate exception and **skip that record**.

Don't let one bad record stop the entire file processing.

---

## 8. Custom Exception

Create:

```python
class InvalidVehicleError(Exception):
    pass
```

If a vehicle has:

* missing fields
* invalid price

raise:

```python
InvalidVehicleError(...)
```

and handle it while processing the file.

---

## 9. Previous Topics — Use Naturally

After loading the valid vehicles:

### Use a list

You already have:

```python
vehicles
```

### Find the most expensive vehicle

You may use:

```python
max()
```

with a `lambda`.

For example:

```python
max(vehicles, key=lambda vehicle: vehicle.price)
```

### Create a dictionary

Create:

```text
vehicle_number → vehicle object
```

For example:

```python
{
    "V101": <Vehicle object>,
    "V102": <Vehicle object>
}
```

---

## 10. `isinstance()` / `issubclass()`

At the end, demonstrate these separately.

For example, determine whether:

```text
Car is a subclass of Vehicle
Truck is a subclass of Vehicle
```

and whether one of your objects is an instance of `Vehicle`.

This is **only to demonstrate your understanding**.

Don't use these checks to implement polymorphism.

---

# 🎯 Expected Flow

Your architecture should roughly look like:

```text
vehicles.txt
     ↓
read file
     ↓
parse strings
     ↓
validate data
     ↓
InvalidVehicleError / ValueError
     ↓
skip invalid record
     ↓
create Vehicle / Car / Truck objects
     ↓
store in list
     ↓
polymorphism
     ↓
display_details()
     ↓
find highest price
     ↓
dictionary by vehicle_number
```

### Important

You don't need to make this production-level.

I'm testing whether you can **connect the concepts**, not whether you can build a complete backend system.

"""


class InvalidVehicleError(Exception):
    pass

class Vehicle:

    def __init__(self,vehicle_number,brand,price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def display_details(self):

        print(f"Vehicle Number: {self.vehicle_number}\nBrand: {self.brand}\nPrice: {self.price}")

    @staticmethod
    def is_valid_price(price):
        return price > 0

    @classmethod
    def from_string(cls, data):
        parts = data.strip().split(",")

        if len(parts) != 5:
            raise InvalidVehicleError("Insufficient Data")
        
        vehicle_type,vehicle_number,brand,raw_price,raw_extra= parts

        price = int(raw_price)

        if not cls.is_valid_price(price):
            raise InvalidVehicleError("Invalid Vehicle Price")

        if vehicle_type.lower() == "car":
            doors = int(raw_extra)
            return Car(vehicle_number, brand, price, doors)

        elif vehicle_type.lower() == "truck":
            load_capacity = int(raw_extra)
            return Truck(vehicle_number, brand, price, load_capacity)

        else:
            raise InvalidVehicleError(f"Unknown Vehicle Type: {vehicle_type}")

    

class Car(Vehicle):

    def __init__(self, vehicle_number, brand, price, doors):
        super().__init__(vehicle_number, brand, price)
        self.doors = doors

    def display_details(self):
        super().display_details()
        print(f"Doors: {self.doors}")


class Truck(Vehicle):

    def __init__(self,vehicle_number, brand, price,load_capacity):
        super().__init__(vehicle_number,brand,price)
        self.load_capacity = load_capacity

    def display_details(self):
        super().display_details()
        print(f"Load Capacity: {self.load_capacity}")




""" --------Main Program------- """





def loadfile(filename):
    try:
        with open(filename) as file:

            vehicles_data = []

            for line in file:

                if not line.strip():
                    continue

                try:

                    vehicle_obj  = Vehicle.from_string(line.strip())
                    vehicles_data.append(vehicle_obj)
                except (InvalidVehicleError,ValueError) as e:
                    print(f"Skipping corrupt record due to error: {e}")
                    continue

               

            return vehicles_data
                
    except FileNotFoundError:
        print("File Not found")
        return None 



def display_all_vehicles(vehicles):

        for vehicle in vehicles:
            vehicle.display_details()


file = "submissions/vehicles.txt"



vehicles = loadfile(file)

if not vehicles:
    print("No data exist")
else:
    print("--- 📋 Displaying All Valid Loaded Vehicles ---")

    display_all_vehicles(vehicles)

    print("\n--- 💰 Most Expensive Vehicle ---")

    
    most_expensive = max(vehicles, key=lambda vehicle: vehicle.price)

    most_expensive.display_details()


    vehicle_dict = {}


    for vehicle in vehicles:

        string = vehicle.vehicle_number
        vehicle_dict[string] = vehicle


    print(vehicle_dict)


# 10. isinstance() / issubclass()

print(isinstance(Car,Vehicle))
print(issubclass(Car,Vehicle))
print(isinstance(Truck,Vehicle))
print(issubclass(Truck,Vehicle))