"""
def main
    min_length = 5
    password = get_password(min_length)
    print_asterisks(password)

def get_password(min_length)
    get password
    while len(password) < min_length
        print ("Password must be at least {min_length} characters long.")
        get password
    return password

def print_asterisks(password, symbol="*")
    print(symbol * len(password))
"""

def main():
    """Main function to get a valid password and print asterisks."""
    min_length = 5
    password = get_password(min_length)
    print_asterisks(password)

def get_password(min_length):
    """Prompt the user for a password and ensure it is not blank."""
    password = input("Enter your password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password, symbol="*"):
    """Print asterisks equal to the length of the password."""
    print(symbol * len(password))

main()