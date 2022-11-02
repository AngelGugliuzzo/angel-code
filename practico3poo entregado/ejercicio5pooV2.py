#5.	Crear la clase Segmento que contiene:
#a.	2 atributos (punto_a, punto_b) del tipo Punto que representan los extremos del Segmento.
#b.	El constructor de la clase Segmento que recibe dos parámetros del tipo Punto para los extremos
#c.	Los métodosgetter y setter de los atributos
#d.	El método __str__ que retorne cómo está conformado el segmento (información de cada punto)
#e.	Un métodolongitud_segmento() que devuelve un número float que representa la longitud del segmento

from ejercicio4pooOk import Punto
from ejercicio3pooV3 import Calculadora
class Segmento:
    def __init__(self,punto_a,punto_b):
        self.punto_a =punto_a
        self.punto_b =punto_b

    def get_punto_a(self, punto_a):
        return self.punto_a

    def set_punto_a(self, punto_a):
        self.punto_a = punto_a

    def get_punto_b(self, punto_b):
        return self.punto_b

    def set_punto_b(self, punto_b):
        self.punto_b = punto_b

    def __str__(self):
        return "punto A: {} punto B: {}".format(self.punto_a, self.punto_b)

    def longitud_segmento(self):
        x1=(self.punto_a.x)
        x2=(self.punto_b.x)
        y1=(self.punto_a.y)
        y2=(self.punto_b.y)
        return (Calculadora.restar(x1,x2) ** 2 + Calculadora.restar(y1,y2) ** 2) ** 0.5

punto_b=Punto(10,10)
punto_a=Punto(-10,10)
segmento = Segmento(punto_a, punto_b)
print(segmento.punto_a,"  ",segmento.punto_b)
print(segmento.longitud_segmento())



