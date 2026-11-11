from abc import ABC, abstractmethod
from types import NotImplementedType
from utils import validate_type


class Shape2D(ABC):
    def __init__(self, x: int|float = 0, y: int|float = 0) -> None:
        self.x = validate_type(x)
        self.y = validate_type(y)

    def translate(self, x: int|float, y: int|float) -> None:
        validate_type(x)
        validate_type(y)
        self.x += x
        self.y += y
    
    def __lt__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape2D):
            return self.area < other.area
        return NotImplemented

    def __gt__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape2D):
            return self.area > other.area
        return NotImplemented

    def __le__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape2D):
            return self.area <= other.area
        return NotImplemented

    def __ge__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape2D):
            return self.area >= other.area
        return NotImplemented

    @abstractmethod
    def __eq__(self, other: object) -> bool | NotImplementedType:
        pass

    @property
    @abstractmethod
    def area(self) -> int|float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> int|float:
        pass