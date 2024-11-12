"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          12 de noviembre de 2024.
Descripción:    Ejercicios de practica, listas.
"""
from Ciclos.Ciclo_for import alumnos


# DEFINICION DE FUNCIONES:
    # Menu
def menu(opcion):
    print("1) Ver lista de videos por añadidas.")
    print("2) Ver lista de videps por orden A-Z.")
    print("3) Ver lista de videos por orden Z-A.")
    print("4) Añadir videos.")
    print("4) Añadir varios videos.")
    print("4) Eliminar videos.")
    print("0) Salir.")
    opcion = int(input("Ingresa una opcion: "))
    return opcion

    #Orden a-z
def orden_AZ(lista_de_videos):
    lista_de_videos.sort()
    return lista_de_videos

    #Orden z-a
def orden_ZA (lista_de_videos):
    lista_de_videos.sort(reverse=True)
    return lista_de_videos

    #Añadir videos
def añadir_videos (lista_de_videos):
    video_a_añadir = input("Ingresa el video que deseas añadir a la lista: ")
    lista_de_videos.append(video_a_añadir)
    return lista_de_videos

    #Añadir varios videos
def añadir_varios_videos (lista_de_videos):
    contador_de_videos=0
    for video in lista_de_videos:
        contador_de_videos+=1

    valor_de_videos_a_agregar = int(input("¿Cuantos videos deseas agragar? "))

    for iterador in range(valor_de_videos_a_agregar):
        video_a_agregar = input("Agrega el video: ")
        lista_de_videos.append(video_a_agregar)
    return lista_de_videos

    #Eliminar Video
def eliminar_video (lista_de_videos):
    video_a_eliminar= input("Ingresa el video que quieres eliminar: ")
    alumnos.remove(video_a_eliminar)




