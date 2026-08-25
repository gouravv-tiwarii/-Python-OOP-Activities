class Engine:
    def start(self): return "Engine started"

class Lights:
    def on(self): return "Lights on"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()
    def drive(self):
        return f"{self.engine.start()}, {self.lights.on()}"

print(Car().drive())