"""Nombre: Héctor Jesús Méndez Santiago
Fecha:  15 de Octubre del 2024
Descripción: En este programa se realizan las diferentes formas de asignar valores a las variables

"""
# Asignación múltiple
nombre, apellido = input("Ingresa nombre: "), input("Ingresa apellido: ")    # Se puede solicitar seguidamente una lectura en una línea de código.
print(nombre, apellido)

variable1, variable2 = 5, 10                                        # Formas de asignar valores a las variables
valor3, valor4 = 9.14, ("chuy")                                     # Se puede asignar variables de diferentes tipos en una sola línea de código

print(variable1, variable2, valor3, valor4)                         # Imprime las variables

variable5, variable6 = variable1 + variable2, variable1 - variable2 # Suma y resta de las primeras variables, guardándolas en otras variables
print(variable5, variable6)                                         # Imprimir valores

# Asignación encadenada
variable7 = variable8 = variable9 = 10                              # Este tipo de asignación da el mismo valor a todas las variables
print(variable7, variable8, variable9)

# Intercambio de variables
variable10, variable11 = "alberto", "geto"
print(variable10, variable11)
variable11, variable10 = "geto", "alberto"
print(variable11, variable10)

# En esta parte intercambiamos el valor de las dos variables: lo que contenía uno se le pasó al otro



"""Al asignar un valor a las variables, ya sea entero, flotante, de tipo cadena, bool, etc., se debe seguir el orden
de los datos a las variables que queremos asignar."""
