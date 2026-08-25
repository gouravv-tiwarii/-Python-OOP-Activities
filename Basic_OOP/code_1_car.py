class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_info(self):
        print("Car Brand:", self.brand)
        print("Car Price: ₹", self.price)

    def increment_price(self, amount):
        self.price += amount
        print(f"\nPrice of {self.brand} increased by ₹{amount}")

    def decrement_price(self, amount):
        self.price -= amount
        print(f"\nPrice of {self.brand} decreased by ₹{amount}")


c1 = Car("Toyota", 1500000)
c2 = Car("Hyundai", 1200000)
c3 = Car("Honda", 1400000)
c4 = Car("Tata", 1000000)

print("=== Original Car Details ===")
c1.display_info()
print()

c2.display_info()
print()

c3.display_info()
print()

c4.display_info()

c1.increment_price(100000)

c4.decrement_price(50000)

print("\n=== Updated Car Details ===")
c1.display_info()
print()

c2.display_info()
print()

c3.display_info()
print()

c4.display_info()
