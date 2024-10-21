"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          11 de octubre
Descripción:    Ejercicio de práctica, entrada, solicitud y conversiones
                de datos de un usuario.



a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

        Nombre (cadena).
        No. de cubículo (int).
        Horas de que imparte clase a la semana (float con 3 decimales).
        ¿Tiene más de 5 años en la UNSIJ? (booleano).

b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
"""

###SOLICITUD DE DATOS###
print("Cargando...")                                 #  Escribe un letrero.
print("Programa: Datos de profesores.")              #  Escribe un letrero.
nombre_de_profesor, numero_de_cubiculo = input("Profesor, ingrese su nombre: "), int(input("¿Cuál es el número de cubículo donde se le puede encontrar? "))         #   Solicitud y conversión de datos, guardados en variables diferentes.
print()                                                                                                                                                             #   Salto de línea.
cantidad_de_horas_clase, años_en_unsij = float(input("Introduzca la cantidad de horas que imparte clases a la semana: ")), input("¿Usted tiene más de 5 años en la UNSIJ? ")    #   Solicitud y conversión de datos, guardados en variables diferentes.
años_en_unsij = años_en_unsij.lower() == "si"       #   Conversión de la variable: años_en_unsij. A tipo booleano
print("Datos capturados...")                        #   Escritura a pantalla de un letrero.
print()                                             #   Salto de línea.

##ESCRITURA DE DATOS DEL USUARIO##
print(f"{nombre_de_profesor} es un/a profesor/a de la UNSIJ, su número de cubículo para buscarlo/a es: {numero_de_cubiculo}, trabaja dando clases una cantidad de {cantidad_de_horas_clase:.3f} horas a la semana.")     # Escribe en pantalla los datos del profesor.
print(f"¿Tiene más de 5 años en la UNSIJ? {años_en_unsij}")         #   Escribe en una respuesta booleana si el profesor tiene más de 5 años en la UNSIJ.
