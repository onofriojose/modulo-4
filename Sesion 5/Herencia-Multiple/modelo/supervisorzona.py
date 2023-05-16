from modelo.supervisor import Supervisor
from modelo.capacidades import Capacidades

class SupervisorZona(Supervisor, Capacidades):
    def __init__(self, nombre, apellido, rut, area, ncertificado, raiting, promedio):
        Supervisor.__init__(self, nombre, apellido, rut, area)
        Capacidades.__init__(self, ncertificado, raiting)
        self._promedio = promedio
    
    @property
    def promedio(self):
        return self._promedio
    
    @promedio.setter
    def promedio(self, promedio):
        self._promedio = promedio

    def imprimir_supervisor_zona(self):
        SupervisorZona.imprimir_supervisor(self)
        Capacidades.imprimir_capacidades(self)
        print(f'Promedio: {self._promedio}')