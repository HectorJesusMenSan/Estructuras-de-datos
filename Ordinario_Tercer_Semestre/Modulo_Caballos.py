"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 7 de febrero del 2025
Descripción: Este es el mulo correspondiente al juego de
             carrera de caballos con barajas españolas.
"""
from random import randint
import random



def imprimir_matriz(matriz_de_juego) -> None:
    """
    Escribe el tablero de juego
    :param recibe una matriz que tiene cadenas
    :return: No retorna nada
    """
    print("\n")
    print(f"  {matriz_de_juego[0][0]}   {matriz_de_juego[0][1]}   {matriz_de_juego[0][2]}   {matriz_de_juego[0][3]}      |{matriz_de_juego[0][4]}")
    print("____________________________________")
    print(f"  {matriz_de_juego[1][0]}   {matriz_de_juego[1][1]}   {matriz_de_juego[1][2]}   {matriz_de_juego[1][3]}    |{matriz_de_juego[1][4]}")
    print("____________________________________")
    print(f"  {matriz_de_juego[2][0]}   {matriz_de_juego[2][1]}   {matriz_de_juego[2][2]}   {matriz_de_juego[2][3]}   |{matriz_de_juego[2][4]}")
    print("____________________________________")
    print(f"  {matriz_de_juego[3][0]}   {matriz_de_juego[3][1]}   {matriz_de_juego[3][2]}   {matriz_de_juego[3][3]}    |{matriz_de_juego[3][4]}")



def menu_de_interaccion()->int:
    """
    Muestra el menú principal del juego donde el jugador elige qué hacer
    :return: Devuelve la opción seleccionada por el usuario
    """
    print("\n___________________________________________________________")
    print(" -> Bienvenido al juego carera de barajas españolas <-")
    print("\n[1]. Ver reglas.")
    print("[2]. Jugar vs Cpu.")
    print("[3]. Jugador 1 vs Jugador 2.")
    print("[0]. Salir.")
    print("\n___________________________________________________________")
    opcion = input("Ingresa la opción que deseas ejecutar:  ")
    print("\n___________________________________________________________")

    while not opcion.isnumeric():  # Asegura que el usuario ingrese una opción válida
        print("Lo que introdujiste no está dentro de las opciones disponibles.")
        opcion = input(f"Tu escribiste [{opcion}]. Intenta nuevamente: ")

    return int(opcion)

def reglas_de_juego ():
    """
    Esta función escribe en pantalla una pequeña informacion
    de lo que trata el juego.
    :return: No retorna nada
    """
    print("\n===========================================================================")
    print("--- Reglas Básicas del Juego de Carrera de Caballos con Baraja Española --- ")
    print("===========================================================================")
    print()
    print(">>>>>>> Objetivo del Juego")
    print("-El objetivo del juego es adivinar qué carta saldrá en la siguiente tirada.")
    print()
    print("Sacar una carta: El jugador saca una carta del montón en el centro de la mesa.")
    print("Mover su caballo: El jugador puede mover su caballo una casilla hacia adelante o hacia atrás en función de la carta que sacó o lanzó.")
    print("Si el caballo del jugador llega a la casilla final gana la partida")


def juego_contra_cpu (diccionario_de_barajas):
    """
    En esta función se lleva a cabo toda la logica para hacer que los caballos corran
    al levantar una carta y cuando pasen una sección de las ocultas, escoger una para
    que un caballo se regrese. Se uso la implementación de matrices, diccionarios, listas y
    cadenas.
    :param diccionario_de_barajas: Es el diccionario que contiene toda la baraja española
    :return: No retorna nada
    """
    columnas_verficadas = []
    bandera = 0
    contador_escoger = 1
    intentos = 4

    matriz_de_juego = [["copa", "    ", "    ", "    ", "M"], ["abasto", "    ", "    ", "    ", "E"], ["moneda", "    ", "    ", "    ", "T"], ["espada", "    ", "    ", "    ", "A"]]
    print("\n\tComenzando carrera: \n")
    imprimir_matriz(matriz_de_juego)
    print(f"Quedan {intentos} cartas ocultas")

    print("\n->Escoge a qué caballo apostarás:\n ")
    for llave in diccionario_de_barajas.keys():
        print(f"[{contador_escoger}]", end="")
        print(f"Caballo: {llave}")
        contador_escoger += 1

    caballo_usuario = input("Escribe la opción que deseas: ")
    while not caballo_usuario.isnumeric() or int(caballo_usuario) not in range (1, 5):
        caballo_usuario = input("Error, intenta de nuevo: ")
    caballo_usuario = int(caballo_usuario)

    if caballo_usuario == 1:
        caballo_usuario = "moneda"
    elif caballo_usuario == 2:
        caballo_usuario = "copa"
    elif caballo_usuario == 3:
        caballo_usuario = "espada"
    else:
        caballo_usuario = "abasto"


    caballo_Cpu = random.choice(list(diccionario_de_barajas.keys()))

    print(f"\nTu apostaste por el caballo de {caballo_usuario}\nEl cpu apostó al caballo de {caballo_Cpu}")


    levantar = None
    while levantar != 0:
        # Selección aleatoria de carta
        llave_random = random.choice(list(diccionario_de_barajas.keys()))
        print("\nLa carta levantada es: ", llave_random)

        # Manipulación de la matriz de juego
        for renglones in range(0, 4):
            for columnas in range(0, 4):  # Recorrer hasta la columna 4 (índice 4)
                if matriz_de_juego[renglones][columnas] == llave_random:
                    # Verificamos si la carta ha llegado a la meta
                    if matriz_de_juego[renglones][columnas + 1] in ["M", "E", "T", "A"]:
                        matriz_de_juego[renglones][columnas + 1] = llave_random
                        matriz_de_juego[renglones][columnas] = "     "
                        imprimir_matriz(matriz_de_juego)
                        print(f"Quedan {intentos} cartas ocultas")
                        print(f"{llave_random} ha ganado.")
                        if llave_random == caballo_usuario:
                            print("\nHas ganado la apuesta, felicidades")
                        elif llave_random == caballo_Cpu:
                            print("\nEl cpu ha ganado")
                        else:
                            print("\nEsto ha sido un empate, nadie ganó")
                        levantar = 0  # Terminamos el juego
                    else:
                        # Verificación de columnas vacías

                        for c in range(0, 5):  # iteramos hasta la columna 4
                                if bandera == 1:
                                    c=+1

                                contador_columna = 0
                                for r in range(0, 4):  # Iteramos por las filas
                                    if matriz_de_juego[r][c] == "     ":
                                        contador_columna += 1
                                # Regresar cartas
                                if contador_columna == 4:
                                    bandera = 1
                                    for rg in range(0, 4):
                                        for cl in range(0, 5):
                                            columnas_verficadas.append(matriz_de_juego[rg][cl])
                                        break


                                    print(f"La columna {c} tiene 4 celdas vacías.")
                                    regresar_carta = random.choice(list(diccionario_de_barajas.keys()))

                                    for clave, valor in diccionario_de_barajas.items():
                                        if regresar_carta == clave:
                                            numero_de_carta = random.choice(list(valor))
                                            list(valor).remove(numero_de_carta)

                                    print(f"\nLa carta que se regresará un espacio es {regresar_carta}")
                                    print(f"La baraja levantada es: {numero_de_carta} de {regresar_carta}")
                                    intentos -= 1
                                    print(f"Quedan {intentos} cartas ocultas")


                                    for rg in range(0, 4):
                                        for cl in range(0, 5):

                                            if matriz_de_juego[rg][cl] == regresar_carta:
                                                matriz_de_juego[rg][cl] = "    "
                                                matriz_de_juego[rg][cl - 1] = regresar_carta

                                                imprimir_matriz(matriz_de_juego)
                                                print(f"Quedan {intentos} cartas ocultas")
                                    break


                        if contador_columna != 4 :
                            # Si no hay columnas vacías, se mueve la carta
                            matriz_de_juego[renglones][columnas + 1] = llave_random
                            matriz_de_juego[renglones][columnas] = "     "
                            imprimir_matriz(matriz_de_juego)
                            print(f"\nQuedan {intentos} cartas ocultas")
                            break


        if levantar != 0:
            levantar = input("[1] Para levantar otra carta o [0] para terminar programa: ")
            while not levantar.isnumeric() or int(levantar)>1:
                levantar = input("Error ingresa de nuevo: ")

            levantar = int(levantar)


def dos_jugadores (diccionario_de_barajas):
    """
    En esta función se lleva a cabo toda la lógica para hacer que los caballos corran
    al levantar una carta y cuando pasen una sección de las ocultas, escoger una para
    que un caballo se regrese. Se uso la implementación de matrices, diccionarios, listas y
    cadenas. Esta función es para que dos jugadores apuesten a un caballo.
    :param diccionario_de_barajas: Diccionario que contiene las cartas de la baraja española
    :return: No retorna nada
    """
    columnas_verficadas = []
    bandera = 0
    contador_escoger = 1
    intentos = 4

    matriz_de_juego = [["copa", "    ", "    ", "    ", "M"], ["abasto", "    ", "    ", "    ", "E"],
                       ["moneda", "    ", "    ", "    ", "T"], ["espada", "    ", "    ", "    ", "A"]]

    print("\n\tComenzando carrera: \n")
    imprimir_matriz(matriz_de_juego)
    print(f"Quedan {intentos} cartas ocultas")

    print("\n->Escoge a qué caballo apostarás:\n ")
    for llave in diccionario_de_barajas.keys():
        print(f"[{contador_escoger}]", end="")
        print(f"Caballo: {llave}")
        contador_escoger += 1

    caballo_usuario = input("Jugador 1: Escribe la opción que deseas: ")
    while not caballo_usuario.isnumeric() or int(caballo_usuario) not in range(1, 5):
        caballo_usuario = input("Error, intenta de nuevo: ")
    caballo_usuario = int(caballo_usuario)


    caballo_usuario2 = input("Jugador 2: Escribe la opción que deseas: ")
    while not caballo_usuario2.isnumeric() or int(caballo_usuario) not in range(1, 5):
        caballo_usuario2 = input("Error, intenta de nuevo: ")
    caballo_usuario2 = int(caballo_usuario2)

    if caballo_usuario == 1:
        caballo_usuario = "moneda"
    elif caballo_usuario == 2:
        caballo_usuario = "copa"
    elif caballo_usuario == 3:
        caballo_usuario = "espada"
    else:
        caballo_usuario = "abasto"

    if caballo_usuario2 == 1:
        caballo_usuario2 = "moneda"
    elif caballo_usuario2 == 2:
        caballo_usuario2 = "copa"
    elif caballo_usuario2 == 3:
        caballo_usuario2 = "espada"
    else:
        caballo_usuario2 = "abasto"


    print(f"\nTu apostaste por el caballo de {caballo_usuario}\nEl jugador 2 apostó al caballo de {caballo_usuario2}")

    levantar = None
    while levantar != 0:
        # Selección aleatoria de carta
        llave_random = random.choice(list(diccionario_de_barajas.keys()))
        print("\nLa carta levantada es: ", llave_random)

        # Manipulación de la matriz de juego
        for renglones in range(0, 4):
            for columnas in range(0, 4):  # Recorrer hasta la columna 4 (índice 4)
                if matriz_de_juego[renglones][columnas] == llave_random:
                    # Verificamos si la carta ha llegado a la meta
                    if matriz_de_juego[renglones][columnas + 1] in ["M", "E", "T", "A"]:
                        matriz_de_juego[renglones][columnas + 1] = llave_random
                        matriz_de_juego[renglones][columnas] = "     "
                        imprimir_matriz(matriz_de_juego)
                        print(f"{llave_random} ha ganado.")
                        if llave_random == caballo_usuario:
                            print("\nEl jugador 1 ha ganado.")
                        elif llave_random == caballo_usuario2:
                            print("\nEl jugador 2 ha ganado")
                        else:
                            print("\nEsto ha sido un empate, nadie ganó")
                        levantar = 0  # Terminamos el juego
                    else:
                        # Verificación de columnas vacías

                        for c in range(0, 5):  #  iteramos hasta la columna 4
                            if bandera == 1:
                                c = +1

                            contador_columna = 0
                            for r in range(0, 4):  # Iteramos por las filas
                                if matriz_de_juego[r][c] == "     ":
                                    contador_columna += 1
                            # Regresar carta
                            if contador_columna == 4:
                                bandera = 1
                                for rg in range(0, 4):
                                    for cl in range(0, 5):
                                        columnas_verficadas.append(matriz_de_juego[rg][cl])
                                    break

                                print(f"La columna {c} tiene 4 celdas vacías.")
                                regresar_carta = random.choice(list(diccionario_de_barajas.keys()))
                                for clave, valor in diccionario_de_barajas.items():
                                    if regresar_carta == clave:
                                        numero_de_carta = random.choice(list(valor))
                                        list(valor).remove(numero_de_carta)

                                print(f"\nLa carta que se regresará un espacio es {regresar_carta}")
                                print(f"La baraja levantada es: {numero_de_carta} de {regresar_carta}")
                                intentos -= 1
                                print(f"Quedan {intentos} cartas ocultas")

                                for rg in range(0, 4):
                                    for cl in range(0, 5):

                                        if matriz_de_juego[rg][cl] == regresar_carta:
                                            matriz_de_juego[rg][cl] = "    "
                                            matriz_de_juego[rg][cl - 1] = regresar_carta

                                            imprimir_matriz(matriz_de_juego)
                                            print(f"Quedan {intentos} cartas ocultas")
                                break

                        if contador_columna != 4:
                            # Si no hay columnas vacías, se mueve la carta
                            matriz_de_juego[renglones][columnas + 1] = llave_random
                            matriz_de_juego[renglones][columnas] = "     "
                            imprimir_matriz(matriz_de_juego)
                            print(f"Quedan {intentos} cartas ocultas")
                            break

        if levantar != 0:
            levantar = input("[1] Para levantar otra carta o [0] para terminar programa: ")
            while not levantar.isnumeric() or int(levantar) > 1:
                levantar = input("Error ingresa de nuevo: ")

            levantar = int(levantar)


def menu_principal ()->None:
    """
    Menu donde se despliegan las acciones a ejecutar, dependiendo de la opcion que recibamos
    de la función del menú de interacción
    :return: Sin retornos
    """

    diccionario_de_barajas = {'moneda':[1, 2, 3, 4, 5, 6, 7, 10, 11],
                              'copa':[1, 2, 3, 4, 5, 6, 7, 10, 11],
                              'espada':[1, 2, 3, 3, 4, 5, 6, 7, 10, 11],
                              'abasto':[1, 2, 3, 3, 4, 5, 6, 7, 10, 11]}

    for clave, valor in diccionario_de_barajas.items():
        print(f"Clave: {clave} y  valor: {valor}")

    # Despliega menú de interacción.
    opcion = None
    while opcion != 0:
        opcion = menu_de_interaccion()
        if opcion >= 0 and opcion < 4:
            if opcion == 0:
                print("Salida Exitosa. Adiós :)")
            if opcion == 1:
                reglas_de_juego()
            if opcion == 2:
                juego_contra_cpu(diccionario_de_barajas)
            if opcion == 3:
                dos_jugadores(diccionario_de_barajas)
        else:
            print("Error, intenta de nuevo")

if __name__ == '__main__':
    menu_principal()