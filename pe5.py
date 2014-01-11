



def isDiv(n):
    for p in range(19,11,-1):
        if (n%p != 0):
            return False
    return True

x = 2520
cont = True
while (cont):    
    if isDiv(x):
        print(x) 
        cont = False
    else:
        x+=20
