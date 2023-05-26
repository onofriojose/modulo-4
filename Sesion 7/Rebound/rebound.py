'''
Diseñe un programa en Python que pida la edad al usuario por consola. El usuario debe ingresar
un número entero; en caso contrario, el programa arrojará una excepción y le solicitará que
ingrese su edad nuevamente.
Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en caso
contrario, no es un adulto.
'''
edad = 0

while True:
    try:
        edad = int(input('Ingrese edad: '))
        break  # sale del bucle si se ingresó un número entero correctamente
    except ValueError:
        print('El valor ingresado no es un número entero. Inténtelo nuevamente.')

if edad >= 18:
    print('Es un adulto.')
else:
    print('No es un adulto.')