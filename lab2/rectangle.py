from shape2D import Shape2D
from utils import validate_positive_value, validate_type
from types import NotImplementedType


class Rectangle(Shape2D):
    """Subclass of Shape2D, representing shapes in the form of rectangles.

    """
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0) -> None:
        """Initialises the width, height and coordinates of a rectangle.

        Args:
            width (int | float): The width of the rectangle.
            height (int | float): The height of the rectangle.
            x (int | float): The x-coordinate of the rectangle.
            y (int | float): The y-coordinate of the rectangle.

        Raises:
            TypeError: If width, height, x or y is not of type int | float, or is a bool.
            ValueError: If width or height is not greater than 0.
        """
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self) -> int|float:
        """Getter of a rectangle's width.
        
        Returns:
            int | float: The stored value of width.

        """
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """Setter of a rectangle's width.

        Args:
            value (int | float): The new width.

        Raises:
            TypeError: If value is not of type int | float, or is a bool.
            ValueError: If value is not greater than 0.
        """
        self._width = validate_positive_value(validate_type(value))

    @property
    def height(self) -> int|float:
        """Getter of a rectangle's height.
        
        Returns:
            int | float: The stored value of height.

        """
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """Setter of a rectangle's height.

        Args:
            value (int | float): The new height.

        Raises:
            TypeError: If value is not of type int | float, or is a bool.
            ValueError: If value is not greater than 0.
        """
        self._height = validate_positive_value(validate_type(value))

    @property
    def area(self) -> float:
        """Read-only property of a rectangle's area.

        Returns:
            int | float: The calculated area of a rectangle.
        """
        area = self.width*self.height
        return area

    @property
    def perimeter(self) -> int|float:
        """Read-only property of a rectangle's perimeter.

        Returns:
            int | float: The calculated perimeter of a rectangle.
        """
        perimeter = 2*(self.width+self.height)
        return perimeter

    def square_or_not(self) -> bool:
        """Method to check whether a rectangle is a square or not.

        Returns:
            bool: True if a rectangle's width and height are equal to one another, otherwise False.
        """
        return self.width == self.height

    def __eq__(self, other: object) -> bool | NotImplementedType: # code block simplified using ChatGPT, code was a bit redundant before
        """Method which defines what equality means between two rectangles.

        Args:
            other (object): Object to compare to.

        Returns:
            bool: True if the two objects' side lengths are equal to one another, regardless of orientation, otherwise False.
            NotImplementedType: If other is not of the type Rectangle.
        """
        if isinstance(other, Rectangle):
            return (
                (self.width == other.width and self.height == other.height)
                or
                (self.width == other.height and self.height == other.width)
            )
        return NotImplemented

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Rectangle with width {self.width} and height {self.height}, centered at ({self.x}, {self.y})"