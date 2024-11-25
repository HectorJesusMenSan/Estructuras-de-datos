"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          12 de noviembre de 2024.
Descripción:    Ejercicios de practica, listas.
                Listas de compras.
                Programa para agregar, ver
                y eliminar productos elegidos
                por el usuario.
"""


#Declaracion de lista:
lista_de_compras=[]

# Funcion de menu:
def Menu ():                                                    # Sin recepción de datos.
    # Imresion de letreros informativos:
    print("\n______________________________________________")
    print("|     1) Ver lista.                          |")
    print("|     2) Añadir producto a la lista.         |")
    print("|     3) Eliminar producto de la lista.      |")
    print("|     0) Salir.                              |")
    print("|____________________________________________|")
    # Solicitud de datos:
    opcion_del_menu=int(input("ingresa una opción:      "))
    return opcion_del_menu                                      # Retorna un numero.



# Funcion para añadir productos:
def Añadir_productos (lista_de_compras):                        # Recibe una lista.
    # Creacion de una lista auxiliar:
    lista_de_nombre_y_cantidad=[]

    # Solicitud de datos:
    nombre_de_producto_a_agregar, cantidad_de_producto  = input("Ingresa el producto que deseas agregar a la lista: "), input("Ingresa la cantidad: ")

    # Guarda datos en lista auxiliar:
    lista_de_nombre_y_cantidad.append(nombre_de_producto_a_agregar)
    lista_de_nombre_y_cantidad.append(cantidad_de_producto)

    # Guarda lista auxiliar en lista original:
    lista_de_compras.append(lista_de_nombre_y_cantidad)


    return lista_de_compras                                     # Retorna una lista.



#   Funcion para eliminar producto:
def Eliminar_producto (lista_de_compras):                       # Recibe una lista.
    contador=0

    # Ciclo que imprime en pantalla las opciones a eliminar:
    for i in lista_de_compras:
        print(f"\n{contador})  {i} ")
        contador += 1

    # Solicitud de datos:
    casilla_a_eliminar = int(input("\nEscoge que producto eliminar: "))
    lista_de_compras.pop(casilla_a_eliminar)
    return lista_de_compras                                     # Retorna una lista.

#########################################################################################################################################################################

# Modulo o menu principal:

opcion=None
while opcion != 0:
    opcion = Menu()

    if opcion == 1:
        print("\nLa lista de las compras es: ")
        print(lista_de_compras)

    elif opcion == 2:
        Añadir_productos(lista_de_compras)
        print()
        print(lista_de_compras)
    elif opcion == 3:
        Eliminar_producto(lista_de_compras)
        print(lista_de_compras)
    if opcion>3:
        print("Error")

print("Programa finalizado.")



