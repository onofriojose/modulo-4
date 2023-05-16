<<<<<<< HEAD
from modelo.cliente import Cliente #importando a la clase cliente

class ClienteService:
    def crear_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        rut = input("Ingrese el rut del cliente: ")
        descuento = input("Ingrese el descuento del cliente: ")

        #para crear un supervisor se realiza una instancia de su constructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(f"Cliente creado exitosamente: {cliente}")
        return cliente
=======
from modelo.cliente import Cliente #importando a la calase supervisor

class ClienteService:
    def crear_cliente(self):
        nombre = input('ingrese el nombre del cliente')
        apellido = input('Ingrese el apellido del cliente')
        rut = input('Ingrese el rut del cliente')
        descuento= input('Ingrese el area del cliente')
        
        #para crear un sssupervisor se realia una instancia de su constructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(f'Cliente creado: {cliente}')
>>>>>>> bb757d60f14d3adf3258a41b7dc2d1885891ad2f
