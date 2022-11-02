import unittest
from ejercicio7ok import unique_sort

class MyTestCase(unittest.TestCase):
   # def test_ejercicio7ok(self):
     #   self.assertEqual(unique_sort([1, 2, 4, 3]), [1, 2, 3, 4])  # add assertion here

   # def test_ejercicio7ok(self):
    #    self.assertEqual(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]), [1, 2, 3, 4])  # add assertion here

    def test_ejercicio7ok(self):
        self.assertEqual(unique_sort([6, 7, 3, 2, 1]),[1, 2, 3, 6, 7] )  # add assertion here


if __name__ == '__main__':
    unittest.main()
