from shape2D import Shape2D
from utils import validate_type, validate_positive_value

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

    def square_or_not(self):
        return self.width == self.height

    def __eq__(self, other): # code block simplified using ChatGPT, code was a bit redundant before
        if isinstance(other, Rectangle):
            return (
                (self.width == other.width and self.height == other.height)
                or
                (self.width == other.height and self.height == other.width)
            )
        return False

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}, centered at ({self.x}, {self.y})"