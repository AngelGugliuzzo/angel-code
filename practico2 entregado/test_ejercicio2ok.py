import unittest
from ejercicio2ok import same_length


class MyTestCase(unittest.TestCase):
  #  def test_same_length(self):
   #     self.assertEqual(same_length("110011100010"), True)  # add assertion here

   # def test_same_length(self):
       # self.assertEqual(same_length("101010110"),False )  # add assertion here


    #def test_same_length(self):
     #   self.assertEqual(same_length("111100001100"), True)  # add assertion here

    def test_same_length(self):
        self.assertEqual(same_length("111"), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
