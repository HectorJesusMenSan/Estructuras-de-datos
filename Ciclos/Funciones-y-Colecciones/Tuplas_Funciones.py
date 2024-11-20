"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:    Promapa para introducirnos en el temna"""


#Con las tuplas se pueden devolver valores, como en una funcion

###########Calificacion de

def calificacion(calificaciones):
    promedio_parcial = sum(calificaciones [0:2])/3
    promedio_final = promedio_parcial + promedio_parcial[3]/2
    tupla_promedios = (promedio_parcial, promedio_final)
    return tupla_promedios

calificaciones_usuario=[]
for i in range (0, 4):
    if i<3:
        calificacion_1=input(f"Ingresa calificacion parcial {i+1}: ")
        calificaciones_usuario.append(calificacion_1)
    else:
        calificacion_1 = input(f"Ingresa calificacion ordinario: ")
        calificaciones_usuario.append(calificacion_1)

print(f"Prpmedio parcial: {calificacion(calificaciones_usuario)[0]}")