'''
EJERCICIOS:
Partiendo del ejercicio anterior (Rebound Exercises), construya una función que reemplace el
contenido de “Información” por “Procesamiento”, e imprima cuántos reemplazos realizó en el
archivo.
'''

def reemplazar_datos_archivo(texto_viejo, texto_nuevo):
    try:
        contador = 0
        archivo = open('informacion.dat', 'r')  
        reemplazo = '' 
        for linea in archivo:  
            linea = linea.strip() 
            if texto_viejo in linea:
                contador = contador + 1
            cambios = linea.replace(texto_viejo, texto_nuevo)  
            reemplazo = reemplazo + cambios + '\n'  
        archivo.close()  

        archivo_reemplazo = open('informacion.dat', 'w')  
        archivo_reemplazo.write(reemplazo) 
        archivo_reemplazo.close()  
    except FileNotFoundError:
        print('No se encuentra el archivo informacion.dat')  
    except Exception as error:
        print('Ha ocurrido un error no previsto: ', type(error).__name__) 
    finally:
        print(f'Se ha reemplazado {texto_viejo} {contador} veces satisfactoriamente')  

reemplazar_datos_archivo('informacion', 'Procesamiento') 
