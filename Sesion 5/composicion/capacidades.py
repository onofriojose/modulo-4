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
    def raiting(self):
        return self._raiting
    
    @raiting.setter
    def raiting(self, raiting):
        self._raiting = raiting

    def imprimir_capacidades(self):
        print(f'Numero de certificados: {self.ncertificado} \n Raiting: {self.raiting}')

    def __str__(self) -> str:
        return f'Numero de Certificados: {self.ncertificado}\nRaiting: {self.raiting}'