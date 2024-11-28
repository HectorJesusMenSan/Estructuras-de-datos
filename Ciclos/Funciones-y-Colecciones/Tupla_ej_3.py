"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:   Ejercicios para practicar
               Con el tema de tuplas
               rol de juegos"""
from Ciclos.Ciclo_while import contador


def agregaar_equipos(lista_de_equipos):
    print("DEBES INGRESAR UNA CANTIDAD PAR...")
    cantidad_de_equipos=int(input("Cuantos equipos se escribieron? "))
    for i in range(0, cantidad_de_equipos):
        lista_de_equipos.append(f"equipo{i+1}")
    return lista_de_equipos

def jornadas_para_juego (lista_de_equipos):
    lista_de_tuplas = []
    tupla_de_equipos = ()
    cantidad_de_jornadas = int(input("Cuantas jornadas de juego organizaras? "))
    contador_de_lista = len(lista_de_equipos)
    for iterador in range(1, contador_de_lista-1):
        auxiliar=lista_de_equipos[iterador]
        lista_de_equipos=[iterador+1]





print("Cargando programa: Rol de juegos")
