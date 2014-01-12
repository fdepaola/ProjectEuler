from math import floor

print("Project Euler Problem #12")

def numFactors(x):
    f = 2
    if x%2 == 0:
        x = x/2 -1
        f += 2
    for i in range(3,floor(x/2)):
        if x%i == 0:
            f += 1
    return f

limit = 500
num = 1
triangle = 0
factors = 0

while factors <= limit:
    triangle += num
    factors = numFactors(triangle)
    num += 1

print(triangle)
