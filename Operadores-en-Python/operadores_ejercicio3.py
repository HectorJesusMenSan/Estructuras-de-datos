"""
Nombre: Héctor Jesús Méndez Santiago.
fecha:  16 de octubre de 2024.
Descripción: Tercer ejercicio de practica en operadores
             lógicos y relacionales.
"""
###EJERCICIO EN CLASE###
"""
#Solicitar un número.
#Devolver un TRUE si este número ingresado
se encuentra en un rango de: 10-15.

"""

print(f"\t###INICIANDO PROGRAMA###")                                            #Muestra en pantalla un pequeño letrero.
numero=int(input("Ingresa un número: "))                                        #Solicitud y conversión de datos.
print(f"El número: {numero} esta entre 10 y 15? {numero>=10 and numero<=15}")   #Muestra el resultado si el numero esta en el rango de 10-15.


###EJERCICIO 3###
"""
Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña. Para ello:

a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.

b) Pida al usuario una cadena con el usuario.

c) Pida al usuario una cadena con la contraseña.

d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usario se autenticó correctamente.

e) Muestre el resultado en consola como valor booleano (True/False).

Nota: Las cadenas no tiene que ser convertidas a minúsculas.

"""
# Declaración de variables
variable_usuario = "Hector"         # Iniciar variable con valor interno.
variable_contraseña = "longaniza"   # Iniciar variable con valor interno.

print("#EJERCICIO 3#")              # Imprime el ejercicio a realizar.
print()                             # Imprime salto de línea.

print("\tControl de acceso: ")      # Imprime un letrero de información.
variable_usuario_introducido, variable_contraseña_introducido= input("Ingrese usuario: "), input("Ingrese contraseña: ")  # Solicita datos al usuario y guarda en variables distintas.

print(f"Tu contraseña y usuario son: {variable_usuario == variable_usuario_introducido and variable_contraseña == variable_contraseña_introducido}") # Imprime si la comparación de datos es correcta o no.