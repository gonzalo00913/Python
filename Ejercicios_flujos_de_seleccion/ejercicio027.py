def rango_edad (edad, genero):
    if edad < 1 or edad > 120:
        print(f"Edad fuera de rango para {nombre}.")
    elif genero != 'F' and genero != 'M':
        print(f"Género inválido para {nombre}.")
    elif genero == 'F' and edad >= 60:
        print(f"{nombre} Jubilate.")
    elif genero == 'M' and edad >= 65:
        print(f"{nombre} Jubilate.")
    else:
        print(f"{nombre} No se puede jubilar.")

nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad (entre 1 y 120 años): "))
genero = input("Ingresa el género ('F' para mujeres, 'M' para hombres): ")

rango_edad(edad, genero)
