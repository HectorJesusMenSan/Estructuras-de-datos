'''
Nombre: Héctor Jesús Méndez Santiago
Fecha: Viernes 11 de octubre del 2020
Descripción: Este es un programa para conocer el funcionamiento de python, como
las formas en las que podemos cambiar los tipios de variables.
Conversión de tipos de datos (casting) en Python.
'''

# Notas
'''
La conversión de tipos de datos implica manipular datos que no están en el tipo de dato requerido. Ejemplos:
de cadena a entero, de cadena a número flotante, y viceversa.
'''

# *****   Conversión de cadena a entero     *****
var_cadena = "951"
var_int = int(var_cadena)                           #La manera de convertir, es darle un valor del tipo de datos que queremos convertir a nuestra variable inicial, introduciendo el nombre de la variable dentro de unos parentesis.

# Utiliza la letra "f" antes de las comillas para indicar que la cadena será formateada.
# Esto significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final.
print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena}.")          #Para poder escribir la variable convertida se debe usar las llaves
print(f"Número como int más uno: {var_int + 1}.")    #A la variable convertida se le sumó un uno entéro, que se muestra en pantalla.

# *****   Conversión de cadena a flotante     *****
var_cadena = "8.88"                                 #Se le da valor a la varible
var_float = float(var_cadena)                       #Convertimos la variable a cadena
print()                                             #Este print no escribe nada
print("Conversión de cadena a flotante.")
print(f"Número como cadena: {var_cadena}.")         #Imprime la variable tipo cadena
print(f"Número como float más cero punto uno: {var_float + 0.1}.") #Imprime la variable tipo flotante sumandole un 0.1


# *****   Conversión de número a cadena     *****
var_int = 123
var_float = 123.321
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} y {var_float} se convierten a cadena utilizando str(var_int): {str(var_cadena)}, y "
      f"str(var_float): {str(var_float)}.") #Aqui se convirtieron a cadena las variables: var_float y var_cadena. y se escriben
#Las transformaciónes a cadena se hacen utilizando el str().
