"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 15 de enero del 2025
Descripción: Bibliotecas como en c
"""
def imprimir_alumno (nombre: str, edad: int, matricula: str, grupo: int, semestre: int) -> None:
    """
    Funcion que imprime los dats personales del usuario
    :param nombre:
    :param edad:
    :param matricula:
    :param grupo:
    :param semestre:
    :return:
    """
    print("-Estos son los datos personales: \n")
    print(f"-Nombre:  {nombre}\n"
          f"-Edad: {edad}\n"
          f"-Matricula:  {matricula}\n"
          f"-Grupo: {grupo}\n"
          f"-Semestre: {semestre}\n")


def main() -> None:
    nombre, edad, matricula, grupo, semestre = "Hector", 19, 123213123, 303, 3
    imprimir_alumno(nombre, edad, matricula, grupo, semestre)

if __name__ == '__main__':
    main()
