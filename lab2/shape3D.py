from abc import ABC, abstractmethod
from types import NotImplementedType
from utils import validate_type

class Shape3D(ABC):
    def __init__(self, x: int|float = 0, y: int|float = 0, z: int|float = 0) -> None:
        self.x = validate_type(x)
        self.y = validate_type(y)
        self.z = validate_type(z)

    def translate(self, x: int|float, y: int|float, z: int|float) -> None:
        validate_type(x)
        validate_type(y)
        validate_type(z)
        self.x += x
        self.y += y
        self.z += z

    def __lt__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape3D):
            return self.volume < other.volume
        return NotImplemented

    def __gt__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape3D):
            return self.volume > other.volume
        return NotImplemented

    def __le__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape3D):
            return self.volume <= other.volume
        return NotImplemented

    def __ge__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Shape3D):
            return self.volume >= other.volume
        return NotImplemented
    
    @abstractmethod
    def __eq__(self, other: object) -> bool | NotImplementedType:
        pass

    @property
    @abstractmethod
    def volume(self) -> int|float:
        pass

    @property
    @abstractmethod
    def surface_area(self) -> int|float:
        pass