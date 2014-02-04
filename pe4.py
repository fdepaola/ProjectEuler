print("Project Euler Problem #4\n")

def isPal2(x):
    y = str(x)
    b = x[::-1]
    if b == y:
        return True
    return False

'''
def isPal(x):
    y = str(x)
    ly = len(y) - 1
    s = 0
    while (s < ly/2):
        if (y[s] != y[ly-s]):
            return False
        s+=1
    return True
'''

start = 100
end = 999
m = 0

for i in range(end, start, -1):
    for j in range(end, start, -1):
        p = i*j
        if (isPal2(p) and p > m):
            m = p
print(m)
