"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          12 de noviembre de 2024.
Descripción:    Ejercicios de practica, listas.
                Listas de Youtube.
"""

# DEFINICIÓN DE FUNCIONES:
# Menú principal
def menu():
    print("\n1) Ver lista de videos por añadidas.")
    print("2) Ver lista de videos por orden A-Z.")
    print("3) Ver lista de videos por orden Z-A.")
    print("4) Añadir video.")
    print("5) Añadir varios videos.")
    print("6) Eliminar video.")
    print("0) Salir.")
    opcion = int(input("Ingresa una opción: "))
    return opcion

# Ordenar de A-Z
def orden_AZ(lista_de_videos):                  # Recibe una lista
    lista_de_videos.sort()
    return lista_de_videos                      # Retorna la lista

# Ordenar de Z-A
def orden_ZA(lista_de_videos):                  # Recibe una lista
    lista_de_videos.sort(reverse=True)
    return lista_de_videos                      # Retorna la lista

# Añadir un video
def añadir_videos(lista_de_videos):             # Recibe una lista
    video_a_añadir = input("Ingresa el video que deseas añadir a la lista: ")
    lista_de_videos.append(video_a_añadir)
    return lista_de_videos                      # Retorna la lista

# Añadir varios videos
def añadir_varios_videos(lista_de_videos):      # Recibe una lista
    valor_de_videos_a_agregar = int(input("¿Cuántos videos deseas agregar? "))

    for iterador in range(valor_de_videos_a_agregar):
        video_a_agregar = input("Agrega el video: ")
        lista_de_videos.append(video_a_agregar)
    return lista_de_videos                      # Retorna la lista

# Eliminar un video
# Eliminar un video
def eliminar_video(lista_de_videos):            # Recibe una lista
    video_a_eliminar = input("Ingresa el video que quieres eliminar: ")
    lista_de_videos.remove(video_a_eliminar)  # Elimina el video
    return lista_de_videos                      # Retorna la lista

#______________________________MODULO PRINCIPAL______________________________________________________________________________________

lista_de_videos = []
opcion = True

while opcion:
    opcion = menu()  # Llamada al menú

    if opcion >= 1 and opcion <= 6:
        if opcion == 1:
            # Ver lista de videos
            print("Lista de videos añadidos:", lista_de_videos)

        elif opcion == 2:
            # Ver lista de videos ordenados de A-Z
            orden_AZ(lista_de_videos)
            print(lista_de_videos)

        elif opcion == 3:
            # Ver lista de videos ordenados de Z-A
            orden_ZA(lista_de_videos)
            print(lista_de_videos)

        elif opcion == 4:
            # Añadir un video
            añadir_videos(lista_de_videos)
            print( lista_de_videos)

        elif opcion == 5:
            # Añadir varios videos
            añadir_varios_videos(lista_de_videos)
            print(lista_de_videos)

        elif opcion == 6:
            # Eliminar video
            eliminar_video(lista_de_videos)
            print(lista_de_videos)

    elif opcion == 0:
        print("Proceso terminado")
        break

    else:
        print("Error: opción no válida. Intenta de nuevo.")
