import math
from abc import ABC,abstractmethod
class Area_calculator(ABC):
    @abstractmethod
    def print_area(self):
        pass

class Circle(Area_calculator):
    def __init__(self, **kwargs):
        self.radius = kwargs.get('radius')

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        
        return area

    def print_area(self):
        area = self.calculate_area()
        print(f"The area of the circle with radius {self.radius} is {area:.2f}")


class Square(Area_calculator):
    def __init__(self, **kwargs):
        self.side = kwargs.get('side')

    def calculate_area(self):
        area = (self.side ** 2)
        
        return area

    def print_area(self):
        area = self.calculate_area()
        print(f"The area of the circle with radius {self.side} is {area:.2f}")


class Rectangle(Area_calculator):
    def __init__(self, **kwargs):
        self.length = kwargs.get('length')
        self.width = kwargs.get('width')

    def calculate_area(self):
        area = (self.length*self.width)
        
        return area

    def print_area(self):
        area = self.calculate_area()
        print(f"The area of the Rectanngle is {area:.2f}")


# Usage example
# circle = Circle(radius = 15)
# circle.calculate_area()


my_rectangle_object = Rectangle(length=20,width = 40)
#print(my_rectangle_object.print_area())

