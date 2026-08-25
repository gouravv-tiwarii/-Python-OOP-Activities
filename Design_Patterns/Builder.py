class Burger:
    def __init__(self):
        self.cheese = False
        self.patty = 1

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
    def add_cheese(self):
        self.burger.cheese = True
        return self
    def set_patty(self, count):
        self.burger.patty = count
        return self
    def build(self):
        return self.burger

b = BurgerBuilder().add_cheese().set_patty(2).build()
print(f"Patties: {b.patty}, Cheese: {b.cheese}")