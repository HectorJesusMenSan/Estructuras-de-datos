'''
Héctor Jesús Méndez Santiago
9 de octubre de 2024.
Descripción: En este programa estan los tipos de variables en python y su forma en las que se usan.
'''

# Notas:
"""
En Python, no es necesario declarar el tipo de dato al declarar una variable.
Los: valores son automáticos, sin la necesidad de declarar con los que se puede trabajar, en python son todos los siguientes:
Int: números enteros.
Float: números con punto decimal.
String: (str) (cadenas de texto automáticamente).
Boolean: True o False (con inicial mayúscula).
None: Tipo especial que representa una ausencia de valor.
"""

# Ejemplos de tipos de datos.

# Número entero:
mi_variable_entera = 100
print("Tipo de dato entero:",mi_variable_entera)

# Número decimal:
mi_variable_decimal = 12.12
print("Tipo de dato decimal:", mi_variable_decimal)

# Cadena de texto:
mi_variable_texto_nombre = 'Hector'   #Al usar las dos maneras de comillas no afecta en la escritura.
mi_variable_texto_apellido = "Mendez"
print("Cadena de texto:", mi_variable_texto_nombre, mi_variable_texto_apellido) #Automáticamente imprime los dos textos de manera separada.

# Booleno:
mi_variable_booleana = True # A fuérza se le tiene que poner una mayúscula al true sino lo detecta cómo cadena.
print('Tipo booleano:', mi_variable_booleana)

# None:
mi_variable_none = None
print("Tipo none:",mi_variable_none)

# Uso de constantes.
'''
En Python, a diferencia de otros lenguajes de programación, no existe un tipo específico para definir constantes.
Se utilíza una convención de colocar las variables en mayúsculas y no modificarlas.
'''
VARIABLE_CONSTANTE = 3.1416 #El nombre de una variable constante debe ser codificada con todas las letras mayúsculas.
print("Ejemplo de convención de una constante:", VARIABLE_CONSTANTE)

#Concluyendo: Los tipos de datos en phyton son similares a  los de c y c++, solo que aqui no hay necesidad de declararlas porque se hace automáticamente.