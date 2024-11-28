"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          26 de noviembre de 2024.
Descripción:    Ejercicios de practica, listas.
                Promedios del parcial 1.
"""
from random import random

# Se crean dos conjuntos de numeros:
conjuntoA = {11, 7, 10, 9, 5, 1, 15, 7}
conjuntoB = {55, 70, 11, 77, 66, 9, 5}
#Operacones basicas:
union = conjuntoA | conjuntoB               # | Union
print(f"conjunto a = {conjuntoA}\n")
print(f"conjunto b = {conjuntoB}\n")
print( union )

interceccion = conjuntoA & conjuntoB
print(interceccion)

# Lista de animales:
lista_de_animales = ["leon", "leopardo", "aguilia", "gato", "capibara", "chapulin", "leopardo", "leon"]
print(f"La lista: {lista_de_animales}")

conjunto_de_listas= set(lista_de_animales)  # Set para convertira a conjuntos
print(conjunto_de_listas)

lista_modificada = list(conjunto_de_listas) # Listas para convertir a listas
print(lista_modificada)
# tuple para convertir a tuplas

#Seleccionar de una lista un numero aleatorio
random.choice(lista_de_animales)