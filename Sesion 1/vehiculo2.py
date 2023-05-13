class vehiculo:
    #constructor con parametros para realizar una instancia de la clase vehihulo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 0
        self.marcha = False
    
    #getter/setter son funciones para obtener o dar valor a los atributos
    #getters
    def get_marca(self):
        return self.marca
    
    def get_color(self):
        return self.color
    
    #setters
    def set_color(self, color):
        self.color = color
        
    def set_marca(self, marca):
        self.marca = marca
        
    #funciones que realiza el objeto a traves de la instancia 
    def acelerar(self):
        if  self.marcha:
            self.velocidad += 10
            return f"Vehiculo de marca {self.marca} esta en marcha a {self.velocidad}Km/h"
        else:
             return f"Vehiculo de marca {self.marca} esta apagado"
    
    def frenar(self):
        if self.marcha and self.velocidad > 0:
            self.velocidad -= 10
            return f"Vehiculo de marca {self.marca} y {self.modelo} esta frenando"
        else:
            f'El vehiculo de marca {self.marca} y {self.modelo} ya esta detenido'
               
    def girar_izquierda(self):
        if self.marcha:
            return f"Vehiculo de marca: {self.marca} y {self.modelo} esta girando a la izquierda"
        else:
            return f"Vehiculo debe estar en marcha"
        
    def girar_derecha(self):
        if self.marcha:    
            return f"Vehiculo de marca: {self.marca} y {self.modelo} esta girando a la derecha"
        else:
            return f"Vehiculo debe estar en marcha"
    
    def apagar(self):
        if self.marcha:
            self.marcha = False
            return f"Vehiculo de marca {self.marca} y {self.modelo} se ha apagado"
        else:
            return f"Vehiculo de marca {self.marca} y {self.modelo} ya esta apagado"
        
    def encender(self):
        if not self.marcha:
            self.marcha = True
            return f'el vehiculo se ha encendido'
        else:
            f'El vehiculo de marca {self.marca} y {self.modelo} ya esta encendido'
            
    def retroceder(self):
        if self.marcha:
            self.velocidad -= 10
            return f'El vehiculo {self.marca} esta en retroceso'
        else:
            return f'El vehiculo {self.marca} esta en apagado'
#Instaciar vehiculos para realizar las acciones mediante sus funciones o metodos        
mazda = vehiculo('Mazda','Blanco','M4',2000,2.5,2)#encendido = False

#cambiar el comportamiento mediante las funciones accediendo desde la instancia a las funciones
print(mazda.encender())#encendido = True
print(mazda.acelerar())
print(mazda.retroceder())

#get obtener el valor del atributo a traves de notracion de puntos
print(mazda.color)
print(mazda.get_color())

#setear
mazda.color = 'Azul'
mazda.set_color('Rosado')
print(mazda.get_color())