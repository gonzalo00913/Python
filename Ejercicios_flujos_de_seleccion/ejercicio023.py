# Solicitar al usuario que ingrese tres números
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))

def encontrar_extremos(numero_uno, numero_dos, numero_tres):
    # Encontrar el número mayor
    mayor = max(numero_uno, numero_dos, numero_tres)
    # Encontrar el número menor
    menor = min(numero_uno, numero_dos, numero_tres)
    # Encontrar el número en medio
    medio = numero_uno + numero_dos + numero_tres - mayor - menor
    return mayor, medio, menor



# Llamar a la función para encontrar los extremos
mayor, medio, menor = encontrar_extremos(numero_uno, numero_dos, numero_tres)

# Mostrar los resultados
print("El mayor es:", mayor)
print("El medio es:", medio)
print("El menor es:", menor)
