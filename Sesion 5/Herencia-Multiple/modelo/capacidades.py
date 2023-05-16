class Capacidades:
    def __init__(self, ncertificado, raiting) -> None:
        self._ncertificado = ncertificado
        self._raiting = raiting
    
    @property
    def ncertificadoget(self):
        return self._ncertificado
    
    @ncertificadoget.setter
    def ncertificado(self, ncertificado):
        self._ncertificado = ncertificado

    @property
    def raitingget(self):
        return self._raiting
    
    @raitingget.setter
    def raiting(self, raiting):
        self._raiting = raiting


    def imprimir_capacidades(self):
        print(f'Numero de certificados: {self.ncertificado} \n Raiting: {self.raiting}')