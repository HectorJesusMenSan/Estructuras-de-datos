"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          13 de noviembre de 2024.
Descripción:    Ejercicios de practica, listas.
                Promedios del parcial 1.
"""


# Definicion de listas:
lista_de_alumnos = []
lista_de_calificaciones = []
lista_de_materias = ["Estructura de datos", "Derecho y ledislación", "Contabilidad", "Electronica", "Algebra"]

# Definición de menu:
# No recibe ningun dato, y retorna la opcion del menu escogido por el usuario.
def Menu ():
    print("\n______________________________________________")
    print("|     1) Ver calificaciones de alumno.       |")
    print("|     2) Ver promedios de alumnos.           |")
    print("|     3) Añadir alumno.                      |")
    print("|     4) Eliminar alumno.                    |")
    print("|     5) Ver promedio grupal.                |")
    print("|     0) Salir.                              |")
    print("______________________________________________")
    opcion_del_menu=int(input("ingresa una opción:      "))
    return opcion_del_menu


def Recepcion_de_calificaciones_por_materia(lista_de_materias, lista_de_calificaciones):
    print("Ingresa las calificaciones de cada materia:")
    for i in lista_de_materias:
        calificacion=int(input(f"\nCalificacion de {i}: "))
        lista_de_calificaciones.append(calificacion)
    return lista_de_materias, lista_de_calificaciones


#Definicion de la funcion para añadir alumnos:
#Recibe la lista de alumnos y retorna la lista de alumnos actualizada
def Añadir_alumno (lista_de_alumnos, lista_de_materias, lista_de_calificaciones):
    nombre_de_alumno = input("Ingresa el nombre del alumno:        ")
    lista_de_alumnos.append(nombre_de_alumno)
    Recepcion_de_calificaciones_por_materia(lista_de_materias, lista_de_calificaciones)
    return lista_de_alumnos, lista_de_materias, lista_de_calificaciones

def Mostrar_datos (lista_de_alumnos, lista_de_materias, lista_de_calificaciones):
    contador_de_alumnos=0
    contador_auxiliar = 0
    for datos in lista_de_alumnos:
        contador_de_alumnos+=1
    print("_________________________________________________________________________")
    print("\nS E C C I Ó N    D E    C A L I F I C A C I O N E S")
    for datos in range (0, contador_de_alumnos):
        print("..................................................................")
        print(f"\tAlumno: {lista_de_alumnos[datos]}  ")
        for i in lista_de_materias:

            print(f" {i}  :  {lista_de_calificaciones [contador_auxiliar]}")

            contador_auxiliar+=1
        print("..................................................................")


#_____________________________________________________________________________________________________
opcion=None
while opcion != 0:
    opcion = Menu()
    if opcion==3:
        Añadir_alumno(lista_de_alumnos, lista_de_materias, lista_de_calificaciones)
        Mostrar_datos(lista_de_alumnos, lista_de_materias, lista_de_calificaciones)
