"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Ciclos.
                Programa de introducción
                al funcionamiento de los ciclos
                while en Python.
"""


# Declaración de variables:
numero_registrado = int(input("Ingresa un número: "))               # Solicitud de datos.
contador = 1                                                        # Se inicializa un contador.


print(f"Los números del 1 al {numero_registrado}")                   # Letrero informativo.

# Proceso de sumatoria, condición: hasta que el contador sea igual al número registrado.
while contador <= numero_registrado :
    print(contador)
    contador+=1                                                     # No hay contadores unitarios

"""-El ciclo while, requiere una condición, en la
    que esta itera mientras esta sea verdadera.
"""

# Segundo ejercicio
numero_registrado2 = int(input("Ingresa un número: "))
contador2 = 1

print(f"Los números del 1 al {numero_registrado2}")

while contador2 <= numero_registrado2 :
    print(contador2, end= " ")                          # Palabra reservada para imprimir en una sola línea.
    contador2+=1
print("\nFin de cuenta, fuera del ciclo.")


# Tercer ejercicio:
# Imprimir todos los números pares hasta el número solicitado
numero_de_usuario = int(input("Ingresa un número cualquiera: "))
contador3 = 1

print(f"Los números pares de 1 a {numero_de_usuario} son: ")
while contador3 <= numero_de_usuario :
    if contador3 % 2 == 0 :
        # Si el residuo de la división entre 2 es cero imprime el número.
        print(contador3, end=" ")
    contador3 += 1
