class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible!")
        self._celsius = value


if __name__ == "__main__":
    temp = Temperature(25)
    print(f"Current temp: {temp.celsius}°C")
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"Validation caught: {e}")