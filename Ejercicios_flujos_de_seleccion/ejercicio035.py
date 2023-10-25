numero = 15

esDeUnSoloDigito =  -9 <= numero <= 9

esImpar = (numero%2) != 0 

estaEnAmbos = esDeUnSoloDigito and esImpar
noEstaEnNinguno =  not estaEnAmbos


print(
f"""
El numero {numero} tiene un solo digito: {esDeUnSoloDigito}
El numero {numero} es impar: {esImpar}
El numero {numero} esta en ambos: {estaEnAmbos}
El numero {numero} no esta en ninguno: {noEstaEnNinguno}"""
)

print(f"""

{numero} 
estaEnAmbos {estaEnAmbos} 
noEstaEnNinguno {noEstaEnNinguno}
esDeUnSoloDigito {esDeUnSoloDigito}
esImpar {esImpar}""")