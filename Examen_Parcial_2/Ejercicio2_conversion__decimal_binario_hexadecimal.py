"""
Héctor Jesús Méndez Santiago
7 de diciembre de 2024.
Descripción: Programa que hace conversiones de datos ingresados por el usuario.
"""


# -----------------------------F-U-C-I-O-N-E-S----------------------------------------------------------------
# Definición de función: No recibe datos, retorna un número entero que es la opción elegida por el usuario
def menu():
    # Escritura de letreros interactivos
    print("\n__________________________________________________________________________________________")
    print("\n ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("1) Convertir de decimal a binario y hexadecimal.")
    print("2) Convertir de binario a decimal y hexadecimal.")
    print("3) Convertir de hexadecimal a decimal y binario.")
    print("0) Salir")
    # Solicitud de datos
    opcion = int(input("-Ingresa una opción: "))

    return opcion


# Definición de función: No recibe datos y retorna una tupla y un número


def conversion_decimal_a_binarioYHexadecimal():
    lista_de_cantidad_binaria = []
    lista_de_cantidad_hexadecimal = []

    numero = int(input("Ingresa un número decimal: "))
    contador = numero
    #####################conversión binario#############################################
    # Ciclo para hacer divisiones
    while contador > 0:
        residuo = contador % 2  # Obtiene el residuo de la división del contador entre 2
        lista_de_cantidad_binaria.append(residuo)  # Guardar el residuo en lista
        contador = contador // 2  # Reduce el número dividiéndolo entre 2

    lista_de_cantidad_binaria.reverse()  # Invierte la lista

    #####################conversión hexadecimal#############################################
    contador = numero
    # Ciclo para hacer divisiones
    while contador > 0:
        residuo = contador % 16  # Obtiene el residuo de la división del contador entre 16
        lista_de_cantidad_hexadecimal.append(residuo)  # Guardar el residuo en lista
        contador = contador // 16  # Reduce el número dividiéndolo entre 16

    lista_de_cantidad_hexadecimal.reverse()  # Invierte la lista

    cantidad_de_elementos = len(lista_de_cantidad_hexadecimal)  # Calcula la cantidad de elementos en la lista

    for elemento in range(cantidad_de_elementos):
        # Itera sobre la lista, si en dado caso encuentra un residuo que está en este rango: 10-15, cambia el valor

        if lista_de_cantidad_hexadecimal[elemento] == 10:
            lista_de_cantidad_hexadecimal[elemento] = "A"

        elif lista_de_cantidad_hexadecimal[elemento] == 11:
            lista_de_cantidad_hexadecimal[elemento] = "B"

        elif lista_de_cantidad_hexadecimal[elemento] == 12:
            lista_de_cantidad_hexadecimal[elemento] = "C"

        elif lista_de_cantidad_hexadecimal[elemento] == 13:
            lista_de_cantidad_hexadecimal[elemento] = "D"

        elif lista_de_cantidad_hexadecimal[elemento] == 14:
            lista_de_cantidad_hexadecimal[elemento] = "E"

        elif lista_de_cantidad_hexadecimal[elemento] == 15:
            lista_de_cantidad_hexadecimal[elemento] = "F"

    # Guarda las listas en una tupla
    tupla_de_resultados = (lista_de_cantidad_binaria, lista_de_cantidad_hexadecimal)
    # Retorna la tupla y el número ingresado
    return tupla_de_resultados, numero


# Definición de función
def conversion_binario_a_decimalYHexadecimal():
    lista_de_numero_binario = []
    lista_de_cantidad_hexadecimal = []

    lista_auxiliar = []

    # Lectura de datos:
    caracteres = input("Ingresa número binario: ")

    # Conversión a enteros
    for numero in caracteres:
        lista_de_numero_binario.append(int(numero))

    # Cantidad de elementos en lista
    cantidad_de_lista = len(lista_de_numero_binario)

    # Multiplicación y suma de los valores:
    for iterador in range(0, cantidad_de_lista):
        lista_auxiliar.append(lista_de_numero_binario[iterador] * (2 ** iterador))

    # Se suman los elementos de la lista
    numero_en_decimal = sum(lista_auxiliar)
    # -------------------------Binario a hexadecimal------------------------------------------------------------

    contador = numero_en_decimal
    # Ciclo para hacer divisiones
    while contador > 0:
        residuo = contador % 16  # Obtiene el residuo de la división del contador entre 16
        lista_de_cantidad_hexadecimal.append(residuo)  # Guardar el residuo en lista
        contador = contador // 16  # Reduce el número dividiéndolo entre 16

    lista_de_cantidad_hexadecimal.reverse()  # Invierte la lista

    cantidad_de_elementos = len(lista_de_cantidad_hexadecimal)  # Calcula la cantidad de elementos en la lista

    for elemento in range(cantidad_de_elementos):
        # Itera sobre la lista, si en dado caso encuentra un residuo que está en este rango: 10-15, cambia el valor

        if lista_de_cantidad_hexadecimal[elemento] == 10:
            lista_de_cantidad_hexadecimal[elemento] = "A"

        elif lista_de_cantidad_hexadecimal[elemento] == 11:
            lista_de_cantidad_hexadecimal[elemento] = "B"

        elif lista_de_cantidad_hexadecimal[elemento] == 12:
            lista_de_cantidad_hexadecimal[elemento] = "C"

        elif lista_de_cantidad_hexadecimal[elemento] == 13:
            lista_de_cantidad_hexadecimal[elemento] = "D"

        elif lista_de_cantidad_hexadecimal[elemento] == 14:
            lista_de_cantidad_hexadecimal[elemento] = "E"

        elif lista_de_cantidad_hexadecimal[elemento] == 15:
            lista_de_cantidad_hexadecimal[elemento] = "F"

    # Retorna dos variables
    return numero_en_decimal, lista_de_cantidad_hexadecimal


