"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 8 de enero del 2025
Descripción: En la serie "el juego del calamar" se presenta una version
            del juego piedra papel o tijeras, usado las dos manos, este programa
            intentara imitar la misma dinamica con el cpu y un usuario.
"""


#TODO implementar menu: todo es para las tareas pendientes.
def menu():
    pass
#TODO
def cadena_a_entero (cadena):
    ...
#FIXME: Revisar errores o bugs

def cadena_a_flotante (cadena):
    raise NotImplementedError("Implementar funcion") #Implementar un error


opcion = menu()
while opcion != 0:
    if opcion == 1:
        num_cadena = input("Ingresa numero a convertir: ")
        num = cadena_a_entero (num_cadena)
    elif opcion == 2:
        num_cadena = input("Ingresa numero a convertir: ")
        num = cadena_a_flotante (num_cadena)
    elif opcion == 0:
        print("Programa terminado.")
    else:
        print("Error.")