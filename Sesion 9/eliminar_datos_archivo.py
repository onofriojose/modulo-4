def eliminar_datos_archivo():
    try:
        archivo = open('datos.cvs', 'w')  # Abre el archivo 'datos.cvs' en modo escritura
        archivo.close()  # Cierra el archivo
    except FileNotFoundError:  # Captura la excepción si el archivo no se encuentra
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:  # Captura cualquier otra excepción
        print('Se ha generado un error no previsto', type(error).__name__)
    finally:  # Bloque opcional que siempre se ejecuta, sin importar si hay una excepción o no
        print("Se ha eliminado todos los datos del archivo exitosamente")

eliminar_datos_archivo()  # Llama a la función para eliminar los datos del archivo

'''
En resumen:

La función eliminar_datos_archivo() se define para eliminar todos los datos de un archivo.
Se utiliza un bloque try-except-finally para manejar posibles excepciones.
En el bloque try, se abre el archivo 'datos.cvs' en modo escritura utilizando el modo 'w'.
Luego, se cierra el archivo utilizando el método close().
Si ocurre la excepción FileNotFoundError, se imprime el mensaje "No se encuentra el archivo datos.cvs".
Si ocurre cualquier otra excepción, se imprime un mensaje genérico indicando que se ha generado un error no previsto, junto con el nombre de la excepción.
El bloque finally es opcional y siempre se ejecuta, sin importar si se produjo una excepción o no. En este caso, se imprime el mensaje "Se ha eliminado todos los datos del archivo exitosamente".
Finalmente, se llama a la función eliminar_datos_archivo() para ejecutar el proceso de eliminación de datos del archivo.
'''