sueldo_base = 100.00
aumento_sueldo_soltero = 0.05
aumento_sueldo_casado = 0.07
descuento_sueldo_jubilación = 0.11
descuento_obra_social = 0.03
descuento_suelddo_sindicato = 0.03

def sueldo_empleado(sueldo, antiguedad, estado_civil):
    if estado_civil == "S":
        sueldo += (aumento_sueldo_soltero * antiguedad)
    elif estado_civil == "C":
        sueldo += (aumento_sueldo_casado * antiguedad)
    

    jubilacion = sueldo * descuento_sueldo_jubilación
    obra_social = sueldo * descuento_obra_social
    sindicato = sueldo * descuento_suelddo_sindicato

    sueldo_neto = sueldo - jubilacion - obra_social - sindicato
    
    return sueldo_neto

sueldo = float(input("Ingrese su sueldo fijo: "))
antiguedad = int(input("Ingrese su antigüedad: "))
estado_civil = input("Ingrese su estado civil (S/C): ")

resultado = sueldo_empleado(sueldo, antiguedad, estado_civil)
print(resultado)
