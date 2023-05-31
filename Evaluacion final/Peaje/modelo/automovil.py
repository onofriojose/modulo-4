from modelo.vehiculo import Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada) -> None:
        super().__init__(marca, modelo, nro_ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada
    #getter y setter para velocidad
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    #getter y settter para cilindrada
    @property
    def cilindrada(self):
        return self._cilindrada
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self._cilindrada = cilindrada
    
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc'
    