class LuwaEmployee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def introduce(self):
        print(
            f"Hello my name is {self.name}, I work in the {self.department} department, and I earn UGX {self.salary}!")

    def apply_bonus(self, bonus):
        self.salary += bonus
        print(f"{self.name} received a bonus of UGX {bonus}. New salary: {self.salary}.")


#Manager subclass inheriting from LuwaEmployee
class Manager(LuwaEmployee):
    def assign_task(self, employee, task):
        print(f"{self.name} (Manager) assigned {employee.name} a task to {task}.")


# Creating employees
employee1 = LuwaEmployee("Julius", "Engineering", 800000)
employee2 = LuwaEmployee("Shirley", "Application Development", 900000)

# Calling methods
employee1.introduce()
employee1.apply_bonus(50000)

employee2.introduce()
employee2.apply_bonus(70000)

# Creating a manager
manager = Manager("Oscar", "HR", 1200000)
manager.introduce()
manager.assign_task(employee2, "Develop a new product feature")
