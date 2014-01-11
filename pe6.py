print("Project Euler Problem #6")

sum = 0
for i in range(1,101):
    sum += i
sqofsum = sum**2
sumofsq = 0
for i in range(1,101):
    sumofsq += (i**2)
diff = sqofsum-sumofsq
print(diff)
