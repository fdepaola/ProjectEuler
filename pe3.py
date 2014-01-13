import math
print("Project Euler Problem #3\n")

def isPrime(x):
    for j in range(2,math.ceil(math.sqrt(x/2))):
        if (x % j == 0):
            return False
    return True

n = 600851475143
lpf = 0
m = math.floor(n**.5)
for i in range(m, lpf, -1):
    if (n % i == 0):    # i is a factor of n
        if (isPrime(i)):
            print(i)
            exit()
