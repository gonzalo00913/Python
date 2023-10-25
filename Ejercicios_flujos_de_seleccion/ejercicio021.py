num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))

def mayor_menor_igual(num1,num2):
    if num1 > num2:
        print(f"El numero {num1} es mayor a numero {num2}")
    elif num1 < num2:
         print(f"El numero {num1} es menor a numero {num2}")
    else:
       print(f"El numero {num1} es igual a numero {num2}")


mayor_menor_igual(num1,num2)