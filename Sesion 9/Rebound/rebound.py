'''
Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE:
Apertura de archivos.
EJERCICIO:
Diseñe un programa en Python que agregue el siguiente contenido al archivo: informacion.dat.
Hola Mundo
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada

El nuevo archivo contiene la siguiente información:

Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada
'''
#En caso que informacion.dat no exista debe ejecutartse 2 veces, una para crear archivo y otra para agregar la informacion extra
def agregar_datos():
    try:
        with open('informacion.dat', 'x') as file:
            file.write('Datos de informacion en la línea 1\n'
                           'Datos de informacion en la línea 2\n'
                           'Datos de informacion en la línea 3\n'
                           'Datos de informacion en la línea 4\n'
                           'Datos de informacion en la línea 5')
            
    except FileExistsError:
        with open('informacion.dat', 'a') as file:
            file.write('\nHola Mundo\n'
                       'Este en una nueva línea en el archivo\n'
                       'agregando la segunda línea del archivo\n'
                       'finalizando la línea agregada')
    
    except Exception as e:
        print('Error imprevisto', type(e).__name__)

agregar_datos()
with open('informacion.dat', 'r') as file:
    print(file.read())
file.close