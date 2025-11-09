print("Tipo1=12.5%")
print("Tipo2=8.3%")
print("Tipo3=3.2%")
a=str(input("Ingrese el tipo de artículo "))
if a=='Tipo1' or a=='tipo1':
    print("Tiene un descuento del 12.5%")
elif a=='Tipo2' or a=='tipo2':
    print("Tiene un descuento del 8.3%")
elif a=='Tipo3' or a=='tipo3':
    print("Tiene un descuento del 3.2%")
else:
    print("No tiene descuento")