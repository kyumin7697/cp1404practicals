"""
programming_language.py

Estimate: 30 min
Start: 04/07/2025 13:00 p.m.
Actual:
"""
class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """Create the fields and set them to the parameters passed in"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True/False if the programming language is dynamically typed or not."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return readable string representation."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")