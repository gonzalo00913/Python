def edadAltura(edad, altura):
    LIMITE_EDAD = 6
    LIMITE_ALTURA = 1.5
    if edad >= LIMITE_EDAD and altura >= LIMITE_ALTURA:
        print("Podes entrar")
    else:
        print("No cumples con los requisitos de edad y altura para entrar.")

edad = int(input("Edad: "))
altura = float(input("Altura: "))

edadAltura(edad, altura)




