import random

NUMBERS_IN_LINE = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    numbers = []
    for j in range(NUMBERS_IN_LINE):
        number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        while number in numbers:
            number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))
