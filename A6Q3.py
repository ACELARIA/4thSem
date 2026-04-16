class Converter:
    def __init__(self, length, unit):
        self.length = length  
        self.unit = unit.lower()  

        self.conversion_factors = {
            "inches": 1,
            "feet": 1 / 12,
            "yards": 1 / 36,
            "miles": 1 / 63360,
            "millimeters": 25.4,
            "centimeters": 2.54,
            "meters": 0.0254,
            "kilometers": 0.0000254
        }

        if self.unit not in self.conversion_factors:
            raise ValueError("Invalid unit. Please use a valid measurement unit.")
        self.length_in_inches = self.length / self.conversion_factors[self.unit]

    def inches(self):
        return self.length_in_inches
    def feet(self):
        return self.length_in_inches * self.conversion_factors["feet"]
    def yards(self):
        return self.length_in_inches * self.conversion_factors["yards"]
    def miles(self):
        return self.length_in_inches * self.conversion_factors["miles"]
    def millimeters(self):
        return self.length_in_inches * self.conversion_factors["millimeters"]
    def centimeters(self):
        return self.length_in_inches * self.conversion_factors["centimeters"]
    def meters(self):
        return self.length_in_inches * self.conversion_factors["meters"]
    def kilometers(self):
        return self.length_in_inches * self.conversion_factors["kilometers"]


length = float(input("Enter length in inches: "))
unit = input("Enter unit from inches, feet, yards, miles, kilometers, meters, centimeters, millimeters: ")

try:
    c = Converter(length, unit)
    print(f"{c.length} {c.unit} is equal to:")
    print(f"{c.inches():.2f} inches")
    print(f"{c.feet():.2f} feet")
    print(f"{c.yards():.2f} yards")
    print(f"{c.miles():.6f} miles")
    print(f"{c.kilometers():.6f} kilometers")
    print(f"{c.meters():.2f} meters")
    print(f"{c.centimeters():.2f} centimeters")
    print(f"{c.millimeters():.2f} millimeters")
except ValueError as e:
    print(e) 