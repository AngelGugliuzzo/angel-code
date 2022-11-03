#3.	Continuando con el ejercicio anterior, agregaremos una clase concreta Perro que tenga un método dibujar()
#e imprima en consola la cara o silueta de un perro. (https://medium.com/analytics-vidhya/how-to-print-emojis-using-python-2e4f93443f7e).
#a.	Ahora, se nos presenta un problema, tanto las Figuras como el Perro pueden dibujarse, entonces…
# Modifiquen el esquema de clases de tal forma que Perro herede de algún padre el método dibujar()
# y que las figuras puedan heredar de esa misma clase y también hereden los métodos correspondientes a Figura.


from abc import ABC, abstractmethod

pip install emoji

import emoji


class Figura(ABC):
    def __init__(self):
        self.nombre = "cuadrado"
        self.largoLadoA=10
        self.largoLadoB=10

    @abstractmethod
    def get_nombre(self):
       return  self.nombre

    @abstractmethod
    def calcular_area(self):
        return self.largoLadoA*self.largoLadoB

    @abstractmethod
    def calcular_perimetro(self):
        return self.largoLadoA+self.largoLadoB+self.largoLadoA+self.largoLadoB

    @abstractmethod
    def dibujar(self):#------------->¿sera abstracto?
        print(emoji.emojize('python is:dog:'))
       return  self.nombre



#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
class Rectangulo(Figura):

    def __init__(self):
        super(Rectangulo,self).__init__()

    def calcular_area(self):
        super(Rectangulo,self).calcular_area()

    def calcular_perimetro(self):
        super(Rectangulo,self).calcular_perimetro()

    def dibujar(self):
        super(Rectangulo,self).dibujar()

#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
class Cuadrado(Figura):

    def __init__(self):
        super(Cuadrado, self).__init__()

    def calcular_area(self):
        super(Cuadrado, self).calcular_area()

    def calcular_perimetro(self):
        super(Cuadrado, self).calcular_perimetro()

    def dibujar(self):
        super(Cuadrado, self).dibujar()

    #cuadrado=Cuadrado()
    #print(cuadrado.calcular_perimetro())
    #print (cuadrado.get_nombre())

    rectangulo=Rectangulo()
    print(rectangulo.calcular_perimetro())
