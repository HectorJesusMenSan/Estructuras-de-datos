"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 7 de enero del 2025
Descripción:
"""

cadena = input("ingresa una cadena : ")
#Para comprobar si el dato ingresado es numerico
print()
print(cadena.isnumeric())

#Para comprobar si el dato ingresado es alphanumerico
print()
print(cadena.isalpha())

#Para comprobar si el dato ingresado es
print()
print(cadena.isalnum())
#___________________________________________________________primeraParte___________________________________________
numero = input("ingresa un numero : ")

while not numero.isnumeric():
    print("Opcion no valida")
    numero = input("Intenta nuevamente: ")

print()

numero = int(numero)
print(f"El numero {numero} es de tipo {type(numero)}")
#________________________________________________________segundaParte_____________________________________________________
#Para los numeros negativos

def cadena_a_entero (cadena):
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

num_cadena = input("Ingresa Z: ")
numero = cadena_a_entero(num_cadena)

while numero is None:
    print("Opcion no valida: ")
    num_cadena = input("Ingresa Z: ")
    numero = cadena_a_entero(num_cadena)

print(f"El numero {numero} es tipo {type(numero)}")

