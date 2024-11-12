#Sirven para modularidad, permite reciclar y reducir codigo.
"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          11 de noviembre de 2024.
Descripción:    ciclos.
"""
#Codigo principal, codigo nivel de modulo, no es funcion

def hola(nombre):
    print(f"Hola {nombre}")

nombre=input("ingresa nombre: ")
hola(nombre)
print("Adios")

# Funcion para calcular numeros
def calculadora(opcion, numero1, numero2):
    if opcion == 1:
        resultado_de_operacion = numero1 + numero2
    elif opcion == 2:
        resultado_de_operacion= numero1 - numero2
    elif opcion == 3:
        resultado_de_operacion= numero1 * numero2
    elif opcion == 4:
        resultado_de_operacion= numero1 / numero2
    elif opcion == 5:
        resultado_de_operacion= numero1 // numero2
    elif opcion == 6:
        resultado_de_operacion= numero1 % numero2
    else:
        resultado_de_operacion= numero1 ** numero2
    return resultado_de_operacion


# Funcion para el menu:
def menu():
    print("Escoge una opcion: ")
    print("1) Suma")
    print("2) resta")
    print("3) multiplicacion")
    print("4) division")
    print("5) division entera")
    print("6) modulo")
    print("7) potenciacion")
    opcion=int(input("ingresa opcion: "))
    return opcion

opcion=menu()
numero1, numero2= float(input("ingresa el primer nmero: ")), float(input("ingresa el segundo numero: "))
print(f"El resultado de la operacion es : {calculadora(opcion, numero1, numero2) :.3f}")

