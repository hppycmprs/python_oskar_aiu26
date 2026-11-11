from shape3D import Shape3D
from utils import validate_positive_value, validate_type
from types import NotImplementedType


class Cube(Shape3D):
    def __init__(self, side_length: int|float, x: int|float = 0, y: int|float = 0, z: int|float = 0) -> None:
        super().__init__(x, y, z)
        self.side_length = side_length

    @property
    def side_length(self) -> int|float:
        return self._side_length

    @side_length.setter
    def side_length(self, value: int|float) -> None:
        self._side_length = validate_positive_value(validate_type(value))

    @property
    def volume(self) -> int|float:
        volume = self.side_length**3
        return volume

    @property
    def surface_area(self) -> int|float:
        surface_area = 6*(self.side_length**2)
        return surface_area

    def unit_cube_or_not(self) -> bool:
        return self.side_length == 1

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Cube):
            return self.side_length == other.side_length
        return NotImplemented

    def __repr__(self) -> str:
        return f"Cube(side_length={self.side_length}, x={self.x}, y={self.y}, z={self.z})"

    def __str__(self) -> str:
        return f"Cube with side length {self.side_length} centered at ({self.x}, {self.y}, {self.z})"