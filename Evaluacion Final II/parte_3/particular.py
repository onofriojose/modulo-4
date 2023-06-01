from automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puesto) -> None:
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self._nro_puesto = nro_puesto
    
    @property
    def nro_puesto(self):
        return self._nro_puesto
        
    @nro_puesto.setter
    def nro_puesto(self, nro_puesto):
        self._nro_puesto = nro_puesto
    
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc, Puestos: {self.nro_puesto}'