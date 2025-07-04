"""
languages.py

Estimate: 10 min
Actual:  min
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create and test some ProgrammingLanguage objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)