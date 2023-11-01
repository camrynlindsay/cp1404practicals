MENU = "(E)ven Numbers \n(O)dd Numbers \n(S)quare Numbers \n(Q)uit"

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        if first_number % 2 == 1:
            first_number += 1
        for i in range(first_number, second_number + 1, 2):
            print(i, end=' ')
        print()
    elif choice == "O":
        if first_number % 2 == 0:
            first_number += 1
        for i in range(first_number, second_number + 1, 2):
            print(i, end=' ')
        print()
    elif choice == "S":
        for i in range(first_number, second_number + 1):
            print(i ** 2, end=' ')
        print()
    else:
        print("Invalid option.")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
