from abc import ABC, abstractmethod
from utils import validate_type

class Shape2D(ABC):
    def __init__(self, x = 0, y = 0):
        self.x = validate_type(x)
        self.y = validate_type(y)

    def translate(self, x, y):
        validate_type(x)
        validate_type(y)
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

    def __repr__(self):
        return

    def __str__(self):
        return
