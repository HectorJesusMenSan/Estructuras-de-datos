"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          23 de octubre de 2024.
Descripción:    Programa que muestra la manera de usar la sentencia if.
                La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
                dependiendo de si una condición se cumple o no.

#if condición :
    #datos          #si se cuple la condicion hará estos procesos...
    #datos
#instrucciones que siguen despues de pasar por el if.
"""
#programa que determine si alguien es mayor de edad
print("Cargando programa...")                       # Esto escribe en pantalla un letrero.
edad = int(input("¿Cual es tu edad? "))             # Lectura y conversion de datos a tipo entero dados por el usuario.
if edad>=18:                                        # Condicion: si el numero ingresado es mayor o igual a 18.
    # Estas instrucciones se ejecutan si la condicion se cumple.
    print("tu eres mayor de edad")
    print("Este mensaje se imprime dentro del if")

print("Este mensaje esta fuera del if")             # Continuacion del codigo.

"""tiene que estar bien alineado e identado par que haga lo que queremos."""