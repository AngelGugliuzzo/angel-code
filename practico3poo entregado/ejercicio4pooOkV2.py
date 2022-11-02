#4.	Crear la clasePunto en el plano que contiene:
#a.	2 atributos ‘x’ e  ‘y’ que representan las coordenadas del punto en el plano
#b.	El constructor de la clasePunto que recibe por agumentos ‘x’ e ‘y’ que son las coordenadas
#c.	Por defecto, inicializar los atributos ‘x’ e ‘y’ en el centro de coordenadas (es decir, 0, 0),
# a menos que reciba por argumento los valores en el constructor. Buscar como se inicializan los
# parámetros de un método si no se pasa por argumento ningún valor
#d.	Los métodosgetter y setter de los atributos
#e.	El método __str__ , mostrando los valores de x e y del punto
#f.	El métodocuadrante() que devuelve un número entre 1 y 4 que indica el cuadrante en el cual se encuentra el Punto.
#g.	El método distancia_al_centro() que devuelve un número que representa la distancia entre el punto y el
# centro de coordenadas. La fórmula a utilizar se muestra en la siguiente imagen:
#h.	El método __eq__ , que compare los valores de ‘x’ e ‘y’ entre dos objetos de la clase Punto


from ejercicio3pooV4especial import Calculadora

#a),b),f)
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #self.x = 0#----------------------->averiguar, no me toma lo que entra por parametro
        #self.y = 0
        self.Xo = 0
        self.Yo = 0

    def cuadrante(self):
        if self.x>0 and self.y>0:
            return 1
        if self.x<0 and self.y<0:
            return 3
        if self.x<0 and self.y>0:
            return 2
        else:
            return 4

    def distancia_al_centro(self):
        return ((self.x-self.Xo)**2+(self.y-self.Yo)**2)**0.5

   #def __str__(self):
    #    return "X: {} Y: {}".format(self.x, self.y)

    def __str__(self):
        # return "X: {} Y {}".format(self.x, self.y)
        return "Punto en ({},{})".format(self.x, self.y)

    def __eq__(self, other):
       return self.x == other.x and self.y == other.y



#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[0]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
#c),d),e)
class Punto2:
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def __str__(self):
   #     return "X: {} Y {}".format(self.x, self.y)
         return "Punto en X: {} Y {}".format(self.x, self.y)





