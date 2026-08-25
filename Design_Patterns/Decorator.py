class Milk:
    def __init__(self, item):
        self.item = item
    def cost(self):
        return self.item.cost() + 10

class Tea:
    def cost(self):
        return 20

my_tea = Milk(Tea())
print(my_tea.cost())  # 30