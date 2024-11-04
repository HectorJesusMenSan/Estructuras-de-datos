"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 1 de noviembre de 2024
Descripción: Estos son los ejercicios de evaluación
             para el primer parcial, del curso de
             estructuras de datos.

             Modficación: Agrega el menu de dificultades, para modo
             facil, 10 intentos en un rango de 1-50.
             Para modo medio, 5 intentos en un rango de 1-100.
             Y para modo dificil, 4 intentos en un rango de 1-150.
"""
from random import randint

print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print(":::Nombre: Héctor Jesús::::")
print(":::Examen Parcial 1::::::::")
print(":::Juego Adivinador::::::::")
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print()

print(" C A R G A N D O  ;) ")

# Declaración de variables:
variable_para_ciclo = 1
Opcion=True

# Menú de dificultades:
while Opcion:
    print("[F]. Presiona la letra f, para jugar en dificultad facil.")
    print("[M]. Presiona la letra m, para jugar en dificultad medio.")
    print("[D]. Presiona la letra d, para jugar en dificultad dificil.")

    dificultad=input("Ingresa una opción: ")
    dificultad=dificultad.lower()

    if dificultad=="m": #Codigo para dificultad media.
        while variable_para_ciclo <= 5:
            numero_a_adivinar = randint(1, 100)
            # Escritura de letrero y solicitud de datos:
            print(f"\nNúmero de intento: {variable_para_ciclo}", end=".")
            numero_usuario = int(input(" Ingresa un número (1-100): "))

            # Verifica si el número está en el rango:
            if numero_usuario > 0 and numero_usuario <= 100:

                # Si la condición se cumple, verifica si el número y el número a encontrar son iguales:
                if numero_usuario == numero_a_adivinar:
                    # Si se cumple, felicita al usuario y rompe el ciclo
                    print("¡Felicidades, bellako/a! Has encontrado el número.")
                    break


                # La verificación puede ser que el número sea menor que el número a adivinar:
                elif numero_usuario > numero_a_adivinar:
                    # Si el número digitado por el usuario es mayor que el número a encontrar, imprime:
                    print("El número es más pequeño, bro :(")
                else:
                    # Si el número digitado por el usuario es menor que el número a encontrar, imprime:
                    print("¡El número es más grande!")

            # Si el número no está en un rango de 1-100:
            else:
                # Escribe en pantalla letrero informativo.
                print("Lo lamento, el número que ingresaste no está en el rango. Intenta de nuevo :(")

            if variable_para_ciclo == 5:
                print(f"Acabas de perder tus 5 vidas, el número era: {numero_a_adivinar}")

                """Si el contador llega a 5, hace todas las instrucciones antes de esta
                quiere decir que no se pudo encontrar el número y se escribe el letrero
                correspondiente."""

            variable_para_ciclo += 1  # Aumenta el contador en 1.

    elif dificultad=="f": # Codigo para dificultad facil.
        numero_a_adivinar = randint(1, 50)
        while variable_para_ciclo <= 10:
            # Escritura de letrero y solicitud de datos:
            print(f"\nNúmero de intento: {variable_para_ciclo}", end=".")
            numero_usuario = int(input(" Ingresa un número (1-50): "))

            # Verifica si el número está en el rango:
            if numero_usuario > 0 and numero_usuario <= 50:

                # Si la condición se cumple, verifica si el número y el número a encontrar son iguales:
                if numero_usuario == numero_a_adivinar:
                    # Si se cumple, felicita al usuario y rompe el ciclo
                    print("¡Felicidades, bellako/a! Has encontrado el número.")
                    break


                # La verificación puede ser que el número sea menor que el número a adivinar:
                elif numero_usuario > numero_a_adivinar:
                    # Si el número digitado por el usuario es mayor que el número a encontrar, imprime:
                    print("El número es más pequeño, bro :(")
                else:
                    # Si el número digitado por el usuario es menor que el número a encontrar, imprime:
                    print("¡El número es más grande!")

            # Si el número no está en un rango de 1-100:
            else:
                # Escribe en pantalla letrero informativo.
                print("Lo lamento, el número que ingresaste no está en el rango. Intenta de nuevo :(")

            if variable_para_ciclo == 10:
                print(f"Acabas de perder tus 10 vidas, el número era: {numero_a_adivinar}")

                """Si el contador llega a 10, hace todas las instrucciones antes de esta
                quiere decir que no se pudo encontrar el número y se escribe el letrero
                correspondiente."""

            variable_para_ciclo += 1  # Aumenta el contador en 1.

    elif dificultad=="d": # Codigo para dificcultad dificil.
        numero_a_adivinar = randint(1, 150)
        while variable_para_ciclo <= 4:
            # Escritura de letrero y solicitud de datos:
            print(f"\nNúmero de intento: {variable_para_ciclo}", end=".")
            numero_usuario = int(input(" Ingresa un número (1-150): "))

            # Verifica si el número está en el rango:
            if numero_usuario > 0 and numero_usuario <= 150:

                # Si la condición se cumple, verifica si el número y el número a encontrar son iguales:
                if numero_usuario == numero_a_adivinar:
                    # Si se cumple, felicita al usuario y rompe el ciclo
                    print("¡Felicidades, bellako/a! Has encontrado el número.")
                    break


                # La verificación puede ser que el número sea menor que el número a adivinar:
                elif numero_usuario > numero_a_adivinar:
                    # Si el número digitado por el usuario es mayor que el número a encontrar, imprime:
                    print("El número es más pequeño, bro :(")
                else:
                    # Si el número digitado por el usuario es menor que el número a encontrar, imprime:
                    print("¡El número es más grande!")

            # Si el número no está en un rango de 1-100:
            else:
                # Escribe en pantalla letrero informativo.
                print("Lo lamento, el número que ingresaste no está en el rango. Intenta de nuevo :(")

            if variable_para_ciclo == 4:
                print(f"Acabas de perder tus 4 vidas, el número era: {numero_a_adivinar}")

                """Si el contador llega a 4, hace todas las instrucciones antes de esta
                quiere decir que no se pudo encontrar el número y se escribe el letrero
                correspondiente."""

            variable_para_ciclo += 1  # Aumenta el contador en 1.

    else:
        print("Opción invalida :(")
    break