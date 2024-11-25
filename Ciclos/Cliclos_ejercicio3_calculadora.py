"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          26 de octubre de 2024.
Descripción:    Ejercicio 3, calculadora básica:
1. suma             4. división
2. resta            5. división entera
3. multiplicación   6. exponenciación

                -Calculadora que realiza las operaciones
                más básicas, usando un ciclo while,
                como práctica para desarrollar las
                habilidades y lógica en Python.
"""

# Inicialización de variable:
opcion = True  # Se pone en True para que pueda entrar en el ciclo.

while opcion:
    # Impresión de letreros informativos para mostrar el menú al usuario.
    print("Ingresa 0 para salir")
    print("Ingresa 1 para sumar")
    print("Ingresa 2 para restar")
    print("Ingresa 3 para multiplicar")
    print("Ingresa 4 para dividir")
    print("Ingresa 5 para dividir en entero")
    print("Ingresa 6 para exponenciar")

    # Recibe un dato de tipo entero, que es la opción que elige el usuario.
    opcion = int(input("Ingresa una opción: "))
    print()

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

"""
-Este programa utiliza la opción = True, para que en el momento de utilizar el ciclo while entre
siempre, hasta que el usuario introduzca 0, y se ejecute la instrución break que romperá el ciclo.
En las otras opciones, dependiendo de qué opción escoja el usuario del menú otorgado, se ejecutarán las
operaciones correspondientes.
"""
