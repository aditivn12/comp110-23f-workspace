"""Test my zip function!"""

from lessons.zip import zip

__author__ = "730670557"

def test_somethingcrazy() -> None:
    name: dict[str, int] = zip(["test", "python"], [1,2])
    assert name =={"test": 1, "python": 2}
    
def test_lengthsdiff() -> None:
    name: dict[str, int] = zip(["comp110", "assignment"])
    assert name == {}

def test_outputtest() -> None:
    name: dict[str, int] = zip(["alyssa", "byrnes"])
    assert name == {}
