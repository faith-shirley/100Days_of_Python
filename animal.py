class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound..."

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof woof!"

# Cat class inherits from Animal
class Cat(Animal):
    def speak(self):
        return "Meow meow!"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says", dog.speak()) # Buddy says Woof woof!
print(cat.name, "says", cat.speak()) # Whiskers says Meow meow!