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