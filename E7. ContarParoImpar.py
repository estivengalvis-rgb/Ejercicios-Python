a=1
b=0
c=0
while a!=0:
    a=int(input("Ingrese un número: "))
    if a%2==0:
        b+=1
    else:
        c+=1
print("La cantidad de números pares es:", b)
print("La cantidad de números impares es:", c)