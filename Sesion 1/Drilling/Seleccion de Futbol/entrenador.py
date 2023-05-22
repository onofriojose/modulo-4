from seleccion import SeleccionDeFutbol
class Entrenador(SeleccionDeFutbol):
    def __init__(self, id, nombre, apellido, edad, idFederacion) -> None:
        super().__init__(id, nombre, apellido, edad)
        self._idFederacion = idFederacion
    @property
    def idFederacion(self):
        return self._idFederacion
    @idFederacion.setter
    def idFederacion(self, idFederacion):
        self._idFederacion = idFederacion

    #Metodo para dirigir partido
    def dirigirPartido(self):
        print(f'El Entrenador {self} | esta dirigiendo un partido')
    #Metodo para dirigir entrenamiento
    def dirigirEntrenamiento(self):
        print(f'El entrenador {self} | esta dirigiendo un entrenamiento')
