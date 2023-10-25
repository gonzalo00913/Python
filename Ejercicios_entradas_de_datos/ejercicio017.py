cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
resto = cantidad_total
billetes_cien = resto // 100
resto = resto % 100
billetes_cinco = resto // 5
billetes_mil = resto // 1000
billetes_cincuenta = resto // 50
billetes_doscientos = resto // 200
billetes_diez = resto // 10
billetes_docientos = resto // 200
resto = resto % 10
billetes_uno = resto // 1
print("Para la cantidad de  ",cantidad_total,"senecesitan:")
print(billetes_mil,"billetesde 1000")
print(billetes_doscientos, "billetes de  200")
print(billetes_cien,"billetesde 100")
print(billetes_cincuenta, "billetes de  50")
print(billetes_diez,"billetesde 10")
print(billetes_cinco, "billetes de  5")
print(billetes_uno,"billetesde 1")


