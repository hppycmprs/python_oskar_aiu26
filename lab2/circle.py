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

    def __eq__(self, other): # only compares circles to circles
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other): # didn't implement function to handle a number as other, as I couldn't find that particular requirement in the assignment
        if isinstance(other, Circle):
            return self.radius < other.radius
        elif isinstance(other, Shape2D):
            return self.area < other.area
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        elif isinstance(other, Shape2D):
            return self.area > other.area
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        elif isinstance(other, Shape2D):
            return self.area <= other.area
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        elif isinstance(other, Shape2D):
            return self.area >= other.area
        return NotImplemented

    def __repr__(self):
        return

    def __str__(self):
        return