"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          23 de octubre de 2024.
Descripción:    Programa para la practica de las sentencias if y else

if condición :
    #datos
    #datos
else :              #Si no cumple la condicion ejecuta el siguiente segmento de codigo
    #datos
# Código que se ejecuta sin importar la condición.
"""
#programa que determine si un número es par o impar

numero = int(input("Ingresa un número: "))      # Lectura y conversion de datos a tipo entero.
if numero%2==0:                                 # Condicion: Si el residuo de la division del numero introducido entre 2 es = 0.
    print("El número que ingresate es par")     # Se ejecuta si la condicion se cumple.
else:
    print("El número que ingresate no es par")  #Se ejecuta si la condicion no se cumple.
