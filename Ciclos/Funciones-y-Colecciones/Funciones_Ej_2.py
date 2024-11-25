"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          7 de noviembre de 2024.
Descripción:    Ejercicio 2, Pirámide:
                Pedir a usuario un dato que demarque
                la cantidad de filas de la pirámide.

                Programa para practicar la utilización
                de ciclos y funciones, en este caso el for.
"""


# Definición de primera función: Pirámide 1
def Primera_piramide(valor_de_filas):               # Recibe el valor de filas otorgado por el usuario
    contador = 0
    for i in range(1, valor_de_filas + 1):      # Itera desde 1 hasta el valor de las filas que dio el usuario
        contador += 1                           # Aumenta el contador en uno
        for i in range(1, contador + 1):        # Itera en un rango de 1 hasta el valor del contador
            print("*", end=" ")                 # Imprime el asterisco junto a un espacio
        print("\n")                             # Fuera del for más interno, imprime salto de línea para el siguiente renglón


# Definición de segunda función: Pirámide 2
def Segunda_piramide(valor_de_filas):              # Recibe el valor de filas otorgado por el usuario
    contador = valor_de_filas                      # Se iguala el contador con el valor de las filas

    for i in range(1, valor_de_filas + 1):         # Itera de 1 hasta el valor de las filas que quiere el usuario
        for i in range(1, contador + 1):           # Itera en un rango de 1 hasta el valor del contador
            print("*", end=" ")                    # Imprime el asterisco junto a un espacio
        print("\n")                                # Imprime salto de línea
        contador -= 1                              # Se resta el contador


# Definición de tercera función: Pirámide 3
def Tercera_piramide(valor_de_filas):              # Recibe el valor de filas otorgado por el usuario
    contador = valor_de_filas                      # Inicialización y declaración de variables
    escrituras = 0
    espacios = 0
    for i in range(1, valor_de_filas + 1):          # Itera en un rango de 1 hasta el valor de filas
        escrituras = "*" * contador                 # Se multiplica el asterisco por el valor del contador
        espacios = " " * i                          # Se multiplican espacios por el valor del iterador
        print(f"{espacios}{escrituras}")            # Imprime los espacios con los asteriscos
        contador -= 1                               # Se resta uno al contador


# Definición de cuarta función: Pirámide 4
def Cuarta_piramide(valor_de_filas):                # Recibe el valor de filas otorgado por el usuario
    contador = 0                                    # Inicialización de variables
    for i in range(1, valor_de_filas + 1):          # Itera en un rango de 1 hasta el valor de filas
        escrituras = "*" * (contador + 1)           # Se multiplican los asteriscos por el contador más uno
        espacios = " " * (valor_de_filas - i)       # Se multiplican espacios por el valor de filas menos uno
        contador += 2                               # Se aumenta el contador en 2
        print(f" {espacios}{escrituras}")           # Imprime los espacios seguidos de los asteriscos


# Función de menú para mostrar las opciones al usuario
def Menu():                                         # No recibe datos
    print("\nM E N U :")
    print("[0] Salir")
    print("[1] Para ver pirámide 1")
    print("[2] Para ver pirámide 2")
    print("[3] Para ver pirámide 3")
    print("[4] Para ver pirámide 4")
    opcion = int(input("Ingresa la opción que deseas: \n"))
    return opcion                                    # Retorna la opción escogida


#--------------------------------------- MÓDULO PRINCIPAL -----------------------------------------------------#

valor_de_filas = int(input("Introduce el número de filas que tendrá tu pirámide: "))  # Lee y guarda datos otorgados por el usuario

opcion = True

# Despliega el menú para que el usuario escoja qué pirámide ver:
while opcion:
    opcion = Menu()                                           # Llamada a la función menú.
    if opcion >= 0 and opcion <= 4:
        if opcion == 0:
            print("Saliendo :(")  # Letrero informativo
            break                 # Rompe el ciclo y termina el programa
        elif opcion == 1:
            print("P R I M E R A   P I R A M I D E :\n")
            Primera_piramide(valor_de_filas)                # Llamada a la función.
        elif opcion == 2:
            print("S E G U N D A   P I R A M I D E :\n")
            Segunda_piramide(valor_de_filas)                # Llamada a la función.
        elif opcion == 3:
            print("T E R C E R A   P I R A M I D E :\n")
            Tercera_piramide(valor_de_filas)                # Llamada a la función.
        else:
            print("C U A R T A   P I R A M I D E :\n")
            Cuarta_piramide(valor_de_filas)                 # Llamada a la función.
    else:
        print("Error")
        print("Reintenta...")



