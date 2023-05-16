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