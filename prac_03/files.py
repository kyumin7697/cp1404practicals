"""
Practical file
"""

# 1.
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# 2.
file = open("name.txt", "r")
name_from_file = file.read()
file.close()
print(f"Hi {name_from_file}!")

# 3.
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
    print(result)

# 4.
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)