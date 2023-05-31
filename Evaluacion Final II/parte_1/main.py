from automovil import Automovil
def insertar_vehiculos():
    automoviles = []
    crear = int(input('Cuantos vehiculos desea insertar: '))
    for i in range(1, crear+1):
        print(f'Datos del automovil {i}')
        marca = input(f'Insertar marca del vehiculo {i}: ')
        modelo = input(f'Insertar modelo del vehiculo {i}: ')
        nro_ruedas = input(f'Insertar numero de ruedas del vehiculo {i}: ')
        velocidad = input(f'Insertar velocidad del vehiculo {i}: ')
        cilindrada = input(f'Insertar cilindrada del vehiculo {i}: ')
        vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        automoviles.append(vehiculo)

    num = 0
        
    for linea in automoviles:
        num = num+1
        print(f'Datos del vehiculo {num}: {linea}')

insertar_vehiculos()