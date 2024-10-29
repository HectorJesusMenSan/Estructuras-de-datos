"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Primer programa para ejercitar la habilidad con las sentencias

Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales. Para ello:

a) Solicite al usuario dos números decimales.

b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.

c) Muestre el número menor (o que son iguales) en consola.

"""
print("CARGANDO...")                                       # Escritura de comentario
print("Programa: Calcula cual de los numeros es menor.")
#Solicitud de datos
numero1 = int(input("Ingresa primer numero: "))             # Guarda y convierte los datos a tipo entero.
numero2 = int(input("Ingresa segundo numero: "))

#Aplicacion de sentencias y condiciones
if numero1 == numero2 :
    print(f"Los numeros {numero1} y {numero2} son iguales.") # Si ambos numeros son iguales se ejecuta esta accion.
elif numero1 < numero2 :
    print(f"El numero menor es: {numero1}.")                 # Si el numero1 es menor que el numero2 se ejecuta esta accion
else:
    print(f"El numero menor es {numero2}.")                  # Si ninguna de las condiciones anteriores se cumplen es ejecuta esta accion
