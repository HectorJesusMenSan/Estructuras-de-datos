"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 13 de enero del 2025
Descripción: Bibliotecas como en c
"""

from Saludar_modulo import Saludar


#El codigo va dentro de esta condicional
if __name__ == '__main__':
    nombre_de_Usuario = input("Ingresa tu nombre: ")
    Saludar(nombre_de_Usuario)