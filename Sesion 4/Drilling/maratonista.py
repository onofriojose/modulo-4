from persona import Persona


class Maratonista(Persona):
    def __init__(self, nombre, estado) -> None:
        super().__init__(nombre, estado)
        