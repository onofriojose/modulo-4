'''
EJERCICIO:
Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el 
archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente 
creado. 
El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente:
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5  

'''
from io import open
def crear_archivo():
    try:
        archivo = open('informacion.dat', 'x') #crea el archivo y escribe el contenido en caso que no existe. Debo volver a correr el codigo para imprimir el contenido
        archivo.writelines('Datos de informacion en la línea 1\n'
                           'Datos de informacion en la línea 2\n'
                           'Datos de informacion en la línea 3\n'
                           'Datos de informacion en la línea 4\n'
                           'Datos de informacion en la línea 5')
        print(archivo.read)
        archivo.close()
    except FileExistsError:
        print('El archivo informacion.dat ya existe')
        archivo = open('informacion.dat', 'r')
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except Exception as error:
        print('Se ha generado un error imprevisto', type(error).__name__)        

crear_archivo()

