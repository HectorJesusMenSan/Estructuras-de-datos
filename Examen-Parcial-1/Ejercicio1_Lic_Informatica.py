"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 29 de Octubre de 2024
Descripción: Estos son los ejercicios de evaluación
             para el primer parcial, del curso de
             estructuras de datos.
"""
# Presentación del programa:
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print(":::Nombre: Héctor Jesús::::")
print(":::Examen Parcial 1::::::::")
print(":::Múltiplos y sucesiones::")
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print()

print(" C A R G A N D O  ;) ")
"""
 En esa parte se presentaron algunos
 letreros de información para el
 usuario
 
"""
# Declaración de variable:
contador=0

# Solicitud y almacenamiento de datos:
numero_de_usuario = int(input("Para iniciar el programa, digite un número que será el límite de la sucesión: "))
print("Guardando tu número... :V")
print()

"""
Los letreros pueden hacer que la experiencia
usuario-programa pueda ser más divertida...
"""

#####Procesos correspondientes######

# Sucesión sin modificaciones:
print("Sucesión sin modificaciones: ")
while contador < numero_de_usuario:
    contador+=1
    if contador == numero_de_usuario:
        print(contador, end=".")
        break
    print(contador, end=", ")
contador=0                                  #Reinicia el contador.
print()
'''
Se imprimen los números del 1 hasta el 
límite indicado por el usuario; en
el if se agrega la condición, cuando se
va a imprimir el último número sustituye
la "," por "." para indicar al usuario
que la sucesión ha llegado al límite
correspondido.
'''

# Sucesión con modificaciones:
print("\nSucesión con modificaciones: ")
while contador < numero_de_usuario:


    contador+=1
    if contador < numero_de_usuario:                                # Acciones que ejecutará si el contador es diferente al límite
        if contador %3 == 0 and contador %5 == 0:
            print("Licenciatura en informática", end=", ")
        elif contador %5 == 0:
            print("informática", end= ", ")
        elif contador %3 == 0:
            print("licenciatura", end= ", ")
        else:
            if contador < numero_de_usuario:
                print(contador, end=", ")
    else:                                                           # Acciones que ejecutará si el contador es igual al límite
        if contador %3 == 0 and contador %5 == 0:
            print("Licenciatura en informática", end=". ")
            break
        elif contador % 5 == 0:
            print("informática", end=". ")
            break
        elif contador % 3 == 0:
            print("licenciatura", end=". ")
            break
        else:
            print(contador, end=". ")
print()
"""
El ciclo funciona, primero aumentando el contador en 1
compara si es el múltiplo de 3 o 5, si la condición se
cumple, se imprimen las palabras, licenciatura o  y si son ambas licenciatura en informática, 
dependiendo en qué condición entre; si no son múltiplos 
de 3 o 5 imprime el número, en dado caso que sea el 
límite marcado por el usuario se escribirá con un punto para 
demarcar el final, sino continúa pero con una coma.
Y lo último, si el contador ya es igual que el
límite, y si son múltiplos de 3 o 5, se imprime lo
mismo de antes, solo demarcando el final con un punto.
"""

print("\nPrograma finalizado pequeño/a usuario/a, vuelve pronto. :)")





