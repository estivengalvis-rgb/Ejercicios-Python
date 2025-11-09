a=int(input("Ingrese el primer número "))
b=int(input("Ingrese el segundo número "))
c=int(input("Ingrese el tercer número "))
d=int(input("Ingrese el cuarto número "))
if a>b and a>c and a>d:
    print("El número mayor es", a)
elif b>a and b>c and b>d:
    print("El número mayor es", b)
elif c>a and c>b and c>d:
    print("El número mayor es", c)
elif d>a and d>b and d>c:
    print("El número mayor es", d)
else:
    print("No hay un número mayor")