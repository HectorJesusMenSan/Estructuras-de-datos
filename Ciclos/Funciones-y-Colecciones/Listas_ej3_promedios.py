"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          13 de noviembre de 2024.
Descripción:    Ejercicios de practica, listas.
                Promedios del parcial 1.
"""



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
    opcion_del_menu=int(input("ingresa una opción:      \n"))
    return opcion_del_menu


def Recepcion_de_calificaciones_por_materia(lista_de_materias, lista_de_calificaciones, lista_de_calificaciones_por_materia):
    print("\n_________________________________________________________________________")
    print(" S E C C I O N   D E  I N G R E S O  D E   C A L I F I C A C I O N E S:")
    for i in lista_de_materias:
        calificacion = int(input(f"\nCalificacion de la materia {i}: "))
        lista_de_calificaciones_por_materia.append(calificacion)
    print("..................................................................")
    lista_de_calificaciones.append(lista_de_calificaciones_por_materia)
    return lista_de_materias, lista_de_calificaciones, lista_de_calificaciones_por_materia


#Definicion de la funcion para añadir alumnos:
#Recibe la lista de alumnos y retorna la lista de alumnos actualizada
def Añadir_alumno (lista_de_alumnos, lista_de_materias, lista_de_calificaciones, lista_de_calificaciones_):
    nombre_de_alumno = input("\nIngresa el nombre del alumno:        ")
    lista_de_alumnos.append(nombre_de_alumno)
    Recepcion_de_calificaciones_por_materia(lista_de_materias, lista_de_calificaciones)
    return lista_de_alumnos, lista_de_materias, lista_de_calificaciones,

def Mostrar_datos (lista_de_alumnos, lista_de_materias, lista_de_calificaciones):
    contador_auxiliar = 0
    contador_de_alumnos = len(lista_de_alumnos)
    print("\n_________________________________________________________________________")
    print("\nS E C C I Ó N    D E    C A L I F I C A C I O N E S")
    for iterador in range (1, contador_de_alumnos+1):
        print("..................................................................")
        print(f"\tAlumno: {lista_de_alumnos[iterador-1]}  ")
        for materia in lista_de_materias:

            print(f" {materia}  :  {lista_de_calificaciones [contador_auxiliar]}")

            contador_auxiliar+=1
        print("..................................................................")
    return lista_de_alumnos, lista_de_materias, lista_de_calificaciones
#Funcion para mostrar calificaciones de un alumno escogido por el usuario:
def Mostrar_alumno (lista_de_alumnos, lista_de_materias, lista_de_calificaciones):
    print("De cual alumno deseas ver calificaciones:\n")
    contador=0

    #Imprime a los alumnos, dando al usuario la posibilidad de escoger una opcion:
    for alumno in lista_de_alumnos:
        print(f"{contador}) {alumno}")
        contador+=1
    opcion_para_mostrar_alumno = int(input("Ingresa una opcion:     "))
    #Imprime el nombre del alumno:
    print(f"Nombre de alumno: {lista_de_alumnos[opcion_para_mostrar_alumno]}")
    opcion_para_mostrar_alumno=opcion_para_mostrar_alumno*5
    for iterador in range(1, 6):
        print(f"Materia: {lista_de_materias[iterador-1]}        Cal:------{lista_de_calificaciones[opcion_para_mostrar_alumno]}")
        opcion_para_mostrar_alumno+=1
    return lista_de_alumnos, lista_de_materias, lista_de_calificaciones

#Funcion para eliminar:
def Eliminar(lista_de_alumnos, lista_de_materias, lista_de_calificaciones):
    contador=0
    for alumno in lista_de_alumnos:
        print(f"[{contador}] {alumno}\n")
    alumno_a_eliminar = int(input("Escoge el alumno que deseas eliminar: "))
    del lista_de_alumnos[alumno_a_eliminar]
    del  lista_de_calificaciones[alumno_a_eliminar]









#_____________________________________________________________________________________________________
opcion=None# Definicion de listas:
lista_de_calificaciones_por_materia = []
lista_de_alumnos = []
lista_de_calificaciones = []
lista_de_materias = ["Estructura de datos", "Derecho y legislación", "Contabilidad", "Electronica", "Algebra"]
while opcion != 0:
    opcion = Menu()
    if opcion==1:
        Mostrar_alumno(lista_de_alumnos, lista_de_materias, lista_de_calificaciones)

    elif opcion==3:
        Añadir_alumno(lista_de_alumnos, lista_de_materias, lista_de_calificaciones)
    elif opcion==4:
        Eliminar(lista_de_alumnos,lista_de_materias, lista_de_calificaciones)
        Mostrar_datos(lista_de_alumnos, lista_de_materias, lista_de_calificaciones)
