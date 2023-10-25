LIMITE_EDAD = 10
LIMITE_ALTURA = 1.6


nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura: "))

entra_edad = edad >= LIMITE_EDAD
entra_altura = altura > LIMITE_ALTURA
entra = entra_edad and entra_altura



#  False == True
if entra:
    cartel = "Entraste"
else:
    cartel = "No entras"
    if not entra_altura:
        cartel += " altura"
    if not entra_edad:
        cartel += " edad"    

print(f"{nombre} {cartel}")