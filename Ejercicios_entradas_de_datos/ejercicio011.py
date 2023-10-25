persona_1 = float(input("Ingrese la cantidad invertida por la persona 1: "))
persona_2 = float(input("Ingrese la cantidad invertida por la persona 2: "))
persona_3 = float(input("Ingrese la cantidad invertida por la persona 3: "))

total = persona_1 + persona_2 + persona_3

porcentaje_inversion_persona1 = round((persona_1 / total) * 100, 2)
porcentaje_inversion_persona2 = round((persona_2 / total) * 100, 2)
porcentaje_inversion_persona3 = round((persona_3 / total) * 100, 2)


cartel = f"Gonzalo Masa = {porcentaje_inversion_persona1}, Raul Benitez = {porcentaje_inversion_persona2},Emiliano Rojas = {porcentaje_inversion_persona3} "

print(cartel)

