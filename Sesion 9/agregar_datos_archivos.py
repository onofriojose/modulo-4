def agregar_archivo():
    try:
        with open('datos.cvs', 'a') as archivo:
            archivo.write('\nLinea 6 agregada')
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto: ', type(error).__name__)
        
agregar_archivo()
archivo = open('datos.cvs', 'r')
contenido = archivo.read()
archivo.close()
print(contenido)
