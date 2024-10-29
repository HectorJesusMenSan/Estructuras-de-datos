"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          2 de octubre de 2024.
Descripción:    Ejercicio 3, calculadra basica:
1. suma             4. division
2. resta            5. division entera
3. multiplicacion   6. exponenciacion
"""
opcion=True

while opcion:
    print("ingresa 0 para salir")
    print("ingresa 1 para sumar")
    print("ingresa 2 para restar")
    print("ingresa 3 para multiplicar")
    print("ingresa 4 para dividir")
    print("ingresa 5 para dividir en entero")
    print("ingresa 6 para exponenciar")
    opcion=int(input("ingresa una opción: "))
    print()
    if opcion==1:
        numero=float(input("ingresa primer numero: "))
        numero2=float(input("ingresa segundo numero: "))
        print(f"La suma de los dos numeros es: {numero + numero2} \n")
    elif opcion == 2:
        numero = float(input("ingresa primer numero: "))
        numero2 = float(input("ingresa segundo numero: "))
        print(f"La resta de los dos numeros es: {numero - numero2}\n")
    elif opcion == 3:
        numero = float(input("ingresa primer numero: "))
        numero2 = float(input("ingresa segundo numero: "))
        print(f"La multiplicacion de los dos numeros es: {numero * numero2}\n")
    elif opcion == 4:
        numero = float(input("ingresa primer numero: "))
        numero2 = float(input("ingresa segundo numero: "))
        print(f"La resta de los dos numeros es: {numero / numero2}\n")
    elif opcion == 5:
        numero = float(input("ingresa primer numero: "))
        numero2 = float(input("ingresa segundo numero: "))
        print(f"La division entera de los dos numeros es: {numero // numero2}\n")
    elif opcion == 6:
        numero = float(input("ingresa primer numero: "))
        numero2 = float(input("ingresa segundo numero: "))
        print(f"La exponenciacion de los dos numeros es: {numero ** numero2}\n")
    elif opcion == 0:
        print("Saliendo")
        break
    else:
        print("\nError, volviendo a cargar\n")