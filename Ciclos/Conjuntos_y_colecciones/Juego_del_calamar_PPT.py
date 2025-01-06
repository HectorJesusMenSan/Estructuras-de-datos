"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 6 de enero del 2025
Descripción: En la serie "el juego del calamar" se presenta una version
            del juego piedra papel o tijeras, usado las dos manos, este programa
            intentara imitar la misma dinamica con el cpu y un usuario.
"""
from random import choice



#_____________________________________________FUNCIONES__________________________________________________________________________

# Definición de función: Menú.
def menu():
    lista_de_valores = []
    contador = 0
    print("Bienvenido/a al juego :)\n")
    while contador<2:
        print("-----------------------------------------------------")
        print(f"Escoge una opcion para tu mano {contador + 1} : \n")
        print("[1]. Piedra")
        print("[2]. Papel")
        print("[3]. Tijeras")
        print("-----------------------------------------------------")
        # Lectura y solicitud de datos.
        opcion = int(input("Presiona la tecla para escoger una opción: \n"))
        if opcion>0 and opcion<=3:
            if opcion == 1:
                opcion = "piedra"
            elif opcion == 2:
                opcion = "papel"
            else :
                opcion = "tijeras"
            lista_de_valores.append(opcion)
            contador += 1
        else:
            print("Erorr :(")

    # Retorna la opción escogida por el usuario
    return lista_de_valores

def parte_del_cpu ():
    lista_de_opciones_de_cpu = ["piedra", "papel", "tijeras"]
    lista_de_opciones_selecconadas=[]
    contador = 1
    while contador<=2:
        opcion = choice(lista_de_opciones_de_cpu)
        lista_de_opciones_selecconadas.append(opcion)
        contador +=1

    print("Las opciones del cpu son: ")
    for opciones in lista_de_opciones_selecconadas:
        print(f"-{opciones}")

    opcion_a_elegir = choice(lista_de_opciones_selecconadas)
    return opcion_a_elegir


def desarrollo_de_juego (diccionario_de_opciones_ganadoras, lista1):

    opcion_del_cpu = parte_del_cpu()
    contador = 0

    print("Tu escogiste: ")
    for opciones in lista1:
        print(f"[{contador}] {opciones}")
        contador += 1
    opcion_a_eliminar = int(input("Escoge una opcion para eliminar: "))
    del lista1[opcion_a_eliminar]
    opcion_de_usuario = int(lista1)

    if opcion_de_usuario == opcion_del_cpu:
        print("El resultado es empate")
    else:
        tupla_de_resultados = (opcion_de_usuario, opcion_del_cpu)
        for jugada in diccionario_de_opciones_ganadoras:
            if tupla_de_resultados == jugada:
                print("Jugador gana")
                bandera=1
        if bandera == 0:
            print("Cpu gana")






#______________________________________________MODULO___________________________________________________________________
diccionario_de_opciones_ganadoras = {'jugada1' : ("piedra", "tijeras"),
                                     'jugada2': ("papel", "piedra"),
                                     'jugada3': ("tijeras", "papel")}
lista1 = menu()

desarrollo_de_juego(diccionario_de_opciones_ganadoras, lista1)