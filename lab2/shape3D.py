from abc import ABC, abstractmethod
from utils import validate_type

class Shape3D(ABC):
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = validate_type(x)
        self.y = validate_type(y)
        self.z = validate_type(z)

    def translate(self, x, y, z):
        validate_type(x)
        validate_type(y)
        validate_type(z)
        self.x += x
        self.y += y
        self.z += z

    def __lt__(self, other):
        if isinstance(other, Shape3D):
            return self.area < other.area
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Shape3D):
            return self.area > other.area
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Shape3D):
            return self.area <= other.area
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Shape3D):
            return self.area >= other.area
        return NotImplemented
    
    @abstractmethod
    def __eq__(self, other):
        pass

    @property
    @abstractmethod
    def volume(self):
        pass

    @property
    @abstractmethod
    def surface_area(self):
        pass