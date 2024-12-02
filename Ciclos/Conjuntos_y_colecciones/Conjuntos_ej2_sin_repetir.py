"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          26 de noviembre de 2024.
Descripción:   Programa de práctica en actividad
               y tema relacionado con los conjuntos."""
def menu ():
    print("##Juego: Sin repetir##")
    print("-El juego consiste en introducir una palabra")
    print(" tratando de que no se repitan las palabras")
    print(" ingresadas. Puede jugarce en grupo")
    print("------->  :)  <--------\n")

    tema_de_palabras = input("De que tema quieres jugar?  ")
    return tema_de_palabras


def leer_datos (conjunto_de_palabras, tema_de_palabras):
    lista_de_palabras = list(conjunto_de_palabras)
    contador = 1
    palabra_ingresada = input(f"Ingresa una palabra del tema {tema_de_palabras}: ")
    palabra_ingresada = palabra_ingresada.lower()
    lista_de_palabras.append(palabra_ingresada)
    iterador = None
    while iterador!=0:
        palabra_ingresada = input(f"Ingresa otra palabra del tema {tema_de_palabras}: ")
        for palabra2 in lista_de_palabras:
            if palabra_ingresada == palabra2:
                print(f"El juego a terminado, ingresaste una palabra que se repite, introduciste {contador} palabras")
                print(f"La palabra que se repite es: {palabra_ingresada}")
                break
        lista_de_palabras.append(palabra_ingresada)
        contador+=1

#___________________________________________MODULO____________________________________________________________________________________
#Definicion de variables
Conjunto_de_palabras = set()

tema_de_palabras = menu()

leer_datos(Conjunto_de_palabras, tema_de_palabras)