"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Ejercicio 4, cuenta bancaria:
                Este programa otorga un menú
                al usuario, para que escoja
                una opción dependiendo de la
                acción que desea realizar: ingresar,
                retirar o consultar saldo.
"""

# Declaración de variables:
opcion = True                # Se inicializa en True para que entre en el ciclo.
saldo = 5000.00              # Se inicializa el saldo.

# Escritura de letrero:
print("*Bienvenido al banco Azteca*")

while opcion:
    # Escritura de menú informativo para interacción con el usuario:
    print("[1] Consultar saldo")
    print("[2] Ingresar dinero")
    print("[3] Retirar dinero")
    print("[0] Salir")

    # Recepción de datos:
    opcion = int(input("Ingresa una opción: "))

    # Si el valor del dato recibido está en un rango de 0-3, ejecuta las acciones:
    if opcion >= 0 and opcion <= 3:

        # Código para consultar saldo:
        if opcion == 1:
            print(f"Tu saldo es: {saldo}\n")

        # Código para ingresar saldo:
        elif opcion == 2:
            saldo += float(input("Ingresa cantidad de dinero que agregarás a tu saldo: "))
            print(f"Ahora tu saldo es de {saldo}\n")

        # Código para retirar saldo:
        elif opcion == 3:
            # Lee la cantidad de dinero que el usuario quiere retirar:
            dinero = float(input("Ingresa cantidad de dinero que retirarás: "))

            if saldo >= dinero:
                saldo = saldo - dinero
                print(f"Ahora tu saldo es de {saldo}\n")

            # Código si la cantidad introducida es mayor o igual que el saldo en cuenta:
            elif saldo == 0:
                print("¡Ya no tienes saldo! Recargando programa...\n")
            else:
                print("La cantidad ingresada es mayor que tu saldo.")
                print("Intenta de nuevo.")
        # Si la opción elegida es 0, se rompe el ciclo:
        else:
            break
    # Si el valor recibido está fuera del rango de la condición establecida, ejecuta:
    else:
        print("La opción que ingresaste no es válida.\n")  # Letrero informativo.
