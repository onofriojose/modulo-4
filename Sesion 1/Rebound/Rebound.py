class Animal:
    #constructor con parametros
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def caminar(self):
        print(f'El animal  {self.nombre} esta caminando')

    def comer(self):
        print(f'El animal de raza {self.raza} esta comiendo')

    def dormir(self):
        print(f'El animal de edad {self.edad} esta durmiendo')


#definir una instancia animal para un objeto llamado perro
perro = Animal('Brando','San Bernardo',3,2.5)
#definir una instancia animal para un objeto llamado perro
gato = Animal('Roll','Persa',4,3.0)


gato.comer()
perro.dormir()
