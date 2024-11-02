"""
Nombre: Héctor Jesus Mendez Santiago
Fecha: 29 de Octubre 2024
Descripción: Estos son los ejercicios de evaluacion
             para el primer parcial, del curso de
             estructuras de datos.
"""


# Presentacion del programa:
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print(":::Nombre: Hector Jesus::::")
print(":::Examen Parcial 1::::::::")
print(":::Area y perimetros:::::::")
print(":::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::")
print()

print(" C A R G A N D O  ;) ")

# Declaracion de variables
opcion = True
pi = 3.1416

# Escritura del menu:
while opcion:
    print("1) Calcular el área de un rectángulo.")
    print("2) Calcular el perímetro de un rectángulo.")
    print("3) Calcular el área de un círculo.")
    print("4) Calcular el perímetro de un círculo.")
    print("0) Salir.")
    opcion = int(input("Escoge la opcion que quieres realizar: "))
    print(":::::::::::::::::::::::::::::::::::::::::::::::")

    if  opcion>0 and opcion<5:
        if opcion==1:
            #Solicitud de datos:
            print("\nHaz escogido sacar el area de un rectangulo")
            ancho = float(input("Ahora introduce la medida de el ancho: "))
            largo = float(input("Ahora introduce la medida del largo: "))
            # Procesos:
            if ancho > largo:
                print("¡Que mal, pusiste al revez tus medidas!, intenta de nuevo :(\n")
            elif ancho==largo:
                print("¡Nomanches, tus medidas son iguales!, ¿es un cuadro o que?, intenta denuevo.")
            else:
                if ancho>0 and largo>0:
                    print(f"El area de tu rectangulo es: {ancho*largo:.3f}")
                    print("----------------")
                    print("|              |")
                    print(f"|              | Area : {ancho*largo:.3f}" )
                    print("|              |")
                    print("----------------\n")
                else:
                    print("Medidas no validas, intenta denuevo\n")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        elif opcion==2:
            #Solicitud de datos:
            print("\nHaz escogido sacar el perimetro de un rectangulo")
            ancho = float(input("Ahora introduce la medida de el ancho: "))
            largo = float(input("Ahora introduce la medida del largo: "))

            # Procesos:
            if ancho > largo:
                print("¡Que mal, pusiste al revez tus medidas!, intenta de nuevo :(\n")
            elif ancho==largo:
                print("¡Nomanches, tus medidas son iguales!, ¿es un cuadro o que?, intenta denuevo.")
            else:
                if ancho>0 and largo>0:
                    print(f"El perimetro de tu rectangulo es: {(ancho*2)+(largo*2):.3f}")
                    print(f"El area de tu rectangulo es: {(ancho*2)+(largo*2):.3f}")
                    print("----------------")
                    print("|              |")
                    print(f"|              | Perimetro: {(ancho*2)+(largo*2):.3f}" )
                    print("|              |")
                    print("----------------\n")
                else:
                    print("Medidas no validas, intenta denuevo\n")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        elif opcion==3:
            # Solicitud de datos:
            print("Haz escogido calcular el area de un circulo")
            radio=float(input("Introduce la medida del radio: "))
            #Procesos:
            if  radio>0:
                print(f"El area del circulo es: {pi*(radio*radio):.3f}\n")
            else:
                print("Con el dato ingresado es imposible hacer los calculos. \n")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        else:
            #Solicitud de datos:
            print("Haz escogido calcular el perimetro de un circulo")
            radio=float(input("Introduce la medida del radio: "))
            #Procesos:
            if  radio>0:
                print(f"El perimetro del circulo es: {pi*(radio*2):.3f}\n")
            else:
                print("Con el dato ingresado es imposible hacer los calculos. \n")

            print(":::::::::::::::::::::::::::::::::::::::::::::::")
    elif opcion==0:
        print(":::CERRANDO PROGRAMA:::")
        break
    else:
        print("\nOpcion no valida, intenta denuevo pap's :/ \n")
        print(":::::::::::::::::::::::::::::::::::::::::::::::")

"""-El programa da al usuario un menu donde puede escoger las opciones disponibles
   enumerados del 0 al 4, si introduce uno diferentes se muestra un letrero de 
   indicacion. 
   -En la primera y segunda opcion se solicita las medidas del
   ancho y largo, si estos son mayores a cero se ejecutan los procedimientos para
   calcular el area y el perimetro, si los datos son disparejos o iguales, se 
   indica al usuario a reintentar.
   -En la tercera y cuarta opcion se solicitan los datos que seria la medida de
   un radio, para calcular el area o el perimetro, para que se realicen las 
   acciones correspondientes debe ser mayor a cero.
   -Y por ultimo la quinta opcion es cuando en el menu principal el usuario escoje
   salir del programa, esto rompe el ciclo y termina el programa."""
