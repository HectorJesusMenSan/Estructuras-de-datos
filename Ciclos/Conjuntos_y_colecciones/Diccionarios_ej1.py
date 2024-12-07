"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          2 de diciembre de 2024.
Descripción:   Ejercicio para practicar y mejorar las
               habilidades en el tema de diccionarios."""
from secrets import choice




#-------------------------------F-U-N-C-I-O-N-E-S------------------------------------------------------
# Definicion de funcion: Menú.
def menu ():
    print("-----------------------------------------------------")
    print("Bienvenido/a, al juego :)\n")
    print("[1]. Piedra")
    print("[2]. Papel")
    print("[3]. Tijeras")
    print("[0]. Salir")
    print("-----------------------------------------------------")

    #Lectura y solicitud de datos.
    opcion = int(input("Presiona la tecla para escoger una opción: \n"))

    # Retorna la opcion escogida por el usuario
    return opcion

# Definicion de funcion: Escoger ganador:
def ganador (Diccionario_de_elecciones, opcion, usuario, cpu, empate):
    # Crea listas con tuplas de posibilidades de perder o ganar
    lista_de_opciones_a_ganar = [("piedra", "tijeras"), ("papel", "piedra"), ("tijeras", "papel")]
    lista_de_opciones_a_perder = [("tijeras", "piedra"), ("piedra", "papel"), ("papel", "tijeras")]
    lista_de_opciones_a_empate = [("tijeras", "tijeras"), ("piedra", "piedra"), ("papel", "papel")]

    # Se igualan los contadores
    empate = empate
    usuario_gana = usuario
    cpu_gana = cpu

    # Elecciones de usuario y cpu, dependiendo a los diccionarios
    elecccion_de_usuario = Diccionario_de_elecciones['usuario'][opcion-1]
    elecccion_de_cpu = choice(Diccionario_de_elecciones['cpu'])             # Random

    #Escritura de las elecciones
    print(f"La seleccion del usuario: {elecccion_de_usuario}")
    print(f"La seleccion del cpu: {elecccion_de_cpu}\n")

    #Crea una tupla
    tupla_de_elecciones = (elecccion_de_usuario, elecccion_de_cpu)

    # Itera sobre las listas comparando el parecido con las tuplas.
    for opcion in lista_de_opciones_a_ganar:
        if tupla_de_elecciones == opcion:
            usuario_gana +=1

    for opcion in lista_de_opciones_a_perder:
        if tupla_de_elecciones == opcion:
            cpu_gana +=1

    for opcion in lista_de_opciones_a_empate:
        if tupla_de_elecciones == opcion:
            empate+=1

    return usuario_gana, cpu_gana, empate           #Retorna los contadores










#______________________________M O D U L O_________________________________________________________________________
# Declaración de variables:
Diccionario_de_elecciones = {'cpu':["piedra", "papel", "tijeras"],
                             'usuario':["piedra", "papel", "tijeras"]}

opcion = None
usuario, cpu, empate= 0, 0, 0


# Ciclo: Repite el menú hasta que la opcion sea 0.
while opcion != 0:
    opcion = menu()                 #LLamada de la funcion.

    # Rango de elecciones
    if opcion>0 and opcion<=3:
        #LLamada de funcion
        usuario, cpu, empate = ganador(Diccionario_de_elecciones, opcion, usuario, cpu, empate)
        #Imprime los contadores
        print(f"\nUsuario:{usuario}  Cpu:{cpu}  Empate:{empate}\n")
    # Cuando el usuario presione 0:
    elif opcion ==0:
        print("\nSalida del programa con exito.")
    # Cuando ingrese una opcion invalida.
    else:
        print("\nCometiste un error el escoger una opcion... :(")
        print("Vuelve a intentarlo.")

