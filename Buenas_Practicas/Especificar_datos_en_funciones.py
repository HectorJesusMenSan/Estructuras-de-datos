"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 8 de enero del 2025
Descripción: En la serie "el juego del calamar" se presenta una version
            del juego piedra papel o tijeras, usado las dos manos, este programa
            intentara imitar la misma dinamica con el cpu y un usuario.
"""
def menu ():
    print("1) convertir a entero")
    print("2) convertir a flotante")
    opcion = int(input("Ingresa la opcion: "))
    return opcion

def cadena_a_entero (cadena: str) -> int|None:
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")

    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int (cadena)
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

    elif opcion == 0:
        print("Programa terminado.")
        op = 0
    else:
        print("Error.")