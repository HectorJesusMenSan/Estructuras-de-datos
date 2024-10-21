'''
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          11 de octubre
Descripción:    Conversión de cadenas a int, float y boolean mediante la interacción con consola.
                Programa que muestra cómo convertir cadenas a otros tipos de datos
                con la interacción de un usuario y la consola.
'''

# Comentar sobre las funciones anidadas.
##SOLICITUD DE DATOS:##
print("****   Datos de los alumnos    *****")               # Escritura de un letrero.
nombre = input("Ingresa el nombre: ")                       # Guarda en una variable el nombre del usuario.
semestre = int(input("Ingresa el no. de semestre: "))       # Convierte y guarda un dato de tipo entero.
promedio = float(input("Ingresa el promedio: "))            # Solicita un dato, lo convierte y lo guarda como tipo flotante.
es_mujer = input("¿Es mujer (Sí/No)?: ")                     # Solicita que escriba sí o no.

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a minúsculas y lo comparamos con la cadena "sí".
es_mujer = es_mujer.lower() == "sí"                         # Comando reservado, sirve para hacer comparaciones y devolver un valor booleano.

# Se imprimen los datos del alumno.
# Comentar qué es lo que realiza {promedio:.2f} probando con números diferentes.
##ESCRITURA DE DATOS:##
print()                                                     # Escribe un salto de línea.
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")  # El comando :.2f devuelve un valor flotante con una cantidad de dos decimales (dos cifras después del punto).
