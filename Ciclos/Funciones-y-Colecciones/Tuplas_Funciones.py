"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:    Promapa para introducirnos en el temna"""


#Con las tuplas se pueden devolver valores, como en una funcion

###########Calificacion de

def calificacion(calificaciones):
    promedio_parcial = sum(calificaciones[0:3])/ 3
    """En esta parte la funcion sum, suma de los numero 0, como tal interactuamos con el vector, el 3
    agarra de las casillas como conocemos al 3-1, osea la casilla numero 2. por lo cual, sumara
    de las calificaciones parcial 1, 2 y 3
    
    
    
    """
    promedio_final = (promedio_parcial + calificaciones[3])    / 2
    tupla_promedios = (promedio_parcial, promedio_final)
    return tupla_promedios

calificaciones_usuario=[]
for i in range (0, 4):
    if i<3:
        calificacion_1=int(input(f"Ingresa calificacion parcial {i+1}: "))
        calificaciones_usuario.append(calificacion_1)
    else:
        calificacion_1 = int(input(f"Ingresa calificacion ordinario: "))
        calificaciones_usuario.append(calificacion_1)
print(calificaciones_usuario)
tupla_de_calificacion = calificacion(calificaciones_usuario)
print(f"promedio parcial: {tupla_de_calificacion[0]} promedio final: {tupla_de_calificacion[1]}")