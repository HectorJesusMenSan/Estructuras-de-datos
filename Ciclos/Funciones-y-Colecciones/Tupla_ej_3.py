"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:   Ejercicios para practicar
               Con el tema de tuplas
               rol de juegos"""


def agregar_equipos(lista_de_equipos):

    print("DEBES INGRESAR UNA CANTIDAD PAR...")
    cantidad_de_equipos=int(input("Cuantos equipos se escribieron? "))
    for i in range(0, cantidad_de_equipos):
        lista_de_equipos.append(f"equipo{i+1}")

    return lista_de_equipos

def jornadas_para_juego (lista_de_equipos):
    contador_de_lista = len(lista_de_equipos)
    limite = contador_de_lista//2
    for i in range (0, limite):
        contador=contador_de_lista
        while contador>limite:
            print(f"{lista_de_equipos[i]} vs {lista_de_equipos[contador]}")
            contador-=1







#_________________________________________modulo___________________________________

print("Cargando programa: Rol de juegos")
lista_de_equipos=[]
Lista_de_equipos = agregar_equipos(lista_de_equipos)
jornadas_para_juego(lista_de_equipos)