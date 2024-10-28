"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          23 de octubre de 2024.
Descripción:    Forma de usar la sentencia elif.
                La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial.
                Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición
                que sea verdadera.

if condición :
    #datos
    #datos
else :
    #datos
eluf:
    #datos
else
"""

# Determinar el grupo de edad:
#<14 niños y adolecentes, 15 y 25 jovenes, 26 y 45 adultos juvenes, 46 y 60 adultos maduros
# >60 adultos mayores
edad = int(input("ingresa tu edad: "))
if  edad<=14:
    print("grupo de niños y adolecentes.")
elif edad >= 15 and edad <= 25:
    print("grupo de jovenes")
elif edad >= 46 and edad<=60 :
    print("grupo de adultos jovenes")
elif edad>60 :
    print("adultos mayores")