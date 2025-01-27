"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 27 de enero del 2025
Descripción: Ejercicio para la presentación del examen del tercer parcial
             Juego 4 en Raya
"""



def menu_operaciones () -> int:
    """
    Mnú que se desplega para la interaccion con el usuario
    :return: Retorna una opcion escogiida por el usuario.
    """

    print("________   Bienbenido. Esa es una calculadora.  _________")
    print("________       [1].Sumar varios numeros.        _________")
    print("________       [2].Multiplicar varios numeros   _________")
    print("________       [0].Salir                        _________")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    opcion = input("Escoge una opcion del menú: ")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    while not opcion.isnumeric() :
        print("Lo siento, no puedes continuar")
        print("Haz ingresado una opcion invalida")
        opcion = input("Intentalo de nuevo")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    return int(opcion)



def Realizar_operaciones (opcion:int, *Vargs):
    resultado = 0
    if opcion == 1:
        print(sum(list(Vargs)))
    else:
        for i in Vargs:
            resultado *= i
        print(resultado)

def recepcion_de_datos ():
    lista_de_numeros = []
    respuesta = None
    while respuesta != "n":

        numero = input("Ingresa numero: ")
        lista_de_numeros.append(numero)

        respuesta = input("Deseas continuar? [S/N]")

        while not respuesta.isalpha():
            print("Error")

            respuesta = input("Intenta de nuevo")
            respuesta = respuesta.lower()

        if len(respuesta) > 1:
            while len(respuesta)!=1:
                print("Error, dato no valido")

                respuesta = input("Intenta de nuevo: ")
                respuesta = respuesta.lower()


    return lista_de_numeros

def menu ():
    tupla = ()
    opcion = None
    while opcion != 0 :
        opcion = menu_operaciones()
        if opcion == 1:
            tupla = recepcion_de_datos()
            Realizar_operaciones(opcion, tupla)

        elif opcion == 2:
            tupla = recepcion_de_datos()
            Realizar_operaciones(opcion, tupla)
        else:
            print("Salda exitosa")


if __name__ == '__main__':
    menu()