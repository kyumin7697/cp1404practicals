"""
myguitars.py

"""

from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Display the list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def get_new_guitars():
    """Get new guitars from user input and return them as a list."""
    new_guitars = []
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars

