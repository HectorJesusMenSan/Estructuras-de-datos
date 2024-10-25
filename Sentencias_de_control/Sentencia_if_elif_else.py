"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          23 de octubre de 2024.
Descripción:

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