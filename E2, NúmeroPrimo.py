import math
a=float(input("Ingrese un número positivo "))
b=int(math.sqrt(a))+1
c=2
e=0
for c in range(2,b):
    d=a%c
    if d==0:
        e+=1
    

if e==0:
    print("Es un número primo")
else:
    print("No es un número primo")
        