"""CQ07: A Class definition for a Point object."""

from __future__ import annotations


class Point:
    """A class that makes a point object with a x float and y float."""
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Initializes a point object with a x and y value."""
        self.x: float = x_init
        self.y: float = y_init

    def __str__(self) -> str:
        """Prints in a different format."""
        return f"x: {self.x}; y: {self.y}"

    def scale_by(self, factor: int) -> None:
        """Scales the points in within the object by a factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creates a new point object with new x and y coordinates scaled to a certain factor."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)
    
    def __mul__(self, factor: int | float) -> Point: 
        """Function where a point within the object is mulitplied by a factor."""
        mul_func: Point = Point(self.x * factor, self.y * factor)
        return mul_func

    def __add__(self, factor: int | float) -> Point:
        """Function where a point within the object is added by a factor."""
        add_func: Point = Point(self.x + factor, self.y + factor)
        return add_func



    
