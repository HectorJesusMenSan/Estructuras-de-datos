"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          23 de octubre de 2024.
Descripción:    Forma de usar la sentencia elif.
                La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial.
                Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición
                que sea verdadera.

if condición :
    # datos
    # datos
else :
    # datos
elif condición:
    # datos
else:
"""

# Determinar el grupo de edad:
# <14 niños y adolescentes, 15 y 25 jóvenes, 26 y 45 adultos jóvenes, 46 y 60 adultos maduros,
# >60 adultos mayores.
edad = int(input("Ingresa tu edad: "))  # Esto lee datos introducidos por el usuario, los convierte en entero y los almacena.
if edad <= 14:                           # Condición: si la edad es menor o igual a 14.
    print("Grupo de niños y adolescentes.") # Imprime solo si se cumple la condición.
elif edad >= 15 and edad <= 25:         # Condición: si la edad es mayor o igual a 15 y menor o igual a 25.
    print("Grupo de jóvenes")           # Escribe solo si se cumple la condición.
elif edad >= 26 and edad <= 45:         # Condición: si la edad es mayor o igual a 26 y menor o igual a 45.
    print("Grupo de adultos jóvenes")   # Escribe solo si se cumple la condición.
elif edad >= 46 and edad <= 60:         # Condición: si la edad es mayor o igual a 46 y menor o igual a 60.
    print("Grupo de adultos maduros")   # Escribe solo si se cumple la condición.
elif edad > 60:                         # Condición: si la edad es mayor a 60.
    print("Adultos mayores")            # Escribe solo si se cumple la condición.
