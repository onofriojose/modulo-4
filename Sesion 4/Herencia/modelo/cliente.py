from modelo.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        super().__init__(nombre, apellido, rut) #invocando los atributos de la super clase
        self._descuento = descuento
    
    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento
        
    def __str__(self):
        #return super().__str__()
<<<<<<< HEAD
        return f'Cliente(nombre= {self._nombre}, apellido= {self._apellido}, rut= {self._rut}, descuento= {self._descuento}%)'
=======
        return f'Cliente(nombre= {self._nombre}, apellido= {self._apellido}, rut= {self._rut}, descuento= {self._descuento})'
>>>>>>> bb757d60f14d3adf3258a41b7dc2d1885891ad2f
