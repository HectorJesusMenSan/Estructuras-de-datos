"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 27 de enero del 2025
Descripción: Ejercicio para la presentación del examen del tercer parcial
             Juego del Ahorcado
"""
import random
from os import remove


def dibujos (bandera:1)->None:
    """
    Dibujos para representar al ahorcado
    :param bandera: es la variable que determinara que dibujo mostrar

    :return: Sin retornos
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

def menu_Ahorcado()->int:
    """
    Menun desplegado para la iteraccion con el usuario dentro del juego ahorcado.
    :return: Retorna un numero entero, que es la opcion escogida por el usuario
    """
    print("\n___________________________________________________________")
    print("Bienvenido al juego del ahorcado: ")
    print("\n[1]. Ver reglas.")
    print("[2]. Adivinar palabras.")
    print("[0]. Salir.")
    print("\n___________________________________________________________")
    opcion = input("Ingresa la opcion que deceas ejecutar:  ")
    print("\n___________________________________________________________")

    while not opcion.isnumeric():
        print("Lo que introduciste no esta dentro de las opciones disponibles.")
        opcion = input(f"Tu escribiste [{opcion}]. Intenta nuevamente: ")

    return int (opcion)

def reglas_de_juego()->None:
    """
    Funcion que muestra en pantala como jugar al ahorcado, letreros informativos
    para el usuario.
    :return: No retorna nada.

    """
    print("\n E S T A S   S O N  L A S   R E G L A S   D E L   J U E G O : ")
    print("\nUsando una fila de guiones, se representa la palabra a adivinar, dando el número de letras,"
          "\nnúmeros y categoría. Si el jugador adivinador sugiere una letra o número que aparece en la palabra,"
          "\nel Cpu la escribe en todas sus posiciones correctas. Si la letra o el número sugerido"
          "\nno ocurre en la palabra, el Cpu saca un elemento de la figura de hombre palo ahorcado como una marca de conteo."
          "\nEl juego termina cuando:")
    print("-El jugador adivinador completa la palabra, o adivina la palabra completa correctamente."
          "-El otro jugador completa el diagrama.")

def ejecucion_de_juego()->None:
    palabras_por_defecto = ["zorra", "arroz", "sombrilla", "telaraña"]
    errores = 1
    contador = None
    bandera = 1
    bandera2 = 0

    dibujos(bandera)

    palabra_a_adivinar  = random.choice(palabras_por_defecto)

    palabra_resultado = palabra_a_adivinar
    palabra_escondida = "_" * len(palabra_a_adivinar)



    print("\nTienes 5 vidas, encuentra la palabra: \n")
    print()
    print(palabra_escondida)
    print()

    palabra_escondida = list(palabra_escondida)

    while contador != 0:
        letra_De_usuario = input("Ingresa una letra cualquiera del abecedario: ")
        while not letra_De_usuario.isalpha() or len(letra_De_usuario)>1:
            letra_De_usuario = input("\nError, ingresaste un dato que no pertenece al alfabeto. intenta de nuevo: ")
            if len(letra_De_usuario)>1 :
                print("\nIngresate una palabra y no una letra.")
                letra_De_usuario= input("\nIntenta de nuevo: ")

        letra_De_usuario = letra_De_usuario.lower()

        for i in range(len(palabra_a_adivinar)):
            if letra_De_usuario == palabra_a_adivinar[i]:
                for palabra in palabra_escondida:
                    if palabra == letra_De_usuario:
                        print("Letra repetida.\n")
                        break
                palabra_escondida[i] = letra_De_usuario
                bandera2 = 1



        for letra in palabra_escondida:
            print(letra, end=" ")

        if bandera2 == 0:
            print("\nUn error, te costo una vida menos.")
            errores +=1
            dibujos(errores)

        bandera2 = 0

        if errores == 5:
            print("\nHaz consumido todas tus vidas.")
            print(f"\nLa palabra era {palabra_resultado}")
            contador = 0

        if palabra_escondida == list(palabra_a_adivinar):
            print(f"\nHaz ganado el juego y encontrado la palabra {palabra_resultado}")
            contador = 0







def menu_para_ahorcado () -> None:
    """
    A qui van todas las lamadas a las funcioines para hacer que el programa funcione
    :return: No retorna nada.
    """

    opcion = None
    while opcion != 0 :
        opcion = menu_Ahorcado()
        if opcion == 1:
            reglas_de_juego()
        if opcion == 2:
            ejecucion_de_juego()



if __name__ == '__main__':
    menu_para_ahorcado()
