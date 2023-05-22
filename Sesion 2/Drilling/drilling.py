'''
EJERCICIO:Implementar en Python la clase Persona, que tenga como atributos: nombre, apellidos, sexo, edad, estatura y peso. Adicionalmente,se debenimplementarlos métodos get y set que modifiquentodos los atributos antes mencionados de la clase persona, recordando que los métodos get son los métodos que permitenacceder al estado del objeto persona, y los métodos set permitenmodificar el estado de dicho objeto. Cree dos objetos de la instancia persona con los siguientes datos:Persona_ 1:  Pedro, Vivas, Masculino, 20 años, 1.78 mts, 68 Kg.Persona_ 2:  Juan, Camargo, Masculino. 18, 1.8 mts, 75 Kg.Modifique en la Persona_1 su edad a 21 años, y a la Persona_2 el apellido a Santiago, y que se muestre por pantalla las actualizaciones respectivas. 
'''
class Persona:
    def __init__(self, nombre, apellido, genero, edad, estatura, peso):
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad
        self._estatura = estatura
        self._peso = peso
        
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
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def estatura(self):
        return self._estatura
    
    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        self._peso = peso
    
    def __str__(self):
        return f'Persona(nombre= {self.nombre}, apellido= {self.apellido}, genero= {self.genero}, edad= {self.edad}, estatura= {self.estatura}, peso= {self.peso})'
    
persona_1 = Persona('Pedro', 'Vivas', 'Masculino', 20, 1.78, 68)
persona_2 = Persona('Juan', 'Camargo', 'Masculino', 18, 1.18, 75)

#Persona 1
print(f'El nombre de persona 1 es {persona_1.nombre} y su apellido es {persona_1.apellido}')
#imprimimos persona a traves del metodo definido por __str__
print(persona_1)
persona_1.nombre = 'Fulanito'
print(persona_1.edad) #usando getter
persona_1.edad = 21 #usando setter /// Modificando la edad de persona 1 a 21
print(persona_1.edad) #mostrando nuevo valor

print('==================================================================')

#Persona 2
print(f'El nombre de persona 2 es {persona_2.nombre} y su apellido es {persona_2.apellido}')
#imprimimos persona a traves del metodo definido por __str__
print(persona_2)
persona_2.apellido = 'Santiago' # /// Modificando el apellido de persona 2 a Santiago
print(persona_2.apellido) #usando getter /// 
persona_2.edad = 21 #usando setter
print(persona_2.edad) #mostrando nuevo valor