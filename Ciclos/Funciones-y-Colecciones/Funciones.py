# Sirven para modularidad, permiten reciclar y reducir código.
"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          11 de noviembre de 2024.
Descripción:    Introducción a funciones.
"""

# Código principal, código a nivel de módulo, se le llama al código que no va en funciones

"""def para definir función.
   A comparación de C o C++
   en Python solo necesita, el
   nombre y el tipo de datos que
   recibe, esto en tanto de definición.

   -LAS FUNCIONES SIRVEN PARA RESOLVER
   PROBLEMAS GRANDES Y COMPLEJOS, POR 
   PEQUEÑAS SECCIONES-"""


# Definición de función.
def hola(nombre):  # Recibe un nombre.
    # Acción de función
    print(f"Hola {nombre}")  # Imprime el nombre.


# Función para el menú:
def menu():  # No recibe datos.
    # Menú escrito para interacción con el usuario.
    print("Escoge una opción: ")
    print("0) Salir")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) División entera")
    print("6) Módulo")
    print("7) Potenciación")
    opcion = int(input("Escoge una opción: "))
    return opcion


# Función para calcular números
def calculadora():  # No recibe datos
    opcion = True
    while opcion:
        opcion = menu()  # Llamada a función menú

        # Código para implementar suma:
        if opcion == 1:
            numero = float(input("Ingresa primer número: "))
            numero2 = float(input("Ingresa segundo número: "))
            print(f"La suma de los dos números es: {numero + numero2} \n")

        # Código para implementar resta:
        elif opcion == 2:
            numero = float(input("Ingresa primer número: "))
            numero2 = float(input("Ingresa segundo número: "))
            print(f"La resta de los dos números es: {numero - numero2}\n")

        # Código para implementar multiplicación:
        elif opcion == 3:
            numero = float(input("Ingresa primer número: "))
            numero2 = float(input("Ingresa segundo número: "))
            print(f"La multiplicación de los dos números es: {numero * numero2}\n")

        # Código para implementar división:
        elif opcion == 4:
            numero = float(input("Ingresa primer número: "))
            numero2 = float(input("Ingresa segundo número: "))
            print(f"La división de los dos números es: {numero / numero2}\n")

        # Código para implementar división entera:
        elif opcion == 5:
            numero = float(input("Ingresa primer número: "))
            numero2 = float(input("Ingresa segundo número: "))
            print(f"La división entera de los dos números es: {numero // numero2}\n")

        # Código para implementar exponenciación:
        elif opcion == 6:
            numero = float(input("Ingresa primer número: "))
            numero2 = float(input("Ingresa segundo número: "))
            print(f"La exponenciación de los dos números es: {numero ** numero2}\n")

        # Código para implementar salida de programa:
        elif opcion == 0:
            print("Saliendo")  # Letrero informativo.
            break  # Rompe el ciclo.
        # Código en caso de que el usuario introduzca un número diferente a los del menú:
        else:
            print("\nError, volviendo a cargar\n")


calculadora()  # Llamada a función calculadora

nombre = input("Ingresa tu nombre: ")
hola(nombre)  # Llamada a la función hola.
print("Adiós")

