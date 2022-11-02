import unittest
from ejercicio10ok import sevenBoom


class MyTestCase(unittest.TestCase):
    def test_ejercicio10ok(self):
        self.assertEqual(sevenBoom([8, 6, 33, 100]),'no se encuentra el 7 en el array')  # add assertion here

    def test_ejercicio10ok(self):
        self.assertEqual(sevenBoom([1, 2, 3, 4, 5, 6, 7]),'Boom!!!')  # add assertion here

    def test_ejercicio10ok(self):
        self.assertEqual(sevenBoom([2, 55, 60, 97, 86]),'Boom!!!')  # add assertion here

    if __name__ == '__main__':
        unittest.main()
