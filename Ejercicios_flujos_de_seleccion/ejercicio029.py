def notas_de_alumno(nota):
    if nota > 10 or nota < 0:
      print("Error la nota deber ser del 1 al 10") 
    elif nota >= 7:
      print(f"tu nota es {nota}, por lo tanto seras promocianado")
    elif nota > 4:
      print(f"tu nota es {nota}, estas aprobado")
    elif nota < 4:
      print (f"tu nota es {nota}, por lo tanto necestias recuperar")


mi_nota = int(input("Ingresa la nota de el alumno del 1 al 10: ")) 

notas_de_alumno(mi_nota)
