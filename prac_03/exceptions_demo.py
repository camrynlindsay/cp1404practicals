"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when input other than integers (int) are entered.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when 0 is entered in the denominator (Math Error - undefined).
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
The code can change to place an error-checker before the calculation to see if the denominator is equal to
zero or not. Therefore, can remove the ZeroDivisionError exception as it will never be reached.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by 0, try again!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
