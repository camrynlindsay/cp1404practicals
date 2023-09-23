MENU = "(G)et Score\n(P)rint Result\n(S)how Stars\n(Q)uit"

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "G":
        pass
    elif choice == "P":
        pass
    elif choice == "S":
        pass
    else:
        print("Invalid option.")
    print(MENU)
    choice = input(">>> ").upper()
print("Farewell.")
