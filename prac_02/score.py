"""
def main
    get score
    result = evaluate_score(score)
    print result

def evaluate_score(score)
    if score < 0 or score > 100
        return "Invalid score"
    else if score >= 90
        return "Excellent"
    else if score >= 50
        return "Passable"
    else
        return "Bad"
"""

def main():
    """Main function to get a score and print result."""
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

def evaluate_score(score):
    """Evaluate the given score and return a message."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()