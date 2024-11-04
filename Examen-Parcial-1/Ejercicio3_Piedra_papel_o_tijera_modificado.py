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

    Opcion = input("Escribe una opción: ")
    Opcion = Opcion.lower() # Convierte a minusculas.


    if Opcion=="piedra" or Opcion=="papel" or Opcion=="tijeras":
        print("#########################################")

        opcion_de_cpu = randint(1, 3)  # Genera números aleatorios

        # Dependiendo de las opciones de CPU se transforman a:
        if opcion_de_cpu == 1:
            opcion_de_cpu = "piedra"
        if opcion_de_cpu == 2:
            opcion_de_cpu = "papel"
        if opcion_de_cpu == 3:
            opcion_de_cpu = "tijeras"

        # Si son empates:
        if opcion_de_cpu == Opcion:
            print("Empate")
            empate += 1

        # Se imprimen las respuestas o elecciones de ambos:
        print(f"\nJugador: {Opcion}")
        print(f"CPU: {opcion_de_cpu}")

        # Ocasiones cuando el cpu gana:
        if Opcion == "piedra" and opcion_de_cpu == "tijeras":
            print("Gana Cpu")
            cpu += 1
        elif Opcion == "papel" and opcion_de_cpu == "piedra":
            print("Gana cpu")
            cpu += 1
        elif Opcion == "tijeras" and opcion_de_cpu == "papel":
            print("Gana cpu")
            cpu += 1

        # Ocasiones cuando el jugador gana:

        else:
            if opcion_de_cpu == "piedra" and Opcion == "tijeras":
                print("Gana jugador")
                jugador += 1
            elif opcion_de_cpu == "papel" and Opcion == "piedra":
                print("Gana jugador")
                jugador += 1
            elif opcion_de_cpu == "tijeras" and Opcion == "papel":
                print("Gana jugador")

        print("#########################################")

        # Escribe un marcador de victorias o empates
        print(f"Victorias de jugador: {jugador}  Victorias de CPU: {cpu} Empates: {empate} ")

    # Opción de salida del programa
    elif Opcion == "salir":
        print("-SALIENDO-")
        break

    # Opciones diferentes de 0-3:
    else:
        print("\n****Opción inválida :(")

"""Se consideraron las diferentes combinaciones, dependiendo
   las posiciones que elijan tanto el CPU como el jugador."""

"""Las modificaciones fueron, una que en el menú
   se reciban cadenas, y la otra, que los
   datos se inviertan."""
