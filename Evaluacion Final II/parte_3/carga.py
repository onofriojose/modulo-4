from automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso) -> None:
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self._peso = peso
        
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        self._peso = peso
        
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc, Puestos: {self.peso} Kgs'