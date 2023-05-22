from modelo.cliente import Cliente #importando a la clase cliente

class ClienteService:
    
    #carga de archivo, lectura y creacion si el archivo no existe
    def load_clientes(self):
        try:
            with open('clientes.txt', 'r') as file:
                file.readlines() #retrorna una lista de tipo str
        except FileNotFoundError: #si ocurre el error de archivo no existe, se procede a crearlo
            print('Error! Loading Client')
    

    
    #metodo para crear clientes
    def crear_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        rut = input("Ingrese el rut del cliente: ")
        descuento = input("Ingrese el descuento del cliente: ")

        #para crear un supervisor se realiza una instancia de su constructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(f"Cliente creado exitosamente: {cliente}")
        return cliente
