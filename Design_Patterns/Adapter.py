class USAPlug:
    def flat_pin(self): return "110V USA Power"

class EuroAdapter:
    def __init__(self, usa_plug):
        self.usa_plug = usa_plug
    def round_pin(self):
        return f"Adapted: {self.usa_plug.flat_pin()}"

print(EuroAdapter(USAPlug()).round_pin())