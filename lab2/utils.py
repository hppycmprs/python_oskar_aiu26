def validate_type(value: int|float) -> int|float:
    """Validates that the given value is of type int or float.

    Args:
        value (int | float): The value to validate.

    Returns:
        int | float: The original value, if validation succeeds.

    Raises:
        TypeError: If value is not of type int | float or if value is of type bool.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError ("Value can only be a number")
    return value

def validate_positive_value(value: int|float) -> int|float: # skall inte användas för x och y
    """Validates that the given value is greater than 0.

    Args:
        value (int | float): The value to validate.

    Returns:
        int | float: The original value, if validation succeeds.

    Raises:
        ValueError: If value is not greater than 0.
    """
    if not 0 < value:
        raise ValueError ("Value must be greater than 0")
    return value