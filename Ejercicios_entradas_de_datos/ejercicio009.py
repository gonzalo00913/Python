num1 = int(input("Ingrese un valor de numerico: ")) 
num2 = int(input("Ingrese un valor de numerico: ")) 

cartel = f"valor del numero 1 = {num1}, valor del numero 2 = {num2}"

print(cartel)

num1 = num1 + num2 
num2 = num1 - num2 
num1 = num1 - num2 

print(num1, num2)
