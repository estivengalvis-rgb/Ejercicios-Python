a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a + b > c and a + c > b and b + c > a:
    print("Forma un triángulo válido.")
    if a == b == c:
        print("Tipo: Equilátero.")
    elif a == b or b == c or a == c:
        print("Tipo: Isósceles.")
    else:
        print("Tipo: Escaleno.")
else:
    print("No es un triángulo válido.")
