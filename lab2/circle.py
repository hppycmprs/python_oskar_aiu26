from shape2D import Shape2D
from utils import validate_type, validate_positive_value
import numpy as np

class Circle(Shape2D):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = validate_positive_value(validate_type(value))

    @property
    def area(self):
        area = self.radius**2*np.pi
        return area

    @property
    def perimeter(self):
        perimeter = self.radius*2*np.pi
        return perimeter

    def unit_circle_or_not(self): # code block simplified using ChatGPT
        return self.radius == 1 and self.x == 0 and self.y == 0

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self):
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"

    def __str__(self):
        return f"Circle with radius {self.radius}, centered at ({self.x}, {self.y})"