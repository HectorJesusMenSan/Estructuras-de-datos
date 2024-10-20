"""
Nombre: Héctor Jesús Méndez Santiago.
fecha:  16 de octubre de 2024.
Descripción: Segundo ejercicio de practica en operadores
             lógicos y relacionales.
"""

"""
#Solicitar un número.
#Devolver un TRUE si este número ingresado
se encuentra en un rango de: 10-15.

"""

print(f"\t###INICIANDO PROGRAMA###")                                            #Muestra en pantalla un pequeño letrero.
numero=int(input("Ingresa un número: "))                                        #Solicitud y conversión de datos.
print(f"El número: {numero} esta entre 10 y 15? {numero>=10 and numero<=15}")   #Muestra el resultado si el numero esta en el rangp de 10-15.