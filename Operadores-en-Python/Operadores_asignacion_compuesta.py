'''
Nombre:
Fecha:
Descripción:
Operadores de asignacion compuestas.
'''

numero1, numero2 = int(input("ingresa numero 1: ")), int(input("ingresa numero 2: "))
print(numero1, numero2)

numero1 += 3            #Es como tener nummero1 = numero + 3
print(numero1)

numero2 -= 5
print(numero2)

numero1 *= 2
print(numero1)

numero2 /= 4
print(numero2)


#Comienza segunda actividad#
numero3, numero4 = int(input("ingresa numero : ")), int(input("ingresa numero : "))
print(numero3, numero4)

numero3 += numero4
print(numero3)
numero3 *= numero3
print(numero3)
numero3 -= numero4
print(numero3)
numero3 += 3
print(numero3)
numero3 /= 2
print(numero3)