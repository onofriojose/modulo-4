from seleccion import SeleccionDeFutbol
class Masajista(SeleccionDeFutbol):
    def __init__(self, id, nombre, apellido, edad, titulacion, annosExp) -> None:
        super().__init__(id, nombre, apellido, edad)
        self._titulacion = titulacion
        self._annosExp = annosExp
    @property
    def titulacion(self):
        return self._titulacion
    @titulacion.setter
    def titulacion(self, titulacion):
        self._titulacion = titulacion

    @property
    def annosExp(self):
        return self._annosExp
    @annosExp.setter
    def annosExp(self, annosExp):
        self._annosExp = annosExp

    #Metodo para dar masaje
    def darMasaje(self):
        print(f'El masajista {self} | esta dando un masaje')