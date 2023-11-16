"""
Silver Service Taxi
Estimate: 20 minutes
Actual: 26 minutes
"""

from silver_service_taxi import SilverServiceTaxi


def test_run():
    cool_taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(cool_taxi)
    other_taxi = SilverServiceTaxi("Not so cool Taxi", 100, 2)
    other_taxi.drive(18)
    print(other_taxi)
    print(f"{other_taxi.get_fare():.2f}")


test_run()
