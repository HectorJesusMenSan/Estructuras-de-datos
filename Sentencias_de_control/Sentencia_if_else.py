"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          23 de octubre de 2024.
Descripción:    Programa para la práctica de las sentencias if y else.

if condición :
    # datos
    # datos
else :              # Si no se cumple la condición, ejecuta el siguiente segmento de código.
    # datos
# Código que se ejecuta sin importar la condición.


La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.
"""
# Programa que determine si un número es par o impar

numero = int(input("Ingresa un número: "))       # Lectura y conversión de datos a tipo entero.
if numero % 2 == 0:                              # Condición: Si el residuo de la división del número introducido entre 2 es igual a 0.
    print("El número que ingresaste es par")     # Se ejecuta si la condición se cumple.
else:
    print("El número que ingresaste no es par")  # Se ejecuta si la condición no se cumple.
