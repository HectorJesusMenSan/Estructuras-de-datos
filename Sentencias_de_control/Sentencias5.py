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

print("CARGANDO: PROGRAMA PARA PROMEDIAR CALIFICACION")
parcial1=float(input("Ingresa tu calificaion del primer parcial: "))
parcial2=float(input("Ingresa tu calificaion del segundo parcial: "))
parcial3=float(input("Ingresa tu calificaion del tercer parcial: "))
ordinario=float(input("Ingresa tu calificacion final del ordinario"))

promedio= (((parcial1+parcial2+parcial3)/3)+ordinario)/2

if promedio>=6:
    print(f"La calificacion final es {promedio:.1f}.¡Felicidades aprobaste!")
else:
    print(f"La calificacion final es {promedio:.1f}.¡Lo siento, no aprobaste!")

