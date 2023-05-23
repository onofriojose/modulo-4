'''
Diseñe un programa en Python que pida la edad al usuario por consola. El usuario debe ingresar
un número entero; en caso contrario, el programa arrojará una excepción y le solicitará que
ingrese su edad nuevamente.
Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en caso
contrario, no es un adulto.
'''

class MiError(Exception):
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - Código: {self.codigo}"

def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por 0", 805)
    return 5 / n


try:
    division()
except MiError as e:
    print(e)
edad = int
while True:
    try:
        edad = input('Ingrese edad: ')
    except ValueError:
        