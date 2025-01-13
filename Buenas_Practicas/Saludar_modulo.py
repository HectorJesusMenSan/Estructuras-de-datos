

def Saludar(nombre : str) -> None:
    """
    Funcion que imprime la variable, qe almacena una variable de
    tipo string solicitada al usuario.
    :param nombre: Es el nombre de la variable recibido
    :return: No retorna nada
    """
    print(f"Hola {nombre}")

#_______________________________________________________________________________________________
if __name__ == '__main__':

    nombre = input("Escrube un nombre:")
    Saludar(nombre)