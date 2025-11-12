a=int(input("Ingrese la cantidad de estudiantes "))
cnt=0
apr=0
rpr=0
sum=0
while cnt<a:
    cod=str(input("Ingrese el código del estudiante "))
    prm=float(input("Ingrese su nota definitiva "))
    if prm>=3:
        apr+=1
    else:
        rpr+=1
    sum+=prm
    cnt+=1
prmg=sum/a
print("La cantidad de aprobados es", apr)
print("La cantidad de reprobados es", rpr)
print("El promedio del salón es", prmg)