class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount>self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")

#Using the class
account = Bankaccount("Faith", 200000)
account.deposit(50000) #Deposited 50000
account.withdraw(300000) #Insufficient funds!