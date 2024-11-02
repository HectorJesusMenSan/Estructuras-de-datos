"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 29 de Octubre de 2024
Descripción: Estos son los ejercicios de evaluación
             para el primer parcial, del curso de
             estructuras de datos.
"""
from random import randint

# Presentación del programa:
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print(":::Nombre: Héctor Jesús::::")
print(":::Examen Parcial 1::::::::")
print(":::Piedra, papel o tijeras:")
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print()

print(" C A R G A N D O  ;) ")

# Declaración de variables:
Opcion = True
opcion_de_cpu = 0
empate = 0
cpu = 0
jugador = 0
respuesta_de_jugador = "0"

# Menú:
while Opcion:
    print("\n1) Piedra")
    print("2) Papel")
    print("3) Tijeras")
    print("0) Salir")

    print("¿CON QUÉ JUGARÁS?")

    Opcion = int(input("Ingresa una opción: "))

    if Opcion > 0 and Opcion < 4:
        print("#########################################")

        opcion_de_cpu = randint(1, 3)  # Genera números aleatorios

        # Si son empates:
        if opcion_de_cpu == Opcion:
            print("Empate")
            empate += 1

        # Dependiendo de las opciones de CPU se transforman a:
        if opcion_de_cpu == 1:
            opcion_de_cpu = "piedra"
        if opcion_de_cpu == 2:
            opcion_de_cpu = "papel"
        if opcion_de_cpu == 3:
            opcion_de_cpu = "tijeras"

        # Dependiendo de las opciones de jugador ingresadas se transforman a:
        if Opcion == 1:
            respuesta_de_jugador = "piedra"
        if Opcion == 2:
            respuesta_de_jugador = "papel"
        if Opcion == 3:
            respuesta_de_jugador = "tijeras"

        # Se imprimen las respuestas o elecciones de ambos:
        print(f"\nJugador: {respuesta_de_jugador}")
        print(f"CPU: {opcion_de_cpu}")

        # Ocasiones cuando el jugador gana:
        if respuesta_de_jugador == "piedra" and opcion_de_cpu == "tijeras":
            print("Gana Jugador")
            jugador += 1
        elif respuesta_de_jugador == "papel" and opcion_de_cpu == "piedra":
            print("Gana Jugador")
            jugador += 1
        elif respuesta_de_jugador == "tijeras" and opcion_de_cpu == "papel":
            print("Gana Jugador")
            jugador += 1

        # Ocasiones cuando el CPU gana:
        else:
            if opcion_de_cpu == "piedra" and respuesta_de_jugador == "tijeras":
                print("Gana CPU")
                cpu += 1
            elif opcion_de_cpu == "papel" and respuesta_de_jugador == "piedra":
                print("Gana CPU")
                cpu += 1
            elif opcion_de_cpu == "tijeras" and respuesta_de_jugador == "papel":
                print("Gana CPU")

        print("#########################################")

        # Escribe un marcador de victorias o empates
        print(f"Victorias de jugador: {jugador}  Victorias de CPU: {cpu} Empates: {empate} ")

    # Opción de salida del programa
    elif Opcion == 0:
        print("-SALIENDO-")
        break

    # Opciones diferentes de 0-3:
    else:
        print("\n****Opción inválida :(")

"""Se consideraron las diferentes combinaciones, dependiendo
   las posiciones que elijan tanto el CPU como el jugador."""
