class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

class Bike(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

car = Car("Toyota", "Corolla", 2020, 4)
bike = Bike("Yamaha", "YZF-R3", 2019, "sports")
truck = Truck("Ford", "F-150", 2018, 3)

print(f"Car: {car.year} {car.make} {car.model} with {car.doors} doors")
print(f"Bike: {bike.year} {bike.make} {bike.model} which is a {bike.type} bike")
print(f"Truck: {truck.year} {truck.make} {truck.model} with {truck.capacity} ton capacity")
