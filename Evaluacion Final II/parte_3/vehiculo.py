import csv
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas) -> None:
        self._marca = marca
        self._modelo = modelo
        self._nro_ruedas = nro_ruedas
    
    def guardar(self, nombre_archivo):
        try:
            archivo = open(nombre_archivo, "a+", newline='')
            datos = [(self.__class__, self.__dict__)]
            archivo_csv = csv.writer(archivo) #creando instancia de libreria csv para poder escribir
            archivo_csv.writerows(datos)
            archivo.close()
        except FileNotFoundError:
            print('Error: File not found: ', nombre_archivo)
        except Exception as error:
            print('Se ha generado un error imprevisto', type(error).__name__)   
            
    def recuperar(self, nombre_archivo): 
        vehiculos = [] 
        archivo = open(nombre_archivo, "r") 
        archivo_csv = csv.reader(archivo, lineterminator= '\n') 
        for vehiculo in archivo_csv: 
            vehiculos.append(vehiculo)
        archivo.close() 
        return vehiculos
    #getters y setter para marca
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    #getters y setter para modelo    
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    #getters y setter para nro_ruedas
    @property
    def nro_ruedas(self):
        return self._nro_ruedas
    @nro_ruedas.setter
    def nro_ruedas(self, nro_ruedas):
        self._nro_ruedas = nro_ruedas
    