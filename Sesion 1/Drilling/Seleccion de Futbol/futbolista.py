from seleccion import SeleccionDeFutbol

class Futbolista(SeleccionDeFutbol):
    def __init__(self, id, nombre, apellido, edad, dorsal, demarcacion) -> None:
        super().__init__(id, nombre, apellido, edad)
        self._dorsal = dorsal
        self._demarcacion = demarcacion

    @property
    def dorsal(self):
        return self._dorsal
    @dorsal.setter
    def dorsal(self, dorsal):
        self._dorsal = dorsal

    @property
    def demarcacion(self):
        return self._demarcacion
    @demarcacion.setter
    def demarcacion(self, demarcacion):
        self._demarcacion = demarcacion
    
    def jugarPartido(self):
        print(f'El futbolista {self} | está jugando un partido')

    def entrenar(self):
        print(f'El futbolista {self} | está entrenando')

