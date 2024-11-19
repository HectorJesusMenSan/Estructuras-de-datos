"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:    Promapa para introducirnos en el temna"""


"""
-Ordenada
-Inmutable
-Los elemntos se encierran entre parentesis
"""

print("#PRIMER EJEMPLO DE TUPLAS:#")
fechas_cumple=('12-19', '12-27', '12-27', '01-10', '10-18')
print("Las fechas de cumpleaños son: ", fechas_cumple)

print("Inpresion uno por uno con for: ")
for fecha in fechas_cumple:
    print(fecha, end=" ")

#Series
print()
pi_serie=(4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, -4/15, 4/17,- 4/19, 4/21, -4/23)
print(sum(pi_serie[0: 1]))
#sumatorias de un rango a otro.
print(sum(pi_serie[0: 4]))
print(sum(pi_serie[0: 7]))
print(sum(pi_serie[0: 9]))
print(sum(pi_serie[0: 10]))


#Coordenadas:
punto1=(1,0)
punto2=(5,3)
print(f"Coordenadas en tuplas: {punto1} {punto2}")
#Desempaquetado de duplas:
x1, y1 = punto1
x2, y2 = punto2
#Expresion de la recta Y=mx+b
m=(y2-y1)/(x2-x1)
b=y1-m*x1
print(m)
print(f"y={m}x + {b}")