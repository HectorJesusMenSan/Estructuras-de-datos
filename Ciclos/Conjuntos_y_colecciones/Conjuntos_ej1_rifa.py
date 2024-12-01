"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          26 de noviembre de 2024.
Descripción:   Programa de práctica en actividad
               y tema relacionado con los conjuntos.

 ***  Rifa de una computadora  ***
1) Ver correos de participantes.
2) Agregar correo de participante.
3) Eliminar correo de participante.
4) Seleccionar ganador.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice un conjunto para almacenar los correos de los participantes.
b) Utilice un valor aleatorio utilizando la función random.choice(lista). Notar que hay que convertir primero a una lista.
"""

from random import random, choice


# Declaración de Funciones:


# Función, muestra un menú al usuario
def menu():
    # Imprime letreros interactivos
    print("\n______________________________________________")
    print("\n\t###Bienvenido al programa de rifas####")
    print("1) Ver correos de participantes.")
    print("2) Agregar correo de participante.")
    print("3) Eliminar correo de participante.")
    print("4) Seleccionar ganador.")
    print("0) Salir.")
    # Registra opción elegida
    opcion = int(input("-Selecciona la acción deseada: "))
    return opcion

# Función para ver elementos en un conjunto: Recibe un conjunto, no retorna nada
def ver_participantes(conjunto_de_correos):
    # Verifica si el conjunto está vacío
    contador_de_correos = len(conjunto_de_correos)

    if contador_de_correos != 0:  # Si el conjunto tiene elementos
        # Imprime los correos
        print("\n-Los correos de los participantes son: ")
        for elementos in conjunto_de_correos:
            print(end="-")
            print(elementos)
            print("\n")
    # Si el conjunto no tiene elementos
    else:
        print("\n-Aún no se han agregado correos de participantes.")

# Función para agregar correos: Recibe un conjunto, retorna el conjunto actualizado
def agregar_correos(conjunto_de_correos):
    print("_________________________________________________________________________________________________")
    print("\n_SECCIÓN DE AGREGADO_")
    # Solicita cantidad de personas a agregar:
    cantidad_de_elementos_a_agregar = int(input("Ingresa la cantidad de personas que deseas agregar a la rifa: "))
    if cantidad_de_elementos_a_agregar > 0:
        for iterador in range(1, cantidad_de_elementos_a_agregar + 1):
            # Agrega elementos en el conjunto
            elemento_a_agregar = input("Ingresa el correo del participante: ")
            conjunto_de_correos.add(elemento_a_agregar)
            print("Elemento agregado")
    else:
        print("Error, inténtalo de nuevo.")
    return conjunto_de_correos

# Función para eliminar elementos en un conjunto: Recibe un conjunto, retorna conjunto actualizado
def eliminar_elementos(conjunto_de_correos):
    print("_________________________________________________________________________________________________")
    # Verifica si el conjunto tiene elementos
    contador_de_correos = len(conjunto_de_correos)
    if contador_de_correos != 0:
        ver_participantes(conjunto_de_correos)  # Llamada a función para ver o mostrar elementos en pantalla
        # Lectura de datos
        correo_a_eliminar = input("Escribe bien el correo a eliminar: ")
        conjunto_de_correos.remove(correo_a_eliminar)
        print("Elemento eliminado")
    else:
        print("No hay elementos que eliminar.")
    return conjunto_de_correos

# Función para escoger a un ganador: Recibe un conjunto, no retorna nada
def escoger_ganador(conjunto_de_correos):
    print("_________________________________________________________________________________________________")
    # Verifica si el conjunto tiene elementos
    contador_de_elementos = len(conjunto_de_correos)
    if contador_de_elementos != 0:
        # Convierte el conjunto en una lista
        lista_de_correos = list(conjunto_de_correos)
        # Escoge un elemento dentro de la lista y lo imprime
        print(f"El ganador es: {choice(lista_de_correos)}")
    else:
        print("No hay elementos")

# _______________________________________MÓDULO___________________________________________________________

# Declaración de variables:
conjunto_de_correos = set()
opcion = None


while opcion != 0:
    # Llama a la función que contiene el menú:
    opcion = menu()

    if opcion == 1:
        ver_participantes(conjunto_de_correos)
    elif opcion == 2:
        conjunto_de_correos = agregar_correos(conjunto_de_correos)
    elif opcion == 3:
        conjunto_de_correos = eliminar_elementos(conjunto_de_correos)
    elif opcion == 4:
        escoger_ganador(conjunto_de_correos)
    else:
        print("-Cometiste un error al introducir una opción. Intenta de nuevo")


"""EL programa, muestra un menú al usuario con las acciones que puede realizar.
   Puede agregar, eliminar, ver y seleccionar un ganador."""
