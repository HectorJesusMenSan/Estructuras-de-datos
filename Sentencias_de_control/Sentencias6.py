"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Sexto programa para ejercitar la habilidad con las sentencias

Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas:

    Precio de un adulto: $ 200.00
    Precio de un niño: $ 100.00

Además, si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.

Para ello:

a) Solicite al usuario el nombre de la persona a cargo.

b) Defina con valores constantes el precio del boleto del adulto y del niño.

c) Solicite el número de adultos y de niños.

d) Pregunte el día de la semana.

e) Calcule el costo total.

f) Muestre los detalles del cliente y el día, así como el costo total.
"""
costo_niño=100.00
costo_adulto=200.00
total=0
nombre_de_usuario=input("Introdusca nombre del cliente: ")
numero_de_adultos=int(input("Ingrese la cantidad de adultos: "))
numero_de_niños=int(input("Ingrese la cantidad de niños: "))
dia_de_semana=input("Ingresa dia de la semana: ")
dia_de_semana=dia_de_semana.lower()

if dia_de_semana=="lunes" or dia_de_semana=="martes" or  dia_de_semana=="juevez":
    total=(numero_de_niños*costo_niño)+(numero_de_adultos*costo_adulto) - (((numero_de_adultos*costo_adulto)+(numero_de_niños*costo_niño))*10)/100
    print(f"Gracias por tu visita {nombre_de_usuario} este dia {dia_de_semana}, el costo total es de: {total}")
elif dia_de_semana=="miercoles" or dia_de_semana=="viernes":
    total=(numero_de_niños*costo_niño)+(numero_de_adultos*costo_adulto)
    print(f"Gracias por tu visita {nombre_de_usuario} este dia {dia_de_semana}, el costo total es de: {total}")
else:
    print("ERROR")