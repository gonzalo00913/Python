nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

notas = f"Nota 1:{nota1}, Nota 2: {nota2}, Nota 3: {nota3}"
sumar_notas = nota1 + nota2 + nota3

cartel = f"Promedio: {sumar_notas / 3}"
print(notas)
print(cartel)
