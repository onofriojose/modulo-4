from io import open

def crear_archivo():
    try:
        archivo = open('datos.cvs', 'x')
        archivo.close()
    except FileExistsError:
        print('El archivo datos.cvs ya existe')
    except Exception as error:
        print('Se ha generado un error imprevisto', type(error).__name__)        

crear_archivo()