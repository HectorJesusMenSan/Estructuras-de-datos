"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          6 de noviembre de 2024.
Descripción:    Programa de inicialización al
                ciclo for.
Sintaxis:       for "variable" in "secuencia":
"""
# Declaración de variables:
contador_caracteres = 0
cadena_de_usuario = input("Ingresa un texto: ")    # Solicita un texto al usuario

for caracter in cadena_de_usuario:
    contador_caracteres += 1                       # Contador de letras
    print(caracter, end="-")                       # Caracter, va tomando el valor de cada letra de la cadena
print(f"La sucesión tiene: {contador_caracteres} letras.")
print("Fin")

"""Para una cadena de caracteres, el for intera en cada una de ellas
   hasta terminar con toda la cadena. La primer variable que creemos en
   la condición del for, se igualará a cada caracter de la cadena,
   desde el inicio, o sea, desde la primera palabra hasta la última."""

###################################################################################
# Listas
"""Es similar con las cadenas de texto, porque al final de cuentas son vectores."""

alumnos = ["Rosalinda", "Juan", "Yam", "Tania", "Ryan", "Rebe", "Jennofer", "Yo", "Gali", "Patric", "Alberto", "Toro"]  # Arreglo pero mejor
for nombre in alumnos:
    print(f"Hola ", nombre)
##################################################################################

# Secuencias de números:
# Es como usar un ciclo for en C o C++
for i in range(1, 10):     # Palabra o función reservada, imprime de 1 a 9
    print(i, end=", ")


