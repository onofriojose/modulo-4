'''
Implementar un juego de cartas utilizando clases. Puedes tener clases para representar las cartas, la baraja y los jugadores. Incluye métodos para repartir cartas, jugar rondas y determinar ganadores.
'''
import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Baraja:
    def __init__(self):
        palos = ["Picas", "Corazones", "Diamantes", "Tréboles"]
        valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cartas = [Carta(valor, palo) for palo in palos for valor in valores]
        '''
        Explicación de la línea:
        *self.cartas es un atributo de la instancia de la clase Baraja que almacenará todas las cartas de la baraja.
        *Carta(valor, palo) crea una instancia de la clase Carta con el valor y palo actuales.
        *La comprensión de listas anidada for palo in palos for valor in valores genera todas las combinaciones posibles de palos y valores,    creando así todas las cartas de la baraja.
        Al finalizar esta línea de código, la lista self.cartas contendrá todas las cartas de la baraja, representadas como instancias de la clase Carta, en el orden en que se generaron.
    
        Esta parte del código se encarga de crear una baraja de cartas completa, con todas las combinaciones posibles de palos y valores.
        '''
    def barajar(self):
        random.shuffle(self.cartas)

    def repartir_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def recibir_carta(self, carta):
        self.mano.append(carta)

    def jugar_carta(self):
        if len(self.mano) > 0:
            return self.mano.pop(0)
        else:
            return None

# Ejemplo de uso

baraja = Baraja()
baraja.barajar()

jugador1 = Jugador("Jugador 1")
jugador2 = Jugador("Jugador 2")

# Repartir cartas a los jugadores
for _ in range(5):
    carta = baraja.repartir_carta()
    print(carta)
