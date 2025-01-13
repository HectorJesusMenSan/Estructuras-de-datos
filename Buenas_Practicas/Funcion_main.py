"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 13 de enero del 2025
Descripción: Bibliotecas como en c
"""
def cadena_a_flotante(cadena: str) -> float|None:
    no_guiones = cadena.count("-")
    no_puntos = cadena.count(".")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) and no_puntos in(0,1):
        return float(cadena)
    else:
        return None


def operaciones ( opcion : int) -> None:

    """
    Funcion que hace las operaciones correspondientes, a la opcion
    escogida por el usuario
    :param opcion: opcion escogida por el usuario
    :return: no retorna nada
    """

    numero1 = input("Ingresa un numero: ")
    numero1 = cadena_a_flotante(numero1)
    while numero1 is None:
        numero1 = input("Vuelve a escribir el numero: ")
        numero1 = cadena_a_flotante(numero1)

    numero2 = input("Ingresa otro numero")
    numero2 = cadena_a_flotante(numero2)
    while numero2 is None:
        numero2 = input("Vuelve a escribir el numero: ")
        numero2 = cadena_a_flotante(numero2)

    if opcion == 1:

        print(f"La el resultado de la suma es {numero1 + numero2}")
    else:
        print(f"La resta de los numeros es {numero1 - numero2}")


def menu() -> int:
    """
    Muestra el menu del programa
    :return: Dato que el usuario escogio para realizar acciones disponibles
    """
    print("__________________________________________________________________________")
    print("\n1) Sumar")
    print("2) Restar")
    print("0) Salir")
    print("__________________________________________________________________________")
    opcion = input("Ingresa la opcion: ")
    print("__________________________________________________________________________")
    while not opcion.isnumeric():
        print("Opcion no valida")
        opcion = input("Intenta nuevamente: ")


    return int(opcion)

#:::::::::::::::::::::::::::::::::::::::::::::MODULO::::::::::::::::::::::::::::::::::::::::::::::::::::
if __name__ == '__main__':
    opcion = None

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Programa terminado.")
        elif opcion == 1:
            operaciones(opcion)
        elif opcion == 2:
            operaciones(opcion)
        else:
            print("Error")
