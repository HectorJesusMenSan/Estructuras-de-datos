"""Nombre: Héctor Jesús Méndez Santiago
Fecha:  16 de Octubre del 2024
Descripcion: En este programa se realizan las diferentes formas de asignar valores a las variables
"asignacion multiple"
"""

variable1, variable2= 5, 10                                        #Formas de
valor3, valor4= 9.14, ("chuy")

print(variable1, variable2, valor3, valor4)

variable5, variable6= variable1+variable2, variable1-variable2
print(variable5, variable6)

#asignacion encadenada
variable7=variable8=variable9=10
print(variable7,variable8,variable9)

#intercambio de variables
variable10, variable11="alberto", "geto"
print(variable10,variable11)
variable11,variable10="geto", "alberto"
print(variable11,variable10)

nombre, apellido= input("ingresa nombre: "), input("ingresa apellido: ")
print(nombre, apellido)