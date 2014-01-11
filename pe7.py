import math

print("Project Euler Problem #7")

def isPrime(x):
    for j in range(2,math.floor(x/2)):
        if (x % j == 0):
            return False
    return True

n = 6
test = 14
while (n < 10001):
    if (isPrime(test)):
        n += 1
    if (n != 10001):
        test += 1
print(test)
