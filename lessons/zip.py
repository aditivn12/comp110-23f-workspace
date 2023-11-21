"""Combining two lists into a dictionary!"""

author = "730670557"


def zip(firstlist: list[str], secondlist: list[int]) -> dict[str, int]:
    """This makes a singular dictionar0y!"""
    dict_1: dict[str, int] = dict()
    if len(firstlist) == 0 or len(secondlist) == 0:
        dict_1 = {}
    if len(firstlist) != len(secondlist):
        dict_1 = {}
    else:
        dict_1 = {firstlist[lists1]: secondlist[lists1] for lists1 in range(len(firstlist))}
    return dict_1  