from shape2D import Shape2D
from utils import validate_type, validate_positive_value

class Rectangle(Shape2D):
    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = validate_positive_value(validate_type(value))

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = validate_positive_value(validate_type(value))

    @property
    def area(self):
        area = self.width*self.height
        return area

    @property
    def perimeter(self):
        perimeter = 2*(self.width+self.height)
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