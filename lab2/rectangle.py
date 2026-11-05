from shape2D import Shape2D
from utils import validate_type, validate_positive_value
import numpy as np

class Rectangle(Shape2D):
    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = validate_positive_value(validate_type(width))
        self.width = validate_positive_value(validate_type(height))