# Practical 01
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')

number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars + 1):
    print(i * "*")

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

HIGH_THRESHOLD_RATE = 0.15
LOW_THRESHOLD_RATE = 0.1

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * LOW_THRESHOLD_RATE
    else:
        bonus = sales * HIGH_THRESHOLD_RATE
    print(f"Your bonus is ${bonus} based on your sales.")
    sales = float(input("Enter sales: $"))
print("Invalid sales.")

DISCOUNT = 0.1

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total += item_price
if total > 100:
    total = total - (total * DISCOUNT)
print(f"Total price for {number_of_items} items is ${total:.2f}")

"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")