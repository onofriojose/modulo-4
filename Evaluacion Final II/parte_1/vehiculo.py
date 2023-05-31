class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas) -> None:
        self._marca = marca
        self._modelo = modelo
        self._nro_ruedas = nro_ruedas
    #getters y setter para marca
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    #getters y setter para modelo    
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    #getters y setter para nro_ruedas
    @property
    def nro_ruedas(self):
        return self._nro_ruedas
    @nro_ruedas.setter
    def nro_ruedas(self, nro_ruedas):
        self._nro_ruedas = nro_ruedas