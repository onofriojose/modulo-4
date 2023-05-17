'''
Crear una clase para representar una biblioteca, con métodos para agregar y buscar libros, y atributos para almacenar información sobre los libros (título, autor, etc.).
'''

class Libro:
    def __init__(self, titulo, autor, anno) -> None:
        self._titulo = titulo
        self._autor = autor
        self._anno = anno
    #getter y setter para titulo
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    #getter y setter para autor
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor
    #getter y setter para año
    @property
    def anno(self):
        return self._anno
    @anno.setter
    def anno(self, anno):
        self._anno = anno
    
    def __str__(self) -> str:
        return f'Libro creado exitosamente! \nsdfsadfNombre: {self.titulo}\nAutor: {self.autor}\nAño: {self.anno}'
    #metodo para crear libro
    def crear_libro(self):
        #codigo mejorado por sugerencia de GPT:
        self._titulo = input('Ingrese el titulo: ')
        self._autor = input('Ingrese el nombre del autor: ')
        self._anno = input('Ingrese el año de publicacion: ')
        print(self)
        #mi codigo original:
        # titulo = input('Ingrese el titulo: ')
        # autor = input('Ingrese el nombre del autor: ')
        # anno = input('Ingrese el año de publicacion: ')
        # libro = Libro(titulo, autor, anno)
        # print(libro)

libro = Libro()
libro.crear_libro()        