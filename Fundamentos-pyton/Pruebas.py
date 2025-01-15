"""Programa que recibe tres datos de un usuario y
   escribe una salida, el numero mas grande."""

# Declaracion de variables:
numero_mayor = 0

# Solicitud de datos:
variable_1 = int(input("Ingresa prmer numero: "))       # Convierte y almacena datos de tipo entero.
variable_2 = int(input("Ingresa segundo numero: "))
variable_3 = int(input("Ingresa tercer numero: "))

# Proceso de comparación:
if numero_mayor < variable_1:   # Compara si la variable numero mayor es menor que el primer numero introducido
    numero_mayor = variable_1   # Como la variable numero mayor no tiene valor siempre va a entrar a la sentencia
                                # Entonces el valor se actualiza al del numero introducido

if numero_mayor < variable_2:   # Despues compara con el siguiente numero introducido
    numero_mayor = variable_2   # Si el segundo numero introducido es mayor que la variable numero mayor
                                # entonces cambia su valor al del numero mas grande

if numero_mayor < variable_3:
    numero_mayor = variable_3

print(f"El numero mas grande es: ", numero_mayor)

"""Como se aprecia en el programa, en el primer caso,
se va a cumplir la condicion ya que la varaible: numero_mayor
no tiene un valor especifico o vale 0 por defecto.
Lo siguiente es compararlo con el primer numero introducido por el uduario
cualquier numero que digite a menos que sea cero, cumplira con la condicion,
despues la variable numero_mayor guarda el valor del primer numero introducido.
Continua comparando con los siguientes numeros, si son mayores pues 
la variable se actualiza y si no se queda tal y como esta. Al final solo
se escribe la variable que contiene el valor mas grande."""