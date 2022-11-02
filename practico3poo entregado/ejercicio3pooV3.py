#3.	Crear una clase Calculadora que pueda realizar las acciones de sumar, multiplicar, dividir y restar.
    # Todos los métodos de las operaciones poseen dos parámetros/argumentos de entrada (es decir, parámetros
    # o argumentos que recibe el método)
    #IMPORTANTE: analizar si es necesario declarar atributos en la clase para resolver este problema.

#def test_dividir_10_5__2(self):
#calculadora = Calculadora()
#self.assertEqual(calculadora.dividir(10,5), 2)


class Calculadora:
        def __init__(self):
            operando1=0
            operando2=0

        def sumar(self,operando1, operando2):
            return (operando1 + operando2)

        def restar(self,operando1, operando2):
            return (operando1 - operando2)

        def multiplicar(self,operando1, operando2):
             return (operando1 * operando2)

        def dividir(self,operando1, operando2):
            return (operando1 // operando2)



calculadora = Calculadora()
print(calculadora.sumar(2,5))
print(calculadora.restar(2,5))
print(calculadora.multiplicar(2,5))
print(calculadora.dividir(10, 5))
