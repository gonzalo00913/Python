numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))


mayor = max(numero1, numero2)
menor = min(numero1, numero2)


if mayor % menor == 0:
    print(f"{mayor} es divisible por {menor}.")
else:
    print(f"{mayor} no es divisible por {menor}.")