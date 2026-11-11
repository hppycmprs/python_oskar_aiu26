from shape2D import Shape2D
from utils import validate_positive_value, validate_type
from types import NotImplementedType


class Rectangle(Shape2D):
    def __init__(self, width: int|float, height: int|float, x: int|float = 0, y: int|float = 0) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self) -> int|float:
        return self._width

    @width.setter
    def width(self, value: int|float) -> None:
        self._width = validate_positive_value(validate_type(value))

    @property
    def height(self) -> int|float:
        return self._height

    @height.setter
    def height(self, value: int|float) -> None:
        self._height = validate_positive_value(validate_type(value))

    @property
    def area(self) -> int|float:
        area = self.width*self.height
        return area

    @property
    def perimeter(self) -> int|float:
        perimeter = 2*(self.width+self.height)
        return perimeter

    def square_or_not(self) -> bool:
        return self.width == self.height

    def __eq__(self, other: object) -> bool | NotImplementedType: # code block simplified using ChatGPT, code was a bit redundant before
        if isinstance(other, Rectangle):
            return (
                (self.width == other.width and self.height == other.height)
                or
                (self.width == other.height and self.height == other.width)
            )
        return NotImplemented

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Rectangle with width {self.width} and height {self.height}, centered at ({self.x}, {self.y})"