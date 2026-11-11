from abc import ABC, abstractmethod
from types import NotImplementedType
from utils import validate_type

class Shape3D(ABC):
    """Abstract superclass Shape3D, from which Cube and Sphere inherit their common functionality.

    """
    def __init__(self, x: int|float = 0, y: int|float = 0, z: int|float = 0) -> None:
        """Initialises coordinates for a 3-dimensional shape.

        Args:
            x (int | float): The x-coordinate of the shape.
            y (int | float): The y-coordinate of the shape.
            z (int | float): The z-coordinate of the shape.

        Raises:
            TypeError: If x, y or z is not of type int | float, or is a bool.
        """
        self.x = validate_type(x)
        self.y = validate_type(y)
        self.z = validate_type(z)

    def translate(self, x: int|float, y: int|float, z: int|float) -> None:
        """Translates an object's coordinates.

        Args:
            x (int | float): The offset value that is added to the current x-coordinate.
            y (int | float): The offset value that is added to the current y-coordinate.
            z (int | float): The offset value that is added to the current z-coordinate.
        
        Raises:
            TypeError: If x, y or z is not of type int | float, or is a bool.
        """
        validate_type(x)
        validate_type(y)
        validate_type(z)
        self.x += x
        self.y += y
        self.z += z

    def __lt__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of lt (less than).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if volume of self is less than that of other, otherwise False.
            NotImplementedType: If other is not of type Shape3D
        """
        if isinstance(other, Shape3D):
            return self.volume < other.volume
        return NotImplemented

    def __gt__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of gt (greater than).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if volume of self is greater than that of other, otherwise False.
            NotImplementedType: If other is not of type Shape3D
        """
        if isinstance(other, Shape3D):
            return self.volume > other.volume
        return NotImplemented

    def __le__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of le (less than or equal to).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if volume of self is less than or equal to that of other, otherwise False.
            NotImplementedType: If other is not of type Shape3D
        """
        if isinstance(other, Shape3D):
            return self.volume <= other.volume
        return NotImplemented

    def __ge__(self, other: object) -> bool | NotImplementedType:
        """Operator overload of ge (greater than or equal to).

        Args:
            other (object): Object to compare to.
        
        Returns:
            bool: True if volume of self is greater than or equal to that of other, otherwise False.
            NotImplementedType: If other is not of type Shape3D.
        """
        if isinstance(other, Shape3D):
            return self.volume >= other.volume
        return NotImplemented
    
    @abstractmethod
    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Abstract method to be implemented by its subclasses, which in turn lets them define what equality means between 3D-shapes.

        Args:
            other (object): Object to compare to.

        Returns:
            bool: True if the geometrical dimensions of self is equal to that of other, otherwise False.
            NotImplementedType: If other is not of type Shape3D.

        """
        pass

    @property
    @abstractmethod
    def volume(self) -> int|float:
        """Abstract method (read only) to be implemented by its subclasses, which in turn lets them use their own calculations for volume.

        Returns:
            int | float: The volume of a 3-dimensional shape.
        """
        pass

    @property
    @abstractmethod
    def surface_area(self) -> int|float:
        """Abstract method (read only) to be implemented by its subclasses, which in turn lets them use their own calculations for surface area.

        Returns:
            int | float: The surface area of a 3-dimensional shape.
        """
        pass