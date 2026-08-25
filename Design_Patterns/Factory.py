class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

def get_pet(pet_type):
    pets = {"dog": Dog, "cat": Cat}
    return pets.get(pet_type, Dog)()

print(get_pet("cat").speak())  # Meow!