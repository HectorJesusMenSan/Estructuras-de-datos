"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Ejercicio de introducción a los
                ciclos while, el programa intenta
                solicitar un número inicial y un número final
                y hacer la suma acumulativa de todos los números
                que existen dentro de ese rango de números
                dados por el usuario.
"""
"""Calcula la suma acumulativa entre dos números"""

# Escritura de letreros interactivos.
"""Programa que calcula la suma acumulativa"""
print("#Cargando programa: Suma acumulativa#")
print("-_-\n")

# Solicitud de datos:
numero_inicial = int(input("Ingresa el número que marque el inicio: "))
numero_final = int(input("Ingresa el número que marque el final: "))

sumatoria = 0
print(f"La suma desde {numero_inicial} hasta {numero_final}")
while numero_inicial <= numero_final:
    sumatoria += numero_inicial
    numero_inicial += 1
"""-El ciclo: mientras el número inicial sea menor o igual al número
    final, se crea antes una variable que llevará el registro de las sumatorias.
    Este acumulará la suma del número inicial más el número anterior que valía la sumatoria,
    y solo se aumentará el valor de la variable del número inicial.
    Al final, solo se muestra la variable que registra la sumatoria."""

print(f"La suma final es: {sumatoria}")
