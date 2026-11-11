def validate_type(value: int|float) -> int|float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError ("Value can only be a number")
    return value

def validate_positive_value(value: int|float) -> int|float: # skall inte användas för x och y
    if not 0 < value:
        raise ValueError ("Value must be greater than 0")
    return value