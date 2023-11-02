"""
Estimate: 90 minutes
Actual: __ minutes  6 7
"""

import datetime
from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n" \
       "(U)pdate project\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
            print(f"{len(projects)} projects loaded.")
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
    projects = []
    filename = input("What file would you like to load your projects from: ")
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            if line:
                values = line.split('\t')
                projects.append([values[0], values[1], int(values[2]), float(values[3]), int(values[4])])
    return projects


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
