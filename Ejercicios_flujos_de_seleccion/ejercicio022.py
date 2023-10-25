num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
num3 = int(input("ingresa un numero: "))

def mayor_menor_igual(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"El numero {num1} es mayor a numero {num2} y {num3}")
    elif num2 > num1 and num2 > num3:
       print(f"El numero {num2} es mayor a numero {num1} y {num3}")
    elif num3 > num1 and num3 > num2:   
       print(f"El numero {num3} es mayor a numero {num1} y {num2}")
    else:
       print(f"Todos los numeros son iguales") 

mayor_menor_igual(num1,num2,num3)