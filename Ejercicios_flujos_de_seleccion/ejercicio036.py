def operacion_matematicas(num0, operacion, num1):
    if operacion == "+":
        return num0 + num1
    elif operacion == "-":
        return num0 - num1
    elif operacion == "*":
        return num0 * num1
    elif operacion == "/":
        if num1 != 0:
            return num0 / num1
        else:
            return "Error: División por cero"

num0 = float(input("Ingresa un número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")
num1 = float(input("Ingresa otro número: "))

resultado = operacion_matematicas(num0, operacion, num1)
print("Resultado:", resultado)