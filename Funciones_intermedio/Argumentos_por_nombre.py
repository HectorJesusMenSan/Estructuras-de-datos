"""
Nombre: Héctor Jesús Méndez Santiago
Fecha: 15 de enero del 2025
Descripción: Bibliotecas como en c
"""
#Despues del asterisco se tiene que escribir forzosamente el mismo nombre en la llamada.
def imprimir_alumno (nombre: str, edad: int, matricula: str, grupo: int,*, semestre: int= 3) -> None: #Inicializa valores en funcion, por si no le mandamos nada en el menu.
    """
    Funcion que imprime los dats personales del usuario
    :param nombre: Nombre de un usuario.
    :param edad: Edad del usuario.
    :param matricula: Matricula delalumno.
    :param grupo: Grupo del alumno.
    :param semestre: Semestre que cursa el alumno.
    :return: No retorna nada.
    """
    print("-Estos son los datos personales: \n")
    print(f"-Nombre:  {nombre}\n"
          f"-Edad: {edad}\n"
          f"-Matricula:  {matricula}\n"
          f"-Grupo: {grupo}\n"
          f"-Semestre: {semestre}\n")


def main() -> None:
    nombre, edad, matricula, grupo, semestre = "Hector", 19, 123213123, 303, 3
    imprimir_alumno(nombre, edad, matricula,grupo ,semestre )

    #Manda "Argumentos por nombre"
    imprimir_alumno(nombre="Albertano", edad=19, matricula=123232, semestre="4", grupo="303")

    #Despues del aterisco le tenemos llevar la misma palabra sino no agarra.
    imprimir_alumno("jss", 31, "123", 3,  semestre = 12 )



if __name__ == '__main__':
    main()
