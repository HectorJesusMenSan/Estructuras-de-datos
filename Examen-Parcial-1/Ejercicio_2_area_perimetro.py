"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 29 de Octubre de 2024
Descripción: Estos son los ejercicios de evaluación
             para el primer parcial, del curso de
             estructuras de datos.
"""


# Presentación del programa:
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print(":::Nombre: Héctor Jesús::::")
print(":::Examen Parcial 1::::::::")
print(":::Área y perímetros:::::::")
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print()

print(" C A R G A N D O  ;) ")

# Declaración de variables
opcion = True
pi = 3.1416

while opcion:
    # Escritura del menú:
    print("1) Calcular el área de un rectángulo.")
    print("2) Calcular el perímetro de un rectángulo.")
    print("3) Calcular el área de un círculo.")
    print("4) Calcular el perímetro de un círculo.")
    print("0) Salir.")
    opcion = int(input("Escoge la opción que quieres realizar: "))
    print(":::::::::::::::::::::::::::::::::::::::::::::::")

    if  opcion > 0 and opcion < 5:
        if opcion == 1:
            # Solicitud de datos:
            print("\nHas escogido sacar el área de un rectángulo")
            ancho = float(input("Ahora introduce la medida del ancho: "))
            largo = float(input("Ahora introduce la medida del largo: "))
            print("Cargando tus datos...")
            # Procesos:
            if ancho > largo:
                print("¡Qué mal, pusiste al revés tus medidas!, intenta de nuevo :(\n")
            elif ancho == largo:
                print("¡No manches, tus medidas son iguales!, ¿es un cuadro o qué?, intenta de nuevo.")
            else:
                if ancho > 0 and largo > 0:
                    print(f"El área de tu rectángulo es: {ancho * largo:.3f}")
                    print("----------------")
                    print("|              |")
                    print(f"|              | Área : {ancho * largo:.3f}" )
                    print("|              |")
                    print("----------------\n")
                else:
                    print("Medidas no válidas, intenta de nuevo\n")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        elif opcion == 2:
            # Solicitud de datos:
            print("\nHas escogido sacar el perímetro de un rectángulo")
            ancho = float(input("Ahora introduce la medida del ancho: "))
            largo = float(input("Ahora introduce la medida del largo: "))
            print("Cargando tus datos...")

            # Procesos:
            if ancho > largo:
                print("¡Qué mal, pusiste al revés tus medidas!, intenta de nuevo :(\n")
            elif ancho == largo:
                print("¡No manches, tus medidas son iguales!, ¿es un cuadro o qué?, intenta de nuevo.")
            else:
                if ancho > 0 and largo > 0:
                    print(f"El perímetro de tu rectángulo es: {(ancho * 2) + (largo * 2):.3f}")
                    print(f"El área de tu rectángulo es: {(ancho * 2) + (largo * 2):.3f}")
                    print("----------------")
                    print("|              |")
                    print(f"|              | Perímetro: {(ancho * 2) + (largo * 2):.3f}" )
                    print("|              |")
                    print("----------------\n")
                else:
                    print("Medidas no válidas, intenta de nuevo\n")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        elif opcion == 3:
            # Solicitud de datos:
            print("Has escogido calcular el área de un círculo")
            radio = float(input("Introduce la medida del radio: "))
            print("Cargando tus datos...")

            # Procesos:
            if radio > 0:
                print(f"El área del círculo es: {pi * (radio * radio):.3f}\n")
            else:
                print("Con el dato ingresado es imposible hacer los cálculos. \n")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        else:
            # Solicitud de datos:
            print("Has escogido calcular el perímetro de un círculo")
            radio = float(input("Introduce la medida del radio: "))
            print("Cargando tus datos...")

            # Procesos:
            if radio > 0:
                print(f"El perímetro del círculo es: {pi * (radio * 2):.3f}\n")
            else:
                print("Con el dato ingresado es imposible hacer los cálculos. \n")

            print(":::::::::::::::::::::::::::::::::::::::::::::::")
    elif opcion == 0:
        print(":::CERRANDO PROGRAMA:::")
        break
    else:
        print("\nOpción no válida, intenta de nuevo pap's :/ \n")
        print(":::::::::::::::::::::::::::::::::::::::::::::::")

"""-El programa da al usuario un menú donde puede escoger las opciones disponibles
   enumeradas del 0 al 4, si introduce uno diferente se muestra un letrero de 
   indicación. 
   -En la primera y segunda opción se solicitan las medidas del
   ancho y largo, si estos son mayores a cero se ejecutan los procedimientos para
   calcular el área y el perímetro, si los datos son disparejos o iguales, se 
   indica al usuario a reintentar.
   -En la tercera y cuarta opción se solicitan los datos que serían la medida de
   un radio, para calcular el área o el perímetro, para que se realicen las 
   acciones correspondientes debe ser mayor a cero.
   -Y por último, la quinta opción es cuando en el menú principal el usuario escoge
   salir del programa, esto rompe el ciclo y termina el programa.
"""
