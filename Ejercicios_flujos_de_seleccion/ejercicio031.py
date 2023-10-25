COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880

def calcular_costo_libro(paginas):
    if paginas <= 300:
        return COSTO_BASICO + paginas * COSTO_POR_PAGINA
    elif 301 <= paginas <= 600:
        return COSTO_ENC_RUSTICA + paginas * COSTO_POR_PAGINA
    else:
        return COSTO_ENC_ESPECIAL + paginas * COSTO_POR_PAGINA

paginas_del_libro = int(input("Ingresa la cantidad de páginas del libro: "))
costo = calcular_costo_libro(paginas_del_libro)
print(f"El costo del libro es: {costo}")
