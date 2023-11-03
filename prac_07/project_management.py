"""
Estimate: 90 minutes
Actual: __ minutes  76
"""

import datetime
from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n" \
       "(U)pdate project\n(Q)uit"
PERCENTAGE_INDEX = 4
PRIORITY_INDEX = 2


def main():
    """Program that keeps track of current and completed projects."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
            print(f"{len(projects)} projects loaded.")
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid input.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects():
    """Load projects from a file into a list of lists."""
    projects = []
    filename = input("What file would you like to load your projects from: ")
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            if line:
                parts = line.split('\t')
                project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
                projects.append(project)
    return projects


def save_projects(projects):
    """Save projects into a designated file."""
    filename = input("What file would you like to save your projects to: ")
    with open(filename, "w") as output_file:
        for project in projects:
            print(",".join(project), file=output_file)


def display_projects(projects):
    """Display all completed and uncompleted projects."""
    completed_projects = []
    uncompleted_projects = []
    for project in projects:
        if project.percentage == 100:
            completed_projects.append(project)
        else:
            uncompleted_projects.append(project)

    uncompleted_projects.sort(key=lambda project: project.priority)
    completed_projects.sort(key=lambda project: project.priority)

    print("Incomplete projects:")
    for project in uncompleted_projects:
        print(project)
    print("Completed projects:")
    for project in completed_projects:
        print(project)


def filter_projects(projects):
    """Show projects that start after a set date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")  # e.g., "30/9/2022"
    filtered_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        project_start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if project_start_date >= filtered_date:
            print(project)


def add_new_project(projects):
    """Add a new project to the list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = get_valid_priority("Priority: ")
    cost_estimate = float(input("Cost estimate: $"))
    percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, percentage)
    projects.append(project)


def get_valid_priority(prompt):
    """Get a valid input for priority from user."""
    valid_input = False
    while not valid_input:
        try:
            user_input = int(input(f"{prompt}"))
            if user_input > 0:
                valid_input = True
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")
        except TypeError:
            print("Invalid input; enter a valid number.")
    return user_input  # Safe to ignore Pycharm warning


def update_project(projects):
    """Update the completion percentage of a particular project."""
    for i, project in enumerate(projects, start=0):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(projects[choice])
    new_percentage = int(input("New Percentage: "))
    projects[choice][PERCENTAGE_INDEX] = new_percentage
    new_priority = int(input("New Priority: "))
    if new_priority != "":
        projects[choice][PRIORITY_INDEX] = new_priority


main()
