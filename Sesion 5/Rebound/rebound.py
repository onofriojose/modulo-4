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

class C(B, A):
    def __init__(self):
      super().__init__()
    
    def metodo_c(self):
      print('Metodo de clase C')

clase_c = C()
print(clase_c)
clase_c.metodo_b()
clase_c.metodo_a()
clase_c.metodo_c()
