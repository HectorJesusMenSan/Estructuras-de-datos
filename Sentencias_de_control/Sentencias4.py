"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Cuarto programa para ejercitar la habilidad con las sentencias
Este programa determinará si te permiten el acceso al bar "La Negra", por lo que se debe cumplir lo siguiente:

    Tener al menos 18 años.
    Tener al menos $ 250.00 para gastar.

Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!". En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!"

Para ello:

a) Solicite al usuario su edad.

b) Solicite al usuario el dinero con el que cuenta.

c) Utilice la lógica adecuada para determinar el mensaje.

d) Muestre el mensaje adecuado en consola.
"""
dinero=int(input("Ingresa tu presupesto:"))
edad=float(input("Ingresa tu edad: "))

if dinero>=250.00 and edad>=18:
    print("¡Bienbenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar.")

