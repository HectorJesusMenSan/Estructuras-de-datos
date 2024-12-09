"""
Héctor Jesús Méndez Santiago
9 de octubre de 2024.
Descripción: En este programa están los tipos de variables en Python y su forma en las que se usan.
"""
from secrets import choice


#_____________________________________FUNCIONES__________________________________________

# Función menú
def menu_de_inicio ():
    # Escritura de letreros
    print("\n________________________________")
    print("1) Iniciar test.")
    print("2) Salir.")
    # Lectura de datos
    opcion = int(input("Ingresa la opción que desees: "))
    return opcion       # Retorna la opción
# Funciones para cada pregunta:
def pregunta1 (Diccionario_de_preguntas):
    # Se escribe la pregunta en pantalla
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("¿Cuál de las siguientes opciones odiarías más que la gente te llamara?")
    contador = 0
    # Muestra las opciones
    for pregunta in Diccionario_de_preguntas['pregunta1']:
        contador +=1
        print(f"{contador}) {pregunta}\n")

    # Lectura de datos
    opcion = int(input("\nSelecciona una opción :"))
    return opcion       # Retorna la opción

def pregunta2 (Diccionario_de_preguntas):
    # Se escribe la pregunta en pantalla

    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?")
    contador = 0
    # Muestra las opciones

    for pregunta in Diccionario_de_preguntas['pregunta2']:
        contador +=1
        print(f"{contador}) {pregunta}\n")

    # Lectura de datos

    opcion = int(input("\nSelecciona una opción :"))
    return opcion       # Retorna la opción

def pregunta3 (Diccionario_de_preguntas):
    # Se escribe la pregunta en pantalla

    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("Dada la opción, preferirías inventar una poción que garantizara:")
    contador = 0
    # Muestra las opciones

    for pregunta in Diccionario_de_preguntas['pregunta3']:
        contador +=1
        print(f"{contador}) {pregunta}\n")
    # Lectura de datos

    opcion = int(input("\nSelecciona una opción :"))
    return opcion       # Retorna la opción

def pregunta4 (Diccionario_de_preguntas):
    # Se escribe la pregunta en pantalla

    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("¿Cómo te definirías en una sola palabra?")
    contador = 0
    # Muestra las opciones

    for pregunta in Diccionario_de_preguntas['pregunta4']:
        contador +=1
        print(f"{contador}) {pregunta}\n")
    # Lectura de datos

    opcion = int(input("\nSelecciona una opción :"))
    return opcion       # Retorna la opción

def pregunta5 (Diccionario_de_preguntas):
    # Se escribe la pregunta en pantalla

    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("¿Qué cualidad te describe mejor?")
    contador = 0
    # Muestra las opciones

    for pregunta in Diccionario_de_preguntas['pregunta5']:
        contador +=1
        print(f"{contador}) {pregunta}\n")
    # Lectura de datos

    opcion = int(input("\nSelecciona una opción :"))
    return opcion       # Retorna la opción

def pregunta6 (Diccionario_de_preguntas):
    # Se escribe la pregunta en pantalla

    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("¿Cuál es tu clase favorita?")
    contador = 0
    # Muestra las opciones

    for pregunta in Diccionario_de_preguntas['pregunta6']:
        contador +=1
        print(f"{contador}) {pregunta}\n")
    # Lectura de datos

    opcion = int(input("\nSelecciona una opción :"))
    return opcion       # Retorna la opción

def pregunta7 (Diccionario_de_preguntas):
    # Se escribe la pregunta en pantalla

    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("¿Cuál es tu lenguaje de programación favorito?")
    contador = 0
    # Muestra las opciones

    for pregunta in Diccionario_de_preguntas['pregunta7']:
        contador +=1
        print(f"{contador}) {pregunta}\n")
    # Lectura de datos

    opcion = int(input("\nSelecciona una opción :"))
    return opcion  # Retorna la opción




def ejecucion_de_test (Diccionario_de_preguntas):
    # Opciones
    opcion1 = 1
    opcion2 = 1
    opcion3 = 1
    opcion4 = 1
    opcion5 = 1
    opcion6 = 1
    opcion7 = 1

    # Diccionarios:
    Diccionario_de_casas = {'casa':["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw "]}

    # Para pregunta 1:
    while opcion1 != 0:
        opcion1 = pregunta1(Diccionario_de_preguntas)
        if opcion1>0 and opcion1<5:
            opcion1 = 0
        else:
            print("Error")
    # Para pregunta2
    while opcion2 != 0:
        opcion2 = pregunta2(Diccionario_de_preguntas)
        if opcion2>0 and opcion2<5:
            opcion2 = 0
        else:
            print("Error")
    # Para pregunta3
    while opcion3 != 0:
        opcion3 = pregunta3(Diccionario_de_preguntas)
        if opcion3>0 and opcion3<5:
            opcion3 = 0
        else:
            print("Error")
    # Para pregunta4
    while opcion4 != 0:
        opcion4 = pregunta4(Diccionario_de_preguntas)
        if opcion4>0 and opcion4<5:
            opcion4 = 0
        else:
            print("Error")
    # Para pregunta5
    while opcion5 != 0:
        opcion5 = pregunta5(Diccionario_de_preguntas)
        if opcion5>0 and opcion5<5:
            opcion5 = 0
        else:
            print("Error")
    # Para pregunta6
    while opcion6 != 0:
        opcion6 = pregunta6(Diccionario_de_preguntas)
        if opcion6>0 and opcion6<6:
            opcion6 = 0
        else:
            print("Error")
    # Para pregunta7
    while opcion7 != 0:
        opcion7 = pregunta7(Diccionario_de_preguntas)
        if opcion7>0 and opcion7<5:
            opcion7 = 0
        else:
            print("Error")

    # Elige una casa aleatoria
    casa = choice(Diccionario_de_casas['casa'])
    print(f"Tu casa es: {casa}")




#____________________________________MÓDULO_______________________________________________

# Declaración de variables:
opcion = None
Diccionario_de_preguntas = {'pregunta1':("Ordinario", "Ignorante", "Cobarde", "Egoísta"),
                           'pregunta2': ("Te extraña pero sonríe", "Pide más historias sobre tus aventuras",
                                         "Piensa con admiración tus logros", "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta."),
                           'pregunta3': ("Gloria", "Sabiduría", "Amor", "Poder"),
                           'pregunta4': ("Valiente", "Ambicioso", "Leal", "Curioso"),
                           'pregunta5': ("La fuerza", "La astucia", "La paciencia", "La inteligencia"),
                           'pregunta6': ("Vuelo", "Defensa contra las artes oscuras", "Animales fantásticos", "Pociones"),
                           'pregunta7': ("C", "Python", "C++", "JavaScript")}
# Se ejecuta la opción que desee el usuario
while opcion != 0:
    opcion = menu_de_inicio()   # Llamada a la función
    if opcion == 2:
        print("Salida del programa con éxito.")
        opcion = 0
    elif opcion == 1:
        ejecucion_de_test(Diccionario_de_preguntas)     # Llamada a la función
    else:
        print("Error.")
