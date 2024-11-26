"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          13 de noviembre de 2024.
Descripción:    Ejercicios de práctica, listas.
                Promedios del parcial 1.
"""

# Menú principal, pide una opción y la retorna
def Menu ():
    print("\n____________________________________________________________")
    print("|     1) Ver calificaciones de todos los alumnos.             |")
    print("|     2) Ver calificaciones detalladas de un alumno           |")
    print("|     3) Ver promedio del parcial de todos                    |")
    print("|     4) Ver promedio grupal                                  |")
    print("|     5) Agregar alumno y calificaciones                      |")
    print("|     6) Eliminar alumno y calificaciones                     |")
    print("|     0) Salir.                                               |")
    print("______________________________________________________________")
    opcion_del_menu = int(input("Ingresa una opción:      \n"))
    return opcion_del_menu

# Función para ver las calificaciones de un alumno
def ver_calificaciones_de_alumno(lista_de_alumnos, lista_de_calificaciones, lista_de_materias):
    contador_de_alumnos = len(lista_de_alumnos)  # Cuenta cuántos alumnos hay
    if contador_de_alumnos != 0:
        contador = 0
        for alumno in lista_de_alumnos:
            print(f"[{contador}]-  {alumno}")
            contador += 1
        alumno_a_ver = int(input("Escoge el alumno para ver sus calificaciones: "))
        print(f"\t{lista_de_alumnos[alumno_a_ver]}")

        contador2 = 0
        for calificacion in lista_de_calificaciones[alumno_a_ver]:
            print(lista_de_materias[contador2], end=": ")
            print(calificacion)
            contador2 += 1
    else:
        print("No hay alumnos por mostrar.")

# Función para mostrar calificaciones de todos los alumnos
def ver_calificaciones_de_todos(lista_de_alumnos, lista_de_calificaciones):
    contador_de_alumnos = len(lista_de_alumnos)  # Cuenta cuántos alumnos hay
    if contador_de_alumnos != 0:
        contador = 0
        for calificacion in lista_de_calificaciones:
            print(lista_de_alumnos[contador], end=": ")
            print(calificacion)
            contador += 1
    else:
        print("No hay alumnos por mostrar.")

# Agrega un alumno con sus calificaciones
def agregar_alumno_y_calificaciones(lista_de_alumnos, lista_de_calificaciones, lista_de_materias):
    lista_de_calificacion_por_materia = []  # Lista de calificaciones por materia
    nombre = input("-Ingresa el nombre del alumno: ")
    lista_de_alumnos.append(nombre)

    # Calificaciones para cada materia
    calificacion = float(input("Ingresa calificación de Estructura de datos: "))
    lista_de_calificacion_por_materia.append(calificacion)
    calificacion = float(input("Ingresa calificación de Derecho: "))
    lista_de_calificacion_por_materia.append(calificacion)
    calificacion = float(input("Ingresa calificación de Contabilidad: "))
    lista_de_calificacion_por_materia.append(calificacion)
    calificacion = float(input("Ingresa calificación de Álgebra: "))
    lista_de_calificacion_por_materia.append(calificacion)
    calificacion = float(input("Ingresa calificación de Electrónica: "))
    lista_de_calificacion_por_materia.append(calificacion)

    # Añade el nuevo alumno y sus calificaciones a las listas
    lista_de_calificaciones.append(lista_de_calificacion_por_materia)

    return lista_de_alumnos, lista_de_calificaciones, lista_de_calificacion_por_materia

# Elimina un alumno y sus calificaciones
def eliminar_alumno(lista_de_alumnos, lista_de_calificaciones):
    contador_de_alumnos = len(lista_de_alumnos)  # Cuenta cuántos alumnos hay
    if contador_de_alumnos != 0:
        contador = 0
        for alumno in lista_de_alumnos:
            print(f"[{contador}]-  {alumno}")
            contador += 1
        alumno_a_eliminar = int(input("Escoge el alumno para eliminar: "))
        print(f"\t{lista_de_alumnos[alumno_a_eliminar]}")

        # Elimina el alumno y sus calificaciones
        del lista_de_calificaciones[alumno_a_eliminar]
        del lista_de_alumnos[alumno_a_eliminar]

        # Muestra la lista actualizada de calificaciones
        contador = 0
        for calificacion in lista_de_calificaciones:
            print(lista_de_alumnos[contador], end=": ")
            print(calificacion)
            contador += 1
    else:
        print("No hay alumnos por eliminar.")

#________________________________________Módulo Principal_____________________________________________________________
opcion = None
# Definición de las listas
lista_de_alumnos = []
lista_de_calificaciones = []
lista_de_calificacion_por_materia = []
lista_de_materias = ["Estructura de datos", "Derecho", "Contabilidad", "Álgebra", "Electrónica"]

# Ciclo para menu de interacción
while opcion != 0:
    opcion = Menu()  # Muestra el menú
    if opcion == 1:
        ver_calificaciones_de_todos(lista_de_alumnos, lista_de_calificaciones)  # Muestra todas las calificaciones de todos
    elif opcion == 2:
        ver_calificaciones_de_alumno(lista_de_alumnos, lista_de_calificaciones, lista_de_materias)  # Ver un alumno
    elif opcion == 5:
        agregar_alumno_y_calificaciones(lista_de_alumnos, lista_de_calificaciones, lista_de_materias)  # Agregar alumno
    elif opcion == 6:
        eliminar_alumno(lista_de_alumnos, lista_de_calificaciones)  # Eliminar alumno
    else:
        print("Error")  # Opción inválida
"""
Este programa intenta manipular las listas con funciones.
El programa consiste en desplegar un menú donde el usuario interactúa para realizar diferentes acciones , 
como agregar alumnos, ver sus calificaciones, eliminar calificaciones, calcular el promedio de uno y de todos los alumnos.
Siendo sincero, estuve tratando de manipular las listas con las funciones como lo pidió, 
pero en la parte de los promedios no pude, perdí mucho tiempo, esfuerzo, sudor y lágrimas.
"""