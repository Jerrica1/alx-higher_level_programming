#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int) and not isintance(a, float):
        raise TypeError("a must be an integer")
    if not isintance(b, int) and not isintance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
