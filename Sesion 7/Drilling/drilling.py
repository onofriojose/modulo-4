'''
EJERCICIOS:
Diseñe una nueva clase de excepción definida por el usuario, que gestione la entrada del valor de
una variable salario, y la misma se encuentre entre los valores de 1000 y 2000; de lo contrario, se
lanza una excepción que refleja que el salario no se encuentra en el rango de 1000 y 2000.

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
'''

class MyError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje


def calc_salario(salario):
    salario = int(salario)  # Convertir el salario a un número entero
    if 1000 <= salario <= 2000:
        print('El salario está en el rango correcto')
    else:
        raise MyError('El salario no está dentro del rango correcto')


salario = input('Ingrese salario: ')
calc_salario(salario)

