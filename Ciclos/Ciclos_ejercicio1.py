"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    ciclos.
"""

"""programa que calcula la suma acomulativa"""

numero_ingresado = int(input("ingresa un numero que marque el final: "))
contador=0
registro_de_suma=0

print(f"la suma de 0 hasta {numero_ingresado} es: ")
while contador <= numero_ingresado :
    registro_de_suma=registro_de_suma+contador
    contador+=1
print(registro_de_suma)