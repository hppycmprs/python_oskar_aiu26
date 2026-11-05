from shape2D import Shape2D
from utils import validate_type, validate_positive_value
import numpy as np

class Rectangle(Shape2D):
    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = validate_positive_value(validate_type(width))
        self.height = validate_positive_value(validate_type(height))

    @property
    def area(self):
        area = self.width*self.height
        return area

    @property
    def perimeter(self):
        perimeter = (self.width*self.width)+(self.height*self.height)
        return perimeter

    def translate(self, x, y):
        return

    def __eq__(self, other): # code block simplified using ChatGPT, code was a bit redundant before
    if isinstance(other, Rectangle):
        return (
            (self.width == other.width and self.height == other.height)
            or
            (self.width == other.height and self.height == other.width)
        )
    return False

    def __lt__(self, other):
        return

    def __gt__(self, other):
        return

    def __le__(self, other):
        return

    def __ge__(self, other):
        return

    def __repr__(self):
        return

    def __str__(self):
        return