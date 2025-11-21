import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Ecuación degenerada: infinitas soluciones.")
        else:
            print("Inconsistente: sin solución.")
    else:
        x = -c / b
        print("Ecuación lineal.")
        print("x =", x)

else:
    D = b*b - 4*a*c
    print("Discriminante =", D)

    if D > 0:
        print("Dos raíces reales diferentes.")
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

    elif D == 0:
        print("Dos raíces reales iguales.")
        x1 = x2 = -b / (2*a)

    else:
        print("No tiene raíces reales.")
        exit()

    print("x1 =", x1)
    print("x2 =", x2)

    # Clasificación por signo
    if x1 > 0 and x2 > 0:
        print("Ambas raíces positivas.")
    elif x1 < 0 and x2 < 0:
        print("Ambas raíces negativas.")
    else:
        print("Una positiva y una negativa.")
