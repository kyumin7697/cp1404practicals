"""
programming_language.py

Estimate: 30 min
Start: 04/07/2025 13:00 p.m.
Actual:
"""
class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing  # "Static" or "Dynamic"
        self.reflection = reflection  # True/False
        self.year = year