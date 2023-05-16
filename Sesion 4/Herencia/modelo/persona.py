class Persona:
    #constructor
    def __init__(self, nombre, apellido, rut):
        self._nombre = nombre
        self._apellido = apellido
        self._rut = rut
        
    #getters y setter 
    @property #variacion de get() 
    def nombre(self):
        return self._nombre
    
    @nombre.setter #variacion de set()
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter 
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self, rut):
        self._rut = rut

    def get_tipo(self):
        print(f'Soy del tipo {self}')
<<<<<<< HEAD
        return type(self)
=======
        print(type(self))
>>>>>>> bb757d60f14d3adf3258a41b7dc2d1885891ad2f
        
    #funcion para imprimir el objeto en string
    def __str__(self):
        return f'Persona(nombre= {self._nombre}, apellido= {self._apellido}, rut= {self._rut}'