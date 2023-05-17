from modelo.persona import Persona

class Supervisor(Persona):
    def __init__(self, nombre, apellido, rut, area): #constructor
        super().__init__(nombre, apellido, rut) #atributos de la super clase
        self._area = area #atributo agregado a la clase o sub clase suprvisor
        
    @property
    def area(self):
        return self.area
    
    @area.setter
    def area(self, area):
        self._area = area

    def imprimir_supervisor(self):
        print(f'Supervisor(nombre= {self._nombre}, apellido= {self._apellido}, rut= {self._rut}, area= {self._area} )')
    
    def __str__(self): #funcion para imprimir el objeto string en cualquier structura
        #return super().__str__() se comenta para definir un retorno personalizado para la clase supervisor
        return f'Supervisor(nombre= {self._nombre}, apellido= {self._apellido}, rut= {self._rut}, area= {self._area} )'