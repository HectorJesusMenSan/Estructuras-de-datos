"""Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:   Ejercicios para practicar
               Con el tema de tuplas"""


# Función menú
def menu():
    print("_________________________________________________________")
    print("\n1) Ver coordenadas almacenadas.")
    print("2) Agregar coordenada (x,y).")
    print("3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas.")
    print("4) Eliminar coordenada (x,y).")
    print("0) Salir.")
    opcion = int(input("Escoge opción: "))
    return opcion
"""La función menú despliega un conjunto de letreros informativos
   en la interfaz para que el usuario escoja una de las acciones
   que se puede realizar."""

# Función para ver coordenadas
def ver_coordenadas_guardadas(lista_de_tuplas):
    contador = len(lista_de_tuplas)             # Calcula la cantidad de elementos de la lista
    contador2 = 0                               # Contador para enumerar la cantidad de elementos que existen
    if contador != 0:
        for coordenada in lista_de_tuplas:
            print(f"{contador2}- {coordenada}")     # Imprime el número y el contenido de lista por cada iteración
            contador2 += 1
    else:
        print("No hay coordenadas guardadas.")
        print("_________________________________________________________")
"""La función para ver las coordenadas recibe una lista. Si la lista no contiene nada, muestra 
un mensaje para indicar que no se cuentan con datos, pero si sí contiene, se muestran los datos
sección por sección."""

# Función para agregar coordenadas:
def agregar_coordenadas(lista_de_tuplas):
        # Solicitud de datos
        numero1 = float(input("Agrega tu punto x:  "))
        numero2 = float(input("Agrega tu punto y:  "))

        # Guarda datos en tupla
        tupla_de_coordenada = (numero1, numero2)
        # Guarda tupla en lista
        lista_de_tuplas.append(tupla_de_coordenada)
        return lista_de_tuplas
"""La función recibe del módulo una lista. Esta función solicita datos al usuario, los mete en una
tupla, y la tupla los mete en la lista. Al final retorna la lista de tuplas."""


# Función para eliminar coordenadas:
def eliminar_coordenada(lista_de_tuplas):
    contador_de_lista = len(lista_de_tuplas)
    if contador_de_lista != 0:
        contador = 0
        for tuplas in lista_de_tuplas:
            print(f"{contador}) {tuplas}")
            contador += 1
        opcion_eliminar = int(input("Elige opción: "))
        del lista_de_tuplas[opcion_eliminar]
    else:
        print("No hay nada que eliminar.")
        print("_________________________________________________________")
"""La función eliminar lista muestra el contenido de las coordenadas guardadas en forma
de opciones, para que el usuario pueda escoger qué coordenadas eliminar,
claro, si y solo si la lista tiene datos."""

# Función para calcular la pendiente:
def calcular_pendiente(lista_de_tuplas):
    contador_de_lista = len(lista_de_tuplas)
    if contador_de_lista != 0:
        ver_coordenadas_guardadas(lista_de_tuplas)
        coordenada_a_calcular = int(input("Seleccione la primera coordenada: "))
        tupla_de_coordenadas = tuple(lista_de_tuplas[coordenada_a_calcular])
        coordenada_a_calcular = int(input("Seleccione la segunda coordenada: "))
        tupla_de_coordenadas2 = tuple(lista_de_tuplas[coordenada_a_calcular])         # Convierte a tuplas el contenido de la lista, accede a la posición indicada.
        # Desempaquetado de tuplas:

        x1, y1 = tupla_de_coordenadas
        x2, y2 = tupla_de_coordenadas2

        # Expresión de la recta Y=mx+b
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        print("La pendiente es", m)
        print("La ecuación es:", end=" ")
        print(f"y={m}x + {b}")
        print("_________________________________________________________")
    else:
        print("No disponemos de elementos para hacer cálculos.")
        print("_________________________________________________________")

"""Esta función, al momento de que el usuario seleccione el índice de la lista en donde guardamos datos,
crea un par de tuplas, accediendo a la lista, después se desempaquetan las tuplas y siguiendo el procedimiento del cálculo 
de la pendiente y la ecuación, ejecutamos las operaciones correspondientes, y solo imprimimos."""
#_________________módulo_______________________________________________________________________
# Declaración de variables
opcion = None
lista_de_tuplas = []
# Despliegue de menú hasta que el usuario presione 0
while opcion != 0:

    opcion = menu()
    # Ver lista
    if opcion == 1:
        ver_coordenadas_guardadas(lista_de_tuplas)         # Llamada de función
    elif opcion == 2:
        agregar_coordenadas(lista_de_tuplas)                # Llamada de función
    elif opcion == 3:
        calcular_pendiente(lista_de_tuplas)                # Llamada de función
    elif opcion == 4:
        eliminar_coordenada(lista_de_tuplas)                # Llamada de función
    else:
        print("Error")
