"""
Héctor Jesús Méndez Santiago
7 de diciembre de 2024.
Descripción: Programa que hace conversiones de datos ingresados por el usuario.
"""


#_____________________________________FUNCIONES__________________________________________
def menu():
    # Escritura de letreros
    print("\n_____________________________________________________")
    print("\n Bienvenido al traductor: ")
    print("1) Convertir un texto a lenguaje básico.")
    print("2) Convertir un texto a lenguaje intermedio.")
    print("0) Salir.")
    # Lectura de datos
    opcion = int(input("Ingresa la opción que deseas ejecutar: "))
    return opcion   # Retorna la opción escogida por el usuario

# Función para el lenguaje básico
def lenguaje_basico(Diccionario_de_palabras):
    lista_de_palabras = []
    texto = input("Ingresa el texto: ")
    # Agrega letra por letra a la lista
    for palabra in texto:
        lista_de_palabras.append(palabra)
    # Calcula la cantidad de elementos de la lista de palabras
    cantidad_de_elementos = len(lista_de_palabras)

    # Se asignan los valores dependiendo de los caracteres guardados en el diccionario.
    for iterador in range(0, cantidad_de_elementos):
        if lista_de_palabras[iterador] == "a" or lista_de_palabras[iterador] == "A":
            lista_de_palabras[iterador] = Diccionario_de_palabras['vocales'][0]
        elif lista_de_palabras[iterador] == "e" or lista_de_palabras[iterador] == "E":
            lista_de_palabras[iterador] = Diccionario_de_palabras['vocales'][1]
        elif lista_de_palabras[iterador] == "i" or lista_de_palabras[iterador] == "I":
            lista_de_palabras[iterador] = Diccionario_de_palabras['vocales'][2]
        elif lista_de_palabras[iterador] == "o" or lista_de_palabras[iterador] == "O":
            lista_de_palabras[iterador] = Diccionario_de_palabras['vocales'][3]
        elif lista_de_palabras[iterador] == "u" or lista_de_palabras[iterador] == "U":
            lista_de_palabras[iterador] = Diccionario_de_palabras['vocales'][4]

    # Imprime letrero
    print("El texto traducido es: ")
    # Imprime el texto traducido
    for palabra in lista_de_palabras:
        print(palabra, end="")

# Función para el lenguaje intermedio
def lenguaje_intermedio(Diccionario_de_palabras):
    lista_de_palabras = []
    texto = input("Ingresa el texto: ")
    # Agrega letra por letra a la lista
    for palabra in texto:
        lista_de_palabras.append(palabra)
    # Calcula la cantidad de elementos de la lista de palabras
    cantidad_de_elementos = len(lista_de_palabras)

    # Se asignan los valores dependiendo de los caracteres guardados en el diccionario.
    for iterador in range(0, cantidad_de_elementos):
        if lista_de_palabras[iterador] == "a" or lista_de_palabras[iterador] == "A":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][0]

        elif lista_de_palabras[iterador] == "b" or lista_de_palabras[iterador] == "B":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][1]

        elif lista_de_palabras[iterador] == "c" or lista_de_palabras[iterador] == "C":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][2]

        elif lista_de_palabras[iterador] == "d" or lista_de_palabras[iterador] == "D":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][3]

        elif lista_de_palabras[iterador] == "e" or lista_de_palabras[iterador] == "E":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][4]

        elif lista_de_palabras[iterador] == "f" or lista_de_palabras[iterador] == "F":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][5]

        elif lista_de_palabras[iterador] == "g" or lista_de_palabras[iterador] == "G":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][6]

        elif lista_de_palabras[iterador] == "h" or lista_de_palabras[iterador] == "H":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][7]

        elif lista_de_palabras[iterador] == "i" or lista_de_palabras[iterador] == "I":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][8]

        elif lista_de_palabras[iterador] == "j" or lista_de_palabras[iterador] == "J":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][9]

        elif lista_de_palabras[iterador] == "k" or lista_de_palabras[iterador] == "K":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][10]

        elif lista_de_palabras[iterador] == "l" or lista_de_palabras[iterador] == "L":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][11]

        elif lista_de_palabras[iterador] == "m" or lista_de_palabras[iterador] == "M":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][12]

        elif lista_de_palabras[iterador] == "n" or lista_de_palabras[iterador] == "N":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][13]

        elif lista_de_palabras[iterador] == "o" or lista_de_palabras[iterador] == "O":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][14]

        elif lista_de_palabras[iterador] == "p" or lista_de_palabras[iterador] == "P":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][15]

        elif lista_de_palabras[iterador] == "q" or lista_de_palabras[iterador] == "Q":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][16]

        elif lista_de_palabras[iterador] == "r" or lista_de_palabras[iterador] == "R":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][17]

        elif lista_de_palabras[iterador] == "s" or lista_de_palabras[iterador] == "S":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][18]

        elif lista_de_palabras[iterador] == "t" or lista_de_palabras[iterador] == "T":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][19]

        elif lista_de_palabras[iterador] == "u" or lista_de_palabras[iterador] == "U":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][20]

        elif lista_de_palabras[iterador] == "v" or lista_de_palabras[iterador] == "V":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][21]

        elif lista_de_palabras[iterador] == "w" or lista_de_palabras[iterador] == "W":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][22]

        elif lista_de_palabras[iterador] == "x" or lista_de_palabras[iterador] == "X":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][23]

        elif lista_de_palabras[iterador] == "y" or lista_de_palabras[iterador] == "Y":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][24]

        elif lista_de_palabras[iterador] == "z" or lista_de_palabras[iterador] == "Z":
            lista_de_palabras[iterador] = Diccionario_de_palabras['abecedario'][25]

    # Imprime letrero
    print("El texto traducido es: ")
    # Imprime el texto traducido
    for palabra in lista_de_palabras:
        print(palabra, end="")

#____________________________________MÓDULO_______________________________________________
# Declaración de variables
Diccionario_de_palabras = {'vocales': ["4", "3", "1", "0", "(_)"],
                           'abecedario': ["4", "|3", "[", "|)", "3", "ph", "6", "#", "1", "]",
                                          "|<", "1", "/\/\ ", "|\|", "0", "|>", "0_", "|2", "5", "7",
                                          "(_)", "\/", "\/\/", "><", "j", "2"]}

opcion = None

# Ejecución de ciclo
while opcion != 0:
    opcion = menu()

    # Instrucciones que se ejecutan dependiendo de la opción recibida.
    if opcion == 1:
        lenguaje_basico(Diccionario_de_palabras)    # Llamada a función.
    elif opcion == 2:
        lenguaje_intermedio(Diccionario_de_palabras)  # Llamada a función.
    elif opcion == 0:
        print("Salida del programa exitosa.")
    else:
        print("ERROR, OPCIÓN INVÁLIDA.")

"""El programa consiste en verificar cada una de las palabras en un 
   texto introducido por el usuario y cambiarlas, ya sea por el 
   abecedario o las vocales en lenguaje Hacker, dependiendo de la 
   elección del usuario."""