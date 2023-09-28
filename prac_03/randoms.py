import random

# What did you see on line 1?
# Random numbers between the set boundaries - 5 and 20.
# Smallest number that could be seen is 5, largest 20.

# What did you see on line 2?
# Random numbers between 3 and 9, however due to the third condition (2), means it goes up in two's
# so the only possible numbers are 3, 5 ,7, 9.
# Smallest number that could be seen is 3, largest 9.
# Line 2 can not produce a 4 because of the boundary step of 2, so it will never generate a random
# even number.

# What did you see on line 3?
# Random decimals between 2.5 and 5.5 to the 14th decimal place.
# Smallest number that could be seen is 2.50000000000000, largest 5.50000000000000.

print(random.randint(1, 100))
