def cuanto_falta(invitados, asientos):
    if invitados == asientos:
      print("no falta ningun asiento")
    elif invitados != asientos:
        print(f"faltan {invitados % asientos} asientos para los invitados")



invitados = int(input("Ingresa la cantidad de invitados: "))
asientos = int(input("Ingresa la cantidad de asientos disponible: "))

cuanto_falta(invitados,asientos)

