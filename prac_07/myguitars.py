"""
myguitars.py

Estimate: 50 min
Start: 12/07/2025 11:00
Actual: 60 min
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Main program to load, display, sort, add, and save guitars."""
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)

    print("\nAdd your new guitars:")
    guitars += get_new_guitars()

    save_guitars(FILENAME, guitars)
    print(f"\nSaved {len(guitars)} guitars to {FILENAME}.")

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

def save_guitars(filename, guitars):
    """Write the list of guitars to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

if __name__ == "__main__":
    main()

