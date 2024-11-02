"""
Nombre: Héctor Jesus Mendez Santiago
Fecha: 29 de Octubre 2024
Descripción: Estos son los ejercicios de evaluacion
             para el primer parcial, del curso de
             estructuras de datos.
"""

# Presentacion del programa:
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print(":::Nombre: Hector Jesus::::")
print(":::Examen Parcial 1::::::::")
print(":::Multiplos y suceciones::")
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print()

print(" C A R G A N D O  ;) ")
"""
 En esa parte se presentaron algunos
 letreros de informacion para el
 usuario
 
"""
# Declaracion de variable:
contador=0

# Solicitud y almacenamiento de datos:
numero_de_usuario = int(input("Para iniciar el programa, digite un numero que sera el limite de la sucesion: "))
print("Guardando tu numero... :V")
print()

"""
Los letreros pueden hacer que la experiencia
usuario-programa pueda ser mas divertido...
"""

#####Procesos correspondientes######

# Sucesion sin modificaciones:
print("Sucesion sin modificaciones: ")
while contador < numero_de_usuario:
    contador+=1
    if contador == numero_de_usuario:
        print(contador, end=".")
        break
    print(contador, end=", ")
contador=0                                  #Reinicia el contador.
print()
'''
Se imprimen los numeros del 1 hasta el 
limite indicado por el usuario; en
el if se agrega la condicion, cuando se
va a imprimir el ultimo numero sutituye
la "," por "." para indicar al usuario
que la sucesion ha llegado al limite
correspondido.
'''

# Susecion con modificaciones:
print("\nSucesion con modificaciones: ")
while contador < numero_de_usuario:


    contador+=1
    if contador < numero_de_usuario:                                # Acciones que ejecutara si el contador es diferente al limite
        if contador %3 == 0 and contador %5 == 0:
            print("Licenciatura en informatica", end=", ")
        elif contador %5 == 0:
            print("informatica", end= ", ")
        elif contador %3 == 0:
            print("licenciatura", end= ", ")
        else:
            if contador < numero_de_usuario:
                print(contador, end=", ")
    else:                                                           # Acciones que ejecutara si el contador es igual al limite
        if contador %3 == 0 and contador %5 == 0:
            print("Licenciatura en informatica", end=". ")
            break
        elif contador % 5 == 0:
            print("informatica", end=". ")
            break
        elif contador % 3 == 0:
            print("licenciatura", end=". ")
            break
        else:
            print(contador, end=". ")
print()
"""
El ciclio funciona, primero aumentando el contador en 1
compara si es el multiplo de 3 o 5, si la condicion se
cumple, se imprime las palabras, "licenciatura" o 
"informatica" y si son ambas "licenciatura en informatica", 
dependiendo en que condicion entre; si no son multiplos 
de 3 o 5 imprime el numero, en dado caso que sea el 
limite marcado por el usuario se escribira con un punto para 
demarcar el final, sino continua pero con una coma.
Y lo ultimo, si el contador ya es igual que el
limite, y si son multiplos de 3 o 5, se imprime lo
mismo de antes, solo demarcando el final con un punto.
"""

print("\nPrograma finalizado pequeño/a usuario/a, vuelve pronto. :)")




