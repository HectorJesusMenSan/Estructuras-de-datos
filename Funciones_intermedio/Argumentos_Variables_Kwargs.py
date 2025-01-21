"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 21 de enero del 2025
Descripción: Bibliotecas como en c
"""


def preferencias(tema: str, **kwargs):
    print(f"El tema es {tema}")
    #   LLave Valor
    for keys, value in kwargs.items():
        print(f"Nombre: {keys}, prefiere {value}")


if __name__ == '__main__':

    preferencias("Comida", Rebeca="Mole", Juan="Tacos", Bryan="Tlayudas")