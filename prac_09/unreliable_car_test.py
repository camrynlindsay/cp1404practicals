"""
Unreliable Car
Estimate: 30 minutes
Actual: 25 minutes
"""

from unreliable_car import UnreliableCar


def test_unreliable_cars():
    """Tests for a reliable and unreliable car."""
    reliable_car = UnreliableCar("Good Car", 100, 90)
    unreliable_car = UnreliableCar("Bad Bar", 100, 10)
    for i in range(1, 15):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_car} drove {reliable_car.drive(i)}km")
        print(f"{unreliable_car} drove {unreliable_car.drive(i)}km")

    print()  # separate final stats away from the testing
    print(f"After the test run, the cars finished with: ")
    print(reliable_car)
    print(unreliable_car)


test_unreliable_cars()
