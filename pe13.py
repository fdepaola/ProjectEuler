import math

print("Project Euler Problem #13")

f = open("pe13input")
lines = []
sum = 0
for i in range(0,100):
    lines.append(f.readline())
    lines[i] = int(lines[i])
    sum += lines[i]
digits = int(math.log10(sum))+1
trunc = digits-11
print(int(sum/(10*10**trunc)))
