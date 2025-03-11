#defining a class
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello my name is {self.name}. I am {self.age} and I am studying {self.course}!")

#creating objects(students)
Student1 = Student("Faith", 22, "Python Programming")
Student2 = Student("Aaron", 23, "Machine Learning")

# Calling methods on objects
Student1.introduce()
Student2.introduce()