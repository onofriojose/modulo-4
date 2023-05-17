'''
Para llevar a cabo esta actividad, comenzaremos con la base del siguiente código en Python:
class A:
 def __init__(self):
 print("Pertenezco a la clase A")
 def metodo_a(self):
 print("Método heredado de A")

class B:
 def __init__(self):
 print("Clase B")
 def metodo_b(self):
 print("Método heredado de B")
1. Construya una nueva clase C que tenga herencia múltiple de B y A respectivamente, y
que contenga el metodo_c que imprima por pantalla “Método de clase C”.
2. Cree un nuevo objeto C, y al instanciarlo y acceder a cada método: metodo_a, metodo_b
y metodo_c tenga como resultado lo siguiente:

Clase B
Método heredado de A
Método heredado de B
Método es de C
'''
class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    
    def metodo_b(self):
        print("Método heredado de B")

class C(B, A): #al heredar el mas cercano a la izquerda se imprime primero el metodo __init__ de la clase B
    def __init__(self):
        super().__init__()
        A.__init__(self) #se agrega el metodo __init__ de la clase A para que tambien se imprima ya que se heredo primero el de la clase B

    def metodo_c(self):
        print('Método de clase C')


clase_c = C()
clase_c.metodo_a()
clase_c.metodo_b()
clase_c.metodo_c()
clase_a = A()
print(isinstance(clase_c, (A)))
print(isinstance(clase_a, (C)))
