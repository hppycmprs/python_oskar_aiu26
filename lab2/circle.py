from shape2D import Shape2D
import numpy as np
from utils import validate_positive_value, validate_type
from types import NotImplementedType


class Circle(Shape2D):
    """Subclass of Shape2D, representing shapes in the form of circles.

    """
    def __init__(self, radius: float, x: float = 0, y: float = 0) -> None:
        """Initialises the radius and coordinates of a circle.

        Args:
            radius (int | float): The radius of the circle.
            x (int | float): The x-coordinate of the circle.
            y (int | float): The y-coordinate of the circle.

        Raises:
            TypeError: If radius, x or y is not of type int | float, or is a bool.
            ValueError: If radius is not greater than 0.
        """
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self) -> int|float:
        """Getter of a circle's radius.
        
        Returns:
            int | float: The stored value of radius.

        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """Setter of a circle's radius.

        Args:
            value (int | float): The new radius.

        Raises:
            TypeError: If value is not of type int | float, or is a bool.
            ValueError: If value is not greater than 0.
        """
        self._radius = validate_positive_value(validate_type(value))

    @property
    def area(self) -> int|float:
        """Read-only property of a circle's area.

        Returns:
            int | float: The calculated area of a circle.
        """
        area = self.radius**2*np.pi
        return area

    @property
    def perimeter(self) -> int|float:
        """Read-only property of a circle's perimeter.

        Returns:
            int | float: The calculated perimeter of a circle.
        """
        perimeter = self.radius*2*np.pi
        return perimeter

    def unit_circle_or_not(self) -> bool: # code block simplified using ChatGPT
        """Method to check whether a circle is a unit circle or not.

        Returns:
            bool: True if a circle's radius is 1 and its x and y-coordinates are 0, otherwise False.
        """
        return self.radius == 1 and self.x == 0 and self.y == 0

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Method which defines what equality means between two circles.

        Args:
            other (object): Object to compare to.

        Returns:
            bool: True if radius of self is equal to that of other, otherwise False.
            NotImplementedType: If other is not of the type Circle.
        """
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Circle with radius {self.radius}, centered at ({self.x}, {self.y})"