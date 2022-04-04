from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None, grado= "Grado 12"):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self._listaAsignaturas = []
        self._listadoAlumnos = estudiantes
        Grupo.grado = grado

    def listadoAsignaturas(self, *args, **kwargs):
        for x in kwargs.values():
            # self._asignaturas.append(Asignatura(x))
            self._listaAsignaturas.append(Asignatura(x))
        return self._listaAsignaturas

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self._listadoAlumnos = self._listadoAlumnos + lista
        else:
            self._listadoAlumnos = lista + [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre