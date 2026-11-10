from shape3D import Shape3D
from utils import validate_type, validate_positive_value

class Cube(Shape3D):
    def __init__(self, side_length, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.side_length = side_length

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        self._side_length = validate_positive_value(validate_type(value))

    @property
    def volume(self):
        volume = self.side_length**3
        return volume

    @property
    def surface_area(self):
        surface_area = 6*(self.side_length**2)
        return surface_area

    def unit_cube_or_not(self):
        return self.side_length == 1

    def __eq__(self, other):
        if isinstance(other, Cube):
            return self.side_length == other.side_length
        return False

    def __repr__(self):
        return f"Cube(side_length={self.side_length}, x={self.x}, y={self.y}, z={self.z})"

    def __str__(self):
        return f"Cube with side length {self.side_length} centered at ({self.x}, {self.y}, {self.z})"