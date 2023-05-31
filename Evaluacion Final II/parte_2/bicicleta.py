from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo) -> None:
        super().__init__(marca, modelo, nro_ruedas)
        self._tipo = tipo
        
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas, Tipo: {self.tipo}'