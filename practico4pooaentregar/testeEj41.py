import unittest
from prac4ejer1V3 import TableroDeBasquet


class testEj41(unittest.TestCase):
   # def cartelera(self):
   #     tablero=tableroDeBasquet
   #     tablero.adicionarDeAtresVisitante()
   #     tablero.get_puntosVisitante()

       # self.assertEqual(tablero.get_puntosVisitante,3)  # add assertion here

    def cartelera(self):
        tablero=tableroDeBasquet
        tablero.adicionarDeAdosVisitante()
        tablero.get_puntosVisitante()

        self.assertEqual(tablero.get_puntosVisitante,2)  # add assertion here

if __name__ == '__main__':
    unittest.main()
