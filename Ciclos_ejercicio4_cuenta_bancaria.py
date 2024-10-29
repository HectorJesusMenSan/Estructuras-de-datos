"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          2 de octubre de 2024.
Descripción:    Ejercicio 3, calculadra basica:
1. suma             4. division
2. resta            5. division entera
3. multiplicacion   6. exponenciacion
"""
opcion=True
saldo=5000.00
print("*Bienvenido al banco azteca*")
while opcion:
    print("[1] consultar saldo")
    print("[2] ingresar dinero")
    print("[3] retirar dinero")
    print("[0] salir")
    opcion=int(input("Ingresa una opcion: "))
    if opcion>=0 and opcion<=3:
        if opcion==1:
            print(f"Tu saldo es: {saldo}\n")
        elif opcion==2:
            saldo += float(input("Ingresa cantidad de dinero que agregaras a tu saldo: "))
            print(f"Ahora tu saldo es de {saldo}\n")
        elif opcion==3:
            dinero = float(input("Ingresa cantidad de dinero que retiraras: "))
            if saldo >= dinero :
                saldo = saldo-dinero
                print(f"Ahora tu saldo es de {saldo}\n")
            elif saldo==0:
                print("Ya no tienes saldooo!. Recargando...\n")
            else:
                print("La cantidad ingresada es mas alta que tu saldo.")
        else:
            break
    else:
        print("la opcion que ingresaste no es valida")