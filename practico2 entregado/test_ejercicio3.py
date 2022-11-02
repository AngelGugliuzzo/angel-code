import unittest
from ejercicio3ok import operacion_aritmetica

class Ejercicio3TestCase(unittest.TestCase):
   # def test_procesar_suma(self):
   #     self.assertEqual(operacion_aritmetica("12 + 12"),24)  # add assertion here

    #def test_procesar_resta(self):
     #   self.assertEqual(operacion_aritmetica("12 - 12"),0)  # add assertion here

   # def test_procesar_producto(self):
    #    self.assertEqual(operacion_aritmetica("12 * 12"),144)  # add assertion here

        def test_procesar_divicion(self):
           self.assertEqual(operacion_aritmetica("12 // 0"),-1)  # add assertion here

if __name__ == '__main__':
    unittest.main()
