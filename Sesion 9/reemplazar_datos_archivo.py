def reemplazar_datos_archivo(texto_viejo, texto_nuevo):
    try:
        archivo = open('datos.cvs', 'r')  # Abre el archivo 'datos.cvs' en modo lectura
        reemplazo = ''  # Variable para almacenar las líneas modificadas del archivo
        for linea in archivo:  # Recorre cada línea del archivo
            linea = linea.strip()  # Elimina los espacios en blanco al inicio y final de la línea
            cambios = linea.replace(texto_viejo, texto_nuevo)  # Reemplaza el texto viejo por el nuevo en la línea
            reemplazo = reemplazo + cambios + '\n'  # Almacena la línea modificada en la variable de reemplazo
        archivo.close()  # Cierra el archivo (importante cerrar después de abrirlo)

        archivo_reemplazo = open('datos.cvs', 'w')  # Abre el archivo 'datos.cvs' en modo escritura
        archivo_reemplazo.write(reemplazo)  # Escribe el contenido modificado en el archivo
        archivo_reemplazo.close()  # Cierra el archivo de reemplazo
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')  # Manejo de excepción si el archivo no se encuentra
    except Exception as error:
        print('Ha ocurrido un error no previsto: ', type(error).__name__)  # Manejo de excepción genérica
    finally:
        print('Se ha reemplazado satisfactoriamente')  # Se imprime un mensaje al final, haya ocurrido o no una excepción

reemplazar_datos_archivo('linea', 'LINEA')  # Llama a la función para reemplazar los datos en el archivo
