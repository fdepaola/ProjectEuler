import math

print("Project Euler Problem #10")

primes = [2,3,5,7]

def isPrime(x):
    for j in range(2,math.ceil(x**.5+1)):
        if (x % j == 0):
            return False
    return True

for i in range(9,2000000,2):
    if isPrime(i):
        primes.append(i)

print(sum(primes))
