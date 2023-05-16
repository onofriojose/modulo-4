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
        Capacidades.imprimir_capacidades(self)
        print(f'Promedio: {self._promedio}')
    
    def __str__(self): #funcion para imprimir el objeto string en cualquier structura
        #return super().__str__() se comenta para definir un retorno personalizado para la clase supervisor
        return f'Supervisor(nombre= {self._nombre}, apellido= {self._apellido}, rut= {self._rut}, area= {self._area}, certificados= {self._ncertificado}, raiting= {self._raiting}, promedio= {self._promedio} )'