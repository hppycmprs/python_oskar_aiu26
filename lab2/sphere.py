from shape3D import Shape3D
from utils import validate_type, validate_positive_value
import numpy as np

class Sphere(Shape3D):
    def __init__(self, radius, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = validate_positive_value(validate_type(value))

    @property
    def volume(self):
        volume = ((4*np.pi)*(self.radius**3))/3
        return volume

    @property
    def surface_area(self):
        surface_area = (4*np.pi)*(self.radius**2)
        return surface_area

    def unit_sphere_or_not(self):
        return self.radius == 1 and self.x == 0 and self.y == 0 and self.z == 0

    def __eq__(self, other):
        if isinstance(other, Sphere):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self):
        return f"Sphere(radius={self.radius}, x={self.x}, y={self.y}, z={self.z})"

    def __str__(self):
        return f"Sphere with radius {self.radius}, centered at ({self.x}, {self.y}, {self.z})"