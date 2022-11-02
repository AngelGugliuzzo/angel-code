import unittest
from ejercicio12recuV2 import combinaciones

class MyTestCase(unittest.TestCase):
    def test_ejercicio12recuV2(self):
        self.assertEqual( combinaciones(['a', 'b', 'c'], 2),['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'])  # add assertion here

    def test_ejercicio12recuV2(self):
        self.assertEqual(combinaciones(['a', 'b', 'c'], 2),['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'])  # add assertion here

if __name__ == '__main__':
    unittest.main()
