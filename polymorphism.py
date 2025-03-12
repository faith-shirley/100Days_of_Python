class Car:
    def move(self):
        return "The car is driving."

class Boat:
    def move(self):
        return "The boat is sailing."

class Plane:
    def move(self):
        return "The plane is flying."

# Using polymorphism
vehicles = [Car(), Boat(), Plane()]
for vehicle in vehicles:
    print(vehicle.move())