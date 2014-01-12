print("Project Euler Problem #11")

f = open("pe11input")
lines = []
for i in range(0,20):
    lines.append(f.readline())
    lines[i] = lines[i].replace('\n','')
    lines[i] = lines[i].split(' ')
for i in range(0,20):
    for j in range(0,20):
        lines[i][j] = int(lines[i][j])
big = 0
for i in range(0,20):
    for j in range(0,17):
        prod = 1
        for k in range(0,4):
            prod *= lines[i][j+k]
        if prod > big:
            big = prod
for i in range(0,17):
    for j in range(0,20):
        prod = 1
        for k in range(0,4):
            prod *= lines[i+k][j]
        if prod > big:
            big = prod
for i in range(0,17):
    for j in range(0,17):
        prod = 1
        for k in range(0,4):
            prod *= lines[i+k][j+k]
        if prod > big:
            big = prod
for i in range(19,3,-1):
    for j in range(0,17):
        prod = 1
        for k in range(0,4):
            prod *= lines[i-k][j+k]
        if prod > big:
            big = prod
print(big)
