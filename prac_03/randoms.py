"""
random function
"""
import random

print(random.randint(5, 20))
#What did you see on line 1?
#a random number between 5 <= x <= 20
#What was the smallest number you could have seen, what was the largest?
#min = 5, max = 20

print(random.randrange(3, 10, 2))
#What was the smallest number you could have seen, what was the largest?
#min = 3, max = 9
#Could line 2 have produced a 4?
#No

print(random.uniform(2.5, 5.5))
#What did you see on line 3?
#a random floating-point number between 2.5 and 5.5
#What was the smallest number you could have seen, what was the largest?
#min = 2.5, max < 5.5

print(random.randint(1, 100))
