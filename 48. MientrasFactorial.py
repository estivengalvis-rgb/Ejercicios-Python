a=int(input("Ingrese un número"))
if a<0:
    print("No se puede calcular el factorial")
else:
    fc=1
    inf=1
    while inf<=a:
        fc*=inf
        inf+=1
print("El número factorial es",fc)