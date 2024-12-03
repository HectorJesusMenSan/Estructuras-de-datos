"""Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          26 de noviembre de 2024.
Descripción:   Programa de práctica en actividad
               y tema relacionado con los conjuntos."""

# Función para el menú:
def menu():
    # Letreros informativos
    print("##Juego: Sin repetir##")
    print("-El juego consiste en introducir una palabra")
    print(" tratando de que no se repitan las palabras")
    print(" ingresadas. Puede jugarse en grupo")
    print("------->  :)  <--------\n")
    # Recepción de datos
    tema_de_palabras = input("¿De qué tema quieres jugar?  ")
    return tema_de_palabras                 # Retorna el tema del juego.
'''El menú muestra en pantalla las reglas y algunos letreros informativos.
   Además, recepciona el tema del que se jugará.'''

# Función para procesar los datos:
def Procesamiento_de_datos(conjunto_de_palabras, tema_de_palabras):
    lista_de_palabras = list(conjunto_de_palabras)                                          # Convierte a lista
    contador = 1                                                                            # Se inicia un contador en 1
    # Solicitud de datos
    palabra_ingresada = input(f"Ingresa una palabra del tema {tema_de_palabras}: ")
    palabra_ingresada = palabra_ingresada.lower()                                           # Convierte a minúsculas
    lista_de_palabras.append(palabra_ingresada)                                             # Se agrega el primer elemento
    # Inicialización de iterador para un ciclo.
    iterador = None
    while iterador != 0:  # Mientras el iterador sea diferente de cero.
        # Lectura de datos
        palabra_ingresada = input(f"Ingresa otra palabra del tema {tema_de_palabras}: ")
        # Verificar la palabra con cada una de las palabras en lista
        for palabra2 in lista_de_palabras:
            if palabra_ingresada == palabra2:
                # Si se presenta un caso de igualdad se imprime el contador y la palabra repetida
                print(f"El juego ha terminado, ingresaste una palabra que se repite, introduciste {contador+1} palabras")
                print(f"La palabra que se repite es: {palabra_ingresada}")
                iterador = 0                                                                # Corta el ciclo
        # Si el código llega hasta aquí quiere decir que no hay igualdades y la palabra se agrega a la lista
        lista_de_palabras.append(palabra_ingresada)
        contador += 1                                                                       # Aumenta el contador

#___________________________________________MÓDULO____________________________________________________________________________________
# Definición de variables
Conjunto_de_palabras = set()

# Llamada a función menú
tema_de_palabras = menu()

# Llamada a función procesamiento de datos
Procesamiento_de_datos(Conjunto_de_palabras, tema_de_palabras)
