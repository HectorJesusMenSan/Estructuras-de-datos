
"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          16 de octubre de 2024.
Descripción:    En este programa se abordan los temas de operadores relacionales
                que se pueden usar en Python: ==, <, >, !=.
"""
#   Al igual que en c y c++ usamos los mismos operadores o las mismas nomenclaturas.
#   Se utilizan para comparar dos valores.
numero1, numero2 = float(input("Escribir número 1: ")), float(input("Escribir número 2: "))     #   Solicitud, lectura y conversion de datos a flotantes.
print(f"¿El número {numero1:.2f} es mayor que {numero2:.2f}? {numero1>numero2}")                #   Muestra en resultado booleano si el numero1 es mayor al numero2.
print(f"¿El número {numero1:.2f} es mayor o igual que {numero2:.2f}? {numero1>=numero2}")       #   Muestra en resultado booleano si el numero1 es mayor o igual al numero2.
print(f"¿El número {numero1:.2f} es igual que {numero2:.2f}? {numero1==numero2}")               #   Muestra en resultado booleano si ambos números son iguales.
print(f"¿El número {numero1:.2f} es menor que {numero2:.2f}? {numero1<numero2}")                #   Muestra en resultado booleano si el numero1 es menor al numero2.
print(f"¿El número {numero1:.2f} es menor o igual que {numero2:.2f}? {numero1<=numero2}")       #   Muestra en resultado booleano si el numero1 es menor o igual al numero2.
print(f"¿El número {numero1:.2f} es diferente que {numero2:.2f}? {numero1!=numero2}")           #   Muestra en resultado booleano si ambos números son diferentes.

"""
Los operadores relacionales son símbolos que se utilizan en programación para comparar dos valores. 
Estos operadores devuelven un valor booleano (verdadero o falso) dependiendo del resultado de la comparación. 
Son fundamentales para tomar decisiones dentro de un programa, ya que permiten construir expresiones condicionales 
que determinan el flujo de ejecución.

Operadores Relacionales Comunes:
Operador	Significado
==	Igual a
!=	Diferente de
>	Mayor que
<	Menor que
>=	Mayor o igual que
<=	Menor o igual que
"""