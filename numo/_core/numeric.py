def absolute(value):
    if value < 0:
        return -value
    return value


def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    
    guess = x // 2
    
    while guess * guess != x:
        guess = (guess + x // guess) // 2
    
    return guess


__all__ = [
    "absolute",
    "sqrt"
]

