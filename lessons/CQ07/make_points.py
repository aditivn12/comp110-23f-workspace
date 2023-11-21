"""Tests our definition of the point class and tests its methods."""

from lessons.CQ07.point import Point

point1: Point = Point(2.3, 4.3)
point1.scale_by(2)
point2 = point1.scale(3)
