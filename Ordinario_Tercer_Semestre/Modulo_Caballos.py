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



def menu_de_interaccion():
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

    print("===========================================================================")
    print("--- Reglas Básicas del Juego de Carrera de Caballos con Baraja Española --- ")
    print("===========================================================================")
    print()
    print(">>>>>>> Objetivo del Juego")
    print("-El objetivo del juego es adivinar qué carta saldrá en la siguiente tirada.")
    print()
    print(">>>>>>> Preparación del Juego ")
    print("-Se baraja la baraja española de 48 cartas."
          "\n-Se colocan las cartas boca abajo en una pila."
          "\n-El jugador que juega primero es elegido al azar.")
    print()
    print(">>>>>>> Jugabilidad ")



def juego_contra_cpu (diccionario_de_barajas):
    columnas_verificadas = []
    regresos_realizados = []

    matriz_de_juego = [["copa","    ", "    ", "    ", "M"], ["abasto", "    ", "    ", "    ", "E"], ["moneda", "    ", "    ", "    ", "T"], ["espada", "    ", "    ", "    ", "A"]]
    print("\n\tComenzando carrera: \n")
    imprimir_matriz(matriz_de_juego)

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
                        levantar = 0  # Terminamos el juego
                    else:
                        # Verificación de columnas vacías
                        for c in range(0, 5):  # Ahora iteramos hasta la columna 4
                                contador_columna = 0
                                for r in range(0, 4):  # Iteramos por las filas
                                    if matriz_de_juego[r][c] == "     ":
                                        contador_columna += 1

                                if contador_columna == 4:
                                    print(f"La columna {c} tiene 4 celdas vacías.")
                                    regresar_carta = random.choice(list(diccionario_de_barajas.keys()))
                                    print(f"\nLa carta que se regresará un espacio es {regresar_carta}")

                                    for rg in range(0, 4):
                                        for cl in range(0, 5):
                                            if matriz_de_juego[rg][cl] == regresar_carta:
                                                matriz_de_juego[rg][cl] = "       "
                                                matriz_de_juego[rg][cl - 1] = regresar_carta

                                                imprimir_matriz(matriz_de_juego)
                                                break

                        if contador_columna != 4 :
                            # Si no hay columnas vacías, se mueve la carta
                            matriz_de_juego[renglones][columnas + 1] = llave_random
                            matriz_de_juego[renglones][columnas] = "     "
                            imprimir_matriz(matriz_de_juego)
                            break


        if levantar != 0:
            levantar = int(input("[1]. Para levantar otra carta"))






def menu_principal ()->None:
    """

    :return:
    """

    diccionario_de_barajas = {'moneda':[1, 2, 3, 4, 5, 6, 7, 10, 11],
                              'copa':[1, 2, 3, 4, 5, 6, 7, 10, 11],
                              'espada':[1, 2, 3, 3, 4, 5, 6, 7, 10, 11],
                              'abasto':[1, 2, 3, 3, 4, 5, 6, 7, 10, 11]}

    for clave, valor in diccionario_de_barajas.items():
        print(f"Clave: {clave} y  valor: {valor}")

    #Despliega menu de iteraccion.
    opcion = None
    while opcion != 0:
        opcion = menu_de_interaccion()
        if opcion>=0 and opcion<4:
            if opcion == 0:
                print("Salida Exitosa. Adios :)")
            if opcion == 1:
                juego_contra_cpu(diccionario_de_barajas)
            if opcion == 2:
                reglas_de_juego()
            if opcion == 3:
                reglas_de_juego()
        else:
            print("Error inrtenta denuevo")

if __name__ == '__main__':
    menu_principal()