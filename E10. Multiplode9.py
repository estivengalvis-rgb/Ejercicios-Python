a=int(input("Ingrese el primer rango: "))
b=int(input("Ingrese el segundo rango: "))+1
c=0
d=0
e=1
for i in range(a, b):
    if i%9==0 and e==1:
        c+=i
        e+=1
    else:
        d+=1
if c==0:
    print("No hay número multiplo de 9")
else:
    print("El primer multiplo de 9 es:", c)
