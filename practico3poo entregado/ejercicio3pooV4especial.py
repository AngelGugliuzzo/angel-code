#3.	Crear una clase Calculadora que pueda realizar las acciones de sumar, multiplicar, dividir y restar.
    # Todos los métodos de las operaciones poseen dos parámetros/argumentos de entrada (es decir, parámetros
    # o argumentos que recibe el método)
    #IMPORTANTE: analizar si es necesario declarar atributos en la clase para resolver este problema.

#def test_dividir_10_5__2(self):
#calculadora = Calculadora()
#self.assertEqual(calculadora.dividir(10,5), 2)

from ejercicio4pooOk import Punto


class Calculadora:
    def __init__(self):
        operando1 = 0
        operando2 = 0
       # operando3 = 0
       # operando4 = 0

    def sumar(self, operando1, operando2):
        return (operando1 + operando2)

    def restar(self, operando1, operando2):
        return (operando1 - operando2)

    def multiplicar(self, operando1, operando2):
        return (operando1 * operando2)

    def dividir(self, operando1, operando2):
        return (operando1 // operando2)

    def elevar_cuadrado(self,operando1):
        return (operando1**2)

    def radicar_cuadrado(self, operando1):
        return (operando1**0.5)

   # def longitud_segmento(self, punto_a, punto_b):
   #     x1 = (self.punto_a.x)
   #     x2 = (self.punto_b.x)
   #     y1 = (self.punto_a.y)
   #     y2 = (self.punto_b.y)
   #     return ((Calculadora.restar(x1,x2) ** 2 + (Calculadora.restar(y1,y2)) ** 2) ** 0.5



calculadora = Calculadora()
print(calculadora.sumar(2,5))
print(calculadora.restar(2,5))
print(calculadora.multiplicar(2,5))
print(calculadora.dividir(10,5))
#punto_a = Punto(10,10)
#punto_b = Punto(10,10)
#print(calculadora.longitud_segmento(punto_a, punto_b))
