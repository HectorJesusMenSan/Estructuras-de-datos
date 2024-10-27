"""
Nombre: Héctor Jesús Méndez Santiago.
fecha:  27 de octubre de 2024.
Descripción: Cuarto ejercicio de practica en operadores
             lógicos y relacionales.
"""


"""
Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4). Para ello:

a) Pida al usuario cuatro valores booleanos (V/F).

b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.

c) Muestre el resultado en consola como valor booleano (True/False).
"""
print("\t###C A R G A N D O  P R O G R A M A###")                               # Esto imprime un letrero.
print()                                                                         # Salto de línea.
respuesta1, respuesta2, respuesta3, respuesta4 = input("Para tu primer dato, ingresa V/F: "), input("Para tu segundo dato, ingresa V/F: "), input("Para tu tercer dato, ingresa V/F: "), input("Para tu cuarto dato, ingresa V/F: ")  # Solicitud y almacenamiento de datos a variables

#Conversión de variables a booleano:
respuesta1 = respuesta1.lower() == "v" # Esto convierte los datos a minúscula y lo coompara para guardarlo como  valor booleano
respuesta2 = respuesta2.lower() == "v"
respuesta3 = respuesta3.lower() == "v"
respuesta4 = respuesta4.lower() == "v"

print(f"El resultado de la expresión booleana es: {(respuesta1 or respuesta2) and (respuesta3 or respuesta4)}")  #Escribe el resultado de las coomparaciones que pide el ejercicio.