import unittest
from ejercicio1ok import pluralize

class ejercicio1TestCase(unittest.TestCase):
    def test_pluralizar(self):
        self.assertEqual((pluralize(["cow", "pig", "cow", "cow"])), {'cows', 'pig'})  # add assertion here

    def test_pluralizar(self):
        self.assertEqual((pluralize(["table", "table", "table"])), {'tables'})  # add assertion her

    def test_pluralizar(self):
        self.assertEqual((pluralize(["chair", "pencil", "arm"])), {'chair', 'pencil', 'arm'})  # add assertion her
        
if __name__ == '__main__':
    unittest.main()
