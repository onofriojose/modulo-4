class SeleccionDeFutbol: #Construyendo la clase Seleccion de futbol que heredaran las otras clases
    def __init__(self, id, nombre, apellido, edad) -> None:
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    #Creando los getters y seters
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def __str__(self) -> str:
        return f'con id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}'
    
    #Creando los metodos de la clase SeleccionDeFutbol
    #metodo concentrarse
    def concentrarse(self):
        print(f'El miembro de la seleccion {self} se esta concentrando')
    #Metodo viajar
    def viajar(self):
        print(f'El miembro de la seleccion {self} esta viajando')