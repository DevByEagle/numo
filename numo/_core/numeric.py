def absolute(value):
    if value < 0:
        return -value
    return value


def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    guess = x / 2.0
    tolerance = 1e-10


__all__ = [
    "absolute",
    "sqrt"
]

