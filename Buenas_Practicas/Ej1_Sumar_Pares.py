"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 28 de enero del 2025
Descripción: Ejercicio para mejorar la habilidad en el tema de
             argumentos variables.
"""
def calcular_suma(*vargs: list) -> None:
    """
    Calcula de la lista recibida la suma de todos los números pares.
    :param vargs: Una lista que contiene números ingresados por el usuario.
    :return: No retorna nada, pero muestra en pantalla los resultados.
    """
    suma = 0
    if len(vargs) != 0:
        for numeros in vargs:
            if numeros % 2 == 0:
                suma += numeros
        print(f"La suma de todos los números introducidos es: {suma}")
    else:
        print("No has ingresado ningún dato, lo siento, no te puedo dar un resultado.")

def cadena_a_flotante(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-').replace(".", "")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

def menu_de_iteraccion() -> None:
    """
    Menú que proporciona distintas acciones al usuario para realizar, crea una lista con números
    introducidos y los manda a la función calcular_suma, para que se muestren los resultados.
    :return: No retorna nada
    """
    lista_de_numeros = []
    opcion = None
    while opcion != 0:

        numero = input("Ingresa un número o presiona [s] para parar o mostrar suma: ")
        while not cadena_a_flotante(numero) and numero != "s":

            numero = input("Error, Ingresa la opción nuevamente: ")

        if numero == "s":

            calcular_suma(*lista_de_numeros)

            break
        else:
            numero = float(numero)

            lista_de_numeros.append(numero)

if __name__ == '__main__':
    menu_de_iteraccion()