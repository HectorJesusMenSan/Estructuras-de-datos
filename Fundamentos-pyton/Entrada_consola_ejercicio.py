'''
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          10 de octubre de 2024.
Descripción:    Primer ejercicio de pratica en entrada de datos por consola:


                a) Pida 2 números decimales por consola al usuario utilizando la función input.

                b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.

                Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.

'''


#   Solicitud de datos:
print("##PARA QUE EL PROGRAMA FUNCIONE, TUS NÚMEROS DEBEN SER DIFERENTES DE CERO##")                #Escribe un pequeño letrero.
print()                                                                                             #Salto de linea.
numero1, numero2 = int(input("Ingresa primer número: ")), int(input("Ingresa segundo número: "))    #Convierte los datos ingresados a entero y los guarda en variables.

#   Escritura de resultados de las operaciones aritmeticas:
print(f"El resultado de {numero1} + {numero2} = {numero1 + numero2}")                               #Muestra la suma de los dos números ingresados
print(f"El resultado de {numero1} - {numero2} = {numero1 + numero2}")                               #Muestra la resta de los dos números ingresados
print(f"El resultado de {numero1} * {numero2} = {numero1 + numero2}")                               #Muestra la multiplicación de los dos números ingresados
print(f"El resultado de {numero1} / {numero2} = {numero1 + numero2}")                               #Muestra la división de los dos números ingresados