"""
pseudocode:
set total_price to 0

get items_number from user
while items_number < 0
    print "Invalid number of items!"
    get items_number again

for i from 1 to items_number
    get item price
    add item price to total_price

if total_price > 100
    total_price *= 0.9

print items_number and total price with 2 decimal places
"""

total_price = 0

items_number = int(input("Number of items: "))
while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Number of items: "))

for i in range(1, items_number+1):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {items_number} items is ${total_price:.2f}")