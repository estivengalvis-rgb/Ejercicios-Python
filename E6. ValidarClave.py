a=0
b=1
c=2
while b<=3 and a!='0119':
    a=str(input("Ingrese la clave de 4 dígitos "))
    if a=='0119':
        print("Acceso permitido")
    else:
        print("Acceso denegado, te quedan", c, "intentos")
        c-=1
        b+=1