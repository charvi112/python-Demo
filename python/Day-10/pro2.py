class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car("Toyota", "innova", 2024)
bike = Bike("Honda", "SP 125", 2021)

print(f"Car: {car.year} {car.make} {car.model}")
print(f"Bike: {bike.year} {bike.make} {bike.model}")
