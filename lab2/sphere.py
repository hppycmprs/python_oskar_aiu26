from shape3D import Shape3D
from utils import validate_type, validate_positive_value
import numpy as np
from types import NotImplementedType

class Sphere(Shape3D):
    def __init__(self, radius: int|float, x: int|float = 0, y: int|float = 0, z: int|float = 0) -> None:
        super().__init__(x, y, z)
        self.radius = radius

    @property
    def radius(self) -> int|float:
        return self._radius

    @radius.setter
    def radius(self, value: int|float) -> None:
        self._radius = validate_positive_value(validate_type(value))

    @property
    def volume(self) -> int|float:
        volume = ((4*np.pi)*(self.radius**3))/3
        return volume

    @property
    def surface_area(self) -> int|float:
        surface_area = (4*np.pi)*(self.radius**2)
        return surface_area

    def unit_sphere_or_not(self) -> bool:
        return self.radius == 1 and self.x == 0 and self.y == 0 and self.z == 0

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Sphere):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self) -> str:
        return f"Sphere(radius={self.radius}, x={self.x}, y={self.y}, z={self.z})"

    def __str__(self) -> str:
        return f"Sphere with radius {self.radius}, centered at ({self.x}, {self.y}, {self.z})"