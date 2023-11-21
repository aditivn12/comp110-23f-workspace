"""Test my zip function!"""

from lessons.zip import zip

__author__ = "730670557"


def test_1() -> None:
    """Creates a dictionary with the two words given and the values!"""
    assert zip(["test", "python"], [1, 2]) == {"test": 1, "python": 2}
    

def test_2() -> None:
    """A dictionary of two lengths are returned!"""
    assert zip(["comp110", "assignment"], [1])


def test_output() -> None:
    """Checks if a proper dictionay is returned!"""
    assert zip(["Alyssa"], [1]) == dict
