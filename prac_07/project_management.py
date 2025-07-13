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
            save_to_new_file(projects)
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

# 나머지 함수들 아래에 하나씩 추가할 예정

if __name__ == '__main__':
    main()