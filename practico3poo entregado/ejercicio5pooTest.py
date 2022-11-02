import unittest

#class MyTestCase(unittest.TestCase):
 #   def test_something(self):
  #      self.assertEqual(True, False)  # add assertion here

from ejercicio5poo import Segmento
from ejercicio4pooOk import Punto

class Ejercicio5TestCase(unittest.TestCase):
    def test_longitud_segmento(self):
        punto_a = Punto(10, 10)
        punto_b = Punto(10, -10)
        segmento = Segmento(punto_a, punto_b)
        self.assertEqual(segmento.longitud_segmento(), 20.0)

if __name__ == '__main__':
    unittest.main()
