"""
def main
    display_menu
    get choice and convert to uppercase
    while choice != Q
        if choice == C
            get celsius
            convert to fahrenheit using convert_c_to_f
            display result
        else if choice == F
            get fahrenheit
            convert to celsius using convert_f_to_c
            display result
        else
            print "invalid option"
        display menu
        get choice
    print "thank you"

define display_menu
    print menu options

define convert_c_to_f(celsius)
    return converted fahrenheit

define convert_f_to_c(fahrenheit)
    return converted celsius
"""

def main():
    """Main function to run the temperature conversion program."""
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_c_to_f(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_f_to_c(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        display_menu()
        choice = input(">>> ").upper()
    print("Thank you.")

def display_menu():
    """Display the menu of options for temperature conversion."""
    print("C - Convert Celsius to Fahrenheit")
    print("F - Convert Fahrenheit to Celsius")
    print("Q - Quit")

def convert_c_to_f(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_f_to_c(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9

main()