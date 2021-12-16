"""
General geometry routines

circle_area(diameter)
rectangle_area(diameter)

"""
import math

def circle_area(diameter):
    """
    Calculate area of circle

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    return math.pi * (radius **2)

def rectangle_area(length, width):
    """
    Calculate area of rectangle.

    :param length: Length of rectangle
    :param width: Width of rectangle
    :return: Area of rectangle
    """
    return length * width

# "private"
def _toast():
    pass
