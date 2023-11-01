"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """This program takes a score input and prints out the result"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_score(score))
    random_score = random.randint(0, 100)
    print(random_score)
    print(determine_score(random_score))


def determine_score(score):
    """Determine the result based on the score input"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
