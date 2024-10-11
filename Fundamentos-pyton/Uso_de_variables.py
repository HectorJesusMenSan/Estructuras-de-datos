# Héctor Jesús Méndez Santiago.
# 8 de octubre de 2024.
# En este archivo se ejemplifica el uso de variables en Python.

# Notas:
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal.

#En comparación con C en Phyton no es necesario poner librerias ni el main
#Tambien hay algunos cambios en el tema de cómo escribir, en el print no se usa la "f"
#No tenemos la necesidad de indicar que el programa termina o "return 0"

# A cualquier variable que declaremos se le necesita dar un valor inicial, si no, falla el programa.
semestre = 3        # variable con valor inicial de 3
print(semestre)     # imprime el valor de la variable
semestre = 4        # se actualiza el valor de la variable
print(semestre)     # se vuelve a imprimir

# Se crean varias variables para ejemplificar su uso
nombre = "Héctor"  # variable de tipo String
altura = 1.75       # variable de tipo Float
edad = 19           # variable de tipo Int

# Se imprimen las variables, añadiendo información adicional para comprender lo que se imprime
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.70
edad = 30
print()
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento
edad = "diecinueve"      # Edad antes tenía el valor de 19 (Int)
print()
print("Edad (con otro tipo de dato):", edad)


"""Las reglas fundamentales para el uso de variables en phyton son las siguientes:
1. Al declarar alguna variables siempre se deben utilizar unicamente mayúsculas
   o unicamente minúsculas, números y guion bajo.
2. Describir bien el nombre de las variables, para mayor entendimiento, sin usar    
   abreviaciones.
3. Ninguan variable se puede iniciar en números.
4. Para declarar variables no se puede usar las palabras reservadas, un ejemplo es,
   el if, el else, el True o el class, ya que al usarlos el prorama causará error.
5. Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.
"""


# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guion bajo
mi_variable=12#prueba de variable
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "19 de diciembre de 2005"
clase = "Estructuras de Datos"
horas_estudio = 8
nombre = "Hector"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "19 de diciembre del 2005"
fechanacimiento = "1 de enero del 2000"
# class = "Estructuras de Datos"
# 8horas_estudio = 8
Nombre = "H e c t o r"
NOMBRE = "HECTOR"

clas="s"
print("clase", clas)


# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)

#En esta lección aprendimos cómo usar phyton, las maneras correctas para declarar variables.
#Son importantes algunos puntos como la declaración de constantes, que todos son en mayúscula.