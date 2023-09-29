import random

# What did you see on line 1?
# Random numbers between the set parameters - 5 and 20.
# Smallest number that could be seen is 5, largest 20.

# What did you see on line 2?
# Random numbers between 3 and 9, however due to the third parameter (2), means it will go up in two's
# so the only possible numbers are 3, 5 ,7, 9.
# Smallest number that could be seen is 3, largest 9.
# Line 2 can not produce a 4 because of the parameter (step) of 2,
# so it will never generate an even number (since it starts on 3).

# What did you see on line 3?
# Random decimals between 2.5 and 5.5 rounded to 14 decimal places.
# Smallest number that could be seen is 2.50000000000000, largest 5.50000000000000.

print(random.randint(1, 100))
