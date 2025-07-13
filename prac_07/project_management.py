"""
project_management.py

Estimate: 70 min
Start: 13/07/2025 12:40
Actual:
"""

from project import Project
from datetime import datetime
from operator import attrgetter

FILENAME = "projects.txt"

def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def main():
    print("Welcome to Pythonic Project Management")

    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n" \
           "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

    while True:
        print(menu)
        choice = input(">>> ").lower()
        if choice == "l":
            load_new_projects(projects)
        elif choice == "s":
            save_file(projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            quit_program(projects)
            break
        else:
            print("Invalid choice")

def load_new_projects(projects):
    filename = input("Filename: ")
    try:
        projects.clear()
        projects.extend(load_projects(filename))
        print(f"{len(projects)} projects loaded from {filename}")
    except FileNotFoundError:
        print("error")

def save_file(projects):
    filename = input("Filename to save to: ")
    save_projects(filename, projects)
    print(f"{len(projects)} projects saved to {filename}")

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in sorted(incomplete, key=attrgetter("priority")):
        print(f"  {p}")

    print("Completed projects:")
    for p in sorted(complete, key=attrgetter("priority")):
        print(f"  {p}")

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered = [p for p in projects if p.start_date > filter_date]
    for p in sorted(filtered, key=attrgetter("start_date")):
        print(p)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    percent = input("Percent complete: ")

    try:
        new_project = Project(name, start_date_str, priority, cost, percent)
        projects.append(new_project)
    except ValueError:
        print("Invalid input.")

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
    except (ValueError, IndexError):
        print("Invalid project number.")
        return

    print(project)
    new_percent = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percent:
        try:
            project.completion_percentage = int(new_percent)
        except ValueError:
            print("Invalid percentage input.")
    if new_priority:
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority input.")

def quit_program(projects):
    choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if choice in ("y", "yes"):
        save_projects(FILENAME, projects)
        print(f"Saved to {FILENAME}")
    else:
        print("No save performed.")
    print("Thank you for using custom-built project management software.")

if __name__ == '__main__':
    main()