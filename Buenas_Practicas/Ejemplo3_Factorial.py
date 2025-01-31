"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 27 de enero del 2025
Descripción: Ejercicio para mejorar la habilidad en funciones recursivas.
"""

def cadena_a_entero(cadena: str)-> int | None:
    """
    Función que convierte una cadena a entero.
    :param cadena: Cadena a convertir.
    :return: retorna una cadena convertida a entero.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) :
        return int(cadena)
    else:
        return None

def SiEsNumeroValido(cadena: str) -> True|False:
    """
    Función que determina si el número ingresado es mayor o igual a 0.
    :param cadena: Cadena a validar.
    :return: Si la cadena cumple con las condiciones.
    """
    if cadena.isnumeric():
        return True

    else:
        return False

def Ejecutarfactorial(numero:int)->int:
    """
    Función que usa llamada recursiva para calcular el factorial del número ingresado por el usuario.
    :param numero: Número a conocer su factorial.
    :return: Retorna el número ingresado menus uno hasta que sea igual a 1 o 0.
    """
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * Ejecutarfactorial(numero-1)


def Menu_principal()->None:
    """
    Función de interacción de acciones a realizar por el usuario.
    :return: No retorna nada
    """
    numero = input("Ingresa un número mayor o igual a 0 para realizar factorial: ")
    if SiEsNumeroValido(numero):
        numero = int(numero)
        numero_factorial =  Ejecutarfactorial(numero)
        print(f"El factorial del número {numero} es: {numero_factorial}")
    else:
        print("Valor no válido.")

if __name__ == '__main__':
    Menu_principal()