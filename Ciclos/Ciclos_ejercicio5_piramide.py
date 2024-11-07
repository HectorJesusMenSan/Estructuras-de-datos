"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          7 de noviembre de 2024.
Descripción:    Ejercicio 5, Piramide:
Pedir a usuario un dato que demarque
la cantidad de filas de la priamide.
"""
from sys import prefix

contador=0
valor_de_filas = int(input("Introduce el numero de filas que tenga tu piramide: "))
# a)
for asteriscos in range(1, valor_de_filas+1):
    contador+=1
    for asteriscos in range(1, contador+1):
        print("*", end=" ")
    print("\n")
print("______________________________________________________________________")
contador=valor_de_filas
# b)
for asteriscos in range(1, valor_de_filas+1):

    for asteriscos in range (contador):
        print("*", end=" ")
    print("\n")
    contador -= 1
print("______________________________________________________________________")

# c)
contador=valor_de_filas
escrituras=0
espacios=0
for asteriscos in range(1, valor_de_filas+1):
    escrituras="*" * contador
    espacios=" " * asteriscos
    print(f"{espacios}{escrituras}")
    contador-=1
print("______________________________________________________________________")
# d)
contador=valor_de_filas
contador=0
for asteriscos in range(1, valor_de_filas+1):
    escrituras="*" * (contador + 1)
    espacios=" " * (valor_de_filas-asteriscos)
    contador+=2
    print(f"{espacios}{escrituras}")




