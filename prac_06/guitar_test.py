from guitar import Guitar


def run_tests():
    """Test if class Guitar and methods work. """
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    thing = Guitar("Another Guitar", 2011, 20000)

    print(f"{guitar.name} get_age() - Expected {101}. Got {guitar.get_age()}")
    print(f"{thing.name} get_age() - Expected {12}. Got {guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{guitar.name} is_vintage() - Expected {False}. Got {thing.is_vintage()}")


run_tests()
