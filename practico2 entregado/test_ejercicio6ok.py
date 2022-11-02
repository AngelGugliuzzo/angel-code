import unittest
from ejercicio6ok import square_digits

class MyTestCase(unittest.TestCase):
    def test_ejercicio6ok(self):
        self.assertEqual(square_digits(9119), 811181)  # add assertion here

   # def test_ejercicio6ok(self):
   #     self.assertEqual(square_digits(2483), 416649)  # add assertion here

   # def test_ejercicio6ok(self):
   #     self.assertEqual(square_digits(3212), 9414)  # add assertion here


if __name__ == '__main__':
    unittest.main()
