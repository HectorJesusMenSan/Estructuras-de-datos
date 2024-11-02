"""
Nombre: Héctor Jesus Mendez Santiago
Fecha: 29 de Octubre 2024
Descripción: Estos son los ejercicios de evaluacion
             para el primer parcial, del curso de
             estructuras de datos.
"""
from random import randint, random



# Presentacion del programa:
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print(":::Nombre: Hector Jesus::::")
print(":::Examen Parcial 1::::::::")
print(":::Piedra, papel o tijeras:")
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print()

print(" C A R G A N D O  ;) ")


# Declaracion de variables:
Opcion=True
opcion_de_cpu=0
empate=0
cpu=0
jugador=0
respuesta_de_jugador="0"

# Menu:
while Opcion:
    print("\n1) Piedra")
    print("2) Papel")
    print("3) Tijeras")
    print("0) Salir")

    print("¿CON QUE JUGARAS?")

    Opcion = int(input("Ingresa una opcion: "))


    if Opcion>0 and Opcion<4:
        print("#########################################")

        opcion_de_cpu = randint (1, 3)

        if opcion_de_cpu==Opcion:
            print("Empate")
            empate+=1

        if opcion_de_cpu == 1:
            opcion_de_cpu = "piedra"
        if opcion_de_cpu == 2:
            opcion_de_cpu= "papel"
        if opcion_de_cpu == 3:
            opcion_de_cpu = "tijeras"

        if Opcion == 1:
            respuesta_de_jugador= "piedra"
        if Opcion == 2:
            respuesta_de_jugador= "papel"
        if Opcion == 3:
            respuesta_de_jugador= "tijeras"

        print(f"\nJugador: {respuesta_de_jugador}")
        print(f"CPU: {opcion_de_cpu}")

        if respuesta_de_jugador=="piedra" and  opcion_de_cpu == "tijeras":
            print("Gana Jugador")
            jugador+=1
        elif respuesta_de_jugador=="papel" and  opcion_de_cpu == "piedra":
            print("Gana Jugador")
            jugador+=1
        elif respuesta_de_jugador=="tijeras" and  opcion_de_cpu == "papel":
            print("Gana Jugador")
            jugador+=1

        else:
            if opcion_de_cpu=="piedra" and   respuesta_de_jugador== "tijeras":
                print("Gana CPU")
                cpu+=1
            elif opcion_de_cpu=="papel" and   respuesta_de_jugador== "piedra":
                print("Gana CPU")
                cpu+=1
            elif opcion_de_cpu=="tijeras" and   respuesta_de_jugador== "papel":
                print("Gana CPU")
                cpu+=1
        print("#########################################")
        print(f"victorias de jugador: {jugador}  victorias de CPU: {cpu} Empates: {empate} ")

    elif Opcion==0:
        print("SALIENDO")
        break
    else:
        print("\n****Opcion invalida :(")