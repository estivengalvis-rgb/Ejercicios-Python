A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
print(
1. Intercambiar A ↔ B
2. Intercambiar B ↔ C
3. Intercambiar A ↔ C
4. Rotar valores
5. Mayor y menor (la menor toma el doble del mayor)
6. C = A + B)
op=int(input("Opción: "))
if op == 1:
    A, B = B, A
elif op == 2:
    B, C = C, B
elif op == 3:
    A, C = C, A
elif op == 4:
    A, B, C = B, C, A
elif op == 5:
    mayor = max(A, B, C)
    if A == min(A, B, C):
        A = mayor * 2
    elif B == min(A, B, C):
        B = mayor * 2
    else:
        C = mayor * 2
elif op == 6:
    C = A + B
else:
    print("Opción no válida")
print("A =", A)
print("B =", B)
print("C =", C)
