class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model} is starting...")

# Child class: Car
class Car(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} {self.model} roars to life!")

# Child class: Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} {self.model} motorcycle revs up!")

# Creating objects
car1 = Car("Toyota", "Subaru")
bike1 = Motorcycle("Yamaha", "R1")

# Calling methods
car1.start_engine()
bike1.start_engine()