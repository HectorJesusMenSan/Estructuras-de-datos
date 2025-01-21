"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 21 de enero del 2025
Descripción: Son un conjunto de variables, mostrados como una tupla
"""

def colores_favoritos (persona: str, *vargs)-> None:  #Siempre se coloca al final el vargs
    print(f"{persona}:{vargs}")

def Sumar (*vargs) -> int:
    #Sumar los elementos de un vargs en un for:
    resultado = 0
    for i in vargs:
        resultado += i
    return resultado, sum(vargs)


if __name__ == '__main__':
    colores_favoritos("Jennifer", "Morado", "Negro", "Blanco", "Rosa")
    colores_favoritos("Addi", "Azul", "Blanco", "Negro")
    colores_favoritos("Lobetho", "Negro")
    cadena = "HOla"
    tupla = "Hola",
    print(cadena)
    print(tupla)

    res1, res2 = Sumar(5, 3, 4)
    print(f"Prier r={res1}       segundo r={res2}")
