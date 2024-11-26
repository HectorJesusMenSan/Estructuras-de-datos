"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          19 de noviembre de 2024.
Descripción:   Ejercicios para practicar
               Con el tema de tuplas"""
def menu():
    print("\n1) Ver coordenadas almacenadas.")
    print("2) Agregar coordenada (x,y).")
    print("3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas.")
    print("4) Eliminar coordenada (x,y).")
    print("0) Salir.")
    opcion = int(input("Escoege opcion: "))
    return opcion

# Funcion para ver coordenadas
def ver_coordenadas_guardadas (lista_de_tuplas ):
    contador = len(lista_de_tuplas)
    contador2 = 0
    if contador != 0:
        for coordenada in lista_de_tuplas:
            print(f"{contador2}- {coordenada}")
    else:
        print("No hay coordenadas guardadas.")

def agregar_coordenadas(lista_de_tuplas) :
    lista_de_numeros=[]
    numero1 = int(input("Agrega tu punto x"))
    numero2 = int(input("Agrega tu punto y"))
    lista_de_numeros.append(numero1)
    lista_de_numeros.append(numero2)

    tupla_de_coordenada = (numero1, numero2)
    lista_de_tuplas.append(tupla_de_coordenada)
    return lista_de_tupplas

def eliminar_coordenada(lista_de_tuplas):
    contador=0
    for tuplas in lista_de_tuplas :
        print(f"{contador}) {tuplas}")
    opcion_eliminar=int(input("Elige opcion: "))
    del lista_de_tuplas[opcion_eliminar]

def calcular_pendiente ( lista_de_tuplas):
    ver_coordenadas_guardadas(lista_de_tuplas)
    print("Para encontrar pendiente: ")
    punto1 = int(input("ingresa x1")), int(input("ingresa y1"))
    punto2 = int(input("ingresa x2")), int(input("ingresa y2"))
    print(f"Coordenadas en tuplas: {punto1} {punto2}")
    # Desempaquetado de duplas:
    x1, y1 = punto1
    x2, y2 = punto2
    # Expresion de la recta Y=mx+b
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    print(m)
    print(f"y={m}x + {b}")
#_________________modulo_______________________________________________________________________
opcion = None
lista_de_tuplas = []
# Despliegue de menú hasta que el usuario presione 0
while opcion != 0:

    opcion = menu()
    # ver lista
    if opcion == 1:
        ver_coordenadas_guardadas (lista_de_tuplas )         # Llamada de función
    elif opcion == 2:
        agregar_coordenadas(lista_de_tuplas)   # Llamada de función
    elif opcion == 3:
        calcular_pendiente ( lista_de_tuplas)
    elif opcion==4:
        eliminar_coordenada(lista_de_tuplas)
    else:
        print("Error")

