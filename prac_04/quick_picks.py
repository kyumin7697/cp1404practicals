"""
MIN = 1
MAX = 45
NUMBERS_PER_PICK = 6

get number_of_picks

for i in range(num_picks)
numbers = []
    while len(numbers) < NUMBERS_PER_PICK
        number = random.randint(MIN, MAX)
        if number not in numbers
            numbers.append(number)
    numbers.sort()
    print number for n in numbers
"""

import random

MIN = 1
MAX = 45
NUMBERS_PER_PICK = 6

num_picks = int(input("How many quick picks? "))

for i in range(num_picks):
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN, MAX)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print(" ".join(f"{n:2}" for n in numbers))
