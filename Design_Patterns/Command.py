class Light:
    def switch_on(self): return "Light ON"

class Switch:
    def __init__(self, command):
        self.command = command
    def execute(self):
        return self.command()

light = Light()
button = Switch(light.switch_on)
print(button.execute())  # Light ON