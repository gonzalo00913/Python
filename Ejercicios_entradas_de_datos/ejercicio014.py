ancho_de_terreno = float(input("Ingresa el ancho del terreno: "))
largo_de_terreno = float(input("Ingresa el largo del terreno: "))
valor_de_terreno_tierra = float(input("Ingresa el metro cuadrado de tierra: "))
calculo_metros_cuadrados = ancho_de_terreno * largo_de_terreno
total = calculo_metros_cuadrados * valor_de_terreno_tierra

print(f"Valor total del terreno: {total} metros")


altura_1 = 1 
altura_2 = 2  
altura_3 = 3 

perimetro = 2 * (ancho_de_terreno + largo_de_terreno)
alambre_altura_1 = perimetro * altura_1
alambre_altura_2 = perimetro * altura_2
alambre_altura_3 = perimetro * altura_3

metros_de_alambre = float(input("Ingresa la altura de la cerca de alambre: "))


print(f"Metros de alambre necesarios a {altura_1} metro de altura: {alambre_altura_1} metros")
print(f"Metros de alambre necesarios a {altura_2} metros de altura: {alambre_altura_2} metros")
print(f"Metros de alambre necesarios a {altura_3} metros de altura: {alambre_altura_3} metros")

