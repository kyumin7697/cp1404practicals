"""
pseudocode:
for i from 0 to 100, step by 10
    print i

for i from 20 down to 1, step by -1
    print i

get number of stars
for i from 0 to n-1
    print "*"
s
for i from 1 to n
    print "*" repeated i times
"""

# (a) Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# (b) Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# (c) Print n stars on one line
n = int(input("Number of stars: "))
for i in range(n):
    print("*", end='')
print()

# (d) Print n lines of increasing stars
for i in range(1, n + 1):
    print("*" * i)