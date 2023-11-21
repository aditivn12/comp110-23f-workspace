"""Tests the functions defined in dictionary.py with unit tests."""

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_Invert_1() -> None:
    """Makes sure the keys and values invert!"""
    assert invert({"test": "hello", "python": "py"}) == {"hello": "test", "py": "python"}
    

def test_invert_2() -> None:
    """A dictionary of two lengths are returned!"""
    assert invert({"comp110": "python"}) == {"python": "comp110"}


def test_invert_3() -> None:
    """Checks if a proper dictionay is returned!"""
    assert invert({"Alyssa": "alyssa"}) == {"alyssa": "Alyssa"}


def test_favorite_color_1() -> None:
    """Creates a dictionary with the two words given and the values!"""
    assert favorite_color({'Jack': 'blue', 'Aditi': 'green', 'Abhi': 'blue'}) == 'blue'
    

def test_favorote_color_2() -> None:
    """A dictionary of two lengths are returned!"""
    assert favorite_color({}) == ""


def test_favorite_color_3() -> None:
    """Checks if a proper dictionay is returned!"""
    assert favorite_color({"Aditi": "red", "Abhi": "blue", "John": "red"}) == 'red'


def test_alphabetizer() -> None:
    """Checks if a proper dictionay is returned!"""
    assert alphabetizer(["animal", "banana", "cherry", "grape", "alphabet", "blueberry"]) == {'a': ['animal', 'alphabet'], 'b': ['banana', 'blueberry'], 'c': ['cherry'], 'g': ['grape']}


def test_alphabetizer_2() -> None:
    """Checks if a proper dictionay is returned!"""
    assert alphabetizer([]) == {}


def test_alphabetizer_3() -> None:
    """Checks if a proper dictionay is returned!"""
    assert alphabetizer(["Apple", "Banana"]) == {'a': ['Apple'], 'b': ['Banana']}


def test_count_1() -> None:
    """Checks the count of certain elements in a list."""
    assert count(["apple", "banana", "cherry", "apple", "cherry"]) == {'apple': 2, 'banana': 1, 'cherry': 2}


def test_count_2() -> None: 
    """Checks the count function with an empty dictionary."""
    assert count([]) == {}


def test_count_3() -> None: 
    """Counts the specific elements in a list."""
    assert count(['apple', 'apple', 'banana']) == {'apple': 2, 'banana': 1}


def test_updateattendance_1() -> None:
    """Checks if the attendance updates if the same day is used."""
    assert update_attendance({"Tuesday": ["Abhi"]}, "Tuesday", "Aditi") == {"Tuesday": ["Abhi", "Aditi"]}


def test_update_attendance_2() -> None:
    """Checks if the function will work with an empty given dictionary."""
    assert update_attendance({}, "Monday", "Aditi") == {"Monday": ["Aditi"]}


def test_update_attendance_3() -> None:
    """Checks if the function will allow repeats."""
    assert update_attendance({"Friday": ["Aditi"]}, "Friday", "Aditi") == {"Friday": ["Aditi"]}