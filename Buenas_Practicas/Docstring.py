"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 9 de enero del 2025
Descripción: Docstring, para documentar funciones.
             Muestra paramametros y datos que retornan.
"""
def menu ()->int:
    """
    Muestra el menu del programa
    :return: Dato que el usuario escogio para realizar acciones disponibles
    """
    print("__________________________________________________________________________")
    print("\n1) convertir a entero")
    print("2) convertir a flotante")
    print("0) Salir")
    print("__________________________________________________________________________")
    opcion = input("Ingresa la opcion: ")
    print("__________________________________________________________________________")
    while not opcion.isnumeric():
        print("Opcion no valida")
        opcion = input("Intenta nuevamente: ")

    return int (opcion)

def cadena_a_entero (cadena: str) -> int|None:
    """

    :param cadena: Es la cadena a convertir a numero entero

    funcion que convierte cadenas en numeros enteros, con validaciones correctas.

    :return: Un dato entero o un none en caso de que no se introduzca un numero correcto
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")

    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int (cadena)
    else:
        return None

def cadena_a_flotante(cadena: str) -> float|None:
    no_guiones = cadena.count("-")
    no_puntos = cadena.count(".")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) and no_puntos in(0,1):
        return float(cadena)
    else:
        return None

op = 1


while op != 0:
    opcion = menu()
    if opcion == 1:
        num_cadena = input("Ingresa numero a convertir: ")
        num = cadena_a_entero (num_cadena)
        while num is None:
            num_cadena = input("Ingresa numero a convertir: ")
            num = cadena_a_entero(num_cadena)
        print(f"El numero {num} es de tipo {type(num)}")
    elif opcion == 2:
        num_cadena = input("Ingresa numero a convertir: ")
        num = cadena_a_flotante (num_cadena)
        while num is None:
            num_cadena = input("Ingresa numero a convertir: ")
            num = cadena_a_flotante(num_cadena)
        print(f"El numero {num} es de tipo {type(num)}")

    else:
        print("Programa terminado.")
        op = 0
