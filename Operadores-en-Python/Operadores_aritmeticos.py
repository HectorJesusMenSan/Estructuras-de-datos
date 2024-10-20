
"""
Nombre: Héctor Jesús Méndez Santiago.
Fecha:  15 de Octubre del 2024.
Descripción: En este programa aprendemos cómo utilizar todos los
operadores aritméticos que podemos usar en Python.

operadores aritméticos.
"""

print("##INTRODUCIR DOS NÚMEROS##")             # Imprimir un comentario al usuario.
primer_numero = int(input("Ingresa número: "))  # Utilizamos comandos para leer datos y convertirlos a un tipo de dato.
segundo_numero = int(input("Ingresa número: ")) # Leer segundo dato, mostrando un letrero a la vez.

print(f"Resultado de la suma entre los dos números es: {primer_numero + segundo_numero}")            # Imprimimos directamente la suma de los números solicitados con el operador +
print(f"Resultado de la resta entre los dos números es: {primer_numero - segundo_numero}")           # Imprimimos directamente la resta de los números solicitados con el operador -
print(f"Resultado de la multiplicación entre los dos números es: {primer_numero * segundo_numero}")  # Imprimimos directamente la multiplicación de los números solicitados con el operador *
print(f"Resultado de la división entre los dos números es: {(primer_numero / segundo_numero):.2f}")  # Imprimimos los resultados de dividir los dos números con el operador /
# 2f para solo mostrar dos decimales en pantalla

print(f"Resultado es: {primer_numero // segundo_numero}") # // divide los dos números pero sin mostrar datos en decimales.
print(f"Resultado es: {primer_numero ** segundo_numero}") # eleva el primer número a la potencia del segundo número.