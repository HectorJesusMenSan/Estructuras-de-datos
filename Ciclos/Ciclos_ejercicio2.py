"""
Nombre:         Héctor Jesús Méndez Santiago.
Fecha:          28 de octubre de 2024.
Descripción:    ciclos.
"""
"""Calcula la suma acumulativa entre dos numeros"""
numero_inicial=int(input("ingresa numero que marque el inicio:"))
numero_final=int(input("ingresa numero que marque el final: "))

sumatoria=0
print(f"La suma desde {numero_inicial} hasta {numero_final}")
while numero_inicial<=numero_final:
    sumatoria+=numero_inicial
    numero_inicial+=1

print(f"La suma final es: {sumatoria}")