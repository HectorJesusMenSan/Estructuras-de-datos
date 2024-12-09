"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          6 de diciembre de 2024.
Descripción:    Ejercicio que muestra la cantidad
                de escalones ingresada por el
                usuario.
"""

# Declaración de variables
opcion = None

# Ciclo de iteración
while opcion != 0:
    # Solicitud de datos
    cantidad_de_escalones = int(input("Ingresa la cantidad de escalones o ingresa cero [0], si deseas salir: "))
    # Lectura para la opción
    opcion = cantidad_de_escalones

    # Se inicia un contador igualándolo a la cantidad de escalones
    contador_de_espacios = cantidad_de_escalones

    # Si el número de escalones es positivo
    if opcion > 0:
        # Contador para un ciclo que imprima los escalones
        contador1 = 0
        while contador1 <= cantidad_de_escalones:

            # Se multiplican los espacios por el contador de espacios + 1
            espacios = " " * (contador_de_espacios + 1)
            # Escritura de bases
            print(espacios, end="  __\n")

            # Se aplica solo si el contador del ciclo es diferente de la cantidad de escalones
            if contador1 != cantidad_de_escalones:
                # Escritura de altura
                print(espacios, end="  |\n")
            # Se resta contador de espacios
            contador_de_espacios -= 1
            # Se aumenta contador del ciclo
            contador1 += 1

    # Si la cantidad de escalones es negativa
    elif opcion < 0:
        # Contador para un ciclo que imprima los escalones
        contador1 = 0
        while contador1 <= (cantidad_de_escalones * -1):  # Se convierte la cantidad de escalones a positivo
            # Espacios es igual a la multiplicación por el contador
            espacios = " " * contador1
            # Escribe los pisos
            print(f"{espacios}__")
            # Se aplica solo si el contador del ciclo es diferente de la cantidad de escalones
            if contador1 != (cantidad_de_escalones * -1):
                # Imprime la altura
                print(espacios, end=" |\n")
            # Aumenta contador de ciclo
            contador1 += 1

print("Programa terminado")



"""El programa consiste en imprimir una escalera con la cantidad de escalones 
   proporcionados por el usuario, con la restricción de que si el número es 
   positivo, la escalera asciende, y si es negativo, la escalera desciende."""






