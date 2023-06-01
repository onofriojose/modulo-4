from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nroRadios, cuadros, motor) -> None:
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self._nroRadios = nroRadios
        self._cuadros = cuadros
        self._motor = motor

    @property
    def nroRadios(self):
        return self._nroRadios
    
    @nroRadios.setter
    def nroRadios(self, nroRadios):
        self._nroRadios = nroRadios

    @property
    def cuadros(self):
        return self._cuadros
    
    @cuadros.setter
    def cuadros(self, cuadros):
        self._cuadros = cuadros

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self._motor}T, Cuadro: {self.cuadros}, Nro Radios: {self.nroRadios}'