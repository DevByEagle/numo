from typing import Union

def absolute(value: Union[int, float]) -> Union[int, float]: ...

def sqrt(x: Union[int, float]) -> float:
    """Returns the square root of x."""
    ...

__all__ = [
    "absolute",
    "sqrt"
]


