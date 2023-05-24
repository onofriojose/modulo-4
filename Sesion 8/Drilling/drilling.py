'''
EJERCICIOS:
Partiendo de la actividad realizada en el Rebound Exercises, construya una función que lea el
contenido del archivo informacion.dat.
Teniendo como salida lo siguiente:
y
El archivo informacion.dat ya existe, ha sido creado previamente
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5
'''
#no sabia que pedirian lo mismo en el drilling e hice el rebound de la misma forma como lo pide este enunciado, por lo que solo copie el codigo y cambie el mensaje de salida.

from io import open
def crear_archivo():
    try:
        archivo = open('informacion.dat', 'x') #crea el archivo y escribe el contenido en caso que no existe. Debo volver a correr el codigo para imprimir el contenido
        archivo.writelines('Datos de información en la línea 1\n'
                           'Datos de información en la línea 2\n'
                           'Datos de información en la línea 3\n'
                           'Datos de información en la línea 4\n'
                           'Datos de información en la línea 5')
        print(archivo.read)
        archivo.close()
    except FileExistsError:
        print('El archivo informacion.dat ya existe, ha sido creado previamente')
        archivo = open('informacion.dat', 'r')
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except Exception as error:
        print('Se ha generado un error imprevisto', type(error).__name__)        

crear_archivo()

