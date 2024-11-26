"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:   Ejercicios para practicar
               Con el tema de tuplas"""



# Definición de función: menu
def menu():                                            # Sin recepción de datos
    # Despliega menú
    print("\n_________________________________________")
    print("[1]  Ver lista de números: ")
    print("[2]  Añadir número a lista: ")
    print("[3]  Determinar el número máximo y mínimo: ")
    print("[0]  salir: ")

    opcion = int(input("Ingresa una opción: "))           # Lectura de datos
    return opcion                                       # Retorna opción escogida


# Definición de función: Ver elementos de lista
def ver_lista(lista_de_numeros):                       # Recibe lista de números
    contador = len(lista_de_numeros)                      # Cuenta elementos de lista

    if contador != 0:
        # Ejecuta acciones mientras la lista tenga datos
        for numero in lista_de_numeros:
            print(numero, end=" ")
    else:
        print("No hay elementos en lista.")


# Definición de función: Agregar elementos
def agregar_numero(lista_de_numeros):
    # Lectura de datos y agregación de datos al último de una lista
    numero = int(input("Ingresa un número: "))
    lista_de_numeros.append(numero)


# Definición de función: Determinar máximo y mínimo
def determinar_max_min(lista_de_numeros):
    # Inicialización de variables
    numero_maximo = 0
    numero_minimo = 0
    # Itera en todos los elementos de la lista
    for numero in lista_de_numeros:
        # Para número mayor
        if numero > numero_maximo:
            numero_maximo = numero
        # Para número menor
        if numero < numero_minimo:
            numero_minimo = numero
    tupla_de_numeros = (numero_maximo, numero_minimo)   # Se agrega la variable mayor y la variable menor en tupla
    return tupla_de_numeros                             # Retorna tupla


# _____________________________ Módulo _________________________________________________________________________
# Declaración de variables
lista_de_numeros = []
opcion = None
# Despliegue de menú hasta que el usuario presione 0
while opcion != 0:

    opcion = menu()
    # ver lista
    if opcion == 1:
        ver_lista(lista_de_numeros)         # Llamada de función
    elif opcion == 2:
        agregar_numero(lista_de_numeros)    # Llamada de función
    elif opcion == 3:
        tupla_de_maximo_minimo = determinar_max_min(lista_de_numeros)  # Llamada de función
        # Imprime cada uno de los elementos de la tupla que retorna la función
        print(f"El número mayor es: {tupla_de_maximo_minimo[0]}")
        print(f"El número menor es: {tupla_de_maximo_minimo[1]}")
    else:
        print("Error")


