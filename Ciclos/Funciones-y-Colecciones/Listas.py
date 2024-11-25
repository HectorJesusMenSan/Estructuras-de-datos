"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          12 de noviembre de 2024.
Descripción:    ciclos.

"""

"""
Cola:
El primero en entrar es el primero en salir
F I F O

Pila:
Queue.
L I F O.
La ultima en entrar es la primera en salir
"""

#Crea lista:
alumnos=[]

#inserta valor al final de la lista:
alumnos.append("Hector")
alumnos.append("Addi")
alumnos.append("Alberto")
alumnos.append("Juan")
print(alumnos)
print(alumnos[1])

#insertar valores en indice especifico:
alumnos.insert(1, "Tania")
for alumno in alumnos:
    print(alumno, end=" ")

#Eliminar valores:
print("\n")
alumnos.remove("Hector")
for alumno in alumnos:
    print(alumno, end=" ")

#Eliminar por indice:
alumnos.pop(2)
print("\n")
for alumno in alumnos:
    print(alumno, end=" ")
#Otra manera por indice:
del alumnos[2]
print("\n")
for alumno in alumnos:
    print(alumno, end=" ")
print("\n")

"""Tomar en cuenta que son vectores, asi que para acceder a ellos es de 0 a n numero."""

#Listas Declaradas:
print("\nListas declaradas: ")
alumnos= ["Rosalinda", "Juan", "Yam", "Tania", "Ryan", "Rebe", "Jennofer", "Yo", "Gali", "Patric", "Alberto", "Toro"]
print(alumnos)


#Funciones agregando la lista:
print("\nListas con valor agregado: ")
len(alumnos)
print(alumnos)


alumnos.sort() #Funcion para orden alfabetico
print(alumnos)

alumnos.sort(reverse=True) #Funcion para orden alfabetico, al revez
print(alumnos)

print(alumnos[-2]) #Imprime los valores de atras, o los ultimos