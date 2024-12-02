"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          2 de diciembre de 2024.
Descripción:   Un diccionario tambien es ordenado,
               asi como lo ingresamos asi tambien lo
               podemos ver, no ocupa indices, solo
               claves o valores declaradas por
               nosotros."""


print("*Ejemplos de uso, diccionario*")

#Crear diccionarios:
diccionario_profesor = {'nombre': "Hector",
                        'Primer_apellido':"Mendez",
                        'edad':18}
#Comillas órque es una cadena
#: para asignar valor
#"" para cadenas


diccionario_Hector = {}
#Se añaden elementos:
diccionario_Hector ['nombre'] = "Hector"
diccionario_Hector ['apellido'] = "Mendez"
diccionario_Hector ['grupo'] = "303"
print(diccionario_profesor)
print(diccionario_Hector)
#Acceder elementos
nombre_alumno = diccionario_Hector.get('nombre')
print(f"Nombre accedido 1: {nombre_alumno}")
apellido_alumno = diccionario_Hector['apellido']
print(f"Nombre accedido 1: {apellido_alumno}")
#Modificar elementos: llave no, elementos si
diccionario_Hector['nombre'] = "Gotus"
diccionario_Hector['grupo']  = "403"
print(diccionario_Hector)

diccionario_Hector ['segudo_apellido'] = "Santiago"
diccionario_Hector ['materia_favorita'] = "Estructuras de datos"
print(diccionario_Hector)

#Eliminar par clave_valor
del diccionario_Hector['segudo_apellido']
diccionario_Hector.pop('grupo')
print(diccionario_Hector)

#Acceder al par clave-valor
for clave, valor in diccionario_Hector.items():
    print(f"Clave: {clave} y  valor: {valor}")
#Acceder al par valor
for valor in diccionario_Hector.values():
    print(f"  valor: {valor}")
#Acceder al par clave
for llave in diccionario_Hector.keys():
    print(f"  clave: {llave}")

#CONBINACION CON TUPLAS
diccionario_egresados = {'nombre':"Eliezer",
                         ('primer_apellido', 'segundo_apellido'):"locoooo",
                         'edad':23}
print(diccionario_egresados)
#Acceder al par clave-valor
for clave, valor in diccionario_egresados.items():
    print(f"Clave: {clave} y  valor: {valor}")
#Acceder al par valor
for valor in diccionario_egresados.values():
    print(f"  valor: {valor}")
#Acceder al par clave
for llave in diccionario_egresados.keys():
    print(f"  clave: {llave}")

#DIccionario dentro de diccionarios
diccionario_informatica = {'grupo303':{'numero_de_alumnos': 12,
                                       'numero_de_materias': 5,
                                       'promedio_grupal': 7.9},
                           'grupo503':{'numero_de_alumnos': 7,
                                       'numero_de_materias': 5,
                                       'promedio_grupal': 7.5},
                           'grupo703':{'numero_de_alumnos': 12,
                                       'numero_de_materias': 5,
                                       'promedio_grupal': 7.5},
                           'grupo903':{'numero_de_alumnos': 12,
                                       'numero_de_materias': 5,
                                       'promedio_grupal': 3.5},
                           }
print(diccionario_informatica)

for grupo in enumerate(diccionario_informatica):
    print(f"grupos : {grupo}")

promedio_de303 = diccionario_informatica['grupo303']['promedio_grupal']
print(promedio_de303)



