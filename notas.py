print("Bienvenido a el software de Calificaciones")

estudiantes = []
notas_mision1 = []
notas_mision2 = []
notas_mision3 = []

while True:
    estudiante = input("ingrese el nombre del estudiante ")
    if estudiante == "salir":
        break
    nota1 = float(input("ingrese la nota de la mision 1: "))
    nota2 = float(input("ingrese la nota de la mision 2: "))
    nota3 = float(input("ingrese la nota de la mision 3: "))
    estudiantes.append(estudiante)
    notas_mision1.append(nota1)
    notas_mision2.append(nota2)
    notas_mision3.append(nota3)

for i in range(len(estudiantes)):
    promedio = (notas_mision1[i] + notas_mision2[i] + notas_mision3[i])/3
    print(f"el estudiante {estudiantes[i]} tiene un promedio de {promedio}")

