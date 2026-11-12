from abc import ABC, abstractmethod
from types import NotImplementedType
from utils import validate_type


class Shape2D(ABC):
    """Abstract superclass Shape2D, from which Rectangle and Circle inherit their common functionality.

    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """Initialises the coordinates for a 2-dimensional shape.

        Args:
            x (int | float): The x-coordinate of the shape.
            y (int | float): The y-coordinate of the shape.

        Raises:
            TypeError: If x or y is not of type int | float, or is a bool.
        """
        self.x = validate_type(x)
        self.y = validate_type(y)

    def translate(self, x: float, y: float) -> None:
        """Translates the coordinates of an object of Shape2D.

        Args:
            x (int | float): The offset value that is added to the current x-coordinate.
            y (int | float): The offset value that is added to the current y-coordinate.
        
        Raises:
            TypeError: If x or y is not of type int | float, or is a bool.
        """
        validate_type(x)
        validate_type(y)
        self.x += x
        self.y += y
    
    def __lt__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of lt (less than).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if area of self is less than that of other, otherwise False.
            NotImplementedType: If other is not of type Shape2D
        """
        if isinstance(other, Shape2D):
            return self.area < other.area
        return NotImplemented

    def __gt__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of gt (greater than).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if area of self is greater than that of other, otherwise False.
            NotImplementedType: If other is not of type Shape2D
        """
        if isinstance(other, Shape2D):
            return self.area > other.area
        return NotImplemented

    def __le__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of le (less than or equal to).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if area of self is less than or equal to that of other, otherwise False.
            NotImplementedType: If other is not of type Shape2D
        """
        if isinstance(other, Shape2D):
            return self.area <= other.area
        return NotImplemented

    def __ge__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of ge (greater than or equal to).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if area of self is greater than or equal to that of other, otherwise False.
            NotImplementedType: If other is not of type Shape2D
        """
        if isinstance(other, Shape2D):
            return self.area >= other.area
        return NotImplemented

    @abstractmethod
    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Abstract method to be implemented by its subclasses, which in turn lets them define what equality means between 2D-shapes.

        Args:
            other (object): Object to compare to.

        Returns:
            bool: True if the geometrical dimensions of self is equal to that of other, otherwise False.
            NotImplementedType: If other is not of the type in which the method is implemented.

        """
        pass

    @property
    @abstractmethod
    def area(self) -> int|float:
        """Abstract method (read only) to be implemented by its subclasses, which in turn lets them use their own calculations for area.

        Returns:
            int | float: The calculated area of a 2-dimensional shape.
        """
        pass

    @property
    @abstractmethod
    def perimeter(self) -> int|float:
        """Abstract method (read only) to be implemented by its subclasses, which in turn lets them use their own calculations for perimeter.

        Returns:
            int | float: The calculated perimeter of a 2-dimensional shape.
        """
        pass