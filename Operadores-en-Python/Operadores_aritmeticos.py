"""
Nombre: Héctor jesús Méndez Santiago
fecha:
Descripcion: En este programa aprendemos como utlizar todos los
operadores que aritmeticos que podemos usar en python

operadpores aritmeticos

"""


print("##INTRODUCIR DOS NUMEROS##")             #Imprimir un comentario al usuario
primer_numero = int(input("ingresa número: "))  #Utilizamos comandos para leer datos y conbertirolos a un tipo de dato
segundo_numero = int(input("ingresa número: ")) #Leer segundo dato, mostrando un letrero a la vez

print(f"resultado de la suma entre los dos numero es: {primer_numero + segundo_numero}")            #Imprimimos directamente la suma de los números solicitados con el operador +
print(f"resultado de la resta entre los dos numero es: {primer_numero - segundo_numero}")           #Imprimimos directamente la resta de los números solicitados con el operador -
print(f"resultado de la multiplicacion entre los dos numero es: {primer_numero * segundo_numero}")  #Imprimimos directamente la multiplicación de los numeros solicitados con el operador *
print(f"resultado de la division entre los dos numero es: {(primer_numero / segundo_numero):.2f}")  #imprimimos los resultados de dividir los dos numeros con el operador /
#2f para solo mostrar dos decimales en pantalla

print(f"resultado es: {primer_numero // segundo_numero}") #// divide los dos numeros pero sin mostrar datos en decimales
print(f"resultado es: {primer_numero ** segundo_numero}") #eleva el primer numero a la potencia del segundo numero
