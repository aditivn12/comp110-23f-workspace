"""Summing the elements of a list using different loops."""
__author__ = 730670557


def w_sum(vals: list[float]) -> float:
    """This goes through a list and sums up every num in the list using a while statement."""
    final_list = 0.0
    index = 0
    while index < len(vals):
        final_list += vals[index]
        index += 1
    return final_list


def f_sum(vals: list[float]) -> float:
    """This goes through a list and sums up every num in the list using a for statement.""" 
    final_list = 0.0
    for index in vals:
        final_list += index
    return final_list


def f_range_sum(vals: list[float]) -> float:
    """This goes through a list and sums up every num in the list using a for statemnt and an "in range" statement!"""
    final_list = 0.0
    for index in range(len(vals)):
        final_list += vals[index]
    return final_list