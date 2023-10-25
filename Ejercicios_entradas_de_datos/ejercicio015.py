vendedor = input("Ingresa tu nombre: ")
cantidad_vendida = float(input("Ingresa la cantidad de ventas realizadas: "))

salario_base = 100
comision = 0.05

total = cantidad_vendida * comision

resultado = salario_base + total

 
print(f"El vendedor {vendedor} realizo {cantidad_vendida} ventas y tiene un total de {resultado} ganado")

