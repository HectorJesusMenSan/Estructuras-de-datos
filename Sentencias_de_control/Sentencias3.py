"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    Tercer programa para ejercitar la habilidad con las sentencias

Este programa determinará un descuento en compras en "La cona", de acuerdo a lo siguiente:

    Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
    Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
    Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.

Para ello:

a) Solicite al usuario la cantidad comprada en la tienda.

b) Pregunte al usuario si cuenta con la membresía (Si/No).

c) Utilice la lógica adecuada para determinar el total a pagar.

d) Muestre el descuento y el total a pagar en consola utilizando dos decimales.
"""

# Solicitud de datos
print("CARGANDO...")
cantidad_de_la_compra = float(input("Ingrese la cantidad de sus compras: "))                  # Almacena y convierte datos a tipo flotante.
membresia = input("¿Usted cuenta con la membresía? (Sí/No) ")                                      # Pregunta si tiene membresía.
membresia = membresia.lower() == "si"                                                                     # Convierte a minúsculas y a booleano.

# Sentencias y condiciones:
if membresia:                                                     # Si el valor de la membresía es True se ejecutan las acciones.
    if cantidad_de_la_compra >= 1000.00:                                                                # Si la cantidad es mayor o igual a 1000...
        cantidad_de_la_compra = cantidad_de_la_compra - ((cantidad_de_la_compra * 8) / 100)             # Saca el 8% de la cantidad de la compra y lo descuenta.
        print(f"Se le hizo un descuento del 8%, el total a pagar es ${cantidad_de_la_compra:.2f}")      # Imprime resultados.
    else:
        cantidad_de_la_compra = cantidad_de_la_compra - ((cantidad_de_la_compra * 5) / 100)             # Aplica un 5% de descuento.
        print(f"Se le hizo un descuento del 5%, el total a pagar es ${cantidad_de_la_compra:.2f}")      # Imprime resultados.
else:                                                             # Si el valor de membresía es False, entonces ejecuta las siguientes acciones.
    print("Se le invita a formar parte de la membresía, para obtener un descuento de hasta el 8%.")
