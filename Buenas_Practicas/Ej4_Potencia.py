"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 27 de enero del 2025
Descripción: Ejercicio para mejorar la habilidad en funciones recursivas.
"""





def validaciones(cadena1: str, cadena2:str) -> True | False:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param cadena1: Cadena a validar.
    :param cadena2: Segunda cadena a validar.
    :return: Si las cadenas cumplen con la condicion de ser numericos.
    """
    if cadena1.isnumeric() and cadena2.isnumeric():
        return True

    else:
        return False

def EjecutarPotenciacion(base:int, exponente:int)-> int | None:
    """
    Función que calcula la potencia b de a.
    :param base: Número base a.
    :param exponente: Exponente b.
    :return: El número a a la potencia b.
    """
    if base == 0 and exponente == 0:
        return 0
    else:
        return base*(base **(exponente-1))


def menu_principal()->None:
    """
    Función principal de interacción
    :return: Sin retornos
    """
    base = input("Ingresa el número base a: ")
    exponente = input("Ingrese el exponente b: ")
    if validaciones(base, exponente):
        base, exponente = int(base), int(exponente)
        if base ==0 and exponente == 0:
            print(f"{base} ^ {exponente}: Error, no es posible mostrar un esultado.")
        else:
            potencia_numero = EjecutarPotenciacion(base, exponente)
            if potencia_numero == 0:
                print("Error")
            else:
                print(f"{base} ^ {exponente}: {potencia_numero}")
    else:
        print("Error")

if __name__ == '__main__':
    menu_principal()