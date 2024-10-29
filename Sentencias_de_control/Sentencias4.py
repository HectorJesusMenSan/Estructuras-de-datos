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

# Solicitud de datos:
print("CARGANDO PROGRAMA")                            # Escribe un letrero.
print("Programa: Control de acceso en La Negra.")     # Escribe letrero informativo.
dinero = float(input("Ingresa tu presupuesto: "))     # Convierte y guarda datos en flotante.
edad = int(input("Ingresa tu edad: "))                # Convierte y guarda datos en entero.

# Ejecución de condiciones:
if dinero >= 250.00 and edad >= 18:                   # Si el presupuesto es mayor o igual que 250 y la edad mayor o igual que 18.
    print("¡Bienvenido a tu mejor bar!")               # Si se cumple la condición, se le da acceso.
else:                                                 # Si ambas condiciones no se cumplen.
    print("Lo sentimos, ya estamos por cerrar.")      # Si no se cumple, no se les da acceso y se les corre de manera educada.
