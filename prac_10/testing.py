"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter and ending with a single full stop.

    >>> phrase_as_sentence("hello")
    'Hello.'
    >>> phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_as_sentence("nice weather!")
    'Nice weather!.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"


    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car1 = Car()  # default fuel
    assert car1.fuel == 0, "Default fuel should be 0"

    car2 = Car(fuel=10)
    assert car2.fuel == 10, "Fuel should be set to 10"



run_tests()


doctest.testmod()


