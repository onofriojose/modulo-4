from modelo.automovil import Automovil
class AutomovilService:
    def __init__(self) -> None:
        with open('vehiculos.dat', 'a') as self._automoviles:
            pass
    def insertar_vehiculos(self):
        self._automoviles = []
        crear = int(input('Cuantos vehiculos desea insertar: '))
        for i in range(crear):
            print(f'Datos del automovil {i+1}')
            marca = input(f'Insertar marca del vehiculo {i+1}: ')
            modelo = input(f'Insertar modelo del vehiculo {i+1}: ')
            nro_ruedas = input(f'Insertar numero de ruedas del vehiculo {i+1}: ')
            velocidad = input(f'Insertar velocidad del vehiculo {i+1}: ')
            cilindrada = input(f'Insertar cilindrada del vehiculo {i+1}: ')
            vehiuculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
            self._automoviles.append(vehiuculo)
            with open('vehiculos.dat', 'a') as file:
                file.write(str(vehiuculo))
        num = 0
        
        for linea in self._automoviles:
            num = num+1
            print(f'Datos del vehiculo {num}: {linea}')
        