import unittest
from ejercicio8ok import simon_says

class MyTestCase(unittest.TestCase):
    #def test_ejercicio8ok(self):
    #    self.assertEqual(simon_says([1, 2], [5, 1]), True)  # add assertion here

    #def test_ejercicio8ok(self):
    #    self.assertEqual(simon_says([1, 2], [5, 5]), False)  # add assertion here

    #def test_ejercicio8ok(self):
    #    self.assertEqual(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]), True)  # add assertion here

    def test_ejercicio8ok(self):
        self.assertEqual(simon_says([1, 2, 3, 4, 5], [5, 5, 2, 3, 4]), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
