def validate_type(value):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError ("Value can only be a number")
    return value

def validate_positive_value(value): # skall inte användas för x och y
    if not 0 < value < 1000:
        raise ValueError ("Value must be over 0 and below 1000")
    return value