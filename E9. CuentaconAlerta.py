a=int(input("Ingrese un número entero: "))
for a in range(a, -1, -1):
    if a%7==0:
        print(a, "Alerta")
    else:
        print(a)