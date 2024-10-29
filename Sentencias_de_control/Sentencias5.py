"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Quinto programa para ejercitar la habilidad con las sentencias

Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.

Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!". En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!"

Para ello:

a) Solicite al usuario sus tres calificaciones parciales y la calificación del ordinario.

b) Calcule el promedio y determine si aprobó (calificación mínima de 6.0).

d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.
"""

# Solicitud de datos
print("CARGANDO: PROGRAMA PARA PROMEDIAR CALIFICACIÓN")                 # Escribe letrero informativo.
# Conversión y almacenamiento de datos a tipo flotante:
parcial1 = float(input("Ingresa tu calificación del primer parcial: "))
parcial2 = float(input("Ingresa tu calificación del segundo parcial: "))
parcial3 = float(input("Ingresa tu calificación del tercer parcial: "))
ordinario = float(input("Ingresa tu calificación final del ordinario: "))

# Operaciones correspondientes para sacar promedio
promedio = (((parcial1 + parcial2 + parcial3) / 3) + ordinario) / 2
"""
Primero se saca el promedio de los tres parciales juntos, luego se suma con
la calificación final del ordinario. Al final se suman ambos resultados y
se divide entre dos para sacar el promedio general y final.
"""

# Ejecución de condiciones:
if promedio >= 6:     # Si la calificación o promedio es mayor o igual a 6.
    print(f"La calificación final es {promedio:.1f}. ¡Felicidades, aprobaste!")   # Si se cumple la condición, quiere decir que aprobó, esta línea muestra los resultados.
else:
    print(f"La calificación final es {promedio:.1f}. ¡Lo siento, no aprobaste!") # Si no se cumple la condición, quiere decir que no aprobó, esta línea muestra los resultados.
