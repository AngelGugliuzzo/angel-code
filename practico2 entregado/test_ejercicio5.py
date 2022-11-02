import unittest
from ejercicio5 import is_disarium


class MyTestCase(unittest.TestCase):
    def test_ejercicio5(self):
        self.assertEqual(is_disarium(75), False)  # add assertion here


# def test_ejercicio5(self):
#     self.assertEqual(is_disarium(135), True)


def test_ejercicio5(self):
    self.assertEqual(is_disarium(544), False)


# def test_ejercicio5(self):
#     self.assertEqual(is_disarium(518), True)


# def test_ejercicio5(self):
#     self.assertEqual(is_disarium(466), False)


def test_ejercicio5(self):
    self.assertEqual(is_disarium(8), True)

if __name__ == '__main__':
    unittest.main()
