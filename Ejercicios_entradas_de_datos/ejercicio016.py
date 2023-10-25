segundos = int(input("Ingresa el período de tiempo en segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{segundos} segundos equivalen a {dias} días, {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
