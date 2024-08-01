class RexGalaxy:
    def __init__(self, name, distance, diameter):
        self._name = name
        self._distance = distance
        self._diameter = diameter

    @property
    def name(self):
        return self._name

    @property
    def distance(self):
        return self._distance

    @property
    def diameter(self):
        return self._diameter

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Distance from Earth: {self.distance} light-years")
        print(f"Diameter: {self.diameter} light-years")


# Create an instance of RexGalaxy
rex_galaxy = RexGalaxy("Rex Galaxy", 10000, 5000)

# Accessing properties using property methods
print(rex_galaxy.name)  # Output: Rex Galaxy
print(rex_galaxy.distance)  # Output: 10000
print(rex_galaxy.diameter)  # Output: 5000

# Call the print_details() method
rex_galaxy.print_details()
