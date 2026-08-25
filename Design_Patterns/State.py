class Fan:
    def __init__(self):
        self.state = "OFF"
    def toggle(self):
        self.state = "ON" if self.state == "OFF" else "OFF"
        print(f"Fan is {self.state}")

fan = Fan()
fan.toggle()  # Fan is ON
fan.toggle()  # Fan is OFF