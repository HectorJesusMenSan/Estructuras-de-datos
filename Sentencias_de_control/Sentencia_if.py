"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          23 de octubre de 2024.
Descripción:    Programa que muestra la manera de usar la sentencia if.
                La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
                dependiendo de si una condición se cumple o no.

#if condición :
    #datos          # si se cumple la condición hará estos procesos...
    #datos
#instrucciones que siguen después de pasar por el if.
"""
# programa que determine si alguien es mayor de edad
print("Cargando programa...")                       # Esto escribe en pantalla un letrero.
edad = int(input("¿Cuál es tu edad? "))             # Lectura y conversión de datos a tipo entero dados por el usuario.
if edad >= 18:                                      # Condición: si el número ingresado es mayor o igual a 18.
    # Estas instrucciones se ejecutan si la condición se cumple.
    print("Tú eres mayor de edad")
    print("Este mensaje se imprime dentro del if")

print("Este mensaje está fuera del if")              # Continuación del código.

""" Tiene que estar bien alineado e indentado para que haga lo que queremos. """
