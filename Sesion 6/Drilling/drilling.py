'''
EJERCICIOS:
Realiza los pasos que se exponen a continuación:
1.- Se da el siguiente diccionario:
1 usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}

2.- Intente imprimir el valor de la clave:
1 id_usuario = '004'

3.- En caso de KeyError, imprima en la consola el siguiente mensaje:
'La clave 004 no está en el diccionario. Añadiendo clave...'

4.- Luego, agregue esta clave al diccionario con el valor “Ninguno”, e imprima el diccionario de
usuarios en la consola.

Resultado Esperado:
La clave 004 no está en el diccionario. Agregando clave...
{'001': 'Marca', '002': 'Mónica', '003': 'Jacob', '004': Ninguno}

Partiendo del siguiente código en Python:
usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
id_usuario = '004'
'''
usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
mssg = 'La clave 004 no esta en el diccionario. Agregando clave...'
id_usuario = '004'
try:
    print(usuarios[id_usuario])
except KeyError:
    print(mssg)
    usuarios[id_usuario] = None

print(usuarios)