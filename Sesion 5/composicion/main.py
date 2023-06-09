from modelo.persona import Persona
from modelo.capacidades import Capacidades
from modelo.supervisor import Supervisor
from modelo.cliente import Cliente
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService
from modelo.supervisorzona import SupervisorZona

# persona = Persona('Fulanito', 'Perez', '25.101.413-2')
# print(persona)

# cliente = Cliente('Fulanita', 'Gonzalez', '25.991.453-k', 0.5)
# print(cliente)
# cliente.get_tipo()

def main():#creando instancias para poder acceder a los servicios (clases)
    menu_service = MenuService()
    cliente_service = ClienteService()
    supervisor_service = SupervisorService()

    while True:
        menu_service.imprimir_menu()#imprimiendo menu
        opcion = input('Ingrese una opcion: ')
        match opcion:
            case '1':
                cliente_service.crear_cliente()
                break
            case '2':
                supervisor_service.crear_supervisor()
                break
            case '3':
                print('Saliendo del programa')
                break
            case _:
                print('Opcion no valida')
                break

#funcion inicializadora para darle un punto de inicio al programa



#cambios

supervisor = Supervisor('Fulanito', 'Perez', '1-9', 'ventas') 
capacidades = Capacidades(5, 6)
supervisorZona = SupervisorZona(supervisor, capacidades)
print(supervisorZona.capacidades.ncertificado)
print(supervisorZona.supervisor)
supervisorZona.capacidades.imprimir_capacidades()
print('===============================================================================')
