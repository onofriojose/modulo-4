from modelo.supervisor import Supervisor #importando a la calase supervisor

class SupervisorService:
    def crear_supervisor(self):
        nombre = input('ingrese el nombre del supervisor')
        apellido = input('Ingrese el apellido del supervisor')
        rut = input('Ingrese el rut del supervisor')
        area = input('Ingrese el area del supervisor')
        
        #para crear un sssupervisor se realia una instancia de su constructor
        supervisor = Supervisor(nombre, apellido, rut, area)
        print(f'Supervisor creado: {supervisor}')