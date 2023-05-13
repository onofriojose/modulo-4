class Accesadores:
    def __init__(self):
        self.atributo_publico = 'puede ser accedido en toda la estructura'
        self._atributo_protegido = 'puede ser accedido desde las subclases'
        self.__atributo_privado = 'puede ser accedido desde la propia clase'

    def get_variablePrivada(self):
        return self.__atributo_privado
    
    def set_variablePrivada(self,__atributo_privado):
        self.__atributo_privado = __atributo_privado
        
objeto = Accesadores()

print(objeto.get_variablePrivada())
objeto.set_variablePrivada('Ezio Altair')
print(objeto.get_variablePrivada())