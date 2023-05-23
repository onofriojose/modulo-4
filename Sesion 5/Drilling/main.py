from trabajador import Trabajador
from persona import Persona
from departamento import Departamento

def conocer_instancia(objeto, objeto_comparar):#metodo personalizado para cambiar el booleano por una respuesta personalizada cuando se usa isinstamce
    resultado = 'Si' if isinstance(objeto, objeto_comparar) else 'No'
    return resultado  #operador ternario

if __name__ == '__main__':
      trabajador = Trabajador('Juan', 'Perez', 2005, 'Ingenieria de Software', 'IS')
      print(trabajador)
      trabajador.salario = 20_000
      print(trabajador.__dict__)
      #es trabajador una instancia de tipo Persona
      print('es trabajador una instancia de Persona?: ', conocer_instancia(trabajador, Persona))
      print('es trabajador una instancia de Departamento?: ', conocer_instancia(trabajador, Departamento))
      print('es trabajador una instancia de Trabajador?: ', conocer_instancia(trabajador, Trabajador))
      
  