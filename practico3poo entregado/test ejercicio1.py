import unittest
from ejercicio1poo import Rectangulo

class Ejercicio1TestCase(unittest.TestCase):

    def test_area_5base_2altura_10(self):
        rectangulo = Rectangulo(base=5, altura=2)
        area = rectangulo.get_perimetro()

        self.assertEqual(area,14)  # add assertion here


if __name__ == '__main__':
    unittest.main()
