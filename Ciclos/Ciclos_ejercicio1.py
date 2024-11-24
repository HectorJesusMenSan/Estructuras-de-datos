"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Primer ejercicio, para practicar los
                ciclos, en este caso el while:
                El ejercicio consiste en calcular la suma
                acumulativa, de 0 hasta el número que
                indique el usuario del programa.
"""

# Escritura de letreros interactivos.
"""Programa que calcula la suma acumulativa"""
print("#Cargando programa: Suma acumulativa#")
print("-_-")

# Declaración de variables y solicitud de datos.
numero_ingresado = int(input("¿Hasta qué número deseas que termine la suma acumulativa? :) : "))
contador = 1
registro_de_suma = 0

print(f"La suma acumulativa de 0 hasta {numero_ingresado} es: ")
while contador <= numero_ingresado :
    registro_de_suma = registro_de_suma + contador
    print(f"{registro_de_suma - contador} + {contador} = {registro_de_suma}")
    contador += 1
print(f"El resultado final es: {registro_de_suma}")

"""-El funcionamiento del while consiste en iniciar el contador en 1,
    y la condición es que mientras el contador sea menor o igual que
    el número ingresado por el usuario, aumentará el contador. Pero antes
    de la acumulación, debe realizarse una suma. Se inicializa una variable
    que lleve el registro de la suma y esta misma se actualiza constantemente
    mientras que el acumulador aumenta. La suma consiste en sumar
    el registro de suma por el valor que tiene el contador en cada iteración y
    guardándola en sí misma para acumularla. Cabe aclarar que la variable para
    el registro de la suma debe inicializarse en 0.
    Al final, solo se imprime el registro de la suma, que se acumuló en el 
    ciclo hasta que la condición se rompa.
"""

print("\nF I N  D E  P R O G R A M A")
