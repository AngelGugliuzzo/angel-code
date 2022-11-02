import unittest
from ejercicio9ok import get_budgets

class MyTestCase(unittest.TestCase):
    def test_ejercicio9ok(self):
        self.assertEqual(get_budgets(["name":"John","age": 21,"budget": 23000 },{"name":"Steve","age": 32,"budget": 40000},{"name":"Martin","age": 16,"budget": 2700 }]),65700)  # add assertion here

   # def test_ejercicio9ok(self):
   #     self.assertEqual(get_budgets([{ "name": "John",  "age": 21, "budget": 29000 },{ "name": "Steve",  "age": 32, "budget": 32000 },{ "name": "Martin",  "age": 16, "budget": 1600 }]),62600)

if __name__ == '__main__':
    unittest.main()
