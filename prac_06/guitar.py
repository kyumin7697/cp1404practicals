"""
guitar.py

Estimate: 60 min
Start: 04/07/2025 14:10
Actual:
"""

class Guitar:
    """Represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance based on name, year, cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitar's age in years."""
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50+ years old, False otherwise."""
        return self.get_age() >= 50