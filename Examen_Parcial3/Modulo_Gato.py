"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 27 de enero del 2025
Descripción: Ejercicio para la presentación del examen del tercer parcial
             Juego del Gato


"""
import random

def menu_de_interaccion ()->int:
    print("\nOXXXXXXXXXXXXXXXXXXXXXXXXXXXXO")
    print("O Bienvenido al Juego: Gato  O")
    print("O [1] Jugar vs Cpu           O")
    print("O [2] Jugar vs Jugador 2     O")
    print("O [0] Salir                  O")
    print("OXXXXXXXXXXXXXXXXXXXXXXXXXXXXO")
    opcion = input("\n-Ingresa una opcion: ")
    print("____________________________________________")

    while not opcion.isnumeric():
        print("Lo que introduciste no esta dentro de las opciones disponibles.")
        opcion = input(f"Tu escribiste [{opcion}]. Intenta nuevamente: ")

    return int (opcion)

def empate(tablero):
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def ganador(matriz, jugador):
    for i in range(3):  # Corregido para recorrer todo el tablero
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == jugador:  # Revisar filas
            return True
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == jugador:  # Revisar columnas
            return True
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == jugador:  # Revisar diagonal principal
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == jugador:  # Revisar diagonal inversa
        return True
    return False

def imprimir_matriz (matriz_de_juego)->None:
    print("\n")
    print(f"  {matriz_de_juego[0][0]} | {matriz_de_juego[0][1]} | {matriz_de_juego[0][2]}")
    print("______________")
    print(f"  {matriz_de_juego[1][0]} | {matriz_de_juego[1][1]} | {matriz_de_juego[1][2]}")
    print("______________")
    print(f"  {matriz_de_juego[2][0]} | {matriz_de_juego[2][1]} | {matriz_de_juego[2][2]}")

def jugar_contra_cpu ()->None:
    """
    :param Matriz_de_Gato: Mtriz que contiene el mapa del juego.
    :return: Sin retornos
    """
    jugador = "X"
    cpu = "O"
    matriz_de_juego = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    contador = None
    imprimir_matriz(matriz_de_juego)

    while contador != 0:

        print("\nIngresa las coordenadas de tu gusto: ")

        ren = input("Ingresa el renglon:  ")
        while not ren.isnumeric():
            print("Haz cometido un error al ingresar el dato.")
            ren = input("Intentalo de nuevo: ")

        columna = input("Ingresa la columna:  ")
        while not columna.isnumeric():
            print("Haz cometido un error al ingresar el dato.")
            columna = input("Intentalo de nuevo: ")

        bandera = None
        bandera2 = None

        ren = int(ren)
        columna = int(columna)


        while bandera != 0:

            while bandera2 != 0:
                if ren and columna > 3:
                    print("\n-Error, rango invalido")
                    ren = input("Ingresa el renglon:  ")
                    while not ren.isnumeric():
                        print("\nHaz cometido un error al ingresar el dato.")
                        ren = input("Intentalo de nuevo: ")
                    ren = int(ren)

                    columna = input("Ingresa la columna:  ")
                    while not columna.isnumeric():
                        print("\nHaz cometido un error al ingresar el dato.")
                        columna = input("Intentalo de nuevo: ")
                    columna = int(columna)
                else:
                    bandera2 = 0



            if matriz_de_juego[ren][columna] == " ":
                matriz_de_juego[ren][columna] = jugador
                imprimir_matriz(matriz_de_juego)
                bandera = 0
            else:
                print("\nError, ocupado")
                ren = input("Ingresa el renglon:  ")
                while not ren.isnumeric():
                    print("Haz cometido un error al ingresar el dato.")
                    ren = input("Intentalo de nuevo: ")
                ren = int(ren)

                columna = input("Ingresa la columna:  ")
                while not columna.isnumeric():
                    print("\nHaz cometido un error al ingresar el dato.")
                    columna = input("Intentalo de nuevo: ")
                columna = int(columna)

        if ganador(matriz_de_juego, jugador):
            print("Gana jugador")
            contador = 0

        bandera = None

        renglon_cpu = random.randint(0, 2)
        columna_cpu = random.randint(0, 2)

        while bandera != 0:

            if matriz_de_juego[renglon_cpu][columna_cpu] == " ":
                matriz_de_juego[renglon_cpu][columna_cpu] = cpu
                imprimir_matriz(matriz_de_juego)
                bandera = 0
            else:
                renglon_cpu = random.randint(0, 2)
                columna_cpu = random.randint(0, 2)

        if ganador(matriz_de_juego, cpu):
            print("Gana cpu")
            contador = 0

        contador2 = 0
        contador3 = 0
        for renglones in matriz_de_juego:
            for i in range(0, 3):
                if renglones[contador2] == jugador or renglones[contador2] == cpu:
                    contador3 += 1
                contador2 += 1
            contador2 = 0

        if contador3 == 9:
            print("Empate")
            contador = 0

        bandera = None
def jugar_contra_jugador2 ()->None:
    """
    :param Matriz_de_Gato: Mtriz que contiene el mapa del juego.
    :return: Sin retornos
    """
    jugador = "X"
    jugador2 = "O"
    matriz_de_juego = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    contador = None
    imprimir_matriz(matriz_de_juego)

    while contador != 0:

        print("\nJugador1. Ingresa las coordenadas de tu gusto: ")

        ren = input("Ingresa el renglon:  ")
        while not ren.isnumeric():
            print("Haz cometido un error al ingresar el dato.")
            ren = input("Intentalo de nuevo: ")

        columna = input("Ingresa la columna:  ")
        while not columna.isnumeric():
            print("Haz cometido un error al ingresar el dato.")
            columna = input("Intentalo de nuevo: ")

        bandera = None
        bandera2 = None

        ren = int(ren)
        columna = int(columna)


        while bandera != 0:

            while bandera2 != 0:
                if ren and columna > 3:
                    print("\n-Error, rango invalido")
                    ren = input("Ingresa el renglon:  ")
                    while not ren.isnumeric():
                        print("\nHaz cometido un error al ingresar el dato.")
                        ren = input("Intentalo de nuevo: ")
                    ren = int(ren)

                    columna = input("Ingresa la columna:  ")
                    while not columna.isnumeric():
                        print("\nHaz cometido un error al ingresar el dato.")
                        columna = input("Intentalo de nuevo: ")
                    columna = int(columna)
                else:
                    bandera2 = 0



            if matriz_de_juego[ren][columna] == " ":
                matriz_de_juego[ren][columna] = jugador
                imprimir_matriz(matriz_de_juego)
                bandera = 0
            else:
                print("\nError, ocupado")
                ren = input("Ingresa el renglon:  ")
                while not ren.isnumeric():
                    print("Haz cometido un error al ingresar el dato.")
                    ren = input("Intentalo de nuevo: ")
                ren = int(ren)

                columna = input("Ingresa la columna:  ")
                while not columna.isnumeric():
                    print("\nHaz cometido un error al ingresar el dato.")
                    columna = input("Intentalo de nuevo: ")
                columna = int(columna)

        if ganador(matriz_de_juego, jugador):
            print("\nGana jugador1")
            contador = 0
            break

        bandera = None

        contador2 = 0
        contador3 = 0
        for renglones in matriz_de_juego:
            for i in range(0, 3):
                if renglones[contador2] == jugador or renglones[contador2] == jugador2:
                    contador3 += 1
                contador2 += 1
            contador2 = 0

        if contador3 == 9:
            print("\nEmpate")
            contador = 0
            break


        #_________________________JUGADOR2____________________________________________________________________________
        while bandera != 0:
            print("\nJugador2. Ingresa las coordenadas de tu gusto: ")

            ren = input("Ingresa el renglon:  ")
            while not ren.isnumeric():
                print("Haz cometido un error al ingresar el dato.")
                ren = input("Intentalo de nuevo: ")

            columna = input("Ingresa la columna:  ")
            while not columna.isnumeric():
                print("Haz cometido un error al ingresar el dato.")
                columna = input("Intentalo de nuevo: ")

            bandera = None
            bandera2 = None

            ren = int(ren)
            columna = int(columna)

            while bandera != 0:

                while bandera2 != 0:
                    if ren and columna > 3:
                        print("\n-Error, rango invalido")
                        ren = input("Ingresa el renglon:  ")
                        while not ren.isnumeric():
                            print("\nHaz cometido un error al ingresar el dato.")
                            ren = input("Intentalo de nuevo: ")
                        ren = int(ren)

                        columna = input("Ingresa la columna:  ")
                        while not columna.isnumeric():
                            print("\nHaz cometido un error al ingresar el dato.")
                            columna = input("Intentalo de nuevo: ")
                        columna = int(columna)
                    else:
                        bandera2 = 0

                if matriz_de_juego[ren][columna] == " ":
                    matriz_de_juego[ren][columna] = jugador2
                    imprimir_matriz(matriz_de_juego)
                    bandera = 0
                else:
                    print("\nError, ocupado")
                    ren = input("Ingresa el renglon:  ")
                    while not ren.isnumeric():
                        print("Haz cometido un error al ingresar el dato.")
                        ren = input("Intentalo de nuevo: ")
                    ren = int(ren)

                    columna = input("Ingresa la columna:  ")
                    while not columna.isnumeric():
                        print("\nHaz cometido un error al ingresar el dato.")
                        columna = input("Intentalo de nuevo: ")
                    columna = int(columna)

        if ganador(matriz_de_juego, jugador2):
            print("Gana Jugadro 2")
            contador = 0
            break

        contador2 = 0
        contador3 = 0
        for renglones in matriz_de_juego:
            for i in range(0, 3):
                if renglones[contador2] == jugador or renglones[contador2] == jugador2:
                    contador3 += 1
                contador2 += 1
            contador2 = 0

        if contador3 == 9:
            print("\nEmpate")
            contador = 0
            break

        bandera = None

def menu_para_Gato()->None:
    opcion = None
    while opcion != 0:
        opcion = menu_de_interaccion()
        if opcion == 1:
            jugar_contra_cpu()
        elif opcion == 2:
            jugar_contra_jugador2()
        else:
            print("Programa Terminado. :)")

if __name__ == '__main__':
    menu_para_Gato()
