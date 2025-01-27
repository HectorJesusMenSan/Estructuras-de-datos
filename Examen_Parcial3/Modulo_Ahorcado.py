"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 27 de enero del 2025
Descripción: Ejercicio para la presentación del examen del tercer parcial
             Juego del Ahorcado
"""
import random
from os import remove


def dibujos(bandera: 1) -> None:
    """
    Dibuja las diferentes etapas del ahorcado según el número de errores
    :param bandera: Número que indica en qué etapa del juego estamos
    :return: No retorna nada
    """
    if bandera == 1:
        print("_________")
        print("|       |")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("[]       ")
    elif bandera == 2:
        print("_________")
        print("|       |")
        print("|       O ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("[]       ")
    elif bandera == 3:
        print("_________")
        print("|       |")
        print("|       O")
        print("|      ---")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("[]       ")
    elif bandera == 4:
        print("_________")
        print("|       |")
        print("|       O")
        print("|      ---")
        print("|       |")
        print("|        ")
        print("|        ")
        print("|        ")
        print("[]       ")
    else:
        print("_________")
        print("|       |")
        print("|       O")
        print("|      ---")
        print("|       |")
        print("|      / \ ")
        print("|        ")
        print("|        ")
        print("[]       ")

        print("\nHaz perdido. Tus vidas se acabaron.")


def menu_Ahorcado() -> int:
    """
    Muestra el menú principal del juego donde el jugador elige qué hacer
    :return: Devuelve la opción seleccionada por el usuario
    """
    print("\n___________________________________________________________")
    print("Bienvenido al juego del ahorcado: ")
    print("\n[1]. Ver reglas.")
    print("[2]. Adivinar palabras.")
    print("[0]. Salir.")
    print("\n___________________________________________________________")
    opcion = input("Ingresa la opción que deseas ejecutar:  ")
    print("\n___________________________________________________________")

    while not opcion.isnumeric():  # Asegura que el usuario ingrese una opción válida
        print("Lo que introdujiste no está dentro de las opciones disponibles.")
        opcion = input(f"Tu escribiste [{opcion}]. Intenta nuevamente: ")

    return int(opcion)


def reglas_de_juego() -> None:
    """
    Muestra las reglas del juego al usuario
    :return: No retorna nada
    """
    print("\n ESTAS SON LAS REGLAS DEL JUEGO: ")
    print("\nUsando una fila de guiones, se representa la palabra a adivinar, dando el número de letras,"
          "\nnúmeros y categoría. Si el jugador adivinador sugiere una letra o número que aparece en la palabra,"
          "\nel CPU la escribe en todas sus posiciones correctas. Si la letra o el número sugerido"
          "\nno ocurre en la palabra, el CPU saca un elemento de la figura de hombre palo ahorcado como una marca de conteo."
          "\nEl juego termina cuando:")
    print("-El jugador adivinador completa la palabra, o adivina la palabra completa correctamente.")
    print("-El otro jugador completa el diagrama.")


def ejecucion_de_juego() -> None:
    """
    Ejecución principal del juego del ahorcado
    :return: No retorna nada
    """
    palabras_por_defecto = ["zorra", "arroz", "sombrilla", "telaraña"]
    errores = 1
    contador = None
    bandera = 1
    bandera2 = 0

    dibujos(bandera)  # Muestra la figura del ahorcado al iniciar

    palabra_a_adivinar = random.choice(palabras_por_defecto)  # Escoge una palabra aleatoria

    palabra_resultado = palabra_a_adivinar
    palabra_escondida = "_" * len(palabra_a_adivinar)  # Crea una cadena con guiones para representar la palabra

    print("\nTienes 5 vidas, encuentra la palabra: \n")
    print()
    print(palabra_escondida)
    print()

    palabra_escondida = list(palabra_escondida)  # Convierte la cadena en una lista para poder modificarla

    while contador != 0:
        letra_De_usuario = input("Ingresa una letra cualquiera del abecedario: ")

        # Valida que el input sea una sola letra
        while not letra_De_usuario.isalpha() or len(letra_De_usuario) > 1:
            letra_De_usuario = input("\nError, ingresaste un dato que no pertenece al alfabeto. Intenta de nuevo: ")
            if len(letra_De_usuario) > 1:
                print("\nIngresaste una palabra y no una letra.")
                letra_De_usuario = input("\nIntenta de nuevo: ")

        letra_De_usuario = letra_De_usuario.lower()  # Convierte la letra a minúsculas

        # Si la letra está en la palabra, la reemplaza en las posiciones correspondientes
        for i in range(len(palabra_a_adivinar)):
            if letra_De_usuario == palabra_a_adivinar[i]:
                for palabra in palabra_escondida:
                    if palabra == letra_De_usuario:
                        print("Letra repetida.\n")
                        break
                palabra_escondida[i] = letra_De_usuario
                bandera2 = 1

        # Muestra el progreso de la palabra
        for letra in palabra_escondida:
            print(letra, end=" ")

        # Si la letra no está en la palabra, pierde una vida
        if bandera2 == 0:
            print("\nUn error, te costó una vida menos.")
            errores += 1
            dibujos(errores)

        bandera2 = 0  # Reinicia la bandera

        # Si se han perdido todas las vidas, termina el juego
        if errores == 5:
            print("\nHaz consumido todas tus vidas.")
            print(f"\nLa palabra era {palabra_resultado}")
            contador = 0

        # Si se adivina toda la palabra, termina el juego con victoria
        if palabra_escondida == list(palabra_a_adivinar):
            print(f"\nHaz ganado el juego y encontrado la palabra {palabra_resultado}")
            contador = 0


def menu_para_ahorcado() -> None:
    """
    Función principal que llama las opciones del menú
    :return: No retorna nada
    """

    opcion = None
    while opcion != 0:  # Repite el menú hasta que el jugador decida salir
        opcion = menu_Ahorcado()
        if opcion == 1:
            reglas_de_juego()
        if opcion == 2:
            ejecucion_de_juego()


if __name__ == '__main__':
    menu_para_ahorcado()  # Ejecuta el juego
