from Examen_Parcial3.Modulo_Ahorcado import menu_para_ahorcado
from Examen_Parcial3.Modulo_Gato import menu_para_Gato


def menu ():

    print("Este es el menu de juegos")
    print("[1]. Gato")
    print("[2]. Ahorcado")
    opcion = input("Ingresa opcion")
    return int(opcion)

def menuuu():
    opcion = None
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            menu_para_Gato()
        elif opcion == 2:
            menu_para_ahorcado()
        else:
            print("Salida conexito")






if __name__ == '__main__':
    menuuu()
