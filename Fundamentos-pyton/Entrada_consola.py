'''
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          10 de octubre de 2024.
Descripción:    Estes es un programa para entender comop el usuario
                interactuará con un orograma.
Entrada de datos por consola para interacturar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.
numero1_cadena = input("Introduce un número decimal: ")     #   Solicitud de datos, guarda datos en una variable.
numero2_cadena = input("Introduce otro número decimal: ")   #   Ambas variables esta en tipo cadena.
resultado_cadena = numero1_cadena + numero2_cadena          #   Concatena las variables de tipo cadena,
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")        #   Muestra la concatenación

# Comentar por qué se realiza el casting de variables.
numero1_float = float(numero1_cadena)           #   Guarda en una variable el valor de dato ingresado en tipo flotante.
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float #   Aqui ya hace una operación aritmetica.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")   #   Muestra los resultados.

"""
#Se realiza el casting de variables para poder hacer las operaciónes
aritméticas correspondientes a menos que lo que queramos hacer sea
concatenar cadenas.

"""




#segunda forma de estilo de programacion: funciones anidadas
nose_float=float(input("ingresa numero para funcion anidada"))  #   Solicita datos y lo convierte a tipo flotante a la misma véz.
print(nose_float)

nose=input("ingresa cadena si o no:")
nose=nose.lower()=="si" #   Para cambiarlo a bool y coompararlo con algo que queramos.
print(nose)
#   Si la lectura de datos es un si, nso devolverá un TRUE.