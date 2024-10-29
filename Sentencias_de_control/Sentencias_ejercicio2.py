"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Segundo programa para ejercitar la habilidad con las sentencias.

Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario. Para ello:

a) Solicite al usuario un número que representa al mes.

b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:

    3, 4 y 5: Primavera.

    6, 7 y 8: Verano.

    9, 10 y 11: Otoño.

    12, 1 y 2: Invierno.

    Otro caso: Mensaje de mes incorrecto.

c) Muestre la estación correspondiente en consola.
"""

# Solicitud de datos:
print("CARGANDO...")
print("Programa que determina en qué estación está el mes ingresado.")              # Se escriben letreros.
mes_de_usuario = int(input("Ingresa un número que represente el mes del año: "))    # Convierte y almacena datos a tipo entero.

# Apartado de sentencia y condiciones:
if mes_de_usuario >= 1 and mes_de_usuario <= 12:  # Condición del número ingresado, de un rango de 1-12.
    if mes_de_usuario == 12 or mes_de_usuario == 1 or mes_de_usuario == 2:
        print("En el mes es invierno.")                                 # Imprime la estación invierno si los días son 1 o 12 o 2.
    elif mes_de_usuario >= 9 and mes_de_usuario <= 11:
        print("En el mes es otoño.")                                    # Imprime la estación otoño si el número ingresado está en un rango de 9-11.
    elif mes_de_usuario >= 6 and mes_de_usuario <= 8:
        print("En el mes es verano.")                                   # Imprime la estación verano si el número ingresado está en un rango de 6-8.
    else:
        print("En el mes es primavera.")                                # Si no se cumple alguno de los casos se toma que es primavera.
else:                                             # Si no se cumple la condición, quiere decir que el número ingresado es incorrecto.
    print("Número inválido o mes incorrecto.")
