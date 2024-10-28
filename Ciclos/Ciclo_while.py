"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    ciclos.
"""

numero_registrado = int(input("Ingresa un numero: "))
contador = 1

print(f"los numero del 1 al {numero_registrado}")
while contador <= numero_registrado :
    print(contador)
    contador+=1                                     #No hay contadores unitarios

#Segundo Ejercicio
numero_registrado2 = int(input("Ingresa un numero: "))
contador2 = 1

print(f"los numero del 1 al {numero_registrado2}")
while contador2 <= numero_registrado2 :
    print(contador2, end= " ")
    contador2+=1
print("\nFin de cuenta, fuera del ciclo.")


#tercer ejercicio:
#imprimir todos los numero pares hasta el numero solicitado
numero_de_usuario = int(input("ingresa un  numero cualquiera: "))
contador3 = 1

print(f"los numeros pares de 1 a {numero_de_usuario} son: ")
while contador3<=numero_de_usuario :
    if contador3 %2 == 0 :
        print(contador3, end=" ")
    contador3+=1