

"""
Nombre: Héctor Jesús Méndez Santiago
Fecha:  16 de octubre de 2024
Descripción:   En este programa se abordan los temas de operadores lógicos
               que se pueden usar en Python: and, or, not.
"""

# Pedir dos expresiones y que al insertar "sí" o "no" nos devuelva true o false.#

variable_logico = input("Ingresa sí o no: ")       # Solicitud y lectura de datos.
variable_logico = variable_logico.lower() == "si"  # Convertir el dato introducido en booleano, comparándolo con la palabra "sí".
print(variable_logico)                             # Escritura a pantalla de los resultados.

# Segunda solicitud de datos al usuario.#
variable_logico2 = input("Ingresa sí o no: ")             # Solicitud y lectura de datos.
variable_logico2 = variable_logico2.lower() == "si"       # Convertir el dato introducido en booleano, comparándolo con la palabra "sí".
print("La segunda respuesta es: ", variable_logico2)      # Escritura en pantalla del segundo resultado

## Comparaciones de los dos resultados obtenidos ##
"""
Basándonos en los resultados de arriba, ya están convertidos en booleano: 
si fueron "sí", el valor es true, y si no, el valor es false.

"""
print(f"¿Ambas respuestas fueron sí? {variable_logico and variable_logico2}")      # Devuelve un sí booleano, solo si ambos resultados son TRUE.
print(f"¿Una respuesta fue sí? {variable_logico or variable_logico2}")             # Devuelve un sí booleano, si alguno de los dos resultados es TRUE.
print(f"La negación de la primera respuesta es:  {not variable_logico}")           # Devuelve en valor booleano la negación del primer resultado.
print(f"La negación de la segunda respuesta es:  {not variable_logico2}")          # Devuelve en valor booleano la negación del segundo resultado.