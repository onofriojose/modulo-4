'''
EJERCICIOS:
1.Defina una clase que contiene el objeto Persona con un solo atributo nombre. Luego, se crean dos subclases:Maratonista y Ciclista,que pertenecen a la clase Persona.
2.Cada Clase contiene un método que se llama movimiento. Para el caso dela Persona, el estado de movimiento es “caminando”,para el caso del Maratonista es “trotando”, y para el caso del Ciclista es “rodando”.
3.Diseñe la clase en Python que reflejela herencia antes descrita.
'''

class Persona:
    def __init__(self, nombre, estado) -> None:
        self._nombre = nombre
        self._estado = estado
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre= nombre
        
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        self._estado = estado
        
        
    def movimiento(self, accion):
        print(f'{self._nombre} = {accion}')
        self._estado = accion
        
        