"""
Estimate: 90 minutes
Actual: __ minutes  6
"""

import datetime
from project import Project

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# # print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n" \
       "(U)pdate project\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_new_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid input.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def load_projects():
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects():
    pass


def add_new_project():
    pass


def update_project():
    pass


main()
