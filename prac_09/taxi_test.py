"""
Test Taxi
Estimate: 15 minutes
Actual: 9 minutes
"""

from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(my_taxi)
# reset fare to 0
my_taxi.start_fare()
my_taxi.drive(100)
# fuel should equal 0 now with 60km on current fare (distance)
print(my_taxi)
