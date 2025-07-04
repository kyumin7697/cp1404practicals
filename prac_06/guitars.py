"""
guitars.py

Estimate: 25 min
Start: 04/07/2025 15:10 p.m.
Actual: 31 min
"""

from prac_06.guitar import Guitar

def main():
    """Collect guitars from user and display details."""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()