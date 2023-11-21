"""dictonaries!"""
__author__ = "730670557"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values!"""
    keycheck: list[str] = []
    outputdict: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in keycheck:
            raise KeyError("No repeat keys allowed!")
        else:
            keycheck.append(dict1[key])
    for key in dict1:
        outputdict[dict1[key]] = key
    return outputdict


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns which color is in the string appears the most!"""
    colors: list[str] = []
    colorCounts: dict[str, int] = {}

    if len(dict1) == 0:
        return ""

    for key in dict1:
        colors.append(dict1[key])
    
    for color in colors:
        if color not in colorCounts:
            colorCounts[color] = 1
        else:
            colorCounts[color] += 1
    
    output: str = colors[0]
    for countedColor in colorCounts:
        if colorCounts[countedColor] > colorCounts[output]:
            output = countedColor
    
    return output


def count(list1: list[str]) -> dict[str, int]:
    """Counts the times a value appears in a list!"""
    returnDict: dict[str, int] = {}
    for string in list1:
        if string not in returnDict:
            returnDict[string] = 1
        else:
            returnDict[string] += 1
    return returnDict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Returns an alpahbet and a bunch of values that have the start with that alpahbet!"""
    outputDict: dict[str, list[str]] = {}
    for string in list1:
        string2 = string.lower()
        if string2[0] not in outputDict:
            outputDict[string2[0]] = [string]
        else:
            outputDict[string2[0]].append(string)
    return outputDict


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendence with attendence of students that day!"""
    if day not in dict1:
        dict1[day] = [student]
    else:
        if student not in dict1[day]:
            dict1[day].append(student)
    return dict1