"""
def main
    get score
    display menu
    get choice
    while choice != Q
        if choice == G
            get valid score
        else if choice == P
            result = evaluate_score(score)
            print "Result: {result}"
        else if choice == S
            print_stars(score)
        else
            print("Invalid choice")
        get choice
print "Farewell!"

def display_menu
    display menu options
    get user input and return uppercase version

def get_valid_score
    get score
    while score < 0 or score > 100
        get score again
    return valid score

def evaluate_score(score)
    if score >= 90: return "Excellent"
    elif score >= 50: return "Passable"
    else: return "Bad"

def print_stars(score)
    print "*" repeated int(score) times
"""

def main():
    """Main function to run the score menu program."""
    score = get_valid_score()
    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = evaluate_score(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        choice = display_menu()
    print("Farewell!")


def display_menu():
    """Display the menu options and return the user's choice."""
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    return input(">>> ").upper()


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def evaluate_score(score):
    """Evaluate the score and return a result message."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print a line of stars equal to the score."""
    print("*" * int(score))

main()