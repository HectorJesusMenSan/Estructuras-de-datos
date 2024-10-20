
"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          16 de octubre de 2024.
Descripción:    En este programa se abordan los temas de operadores relacionales
                que se pueden usar en Python: ==, <, >, !=.
"""
#   Al igual que en c y c++ usamos los mismos operadores o las mismas nomenlaturas.
#   Se utilizan para comparar dos valores.
numero1, numero2 = float(input("escribir numero 1: ")), float(input("escribir numero 2: "))     #Solicitud, lectura y conversion de datos a flotantes.
print(f"¿El número {numero1:.2f} es mayor que {numero2:.2f}? {numero1>numero2}")                #Muestra en resultado booleano si el numero1 es mayor al numero2.
print(f"¿El número {numero1:.2f} es mayor o igual que {numero2:.2f}? {numero1>=numero2}")       #Muestra en resultado booleano si el numero1 es mayor o igual al numero2.
print(f"¿El número {numero1:.2f} es igual que {numero2:.2f}? {numero1==numero2}")               #Muestra en resultado booleano si ambos numeros son iguales.
print(f"¿El número {numero1:.2f} es menor que {numero2:.2f}? {numero1<numero2}")                #Muestra en resultado booleano si el numero1 es menor al numero2.
print(f"¿El número {numero1:.2f} es menor o igual que {numero2:.2f}? {numero1<=numero2}")       #Muestra en resultado booleano si el numero1 es menor o igual al numero2.
print(f"¿El número {numero1:.2f} es diferente que {numero2:.2f}? {numero1!=numero2}")           #Muestra en resultado booleano si ambos numeros son diferentes.