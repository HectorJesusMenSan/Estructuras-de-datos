'''
Nombre: Héctor Jesús Méndez Santiago
Fecha: Viernes 11 de octubre del 2020
Descripción: Este es un ejercicio para practicar el cambio de tipo de variable
Conversión de tipos de datos (casting) en Python.



a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.

b) De los números anteriores, indica su valor booleano.

c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".

d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".

'''

###CODIGO PARA EL PRIMER INCISO###
print("\t***a)***")                                                              #Imprimo el inciso del trabajo.
variable_numero1 =  3.14159265                                                   #Se crea la variable y se le da un valor.
print(f"El primer número convertido a cadena es: {str(variable_numero1)} ")      #Imprime la variable convertida a cadena.

variable_numero2 =  12                                                           #Se crea variable.
print(f"El segundo número convertido a cadena es: {str(variable_numero2)} ")     #Imprime la variable convertida a cadena.

variable_numero3 =  0                                                            #Se crea variable.
print(f"El segundo número convertido a cadena es: {str(variable_numero3)} ")     #Imprime la variable convertida a cadena.

###CODIGO PARA EL SEGUNDO INCISO###
print("\n\t***b)***")                                                                                                #Imprimo el inciso del trabajo.

variable_verdadero = bool(variable_numero1)                                                                          #Se crea variable tipo bool.
print(f"¿Verdad que la variable: variable_numero1, contiene un valor diferente de cero? {variable_verdadero}")       #Se imprime el valor del tipo bool.

variable_verdadero = bool(variable_numero2)                                                                          #Modificamos el valor del bool.
print(f"¿Verdad que la variable: variable_numero2, contiene un valor diferente de cero? {variable_verdadero}")       #Se imprime el valor del tipo bool.

variable_verdadero = bool(variable_numero3)                                                                          #Modificamos el valor del bool.
print(f"¿Verdad que la variable: variable_numero2, contiene un valor diferente de cero? {variable_verdadero}")       #Se imprime el valor del tipo bool.

###CODIGO PARA EL SEGUNDO INCISO###

print("\n\t***c)***")                                                                                                #Imprimo el inciso del trabajo.

variable_cadena1 = "10002"                                                  #Creamos la variable de tipo cadena y le agregamos contenido.

variable_cadena2 = "100.02"                                                 #Creamos la variable de tipo cadena y le agregamos contenido.

variable_cadena3 = "0"                                                      #Creamos la variable de tipo cadena y le agregamos contenido.

variable_numero = int(variable_cadena1)                                                 #Creamos la variable de conversión.
print(f"La variable: variable_cadena1. se cambio a entero: {variable_numero}")          #Imprime la variable cambiada.

variable_numero = float(variable_cadena2)                                               #Creamos la variable de conversión.
print(f"La variable: variable_cadena2. se cambio a flotante: {variable_numero}")        #Imprime la variable cambiada.

variable_numero = int(variable_cadena3)                                                 #Creamos la variable de conversión.
print(f"La variable: variable_cadena3. se cambio a entero: {variable_numero}")          #Imprime la variable cambiada.

###CODIGO PARA EL TERCER INCISO###

print("\n\t***d)***")                                                                                                #Imprimo el inciso del trabajo.
variable_verdadero = bool(variable_cadena1)                                                                          #Conversión de dato.
print(f"La variable de la primera cadena es: {variable_verdadero}")                                                  #Escribimos los resultados de la conversión.

variable_verdadero = bool(variable_cadena2)                                                                          #Conversión de dato.
print(f"La variable de la segunda cadena es: {variable_verdadero}")                                                  #Escribimos los resultados de la conversión.

variable_verdadero = bool(variable_cadena3)                                                                          #Conversión de dato.
print(f"La variable de la tercera cadena es: {variable_verdadero}")                                                  #Escribimos los resultados de la conversión.

"""El resultado final del tercer caso es que efectivamente es verdadero
porque al ingresar un dato de tipo cadena el cero, se cuenta como cadena,
sería diferente si el tipo de dato fuera un entero, ahi si maracaría falso
porque es lo que indican las reglas"""
