class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

#creating an object
my_laptop = Laptop("Huawei", 3000000) #UGX 3,000,000
print(my_laptop.brand)
print(my_laptop.price)