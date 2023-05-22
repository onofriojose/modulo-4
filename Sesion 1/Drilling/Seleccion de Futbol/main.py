from futbolista import Futbolista
from entrenador import Entrenador
from masajista import Masajista

#instaciando un objeto de la clase futbolista para usar el metodo viajar de la clase padre 'SeleccionDeFutbol'
futbolista1 = Futbolista(2510, 'Ezio Altair', 'Mora', 19, 10, 'Delantero')
futbolista1.viajar()
print('========================================================================')
#instaciando un objeto de la clase masajista para usar el metodo concentrarse de la clase padre 'SeleccionDeFutbol'
masajista1 = Masajista(3120, 'Linda', 'Ming', 27, 'Fisicoterapeuta', 5)
masajista1.concentrarse()
print('========================================================================')
#instaciando un objeto entrenador para usar los metodos de la clase Entrenador
entrenador1 = Entrenador(1110, 'Lionel', 'Scaloni', 50, 'AFA')
entrenador1.dirigirEntrenamiento()
entrenador1.dirigirPartido()

