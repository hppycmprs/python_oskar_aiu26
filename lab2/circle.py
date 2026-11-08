from shape2D import Shape2D
from utils import validate_type, validate_positive_value
import numpy as np

class Circle(Shape2D):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = validate_positive_value(validate_type(radius))

    @property
    def area(self):
        area = self.radius**2*np.pi
        return area

    @property
    def perimeter(self):
        perimeter = self.radius*2*np.pi
        return perimeter

    def unit_circle_or_not(self): # code block simplified using ChatGPT
        return self.radius == 1

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self):
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"

    def __str__(self):
        return f"Circle with radius {self.radius}, centered at ({self.x}, {self.y})"