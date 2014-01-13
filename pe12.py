print("Project Euler Problem #12")

def sieve(x):
    global primes
    primes = [True] * x
    for i in range(2,round(x**.5)+1):
        if primes[i]:
            for j in range(i+i,x,i):
                primes[j] = False

def powerXinY(x,y):
    n = 0
    while y%x == 0:
        n+=1
        y = y/x
    return n

def primeFactors(x):
    global primes
    factors = []
    for p in range(2,high):
        if primes[p]:
            if p*p > x: break
            if x%p == 0:
                factors.append(p)
    return factors

limit = 500
num = 1
triangle = 0
nfact = 0
max = 0
high = int(2e6)

sieve(high)
while nfact <= limit:
    triangle += num
    if not triangle%2 == 0:
        num+=1
        triangle += num
    factors = primeFactors(triangle)
    nfact = 1
    for f in factors:
        nfact *= 1+powerXinY(f,triangle)
    if nfact > max:
        max = nfact
    num += 1

print(triangle)
