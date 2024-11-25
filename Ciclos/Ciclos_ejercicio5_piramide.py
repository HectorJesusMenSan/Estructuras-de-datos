"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          7 de noviembre de 2024.
Descripción:    Ejercicio 5, Pirámide:
                Pedir a usuario un dato que demarque
                la cantidad de filas de la pirámide.

                Programa para practicar la utilización
                de ciclos, en este caso el for.
"""

# Inicialización de variables:
contador = 0
valor_de_filas = int(input("Introduce el número de filas que tenga tu pirámide: "))  # Lee y guarda datos otorgados por el usuario


# a)
for i in range(1, valor_de_filas + 1):  # Itera desde 1 hasta el valor de las filas que dio el usuario.
    contador += 1                       # Aumenta el contador en uno.
    for i in range(1, contador + 1):    # Itera en un rango de 1 hasta el valor del contador.
        print("*", end=" ")             # Imprime el asterisco, junto a un espacio.
    print("\n")                         # Fuera del for más interno, imprime salto de línea para el siguiente renglón.

# Indica que la primera pirámide se ha escrito en pantalla y delimita con la siguiente.
print("______________________________________________________________________")



# b)
contador = valor_de_filas                # Se iguala el contador con el valor de las filas
for i in range(1, valor_de_filas + 1):   # Itera de 1 hasta el valor de las filas que quiere el usuario.

    for i in range(1, contador + 1):     # Itera en un rango de 1 hasta el valor del contador.
        print("*", end=" ")              # Imprime el asterisco, junto a un espacio.
    print("\n")                          # Imprime salto de línea.
    contador -= 1                        # Se resta el contador
# Indica que la segunda pirámide se ha escrito en pantalla y delimita con la siguiente.
print("______________________________________________________________________")



# c)
# Inicialización y declaración de variables:
contador = valor_de_filas
escrituras = 0
espacios = 0
for i in range(1, valor_de_filas + 1):      # Itera en un rango de 1 hasta el valor de filas.
    escrituras = "*" * contador             # Se multiplica el asterisco por las veces que queramos, en este caso igual al contador
    espacios = " " * i                      # Se multiplican espacios por el valor del iterador
    print(f"{espacios}{escrituras}")        # Imprime espacios con los asteriscos
    contador -= 1                           # Se resta uno al contador
# Indica que la tercera pirámide se ha escrito en pantalla y delimita con la siguiente.
print("______________________________________________________________________")


# d)
# Inicialización de variables:
contador = 0

for i in range(1, valor_de_filas + 1):      # Itera en un rango de 1 hasta el valor de filas.
    escrituras = "*" * (contador + 1)       # Se multiplican los asteriscos por el contador más uno.
    espacios = " " * (valor_de_filas - i)   # Se multiplican espacios por el valor de filas menos uno.
    contador += 2                           # Se aumenta el contador pero en 2
    print(f" {espacios}{escrituras}")       # Imprime asteriscos y espacios
