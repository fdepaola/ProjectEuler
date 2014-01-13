print("Project Euler Problem #14")

def collatzChain(x):
    global dict
    i = x
    c = 1
    while not i == 1:
        if i in dict:
            c+=dict[i]
            dict[x] = c
            return c
        if i%2 == 0:
            i /= 2
            dict[x] = c
        else:
            i = 3*i+1
            dict[x] = c
        c+=1
    return c

dict = {}
max = 1000000
big = 0
bigc = 0
for i in range(13,max):
    t = collatzChain(i)
    if t > bigc:
        big = i
        bigc = t
print(big)
