def lectura_archivo():
    try:
        archivo = open('datos.cvs', 'r')
        contenido = archivo.read()
        #contenido = archivo.readlines()
        archivo.close()
        print(contenido)
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)

lectura_archivo()