# Definición de función
def conversion_hexadecimal_a_decimalYBinario():
    # Declaración de Listas
    lista_de_numero_hexadecimal = []
    lista_auxiliar = []
    lista_auxiliar2 = []
    lista_de_cantidad_binaria = []

    # Solicitud de datos
    caracteres = input("Ingresa número hexadecimal: ")

    # Se agregan los datos uno por uno a una lista
    for numero in caracteres:
        lista_de_numero_hexadecimal.append(numero)

    # Se calcula la cantidad de elementos
    cantidad_de_lista = len(lista_de_numero_hexadecimal)

    # Convierte los caracteres a enteros
    for numero in range(0, cantidad_de_lista):
        if lista_de_numero_hexadecimal[numero] == "A":
            lista_auxiliar2.append(10)
        elif lista_de_numero_hexadecimal[numero] == "B":
            lista_auxiliar2.append(11)
        elif lista_de_numero_hexadecimal[numero] == "C":
            lista_auxiliar2.append(12)
        elif lista_de_numero_hexadecimal[numero] == "D":
            lista_auxiliar2.append(13)
        elif lista_de_numero_hexadecimal[numero] == "E":
            lista_auxiliar2.append(14)
        elif lista_de_numero_hexadecimal[numero] == "F":
            lista_auxiliar2.append(15)
        else:
            lista_auxiliar2.append(int(lista_de_numero_hexadecimal[numero]))

    # Se vuelve a calcular la cantidad
    cantidad_de_lista = len(lista_auxiliar2)
    # Se invierte la lista
    lista_auxiliar2.reverse()
    # Se ejecutan las multiplicaciones de los valores
    for iterador in range(0, cantidad_de_lista):
        lista_auxiliar.append((lista_auxiliar2[iterador]) * (16 ** iterador))

    # Se suman todos los valores de la lista
    numero_en_decimal = sum(lista_auxiliar)

    #####################conversión binario#############################################
    # Ciclo para hacer divisiones
    contador = numero_en_decimal
    while contador > 0:
        residuo = contador % 2  # Obtiene el residuo de la división del contador entre 2
        lista_de_cantidad_binaria.append(residuo)  # Guardar el residuo en lista
        contador = contador // 2  # Reduce el número dividiéndolo entre 2

    lista_de_cantidad_binaria.reverse()  # Invierte la lista

    return numero_en_decimal, lista_de_cantidad_binaria


# -------------------------------------------M-Ó-D-U-L-O--------------------------------------------------------
opcion = None
lista1 = []
lista2 = []

while opcion != 0:
    opcion = menu()

    if opcion >= 0 and opcion <= 3:
        if opcion == 0:
            print("Salida del programa exitosa.")
        elif opcion == 1:
            # Llamada a la función
            tupla_de_conversion, numero = conversion_decimal_a_binarioYHexadecimal()  # Guarda los datos retornados en variables

            # Desempaqueta las listas de la tupla
            lista1, lista2 = tupla_de_conversion

            # Imprime el contenido de las listas:
            print(f"\nEl número {numero} en binario es: ", end="")
            for elemento in lista1:
                print(elemento, end="")

            print(f"\nEl número {numero} en hexadecimal es: ", end="")
            for elemento in lista2:
                print(elemento, end="")

        elif opcion == 2:
            numero_decimal, lista1 = conversion_binario_a_decimalYHexadecimal()
            print(f"El número en decimal es: {numero_decimal}")

            # Imprime el contenido de las listas:
            print(f"\nEl número en hexadecimal es: ", end="")
            for elemento in lista1:
                print(elemento, end="")

        else:
            numero, lista2 = conversion_hexadecimal_a_decimalYBinario()
            print(f"El número en decimal es: {numero}")

            # Imprime el contenido de las listas:
            print(f"\nEl número en binario es: ", end="")
            for elemento in lista2:
                print(elemento, end="")
    else:
        print("ERROR. OPCIÓN INVÁLIDA")


"""El programa consiste en convertir un número introducido 
  por el usuario, ya sea decimal, hexadecimal o binario, 
  dependiendo de la elección del usuario."""