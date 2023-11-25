"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
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


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default

    # values passed in
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    # default
    test_car = Car()
    assert test_car.fuel == 0


# run_tests()

# 3. Uncomment the following line and run the doctests
doctest.testmod()


def convert_phrase_to_sentence(phrase):
    """Turn a phrase into a sentence by capitalising the start and adding
    a full stop if it's needed.
    >>> convert_phrase_to_sentence('hello')
    'Hello.'
    >>> convert_phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> convert_phrase_to_sentence('I think it will rain today')
    'I think it will rain today.'
    """
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence
