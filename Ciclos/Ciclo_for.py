"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          6 de noviembre de 2024.
Descripción:    ciclos.
Sintaxis:       for "variable" in "secuencia":
"""
contador_caracteres=0
cadena_de_usuario= input("ingresa un texto: ")
for caracter in cadena_de_usuario:
    contador_caracteres+=1
    print(caracter, end="-")
print(f"la sucesion tiene : {contador_caracteres} letras.")
print("Fin")

###################################################################################
# Listas
alumnos= ["Rosalinda", "Juan", "Yam", "Tania", "Ryan", "Rebe", "Jennofer", "Yo", "Gali", "Patric", "Alberto", "Toro"] #Arreglo pero mejor
for nombre in alumnos:
    print(f"Hola ", nombre)
##################################################################################
# Secuencias de numeros:
    # Es como usar un ciclo for en c o c++
for i in range(1,10):     #plabra o funcion reservada, imprime de 10-1
    print(i, end=", ")


