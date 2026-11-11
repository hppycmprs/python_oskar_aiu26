from shape2D import Shape2D
import numpy as np
from utils import validate_positive_value, validate_type
from types import NotImplementedType


class Circle(Shape2D):
    def __init__(self, radius: int|float, x: int|float = 0, y: int|float = 0) -> None:
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self) -> int|float:
        return self._radius

    @radius.setter
    def radius(self, value: int|float) -> None:
        self._radius = validate_positive_value(validate_type(value))

    @property
    def area(self) -> int|float:
        area = self.radius**2*np.pi
        return area

    @property
    def perimeter(self) -> int|float:
        perimeter = self.radius*2*np.pi
        return perimeter

    def unit_circle_or_not(self) -> bool: # code block simplified using ChatGPT
        return self.radius == 1 and self.x == 0 and self.y == 0

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Circle with radius {self.radius}, centered at ({self.x}, {self.y})"