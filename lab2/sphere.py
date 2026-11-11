from shape3D import Shape3D
from utils import validate_type, validate_positive_value
import numpy as np
from types import NotImplementedType

class Sphere(Shape3D):
    """Subclass of Shape3D, representing shapes in the form of spheres.

    """
    def __init__(self, radius: int|float, x: int|float = 0, y: int|float = 0, z: int|float = 0) -> None:
        """Initialises the radius and coordinates of a sphere.

        Args:
            radius (int | float): The radius of the sphere.
            x (int | float): The x-coordinate of the sphere.
            y (int | float): The y-coordinate of the sphere.
            z (int | float): The z-coordinate of the sphere.

        Raises:
            TypeError: If radius, x, y or z is not of type int | float, or is a bool.
            ValueError: If radius is not greater than 0.
        """
        super().__init__(x, y, z)
        self.radius = radius

    @property
    def radius(self) -> int|float:
        """Getter of a sphere's radius.
        
        Returns:
            int | float: The stored value of radius.

        """
        return self._radius

    @radius.setter
    def radius(self, value: int|float) -> None:
        """Setter of a sphere's radius.

        Args:
            value (int | float): The new radius.

        Raises:
            TypeError: If value is not of type int | float, or is a bool.
            ValueError: If value is not greater than 0.
        """
        self._radius = validate_positive_value(validate_type(value))

    @property
    def volume(self) -> int|float:
        """Read-only property of a sphere's volume.

        Returns:
            int | float: The calculated volume of a sphere.
        """
        volume = ((4*np.pi)*(self.radius**3))/3
        return volume

    @property
    def surface_area(self) -> int|float:
        """Read-only property of a sphere's surface area.

        Returns:
            int | float: The calculated surface area of a sphere.
        """
        surface_area = (4*np.pi)*(self.radius**2)
        return surface_area

    def unit_sphere_or_not(self) -> bool:
        """Method to check whether a sphere is a unit sphere or not.

        Returns:
            bool: True if a sphere's radius is 1 and its x, y and z-coordinates are 0, otherwise False.
        """
        return self.radius == 1 and self.x == 0 and self.y == 0 and self.z == 0

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Method which defines what equality means between two spheres.

        Args:
            other (object): Object to compare to.

        Returns:
            bool: True if radius of self is equal to that of other, otherwise False.
            NotImplementedType: If other is not of the type Sphere.
        """
        if isinstance(other, Sphere):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self) -> str:
        return f"Sphere(radius={self.radius}, x={self.x}, y={self.y}, z={self.z})"

    def __str__(self) -> str:
        return f"Sphere with radius {self.radius}, centered at ({self.x}, {self.y}, {self.z})"