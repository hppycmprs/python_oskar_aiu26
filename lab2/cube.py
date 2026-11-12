from shape3D import Shape3D
from utils import validate_positive_value, validate_type
from types import NotImplementedType


class Cube(Shape3D):
    """Subclass of Shape3D, representing shapes in the form of cubes.

    """
    def __init__(self, side_length: float, x: float = 0, y: float = 0, z: float = 0) -> None:
        """Initialises the side length and coordinates of a cube.

        Args:
            side_length (int | float): The side length of the cube.
            x (int | float): The x-coordinate of the cube.
            y (int | float): The y-coordinate of the cube.
            z (int | float): The z-coordinate of the cube.

        Raises:
            TypeError: If side_length, x, y or z is not of type int | float, or is a bool.
            ValueError: If side_length is not greater than 0.
        """
        super().__init__(x, y, z)
        self.side_length = side_length

    @property
    def side_length(self) -> int|float:
        """Getter of a cube's side length.
        
        Returns:
            int | float: The stored value of side_length.

        """
        return self._side_length

    @side_length.setter
    def side_length(self, value: float) -> None:
        """Setter of a cube's side length.

        Args:
            value (int | float): The new side length.

        Raises:
            TypeError: If value is not of type int | float, or is a bool.
            ValueError: If value is not greater than 0.
        """
        self._side_length = validate_positive_value(validate_type(value))

    @property
    def volume(self) -> int|float:
        """Read-only property of a cube's volume.

        Returns:
            int | float: The calculated volume of a cube.
        """
        volume = self.side_length**3
        return volume

    @property
    def surface_area(self) -> int|float:
        """Read-only property of a cube's surface area.

        Returns:
            int | float: The calculated surface area of a cube.
        """
        surface_area = 6*(self.side_length**2)
        return surface_area

    def unit_cube_or_not(self) -> bool:
        """Method to check whether a cube is a unit cube or not.

        Returns:
            bool: True if a cube's side length is 1, otherwise False.
        """
        return self.side_length == 1

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Method which defines what equality means between two cubes.

        Args:
            other (object): Object to compare to.

        Returns:
            bool: True if side length of self is equal to that of other, otherwise False.
            NotImplementedType: If other is not of the type Cube.
        """
        if isinstance(other, Cube):
            return self.side_length == other.side_length
        return NotImplemented

    def __repr__(self) -> str:
        return f"Cube(side_length={self.side_length}, x={self.x}, y={self.y}, z={self.z})"

    def __str__(self) -> str:
        return f"Cube with side length {self.side_length} centered at ({self.x}, {self.y}, {self.z})"