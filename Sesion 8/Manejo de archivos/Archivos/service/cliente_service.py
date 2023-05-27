from modelo.cliente import Cliente #importando a la clase cliente

class ClienteService:
    #constructor
    def __init__(self) -> None:
        #clienteService tiene una lista de cliente como atributo para que la lista persista en la ejecucion
        self._clientes = self.load_clientes()
    #carga de archivo, lectura y creacion si el archivo no existe
    def load_clientes(self):
        try:
            with open('clientes.txt', 'r') as file:
                clientes = file.readlines() #retrorna una lista de tipo str
        except FileNotFoundError: #si ocurre el error de archivo no existe, se procede a crearlo
            clientes = []
            with open('clientes.txt','w') as file:
                file.writelines(clientes) #crear el archivo si no existe, w es para escribir
        return clientes

    #guardado d archivo, escritura sobre el archivo de la lista de clientes
    def save_clientes(self):
        with open('clientes.txt', 'w') as file:
            for cliente in self._clientes:#se recorre la lista de clientes
                file.write(str(cliente))#se va escribiendo en el archivo cliente a cliente
        
    
    #metodo para crear clientes
    def crear_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        rut = input("Ingrese el rut del cliente: ")
        descuento = input("Ingrese el descuento del cliente: ")

        #para crear un cliente se realiza una instancia de su constructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(f"Cliente creado exitosamente: {cliente}")
        
        #agregar cliente a la lista
        self._clientes.append(cliente)
        
        #guardar clientes
        self.save_clientes()
        #return cliente
    
    def list_clientes(self):
        print('Lista de clientes: ')
        for cliente in self._clientes:
            print(cliente)
