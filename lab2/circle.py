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

    def translate(self, x, y):
        return

    def __eq__(self, other):
        return

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