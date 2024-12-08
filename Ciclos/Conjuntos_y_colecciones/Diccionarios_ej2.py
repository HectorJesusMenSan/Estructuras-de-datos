"""Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          2 de diciembre de 2024.
Descripción:   Ejercicio para practicar y mejorar las
               habilidades en el tema de diccionarios."""
from secrets import choice




# Definición de función: Menú
def menu():
    print("-----------------------------------------------------")
    print("Bienvenido/a al juego :)\n")
    print("[1]. Piedra")
    print("[2]. Papel")
    print("[3]. Tijeras")
    print("[4]. Lagarto")
    print("[5]. Spock")
    print("[6]. Ver reglas")
    print("[0]. Salir")
    print("-----------------------------------------------------")

    # Lectura y solicitud de datos.
    opcion = int(input("Presiona la tecla para escoger una opción: \n"))

    # Retorna la opción escogida por el usuario
    return opcion

# Definición de función: Reglas
def reglamento ():
    print("===============================================")
    print("\n->Esta es la sección del reglamento: \n")
    print("-Tijeras corta papel.")
    print("-Papel cubre piedra.")
    print("-Piedra aplasta lagarto.")
    print("-Lagarto envenena Spock.")
    print("-Spock destruye tijeras.")
    print("-Tijeras decapitan lagarto.")
    print("-Lagarto come papel.")
    print("-Papel desaprueba Spock.")
    print("-Spock vaporiza piedra.")
    print("-Piedra aplasta tijeras.")
    print("===============================================")

# Definición de función: Definir ganador
def definir_ganador(Diccionario_de_combinaciones, opcion, Diccionario_de_elecciones, usuario, cpu, empate ):

    # Elecciones del usuario y de la cpu
    eleccion_de_usuario = Diccionario_de_elecciones['elecciones'][opcion-1]
    eleccion_de_cpu = choice(Diccionario_de_elecciones['elecciones'])

    # Escritura de las elecciones
    print(f"La selección del usuario: {eleccion_de_usuario}")
    print(f"La selección de la cpu: {eleccion_de_cpu}\n")

    # En caso de que las elecciones sean empates
    if eleccion_de_cpu == eleccion_de_usuario:
        empate +=1
        print("Empate")

    # Crea una tupla
    tupla_de_elecciones_usuario = (eleccion_de_usuario, eleccion_de_cpu)
    tupla_de_elecciones_cpu = (eleccion_de_cpu,eleccion_de_usuario )

    # Itera sobre las combinaciones
    for combinacion in Diccionario_de_combinaciones['combinacion']:
        # Ocasión cuando gana el usuario
        if tupla_de_elecciones_usuario == combinacion:
            usuario += 1
            print("Gana el usuario")
            break
        # Ocasión cuando gana la cpu
        if tupla_de_elecciones_cpu == combinacion:
            cpu += 1
            print("Gana la cpu")
            break

    return usuario, cpu, empate             #Retorna los contadores





#-----------------------------------------MÓDULO-------------------------------------------------------
Diccionario_de_combinaciones = {'combinacion': [("tijeras", "papel"), ("papel", "piedra"), ("piedra", "lagarto"),
                                        ("lagarto", "spock"), ("spock", "tijeras"), ("tijeras", "lagarto"),
                                        ("lagarto", "papel"), ("papel", "spock"), ("spock", "piedra"), ("piedra", "tijeras")]}

Diccionario_de_elecciones = {'elecciones':["piedra", "papel", "tijeras", "lagarto", "spock"]}

usuario, cpu, empate = 0, 0, 0

opcion = None

# Ciclo: Repite el menú hasta que la opción sea 0.
while opcion != 0:
    opcion = menu()                 # Llamada de la función.

    # Rango de elecciones
    if opcion > 0 and opcion <= 5:
        # Llamada de función
        usuario, cpu, empate = definir_ganador(Diccionario_de_combinaciones, opcion, Diccionario_de_elecciones, usuario, cpu, empate)
        # Imprime los contadores
        print(f"\nUsuario: {usuario}  Cpu: {cpu}  Empate: {empate}\n")

    elif opcion == 6:
        reglamento()

    # Cuando el usuario presione 0:
    elif opcion == 0:
        print("\nSalida del programa con éxito.")

    # Cuando ingrese una opción inválida.
    else:
        print("\nCometiste un error al escoger una opción... :(")
        print("Vuelve a intentarlo.")
