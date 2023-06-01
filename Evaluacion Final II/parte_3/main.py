from bicicleta import Bicicleta
from motocicleta import Motocicleta
from carga import Carga
from particular import Particular
from vehiculo import Vehiculo
from automovil import Automovil

        
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
'''
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print(f'Motocicleta es instancia con relacion a Vehiculo: {isinstance(motocicleta, Vehiculo)}')
print(f'Motocicleta es instancia con relacion a Automovil: {isinstance(motocicleta, Automovil)}')
print(f'Motocicleta es instancia con relacion a Vehiculo Particular: {isinstance(motocicleta, Particular)}')
print(f'Motocicleta es instancia con relacion a Vehiculo de Carga: {isinstance(motocicleta, Carga)}')
print(f'Motocicleta es instancia con relacion a Bicicleta: {isinstance(motocicleta, Bicicleta)}')
print(f'Motocicleta es instancia con relacion a Motocicleta: {isinstance(motocicleta, Motocicleta)}')
'''
automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
particular.guardar("ejemplo.csv")
carga.guardar('ejemplo.csv')
bicicleta.guardar("ejemplo.csv")
motocicleta.guardar("ejemplo.csv")
automoviles = automovil.recuperar("ejemplo.csv")

print('Lista de Vehiculos Particular')
for automovil in automoviles:
    if automovil[0] == "<class 'particular.Particular'>":
        print(automovil)
print('\n')

print('Lista de Vehiculos Carga')
for automovil in automoviles:
    if automovil[0] == "<class 'carga.Carga'>":
        print(automovil)
print('\n')
        
print('Lista de Vehiculos Bicicleta')
for automovil in automoviles:
    if automovil[0] == "<class 'bicicleta.Bicicleta'>":
        print(automovil)
print('\n')
        
print('Lista de Vehiculos Motocicleta')
for automovil in automoviles:
    if automovil[0] == "<class 'motocicleta.Motocicleta'>":
        print(automovil)
print('\n')