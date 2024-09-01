


# Base class Vehicle
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model} engine started")

# Derived class Car
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} car engine started with a vroom!")

# Derived class Truck
class Truck(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} truck engine started with a rumble!")

# Function to demonstrate polymorphism
def start_vehicle_engine(vehicle):
    vehicle.start_engine()

# Example usage:
car = Car("Toyota", "Corolla")
truck = Truck("Ford", "F-150")

start_vehicle_engine(car)  # Output: Toyota Corolla car engine started with a vroom!
start_vehicle_engine(truck)  # Output: Ford F-150 truck engine started with a rumble!

 