#2.	Crear una clase abstracta que se llame Figura que tenga:
#a.	Los métodos get_nombre() , calcular_area(), calcular_perimetro()
#b.	El método dibujar() que imprima en consola la figura.
# Por ejemplo: si ingresé un cuadrado de lado 3, deberá imprimir un cuadrado de 3 x 3
#c.	Luego, crear clases concretas como Rectangulo y Cuadrado los cuales implementarán
# los métodos de las clases abstractas.
#d.	Se deberán definir los atributos que requiera cada clase concreta para poder
# implementar la solución (buscar en internet formulas o consultar al profesor).

from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self):
        self.nombre = "cuadrado"
        #self.largoLadoA=largoLadoA
        #self.largoLadoB=largoLadoB
        self.largoLadoA = 10
        self.largoLadoB = 10

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


