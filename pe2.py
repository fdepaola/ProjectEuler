print("Project Euler Problem #2\n")
sum = 0
max = 4000000
one = 1
two = 1
while (two < max):
    next = two + one
    one = two
    two = next
    if (two % 2 == 0):
        sum += two
print(sum)
