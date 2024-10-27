'''
Nombre: Héctor Jesús Méndez Santiago
Fecha:  16 de octubre del 2024
Descripción:   Programa en el que se aborda el tema
               de cómo se asignan o aumentan valores
               a una variable, y simplificaciones de
               operaciones, para hacer más eficiente
               y/o más corto el código.
Operadores de asignación compuestos.
'''

numero1, numero2 = int(input("Ingresa número 1: ")), int(input("Ingresa número 2: "))   # Solicitar dos datos al usuario, convertidos a números enteros.
print(numero1, numero2)                                                                 # Escritura de los dos números

numero1 += 3            # Es como tener numero1 = numero1 + 3
print(numero1)

numero2 -= 5            # Simplificación de operación: numero2 = numero2 - 5
print(numero2)

numero1 *= 2            # Simplificación de operación: numero1 = numero1 * 2
print(numero1)

numero2 /= 4
print(numero2)

## Comienza segunda actividad ##
numero3, numero4 = int(input("Ingresa número: ")), int(input("Ingresa número: ")) # Solicitud y lectura de datos.
print(numero3, numero4)                                                             # Escritura de datos.

numero3 += numero4      # Al numero3 se le aumenta el valor del numero4.
print(numero3)          # Escritura de resultados.
numero3 *= numero3      # El valor del numero3 es multiplicado por sí mismo.
print(numero3)          # Escritura de los resultados.
numero3 -= numero4      # Al numero3 se le resta el valor del numero4.
print(numero3)          # Escritura de los resultados.
numero3 += 3            # Al valor del numero3 se le aumenta una cantidad de 3.
print(numero3)          # Escritura de resultados.
numero3 /= 2            # Al valor del numero3 se le divide entre 2.
print(numero3)          # Escritura del resultado de la operación.

"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.) 
con el operador de asignación (=).
"""