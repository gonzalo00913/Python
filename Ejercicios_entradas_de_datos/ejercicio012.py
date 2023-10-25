medida_angulo_1 = int(input("Ingrese el valor en grados del primer ángulo: "))
medida_angulo_2 = int(input("Ingrese el valor en grados del segundo ángulo: "))

if medida_angulo_1 < 0 or medida_angulo_2 < 0:
    print("Los ángulos no pueden ser negativos.")
elif medida_angulo_1 + medida_angulo_2 >= 180:
    print("La suma de los ángulos ingresados es mayor o igual a 180 grados.")
else:
    angulo_restante = 180 - (medida_angulo_1 + medida_angulo_2)
    print(f"El valor en grados del ángulo restante es: {angulo_restante} grados.")
