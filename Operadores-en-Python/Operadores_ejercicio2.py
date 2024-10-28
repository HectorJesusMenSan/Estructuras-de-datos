"""
Nombre: Héctor Jesús Méndez Santiago.
fecha:  16 de octubre de 2024.
Descripción: Segundo ejercicio de practica en operadores
             lógicos y relacionales.
"""

"""
Pregntar al usuario si es profesor.
Preguntar al usuario si es alumno.
Si solo una de las respuestas a las preguntas es si
devolver a booleano si pertenece o es miembro de la
comunidad universitaria.

"""

#   Solicitud de datos:
opcion2=input("¿Eres profesor? si/no : ")
opcion3=input("¿Eres alumno? si/no : ")

print(f"¿Tú eres miembro de la comunidad universitaria? {opcion2 == 'si' or opcion3== 'si' }") # Respuesta en booleano.

#   Se usó el operador lógico or, porque si solo una resouesta fuece si, quiere decir que es miembro de la comunidad.

"En la maquina de la universidad al usar la comparaión de cadena con "" si compila. En mi maquina funciona con ''."