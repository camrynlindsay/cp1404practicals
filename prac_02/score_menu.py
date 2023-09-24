MENU = "(G)et Score\n(P)rint Result\n(S)how Stars\n(Q)uit"


def main():
    """This is a menu-driven program that interacts with the user's score in various ways"""
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    """Get a valid score between 0 and 100"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_score(score):
    """Determine the result based on the score input"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print number of stars based on the score"""
    print(score * "*")


main()
