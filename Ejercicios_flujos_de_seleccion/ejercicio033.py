def calcular_descuento_precio(importe):
    if importe < 5500.0:
        descuento = importe * 0.045  # Descuento del 4.5%
    elif importe <= 10000.0:
        descuento = importe * 0.08  # Descuento del 8%
    else:
        descuento = importe * 0.105  # Descuento del 10.5%

    precio_neto = importe - descuento

    print(f"Importe de la compra: ${importe:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Precio neto a cobrar: ${precio_neto:.2f}")


importe_compra = float(input("Ingrese el importe de la compra: "))

calcular_descuento_precio(importe_compra)
