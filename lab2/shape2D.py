from abc import ABC, abstractmethod
from utils import validate_type, validate_positive_value

class Shape2D(ABC):
    def __init__(self, x = 0, y = 0):
        validate_type(x)
        self.x = value
        validate_type(y)
        self.y = value

    def translate(self, x, y):
        self.valid_type(x, y)
        self.x += x
        self.y += y

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass
