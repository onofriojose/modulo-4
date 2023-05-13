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

    
#crando una instancia de la clase vehiculo
vehiculo_uno = vehiculo("Mazda","Blanco","M3",2000,2.5,2.0)
vehiculo_dos = vehiculo('BMW','Gris','M4',800,2.1,1.5)
vehiculo_tres = vehiculo()

#accedciendo a los atributos del objeto vehiculo
print(vehiculo_uno.marca)#Mazda
print(vehiculo_uno.color)
print(vehiculo_uno.modelo)
print(vehiculo_uno.peso)
print(vehiculo_uno.ancho)
print(vehiculo_uno.alto)

#cambiar los valores de los atributos del objeto llamado vehiculo_uno
vehiculo_uno.marca = "Toyota"
vehiculo_uno.color = "Negro"
vehiculo_uno.modelo = "Camry"
vehiculo_uno.peso = 1000
vehiculo_uno.ancho = 2.0
vehiculo_uno.alto = 1.5
print(vehiculo_uno.marca)#Toyota


#asignar los valores al objeto vehiculo llamado vehiculo_tres
vehiculo_tres.marca = 'VW'
vehiculo_tres.color = 'Rosado'
