"""
pseudocode:
get name

print menu
(H)ello
(G)oodbye
(Q)uit

get choice (convert to uppercase)

while choice != Q:
    if choice == H:
        print "Hello" and name
    else if choice == G:
        print "Goodbye" and name
    else:
        print "Invalid choice"

    print menu again
    get choice

print "Finished."
"""

name = input("Enter name: ")

print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = input(">>> ").upper()

print("Finished.")