#creando la clase animal
class Animal:
    def __init__(self, nombre, edad, raza, peso) -> None:
        self._nombre = nombre
        self._edad =  edad
        self._raza = raza
        self._peso = peso
    def __str__(self) -> str:
        return f'{self._nombre} tiene {self._edad} años con {self._peso}Kg y es un {self._raza}'
    
#instaciando objetos con la clase animal
caballo = Animal('Zeus', 5, 'Pura Sangre', 450)
leon = Animal('Boulder', 10, 'Atlas', 130)

print(caballo)
print(leon)