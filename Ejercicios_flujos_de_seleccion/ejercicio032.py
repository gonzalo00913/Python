def viaje(total_km):
    tarifa_minima = 50  
    tarifa_km_0_10 = 20 
    tarifa_km_10_plus = 15  

    if total_km <= 0:
        return "La distancia debe ser mayor que 0 km"
    elif total_km <= 10:
        precio_viaje = tarifa_minima + total_km * tarifa_km_0_10
    else:
        precio_viaje = tarifa_minima + 10 * tarifa_km_0_10 + (total_km - 10) * tarifa_km_10_plus

    return f"El precio del viaje es: ${precio_viaje}"


try:
    km_deseados = float(input("Ingrese la cantidad de km que desea recorrer: "))
    resultado = viaje(km_deseados)
    print(resultado)
except ValueError:
    print("Por favor, ingrese una cantidad válida de km.")
