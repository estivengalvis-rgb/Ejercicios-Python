import math
a=int(input("Ingrese un número entero "))
b=0
while a>0:
    e=a%10
    b=(b*10)+e
    a=math.trunc(a/10)
print("El número invertido es", b)