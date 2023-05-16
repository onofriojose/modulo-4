from persona import Persona
from ciclista import Ciclista
from maratonista import Maratonista

persona_1 = Persona('Onofrio', '')
persona_1.movimiento('Caminando')
print(persona_1.estado)

ciclista = Ciclista('Raul', '')
print(ciclista.estado)
ciclista.movimiento('rodando')
print(ciclista.estado)
print('=============================')
maratonista = Maratonista('Ezio', '')
maratonista.movimiento('trotando')

