"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:   Ejercicios para practicar
               Con el tema de tuplas
               rol de juegos"""


def agregaar_equipos(lista_de_equipos):
    print("DEBES INGRESAR UNA CANTIDAD PAR...")
    cantidad_de_equipos=int(input("Cuantos equipos se escribieron? "))
    for i in range(0, cantidad_de_equipos):
        lista_de_equipos.append(f"equipo{i}")
    return lista_de_equipos

def jornadas_para_juego (lista_de_equipos):
    lista_de_tuplas = []
    tupla_de_equipos = ()
    cantidad_de_jornadas = int(input("Cuantas jornadas de juego organizaras? "))
    contador_de_lista = len(lista_de_equipos)
    contador_de_lista2 = contador_de_lista/2
    for iterador in range(1, contador_de_lista):
        auxiliar = lista_de_equipos[iterador]
        lista_de_equipos[iterador]=lista_de_equipos[iterador+1]
        lista_de_equipos[iterador+1]= auxiliar
        iterador2=0
        while iterador2 <= contador_de_lista2:
            tupla_de_equipos= (lista_de_equipos[iterador2], lista_de_equipos[iterador2+1])
            lista_de_tuplas.append(tupla_de_equipos)
            iterador2+=2
            contador_de_lista_de_tuplas = len(lista_de_tuplas)
        for enfrentamientos in range(0, contador_de_lista_de_tuplas):
            tupla_de_equipos = lista_de_tuplas[enfrentamientos]
            print(f"{tupla_de_equipos[0]} vs {tupla_de_equipos[1]}")





#_________________________________________modulo___________________________________

print("Cargando programa: Rol de juegos")
lista_de_equipos=[]
agregaar_equipos(lista_de_equipos)
jornadas_para_juego(lista_de_equipos)