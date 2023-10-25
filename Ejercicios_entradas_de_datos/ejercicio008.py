valor_hora = float(input("Ingrese el valor monetario de una hora de trabajo: "))
horas_trabajadas_por_dia = float(input("Ingrese la cantidad de horas trabajadas por día: "))

salario_diario = valor_hora * horas_trabajadas_por_dia
dias_habiles = 5
horas_sabado = horas_trabajadas_por_dia / 2
salario_sabado = valor_hora * horas_sabado

salario_semanal = (salario_diario * dias_habiles) + salario_sabado

calcular_salario = f"Usted gana un total de ${salario_semanal:.2f} dólares."

print(calcular_salario)
