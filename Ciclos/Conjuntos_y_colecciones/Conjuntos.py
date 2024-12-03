"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          25 de noviembre de 2024.
Descripción:    Programa de introduccion
                a conjuntos.
"""


"""
Un conjunto es desordenado y es mutable
"""
# Para crear conjunto vacio:
conjunto_nombres= set()
conjunto_nombres : {print(conjunto_nombres)}


# Se añaden valores al conjunto:
conjunto_nombres.add("Rebeca")
conjunto_nombres.add("juan")
conjunto_nombres.add("ryan")
conjunto_nombres.add("Yam")
conjunto_nombres.add("gali")
conjunto_nombres.add("Marlen")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Yo")
conjunto_nombres.add("pati")
conjunto_nombres.add("addi")
conjunto_nombres.add("Alberto")
conjunto_303:{print(conjunto_nombres)}
#Intento nombres repetidos:
conjunto_nombres.add("Rebeca")
conjunto_303:{print(conjunto_nombres)}
#Elimira un dato de un conjunto
conjunto_nombres.remove("juan")
conjunto_303:{print(conjunto_nombres)}
#mostrar datos
for nombre in conjunto_nombres:
    print(nombre, end=",")
# Verifica si un elemento pertenecea a un conjunto
print(f"El elemento {nombre} pertenece al conjunto? {nombre in conjunto_nombres}")


Conjunto_De_Numeros={1, 1.2, 3.2, 4.1}
#Funcion tamaño del conjunto:
tamaño_de_conjunto= len(Conjunto_De_Numeros)
#Funcin para sumar todos los elementos:
suma_de_los_elementos: sum(Conjunto_De_Numeros)

