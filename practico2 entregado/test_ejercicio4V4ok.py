import unittest
from ejercicio4V4ok import check_flush

class ejercicio4V4okTestCase(unittest.TestCase):
    def test_ejercicio4V4ok(self):
        self.assertEqual(check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]), True)  # add assertion here


    #def test_ejercicio4V4ok(self):
    #    self.assertEqual(check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]), True)

   # def test_ejercicio4V4ok(self):
   #     self.assertEqual(check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]), False)

if __name__ == '__main__':
    unittest.main()
