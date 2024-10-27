"""
Nombre: Héctor Jesús Méndez Santiago.
fecha:  16 de octubre de 2024.
Descripción: Primer ejercicio de practica en operadores
             lógicos y relacionales.
"""




#   Solicitar una cantidad de dinero
#   Preguntar si compra a meses sin intereses

""" Si la cantidad ingresada es mayor o igual a 5000, y la respuesta es si,
    se devolvera una respuesta en booleano si a el usuario se le aplicará una
    bonificación. """

#EJERCICIO
print("\t###C A R G A N D O  P R O G R A M A###")
print()
respuesta = float(input("Ingresa la cantidad de dinero que gastaste en tu compra: ")) # Solicitud y conversion de datos.

respuesta2 = input("¿Compras a meses en intereses?")                                  # Lectura de respuesta a pregunta.

print(f"Aplicaste a la bonificación? { respuesta>=5000 and respuesta2 == 'si' or respuesta2 == 'Si' or respuesta2== 'SI' }")         # Se le da a conocer el resultado de aplicación a bonificación en booleano al usuario.

"En la maquina de la universidad al usar la comparaión de cadena con "" si compila. En mi maquina funciona con ''."